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


IMPLEMENT_APPLICATION(ZEDLiveLinkPlugin, "ZEDLiveLink");

using namespace std;

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
};


void LibInit();


int main(int argc, char **argv)
{
	LibInit();
	printf("Hello world!\n");

	LiveLinkProvider.Reset();
	return EXIT_SUCCESS;
}

//// Initialize tool
void LibInit()
{
	GEngineLoop.PreInit(TEXT("ZEDLiveLink -Messaging"));
	ProcessNewlyLoadedUObjects();
	// Tell the module manager that it may now process newly-loaded UObjects when new C++ modules are loaded
	FModuleManager::Get().StartProcessingNewlyLoadedObjects();
	FModuleManager::Get().LoadModule(TEXT("UdpMessaging"));
}

