// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "ZEDUnrealLiveLinkEditor/Public/AnimGraphNode_ZEDLiveLinkPose.h"
#include "ZEDUnrealLiveLink/AnimNode_ZEDLiveLinkPose.h"
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeAnimGraphNode_ZEDLiveLinkPose() {}
// Cross Module References
	ANIMGRAPH_API UClass* Z_Construct_UClass_UAnimGraphNode_Base();
	UPackage* Z_Construct_UPackage__Script_ZEDUnrealLiveLinkEditor();
	ZEDUNREALLIVELINK_API UScriptStruct* Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose();
	ZEDUNREALLIVELINKEDITOR_API UClass* Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose();
	ZEDUNREALLIVELINKEDITOR_API UClass* Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_NoRegister();
// End Cross Module References
	void UAnimGraphNode_ZEDLiveLinkPose::StaticRegisterNativesUAnimGraphNode_ZEDLiveLinkPose()
	{
	}
	IMPLEMENT_CLASS_NO_AUTO_REGISTRATION(UAnimGraphNode_ZEDLiveLinkPose);
	UClass* Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_NoRegister()
	{
		return UAnimGraphNode_ZEDLiveLinkPose::StaticClass();
	}
	struct Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_Node_MetaData[];
#endif
		static const UECodeGen_Private::FStructPropertyParams NewProp_Node;
		static const UECodeGen_Private::FPropertyParamsBase* const PropPointers[];
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UECodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_UAnimGraphNode_Base,
		(UObject* (*)())Z_Construct_UPackage__Script_ZEDUnrealLiveLinkEditor,
	};
	static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::DependentSingletons) < 16);
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::Class_MetaDataParams[] = {
		{ "IncludePath", "AnimGraphNode_ZEDLiveLinkPose.h" },
		{ "ModuleRelativePath", "Public/AnimGraphNode_ZEDLiveLinkPose.h" },
	};
#endif
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::NewProp_Node_MetaData[] = {
		{ "Category", "Settings" },
		{ "ModuleRelativePath", "Public/AnimGraphNode_ZEDLiveLinkPose.h" },
	};
#endif
	const UECodeGen_Private::FStructPropertyParams Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::NewProp_Node = { "Node", nullptr, (EPropertyFlags)0x0010008000000001, UECodeGen_Private::EPropertyGenFlags::Struct, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(UAnimGraphNode_ZEDLiveLinkPose, Node), Z_Construct_UScriptStruct_FAnimNode_ZEDLiveLinkPose, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::NewProp_Node_MetaData), Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::NewProp_Node_MetaData) }; // 3286577694
	const UECodeGen_Private::FPropertyParamsBase* const Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::PropPointers[] = {
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::NewProp_Node,
	};
	const FCppClassTypeInfoStatic Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<UAnimGraphNode_ZEDLiveLinkPose>::IsAbstract,
	};
	const UECodeGen_Private::FClassParams Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::ClassParams = {
		&UAnimGraphNode_ZEDLiveLinkPose::StaticClass,
		nullptr,
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::PropPointers,
		nullptr,
		UE_ARRAY_COUNT(DependentSingletons),
		0,
		UE_ARRAY_COUNT(Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::PropPointers),
		0,
		0x008000A0u,
		METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::Class_MetaDataParams), Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::Class_MetaDataParams)
	};
	static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::PropPointers) < 2048);
	UClass* Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose()
	{
		if (!Z_Registration_Info_UClass_UAnimGraphNode_ZEDLiveLinkPose.OuterSingleton)
		{
			UECodeGen_Private::ConstructUClass(Z_Registration_Info_UClass_UAnimGraphNode_ZEDLiveLinkPose.OuterSingleton, Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose_Statics::ClassParams);
		}
		return Z_Registration_Info_UClass_UAnimGraphNode_ZEDLiveLinkPose.OuterSingleton;
	}
	template<> ZEDUNREALLIVELINKEDITOR_API UClass* StaticClass<UAnimGraphNode_ZEDLiveLinkPose>()
	{
		return UAnimGraphNode_ZEDLiveLinkPose::StaticClass();
	}
	UAnimGraphNode_ZEDLiveLinkPose::UAnimGraphNode_ZEDLiveLinkPose(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer) {}
	DEFINE_VTABLE_PTR_HELPER_CTOR(UAnimGraphNode_ZEDLiveLinkPose);
	UAnimGraphNode_ZEDLiveLinkPose::~UAnimGraphNode_ZEDLiveLinkPose() {}
	struct Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLinkEditor_Public_AnimGraphNode_ZEDLiveLinkPose_h_Statics
	{
		static const FClassRegisterCompiledInInfo ClassInfo[];
	};
	const FClassRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLinkEditor_Public_AnimGraphNode_ZEDLiveLinkPose_h_Statics::ClassInfo[] = {
		{ Z_Construct_UClass_UAnimGraphNode_ZEDLiveLinkPose, UAnimGraphNode_ZEDLiveLinkPose::StaticClass, TEXT("UAnimGraphNode_ZEDLiveLinkPose"), &Z_Registration_Info_UClass_UAnimGraphNode_ZEDLiveLinkPose, CONSTRUCT_RELOAD_VERSION_INFO(FClassReloadVersionInfo, sizeof(UAnimGraphNode_ZEDLiveLinkPose), 3173628770U) },
	};
	static FRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLinkEditor_Public_AnimGraphNode_ZEDLiveLinkPose_h_1223690081(TEXT("/Script/ZEDUnrealLiveLinkEditor"),
		Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLinkEditor_Public_AnimGraphNode_ZEDLiveLinkPose_h_Statics::ClassInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLinkEditor_Public_AnimGraphNode_ZEDLiveLinkPose_h_Statics::ClassInfo),
		nullptr, 0,
		nullptr, 0);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
