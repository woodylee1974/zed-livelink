// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "ZEDUnrealLiveLink/AnimNode_ZEDLiveLinkPose.h"
#include "../../Source/Runtime/Engine/Classes/Animation/AnimNodeBase.h"
#include "LiveLinkTypes.h"
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeAnimNode_ZEDLiveLinkPose() {}
// Cross Module References
	COREUOBJECT_API UClass* Z_Construct_UClass_UClass();
	ENGINE_API UClass* Z_Construct_UClass_USkeletalMeshComponent_NoRegister();
	ENGINE_API UScriptStruct* Z_Construct_UScriptStruct_FAnimNode_Base();
	ENGINE_API UScriptStruct* Z_Construct_UScriptStruct_FPoseLink();
	LIVELINKINTERFACE_API UScriptStruct* Z_Construct_UScriptStruct_FLiveLinkSubjectName();
	UPackage* Z_Construct_UPackage__Script_ZEDUnrealLiveLink();
	ZEDUNREALLIVELINK_API UClass* Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_NoRegister();
	ZEDUNREALLIVELINK_API UScriptStruct* Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose();
// End Cross Module References

static_assert(std::is_polymorphic<FAnimNode_ZEDLiveLinkPose>() == std::is_polymorphic<FAnimNode_Base>(), "USTRUCT FAnimNode_ZEDLiveLinkPose cannot be polymorphic unless super FAnimNode_Base is polymorphic");

	static FStructRegistrationInfo Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose;
