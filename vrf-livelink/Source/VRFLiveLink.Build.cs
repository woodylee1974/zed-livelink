// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;
using System.IO;
using System;

public class VRFLiveLink : ModuleRules
{
	public VRFLiveLink(ReadOnlyTargetRules Target) : base(Target)
	{
		bEnableUndefinedIdentifierWarnings = false;

		if (Target.Platform == UnrealTargetPlatform.Win64)
		{
			//Do nothing
		}
		else if (Target.Platform == UnrealTargetPlatform.Linux)
		{
			//Do nothing
		}

		string WrapperPath = Path.GetFullPath(Path.Combine(ModuleDirectory, "../lib/"));

		PrivateIncludePaths.AddRange(new string[] { "Runtime/Launch/Public", "Runtime/Launch/Private" });

		// Unreal dependency modules
		PrivateDependencyModuleNames.AddRange(new string[]
		{
			"Core",
			"CoreUObject",
			"ApplicationCore",
			"Projects",
			"UdpMessaging",
			"LiveLinkInterface",
			"LiveLinkMessageBusFramework",
			"Networking"
		});

	}
}

