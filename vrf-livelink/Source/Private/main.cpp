///////////////////////////////////////////////////////////////////////////
//
// Copyright (c) 2022, STEREOLABS.
//
// All rights reserved.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
///////////////////////////////////////////////////////////////////////////
#include "Roles/LiveLinkCameraRole.h"
#include "Roles/LiveLinkCameraTypes.h"
#include "LiveLinkProvider.h"
#include "RequiredProgramMainCPPInclude.h"
#include "Modules/ModuleManager.h"
#include "LiveLinkRefSkeleton.h"
#include "Roles/LiveLinkAnimationRole.h"
#include "Roles/LiveLinkAnimationTypes.h"
#include "Common/TcpListener.h"
#include "utils/common.h"
#include "HAL/PlatformProcess.h"

#include <iostream>


IMPLEMENT_APPLICATION(VRFLiveLinkPlugin, "VRFLiveLink");

using namespace std;

TArray<FString> targetBone;
TArray<int> parentsIdx;

static TSharedPtr<ILiveLinkProvider> LiveLinkProvider;

struct StreamedSkeletonData
{
	FName SubjectName;
	double Timestamp;
	TArray<FTransform> Skeleton;

	StreamedSkeletonData() {}
	StreamedSkeletonData(FName inSubjectName) : SubjectName(inSubjectName) {}
};

struct StreamedCameraData
{
	FName SubjectName;
	StreamedCameraData() {}
	StreamedCameraData(FName inSubjectName) : SubjectName(inSubjectName) {}

	void InitCamera();
	void UpdateFrameData();
	bool ReadDataFromSocket();
	void UpdateCameraFrameData();
	void UpdateSkeletonStaticData();
	bool HandleListenerConnectionAccepted(FSocket* ClientSocket, const FIPv4Endpoint& ClientEndpoint);
	void UpdateAnimationFrameData();
	unsigned char* GetBuffer(int offset);
	void RewindReadBuffer();

private:
	TSharedPtr<FTcpListener> Listener;
	FSocket* ClientSocket;
	FIPv4Endpoint ClientEndpoint;
	unsigned char Buffer[4096];
	int BufSize;
	int Pos;
	int ReadPos;
};


void LibInit()
{
	GEngineLoop.PreInit(TEXT("VRFLiveLink -Messaging"));
	ProcessNewlyLoadedUObjects();
	// Tell the module manager that it may now process newly-loaded UObjects when new C++ modules are loaded
	FModuleManager::Get().StartProcessingNewlyLoadedObjects();
	FModuleManager::Get().LoadModule(TEXT("UdpMessaging"));
	FModuleManager::Get().LoadModule(TEXT("Networking"));

}

void UpdateCameraStaticData(FName SubjectName)
{
	FLiveLinkStaticDataStruct StaticData(FLiveLinkCameraStaticData::StaticStruct());
	FLiveLinkCameraStaticData& CameraData = *StaticData.Cast<FLiveLinkCameraStaticData>();
	CameraData.bIsAspectRatioSupported = true;
	CameraData.bIsFieldOfViewSupported = true;
	CameraData.bIsFocalLengthSupported = false;
	CameraData.bIsFocusDistanceSupported = false;
	CameraData.bIsProjectionModeSupported = true;
	LiveLinkProvider->UpdateSubjectStaticData(SubjectName, ULiveLinkCameraRole::StaticClass(), MoveTemp(StaticData));
}


bool IsConnected = false;
StreamedCameraData StreamedCamera("VRF0001");

