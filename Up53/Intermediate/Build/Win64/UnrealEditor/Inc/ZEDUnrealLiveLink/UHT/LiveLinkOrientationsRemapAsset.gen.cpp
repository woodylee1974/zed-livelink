// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "ZEDUnrealLiveLink/LiveLinkOrientationsRemapAsset.h"
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeLiveLinkOrientationsRemapAsset() {}
// Cross Module References
	LIVELINKANIMATIONCORE_API UClass* Z_Construct_UClass_ULiveLinkRemapAsset();
	UPackage* Z_Construct_UPackage__Script_ZEDUnrealLiveLink();
	ZEDUNREALLIVELINK_API UClass* Z_Construct_UClass_ULiveLinkOrientationsRemapAsset();
	ZEDUNREALLIVELINK_API UClass* Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_NoRegister();
// End Cross Module References
	void ULiveLinkOrientationsRemapAsset::StaticRegisterNativesULiveLinkOrientationsRemapAsset()
	{
	}
	IMPLEMENT_CLASS_NO_AUTO_REGISTRATION(ULiveLinkOrientationsRemapAsset);
	UClass* Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_NoRegister()
	{
		return ULiveLinkOrientationsRemapAsset::StaticClass();
	}
	struct Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UECodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_ULiveLinkRemapAsset,
		(UObject* (*)())Z_Construct_UPackage__Script_ZEDUnrealLiveLink,
	};
	static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::DependentSingletons) < 16);
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::Class_MetaDataParams[] = {
#if !UE_BUILD_SHIPPING
		{ "Comment", "/**\n *\n */" },
#endif
		{ "IncludePath", "LiveLinkOrientationsRemapAsset.h" },
		{ "ModuleRelativePath", "LiveLinkOrientationsRemapAsset.h" },
	};
#endif
	const FCppClassTypeInfoStatic Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<ULiveLinkOrientationsRemapAsset>::IsAbstract,
	};
	const UECodeGen_Private::FClassParams Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::ClassParams = {
		&ULiveLinkOrientationsRemapAsset::StaticClass,
		nullptr,
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		nullptr,
		nullptr,
		UE_ARRAY_COUNT(DependentSingletons),
		0,
		0,
		0,
		0x001000A0u,
		METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::Class_MetaDataParams), Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::Class_MetaDataParams)
	};
	UClass* Z_Construct_UClass_ULiveLinkOrientationsRemapAsset()
	{
		if (!Z_Registration_Info_UClass_ULiveLinkOrientationsRemapAsset.OuterSingleton)
		{
			UECodeGen_Private::ConstructUClass(Z_Registration_Info_UClass_ULiveLinkOrientationsRemapAsset.OuterSingleton, Z_Construct_UClass_ULiveLinkOrientationsRemapAsset_Statics::ClassParams);
		}
		return Z_Registration_Info_UClass_ULiveLinkOrientationsRemapAsset.OuterSingleton;
	}
	template<> ZEDUNREALLIVELINK_API UClass* StaticClass<ULiveLinkOrientationsRemapAsset>()
	{
		return ULiveLinkOrientationsRemapAsset::StaticClass();
	}
	ULiveLinkOrientationsRemapAsset::ULiveLinkOrientationsRemapAsset(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer) {}
	DEFINE_VTABLE_PTR_HELPER_CTOR(ULiveLinkOrientationsRemapAsset);
	ULiveLinkOrientationsRemapAsset::~ULiveLinkOrientationsRemapAsset() {}
	struct Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_LiveLinkOrientationsRemapAsset_h_Statics
	{
		static const FClassRegisterCompiledInInfo ClassInfo[];
	};
	const FClassRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_LiveLinkOrientationsRemapAsset_h_Statics::ClassInfo[] = {
		{ Z_Construct_UClass_ULiveLinkOrientationsRemapAsset, ULiveLinkOrientationsRemapAsset::StaticClass, TEXT("ULiveLinkOrientationsRemapAsset"), &Z_Registration_Info_UClass_ULiveLinkOrientationsRemapAsset, CONSTRUCT_RELOAD_VERSION_INFO(FClassReloadVersionInfo, sizeof(ULiveLinkOrientationsRemapAsset), 1054465733U) },
	};
	static FRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_LiveLinkOrientationsRemapAsset_h_2756262974(TEXT("/Script/ZEDUnrealLiveLink"),
		Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_LiveLinkOrientationsRemapAsset_h_Statics::ClassInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Engine_Source_Programs_zed_livelink_Up53_Source_ZEDUnrealLiveLink_LiveLinkOrientationsRemapAsset_h_Statics::ClassInfo),
		nullptr, 0,
		nullptr, 0);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