class UScriptStruct* FAnimNode_ZEDLiveLinkPose::StaticStruct()
{
	if (!Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose.OuterSingleton)
	{
		Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose.OuterSingleton = GetStaticStruct(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose, (UObject*)Z_Construct_UPackage__Script_ZEDUnrealLiveLink(), TEXT("AnimNode_ZEDLiveLinkPose"));
	}
	return Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose.OuterSingleton;
}
template<> ZEDUNREALLIVELINK_API UScriptStruct* StaticStruct<FAnimNode_ZEDLiveLinkPose>()
{
	return FAnimNode_ZEDLiveLinkPose::StaticStruct();
}
	struct Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics
	{
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam Struct_MetaDataParams[];
#endif
		static void* NewStructOps();
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_InputPose_MetaData[];
#endif
		static const UECodeGen_Private::FStructPropertyParams NewProp_InputPose;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_LiveLinkSubjectName_MetaData[];
#endif
		static const UECodeGen_Private::FStructPropertyParams NewProp_LiveLinkSubjectName;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_SkeletalMesh_MetaData[];
#endif
		static const UECodeGen_Private::FObjectPtrPropertyParams NewProp_SkeletalMesh;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_bBoneScaling_MetaData[];
#endif
		static void NewProp_bBoneScaling_SetBit(void* Obj);
		static const UECodeGen_Private::FBoolPropertyParams NewProp_bBoneScaling;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_HeightOffset_MetaData[];
#endif
		static const UECodeGen_Private::FFloatPropertyParams NewProp_HeightOffset;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_bStickAvatarOnFloor_MetaData[];
#endif
		static void NewProp_bStickAvatarOnFloor_SetBit(void* Obj);
		static const UECodeGen_Private::FBoolPropertyParams NewProp_bStickAvatarOnFloor;
#if WITH_EDITORONLY_DATA
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_SubjectName_MetaData[];
#endif
		static const UECodeGen_Private::FNamePropertyParams NewProp_SubjectName;
#endif // WITH_EDITORONLY_DATA
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_RetargetAsset_MetaData[];
#endif
		static const UECodeGen_Private::FClassPropertyParams NewProp_RetargetAsset;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_CurrentRetargetAsset_MetaData[];
#endif
		static const UECodeGen_Private::FObjectPtrPropertyParams NewProp_CurrentRetargetAsset;
		static const UECodeGen_Private::FPropertyParamsBase* const PropPointers[];
#if WITH_EDITORONLY_DATA
#endif // WITH_EDITORONLY_DATA
		static const UECodeGen_Private::FStructParams ReturnStructParams;
	};
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::Struct_MetaDataParams[] = {
		{ "BlueprintInternalUseOnly", "true" },
		{ "BlueprintType", "true" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
	};
#endif
	void* Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewStructOps()
	{
		return (UScriptStruct::ICppStructOps*)new UScriptStruct::TCppStructOps<FAnimNode_ZEDLiveLinkPose>();
	}
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_InputPose_MetaData[] = {
		{ "Category", "Input" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
	};
#endif
	const UECodeGen_Private::FStructPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_InputPose = { "InputPose", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Struct, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, InputPose), Z_Construct_UScriptStruct_FPoseLink, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_InputPose_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_InputPose_MetaData) }; // 1465313103
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_LiveLinkSubjectName_MetaData[] = {
		{ "Category", "SourceData" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
		{ "PinShownByDefault", "" },
	};
#endif
	const UECodeGen_Private::FStructPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_LiveLinkSubjectName = { "LiveLinkSubjectName", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Struct, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, LiveLinkSubjectName), Z_Construct_UScriptStruct_FLiveLinkSubjectName, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_LiveLinkSubjectName_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_LiveLinkSubjectName_MetaData) }; // 3493280904
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SkeletalMesh_MetaData[] = {
		{ "Category", "SourceData" },
		{ "EditInline", "true" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
		{ "PinShownByDefault", "" },
	};
#endif
	const UECodeGen_Private::FObjectPtrPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SkeletalMesh = { "SkeletalMesh", nullptr, (EPropertyFlags)0x001400000008000d, UECodeGen_Private::EPropertyGenFlags::Object | UECodeGen_Private::EPropertyGenFlags::ObjectPtr, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, SkeletalMesh), Z_Construct_UClass_USkeletalMeshComponent_NoRegister, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SkeletalMesh_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SkeletalMesh_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling_MetaData[] = {
		{ "Category", "SourceData" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
		{ "PinShownByDefault", "" },
	};
#endif
	void Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling_SetBit(void* Obj)
	{
		((FAnimNode_ZEDLiveLinkPose*)Obj)->bBoneScaling = 1;
	}
	const UECodeGen_Private::FBoolPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling = { "bBoneScaling", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Bool | UECodeGen_Private::EPropertyGenFlags::NativeBool, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, sizeof(bool), sizeof(FAnimNode_ZEDLiveLinkPose), &Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling_SetBit, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_HeightOffset_MetaData[] = {
		{ "Category", "SourceData" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
		{ "PinShownByDefault", "" },
	};
#endif
	const UECodeGen_Private::FFloatPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_HeightOffset = { "HeightOffset", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Float, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, HeightOffset), METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_HeightOffset_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_HeightOffset_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor_MetaData[] = {
		{ "Category", "SourceData" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
		{ "PinShownByDefault", "" },
	};
#endif
	void Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor_SetBit(void* Obj)
	{
		((FAnimNode_ZEDLiveLinkPose*)Obj)->bStickAvatarOnFloor = 1;
	}
	const UECodeGen_Private::FBoolPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor = { "bStickAvatarOnFloor", nullptr, (EPropertyFlags)0x0010000000000005, UECodeGen_Private::EPropertyGenFlags::Bool | UECodeGen_Private::EPropertyGenFlags::NativeBool, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, sizeof(bool), sizeof(FAnimNode_ZEDLiveLinkPose), &Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor_SetBit, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor_MetaData) };
#if WITH_EDITORONLY_DATA
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SubjectName_MetaData[] = {
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
	};
#endif
	const UECodeGen_Private::FNamePropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SubjectName = { "SubjectName", nullptr, (EPropertyFlags)0x0010000820000000, UECodeGen_Private::EPropertyGenFlags::Name, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, SubjectName_DEPRECATED), METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SubjectName_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SubjectName_MetaData) };
#endif // WITH_EDITORONLY_DATA
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_RetargetAsset_MetaData[] = {
		{ "Category", "Retarget" },
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
		{ "NeverAsPin", "" },
	};
#endif
	const UECodeGen_Private::FClassPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_RetargetAsset = { "RetargetAsset", nullptr, (EPropertyFlags)0x0014000002000005, UECodeGen_Private::EPropertyGenFlags::Class, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, RetargetAsset), Z_Construct_UClass_UClass, Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_NoRegister, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_RetargetAsset_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_RetargetAsset_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_CurrentRetargetAsset_MetaData[] = {
		{ "ModuleRelativePath", "AnimNode_ZEDLiveLinkPose.h" },
	};
#endif
	const UECodeGen_Private::FObjectPtrPropertyParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_CurrentRetargetAsset = { "CurrentRetargetAsset", nullptr, (EPropertyFlags)0x0014000000002000, UECodeGen_Private::EPropertyGenFlags::Object | UECodeGen_Private::EPropertyGenFlags::ObjectPtr, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(FAnimNode_ZEDLiveLinkPose, CurrentRetargetAsset), Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_NoRegister, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_CurrentRetargetAsset_MetaData), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_CurrentRetargetAsset_MetaData) };
	const UECodeGen_Private::FPropertyParamsBase* const Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::PropPointers[] = {
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_InputPose,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_LiveLinkSubjectName,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SkeletalMesh,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bBoneScaling,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_HeightOffset,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_bStickAvatarOnFloor,
#if WITH_EDITORONLY_DATA
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_SubjectName,
#endif // WITH_EDITORONLY_DATA
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_RetargetAsset,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewProp_CurrentRetargetAsset,
	};
	const UECodeGen_Private::FStructParams Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::ReturnStructParams = {
		(UObject* (*)())Z_Construct_UPackage__Script_ZEDUnrealLiveLink,
		Z_Construct_UScriptStruct_FAnimNode_Base,
		&NewStructOps,
		"AnimNode_ZEDLiveLinkPose",
		Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::PropPointers,
		UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::PropPointers),
		sizeof(FAnimNode_ZEDLiveLinkPose),
		alignof(FAnimNode_ZEDLiveLinkPose),
		RF_Public|RF_Transient|RF_MarkAsNative,
		EStructFlags(0x00000205),
		METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::Struct_MetaDataParams), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::Struct_MetaDataParams)
	};
	static_assert(UE_ARRAY_COUNT(Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::PropPointers) < 2048);
	UScriptStruct* Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose()
	{
		if (!Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose.InnerSingleton)
		{
			UECodeGen_Private::ConstructUScriptStruct(Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose.InnerSingleton, Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::ReturnStructParams);
		}
		return Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose.InnerSingleton;
	}
	struct Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_AnimNode_ZEDLiveLinkPose_h_Statics
	{
		static const FStructRegisterCompiledInInfo ScriptStructInfo[];
	};
	const FStructRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_AnimNode_ZEDLiveLinkPose_h_Statics::ScriptStructInfo[] = {
		{ FAnimNode_ZEDLiveLinkPose::StaticStruct, Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose_Statics::NewStructOps, TEXT("AnimNode_ZEDLiveLinkPose"), &Z_Registration_Info_UScriptStruct_AnimNode_ZEDLiveLinkPose, CONSTRUCT_RELOAD_VERSION_INFO(FStructReloadVersionInfo, sizeof(FAnimNode_ZEDLiveLinkPose), 3286577694U) },
	};
	static FRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_AnimNode_ZEDLiveLinkPose_h_1346445507(TEXT("/Script/ZEDUnrealLiveLink"),
		nullptr, 0,
		Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_AnimNode_ZEDLiveLinkPose_h_Statics::ScriptStructInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_AnimNode_ZEDLiveLinkPose_h_Statics::ScriptStructInfo),
		nullptr, 0);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