void StreamedCameraData::InitCamera()
{
	const FString ExecutablePath = TEXT("python/envs/3DHuman/python.exe");
	const FString PythonScriptPath = TEXT("python/vrfcam/main.py");

	// Launch the executable
	if (FPaths::FileExists(ExecutablePath) && FPaths::FileExists(PythonScriptPath))
	{
		FProcHandle handle = FPlatformProcess::CreateProc(
			*ExecutablePath,
			*PythonScriptPath,  // Command line parameters (can be nullptr)
			true,     // Set to true to launch the process in the background
			false,    // Don't launch the process with elevated privileges
			false,    // Don't create a new window for the process
			nullptr,  // Don't specify a custom environment
			0,
			nullptr,  // Don't specify a custom working directory
			nullptr   // Process handle (output)
		);
		if (!handle.IsValid()) {
			printf("Launch %s failed!\n", TCHAR_TO_ANSI(*PythonScriptPath));
		}
	}
	else
	{
		// Handle the error (executable not found)
		printf("Executable not found: %s\n", TCHAR_TO_ANSI(*ExecutablePath));
	}
	this->ClientSocket = NULL;
	FIPv4Endpoint LocalEndpoint;
	FIPv4Endpoint::Parse(TEXT("0.0.0.0:6699"), LocalEndpoint);
	this->Listener = MakeShareable(new FTcpListener(LocalEndpoint));
	this->Listener->OnConnectionAccepted().BindRaw(this, &StreamedCameraData::HandleListenerConnectionAccepted);

	//FIXME: this size should be obtained from sockets.
	this->BufSize = 952;
}

void StreamedCameraData::UpdateFrameData()
{
	if (this->ReadDataFromSocket()) {
	    this->UpdateAnimationFrameData();
		this->RewindReadBuffer();
	}
}

void StreamedCameraData::RewindReadBuffer()
{
	this->Pos = 0;
	this->ReadPos = 0;
}

unsigned char* StreamedCameraData::GetBuffer(int offset)
{
	unsigned char* ret = this->Buffer + this->ReadPos;
	this->ReadPos += offset;
	return ret;
}

bool StreamedCameraData::ReadDataFromSocket()
{
	if (this->ClientSocket == NULL) {
		return false;
	}
	if (this->ClientSocket->GetConnectionState() != SCS_Connected) {
		return false;
	}

	int ByteReads;
	this->ClientSocket->Recv(this->Buffer + this->Pos, this->BufSize - this->Pos, ByteReads);
	this->Pos += ByteReads;
	if (this->Pos < this->BufSize) {
		return false;
	}
	return true;
}

void StreamedCameraData::UpdateCameraFrameData()
{
	FLiveLinkFrameDataStruct FrameData(FLiveLinkCameraFrameData::StaticStruct());
	FLiveLinkCameraFrameData& CameraData = *FrameData.Cast<FLiveLinkCameraFrameData>();
	CameraData.AspectRatio = 16. / 9;
	CameraData.FieldOfView = 90.f;
	CameraData.ProjectionMode = ELiveLinkCameraProjectionMode::Perspective;
	FTransform Pose = FTransform::Identity;
	FRotator Rotation(0.0f, 180.0f, 0.0f);
	Pose.SetRotation(FQuat(Rotation));
	CameraData.Transform = Pose;
	double StreamTime = FPlatformTime::Seconds();
	CameraData.WorldTime = StreamTime;
	LiveLinkProvider->UpdateSubjectFrameData(this->SubjectName, MoveTemp(FrameData));
}

void StreamedCameraData::UpdateSkeletonStaticData()
{
	FLiveLinkStaticDataStruct StaticData(FLiveLinkSkeletonStaticData::StaticStruct());
	FLiveLinkSkeletonStaticData& AnimationData = *StaticData.Cast<FLiveLinkSkeletonStaticData>();

	for (int i = 0; i < targetBone.Num(); i++)
	{
		AnimationData.BoneNames.Add(FName(targetBone[i]));
		AnimationData.BoneParents.Add(parentsIdx[i]);
	}

	LiveLinkProvider->UpdateSubjectStaticData(FName("Superman"), ULiveLinkAnimationRole::StaticClass(), MoveTemp(StaticData));
}

#define READ_FIELD(name, type) \
   *(type*)(this->GetBuffer(sizeof(type)));

void StreamedCameraData::UpdateAnimationFrameData() 
{
	FLiveLinkFrameDataStruct FrameData(FLiveLinkAnimationFrameData::StaticStruct());
	FLiveLinkAnimationFrameData& AnimationData = *FrameData.Cast<FLiveLinkAnimationFrameData>();

	//FName AnimationSubjectName = FName((const char*)this->GetBuffer(VRF::ROLE_NAME));
	FName AnimationSubjectName = FName("Superman");
	double StreamTime = FPlatformTime::Seconds();
	AnimationData.WorldTime = StreamTime;
	//printf("UpdateAnimationFrameData at %14.4f\n", StreamTime);

	TMap<FString, FTransform> rigBoneTarget;
	VRF::float3 bodyPosition = READ_FIELD("BodyPosition", VRF::float3);
	VRF::float4 bodyRotation = READ_FIELD("BodyOrientation", VRF::float4);

	for (int i = 0; i < targetBone.Num(); i++)
	{
		rigBoneTarget.Add(targetBone[i], FTransform::Identity);
	}
	
	FVector position = FVector(bodyPosition.x, bodyPosition.y, bodyPosition.z);
	FQuat global_rotation = FQuat(bodyRotation.x, bodyRotation.y, bodyRotation.z, bodyRotation.w);

	if (position.ContainsNaN())
	{
		position = FVector::ZeroVector;
	}

	rigBoneTarget["PELVIS"].SetLocation(position);
	rigBoneTarget["PELVIS"].SetRotation(global_rotation.GetNormalized());


	for (int i = 1; i < targetBone.Num() / 2; i++)
	{
		VRF::float3 localTranslation = READ_FIELD("LocalTranslate", VRF::float3);
		VRF::float4 localRotation = READ_FIELD("LocalOrientation", VRF::float4);

		position = FVector(localTranslation.x, localTranslation.y, localTranslation.z);
		printf("%d - %7.2f, %7.2f, %7.2f\n", i, localTranslation.x, localTranslation.y, localTranslation.z);

		if (position.ContainsNaN())
		{
			position = FVector::ZeroVector;
		}

		FQuat jointRotation = FQuat(localRotation.x, localRotation.y, localRotation.z, localRotation.w).GetNormalized();

		if (jointRotation.ContainsNaN())
		{
			position = FVector::ZeroVector;
		}

		rigBoneTarget[targetBone[i]].SetLocation(position);
		rigBoneTarget[targetBone[i]].SetRotation(jointRotation);
	}

	TArray<FTransform> transforms;
	for (int i = 0; i < targetBone.Num() / 2; i++)
	{
		FString trf = rigBoneTarget[targetBone[i]].ToHumanReadableString();
		//printf("%d - %s\n", i, TCHAR_TO_UTF8(*trf));
		transforms.Push(rigBoneTarget[targetBone[i]]);
	}

	// Add keypoints confidence at the end of the Array of transforms.
	for (int i = 0; i < targetBone.Num() / 2; i++)
	{
		FTransform kp_conf = FTransform::Identity;
		kp_conf.SetLocation(FVector(1.0f, 1.0f, 1.0f));
		transforms.Push(kp_conf);
	}

	AnimationData.Transforms = transforms;
	LiveLinkProvider->UpdateSubjectFrameData(AnimationSubjectName, MoveTemp(FrameData));
}


bool StreamedCameraData::HandleListenerConnectionAccepted(FSocket* aClientSocket, const FIPv4Endpoint& aClientEndpoint)
{
	this->ClientSocket = aClientSocket;
	this->ClientEndpoint = aClientEndpoint;

	return true;
}


int main(int argc, char **argv)
{
	LibInit();
	LiveLinkProvider = ILiveLinkProvider::CreateLiveLinkProvider(TEXT("VRF-003243242"));

	targetBone = targetBone34;
	parentsIdx = parents34Idx;

	cout << "Waiting for connection..." << endl;
	//// Update static camera data.
	if (LiveLinkProvider.IsValid()) {
		StreamedCamera.InitCamera();
	}

	while (true) {
		if (LiveLinkProvider->HasConnection()) {
			if (!IsConnected) {
				IsConnected = true;
				cout << "VRFLivelink is connected! " << endl;
				UpdateCameraStaticData(StreamedCamera.SubjectName);
				StreamedCamera.UpdateSkeletonStaticData();
				StreamedCamera.UpdateCameraFrameData();
			}
			StreamedCamera.UpdateFrameData();
		}
		else if (IsConnected) {
			cout << "VRFLivelink is disconnected! " << endl;
			IsConnected = false;
		}
		else {
			//cout << "VRFLivelink is waiting for connection..." << endl;
		}
		FPlatformProcess::Sleep(0.01f);
	}

	LiveLinkProvider.Reset();
	return EXIT_SUCCESS;
}


