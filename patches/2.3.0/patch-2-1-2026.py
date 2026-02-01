def MultisaveHelper(ReturnOne=None, ReturnPathOnly=False, LastUsed=False, LoadPrompt=True, LookingForVictorFile=False, PredefinedSavePath=None):
	SavePaths = {}; multisave = configparser.ConfigParser(); global PinorINI, RunsINI, InventorINI, EnemyPopINI, LastUsedSave, CurrentSavePath, MultipleSaves; PathRemovals = []
	try:
		if CurrentSavePath: pass
	except: CurrentSavePath = None
	Log(f"Return one only?: {ReturnOne}\nReturn path only?: {ReturnPathOnly}\nLast used path?: {LastUsed}\nLoad prompt?: {False}\nLooking for VICTOR.Y?: {LookingForVictorFile}\nPredefined Save Path?: {PredefinedSavePath}")
	if os.path.exists(GetCustomFilePath("SavePaths.ini")): multisave.read(GetCustomFilePath("SavePaths.ini")); LastUsedSave = multisave["Last Used"]["path"]; Log(f"Last Used Save: {LastUsedSave}")
	else:
		print("SavePaths.ini does not exist. Defaulting to the game's root directory."); pause(); CurrentSavePath = os.getcwd()
		SavePathsINISetup(); print("SavePaths.ini should now exist. If so, this error should NOT re-appear next time you run PyNori."); pause()
		if not ReturnOne: return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
		elif ReturnOne == "Pinori": return GetPinorINIPath()
		elif ReturnOne == "Runs": return GetRunsINIPath()
		elif ReturnOne == "Inventory": return GetInventorINIPath()
		elif ReturnOne == "EnemyPop": return GetEnemyPopINIPath()
	if "Default Path" not in multisave:
		print(f"Default Path does not exist. Using the {"game's root directory" if not LastUsed and not LastUsedSave else "last used Save Path"} as a failsafe."); pause(); cls(); CurrentSavePath = os.getcwd()
		if not LastUsed:
			if not ReturnOne: return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
			elif ReturnOne == "Pinori": return GetPinorINIPath()
			elif ReturnOne == "Runs": return GetRunsINIPath()
			elif ReturnOne == "Inventory": return GetInventorINIPath()
			elif ReturnOne == "EnemyPop": return GetEnemyPopINIPath()
		else:
			if not ReturnOne: return GetCustomFilePath("Pinori.ini", subdir1=Path(LastUsedSave).resolve()), GetCustomFilePath("Runs.ini", subdir1=Path(LastUsedSave).resolve()), GetCustomFilePath("inventory.ini", subdir1=Path(LastUsedSave).resolve()), GetCustomFilePath("EnemyPopulation.ini", subdir1=Path(LastUsedSave).resolve())
			elif ReturnOne == "Pinori": return GetCustomFilePath("Pinori.ini", subdir1=Path(LastUsedSave).resolve())
			elif ReturnOne == "Runs": return GetCustomFilePath("Runs.ini", subdir1=Path(LastUsedSave).resolve())
			elif ReturnOne == "Inventory": return GetCustomFilePath("inventory.ini", subdir1=Path(LastUsedSave).resolve())
			elif ReturnOne == "EnemyPop": return GetCustomFilePath("EnemyPopulation.ini", subdir1=Path(LastUsedSave).resolve())
	else: 
		try: sp_default = multisave.get("Default Path", "path"); Log(f"Default Path: {sp_default}")
		except: Log("Default Path section exists, but the key doesn't. Using the game's root directory as a failsafe."); return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
	try:
		while True:
			if "Custom Paths" not in multisave: Log("No custom paths found."); break
			else:
				sp_customs = multisave["Custom Paths"]
				for name, key in sp_customs.items(): SavePaths[name] = key; Log(f"Custom Path named {name} leads to \"{key}\"."); Log(f"{name} contains a valid path." if os.path.exists(Path(SavePaths[name]).resolve()) else f"{name} points to a nonexistent directory or is not a valid path.")
				break
	except KeyboardInterrupt:
		if not LastUsed:
			if not ReturnOne: return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
			elif ReturnOne == "Pinori": return GetPinorINIPath()
			elif ReturnOne == "Runs": return GetRunsINIPath()
			elif ReturnOne == "Inventory": return GetInventorINIPath()
			elif ReturnOne == "EnemyPop": return GetEnemyPopINIPath()
		else:
			if not ReturnOne: return os.path.join(Path(LastUsedSave).resolve(), "Pinori.ini"), os.path.join(Path(LastUsedSave).resolve(), "Runs.ini"), os.path.join(Path(LastUsedSave).resolve(), "inventory.ini"), os.path.join(Path(LastUsedSave).resolve(), "EnemyPopulation.ini")
			elif ReturnOne == "Pinori": return os.path.join(Path(LastUsedSave).resolve(), "Pinori.ini")
			elif ReturnOne == "Runs": return os.path.join(Path(LastUsedSave).resolve(), "Runs.ini")
			elif ReturnOne == "Inventory": return os.path.join(Path(LastUsedSave).resolve(), "inventory.ini")
			elif ReturnOne == "EnemyPop": return os.path.join(Path(LastUsedSave).resolve(), "EnemyPopulation.ini")
	except ValueError as VE: Log(f"How did I mess this up bro smh: {VE}")
	except: Log("Custom Paths section exists, but has no keys. Defaulting to the game's root directory."); return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
	Log(f"Custom Paths found: {len(SavePaths)}")
	for name, path in SavePaths.items():
		try:
			if os.path.exists(os.path.join(Path(path).resolve(), "Pinori.ini")): Log(f"{name} contains PyNori Save Data.")
			else: raise FileNotFoundError
			if os.path.exists(os.path.join(Path(path).resolve(), "inventory.ini")): Log(f"{name} contains Inventory Data.")
			else: raise FileNotFoundError
			if os.path.exists(os.path.join(Path(path).resolve(), "Runs.ini")): Log(f"{name} contains Run Data.")
			else: raise FileNotFoundError
			if os.path.exists(os.path.join(Path(path).resolve(), "EnemyPopulation.ini")): Log(f"{name} contains Enemy Population Data.")
			else: raise FileNotFoundError
		except FileNotFoundError: Log(f"{name} is missing one or more necessary files, so it cannot be used."); PathRemovals.append(name)
	for remove in PathRemovals: del SavePaths[remove]
	if ReturnOne:
		if (not LookingForVictorFile) or ReturnOne != "Victory":
			if ReturnPathOnly and not LastUsed: return f"{os.path.join(sp_default, f"{ReturnOne}.ini")}"
			elif ReturnPathOnly and LastUsed: return f"{os.path.join(multisave["Last Used"]["path"], f"{ReturnOne}.ini")}"
			elif ReturnPathOnly and PredefinedSavePath: return f"{os.path.join(PredefinedSavePath, f"{ReturnOne}.ini")}"
		else:
			if ReturnPathOnly and not LastUsed: return f"{os.path.join(sp_default, "VICTOR.Y")}"
			elif ReturnPathOnly and LastUsed: return f"{os.path.join(multisave["Last Used"]["path"]), "VICTOR.Y"}"
			elif ReturnPathOnly and PredefinedSavePath: return f"{os.path.join(PredefinedSavePath, "VICTOR.Y")}"
	else:
		if ReturnPathOnly and not LastUsed and not PredefinedSavePath: Log("RETURNING PATH BASED ON GAME'S ROOT DIRECTORY"); return f"{os.path.join(sp_default, "Pinori.ini")}", f"{os.path.join(sp_default, "Runs.ini")}", f"{os.path.join(sp_default, "inventory.ini")}", f"{os.path.join(sp_default, "EnemyPopulation.ini")}"
		elif ReturnPathOnly and LastUsed and not PredefinedSavePath: Log("RETURNING PATH BASED ON LAST USED SAVE"); return f"{os.path.join(os.path.join(multisave["Last Used"]["path"]), "Pinori.ini")}", f"{os.path.join(os.path.join(multisave["Last Used"]["path"]), "Runs.ini")}", f"{os.path.join(os.path.join(multisave["Last Used"]["path"]), "inventory.ini")}", f"{os.path.join(os.path.join(multisave["Last Used"]["path"]), "EnemyPopulation.ini")}"
		elif ReturnPathOnly and PredefinedSavePath: Log(f"RETURNING PATH BASED ON PRE-DEFINED ONE (Pinori.ini: {os.path.join(PredefinedSavePath, "Pinori.ini")})"); return f"{os.path.join(PredefinedSavePath, "Pinori.ini")}", f"{os.path.join(PredefinedSavePath, "Runs.ini")}", f"{os.path.join(PredefinedSavePath, "inventory.ini")}", f"{os.path.join(PredefinedSavePath, "EnemyPopulation.ini")}"
	if len(SavePaths) != 0: Log(f"Usable Custom Paths: {len(SavePaths)}"); SaveFileChooser = ""
	else: print("There are no usable custom Save Paths. Defaulting to the game's root directory. Press any key to continue."); pause(); cls(); return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
	if LoadPrompt and MultipleSaves:
		if PredefinedSavePath is None:
			print("= Save Files =\n\n"+Fore.YELLOW+"Default"+Fore.WHITE); print("\n".join(SavePaths.keys()))
			while True:
				try: SaveFileChooser = input("\nPlease type the name of the Save Data group you want to load: "); CurrentSavePath = Path(SavePaths[SaveFileChooser if SaveFileChooser == "Default" else SaveFileChooser.lower()]).resolve() if SaveFileChooser != "Default" else sp_default
				except: print("Invalid Save Data group."); continue
				if SaveFileChooser != "Default": SaveFileChooser = SaveFileChooser.lower()
				if SaveFileChooser in SavePaths.keys() or SaveFileChooser == "Default":
					if SaveFileChooser != "Default": LastUsedSave = SavePaths[SaveFileChooser]
					else: LastUsedSave = sp_default
					break
				else: print("Invalid Save Data group."); continue
			if SaveFileChooser == "Default": print("Loading Save Data from the default path. Press any key to continue."); pause(); cls(); PinorINI, InventorINI, RunsINI, EnemyPopINI = os.path.join(Path(sp_default).resolve(), "Pinori.ini"), os.path.join(Path(sp_default).resolve(), "inventory.ini"), os.path.join(Path(sp_default).resolve(), "Runs.ini"), os.path.join(Path(sp_default).resolve(), "EnemyPopulation.ini"); return PinorINI, RunsINI, InventorINI, EnemyPopINI
			else: print(f"Loading Save Data from the {SaveFileChooser.lower()} group. Press any key to continue."); pause(); cls(); PinorINI, InventorINI, RunsINI, EnemyPopINI = os.path.join(Path(SavePaths[SaveFileChooser]).resolve(), "Pinori.ini"), os.path.join(Path(SavePaths[SaveFileChooser]).resolve(), "inventory.ini"), os.path.join(Path(SavePaths[SaveFileChooser]).resolve(), "Runs.ini"), os.path.join(Path(SavePaths[SaveFileChooser]).resolve(), "EnemyPopulation.ini"); return PinorINI, RunsINI, InventorINI, EnemyPopINI
		else: CurrentSavePath = PredefinedSavePath; return f"{os.path.join(PredefinedSavePath, "Pinori.ini")}", f"{os.path.join(PredefinedSavePath, "inventory.ini")}", f"{os.path.join(PredefinedSavePath, "Runs.ini")}", f"{os.path.join(PredefinedSavePath, "EnemyPopulation.ini")}"
	else:
		if not MultipleSaves: LastUsedSave = sp_default
		if not LastUsed:
			if not ReturnOne: return GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath()
			elif ReturnOne == "Pinori": return GetPinorINIPath()
			elif ReturnOne == "Runs": return GetRunsINIPath()
			elif ReturnOne == "Inventory": return GetInventorINIPath()
			elif ReturnOne == "EnemyPop": return GetEnemyPopINIPath()
		else:
			if not ReturnOne: return os.path.join(Path(LastUsedSave).resolve(), "Pinori.ini"), os.path.join(Path(LastUsedSave).resolve(), "Runs.ini"), os.path.join(Path(LastUsedSave).resolve(), "inventory.ini"), os.path.join(Path(LastUsedSave).resolve(), "EnemyPopulation.ini")
			elif ReturnOne == "Pinori": return os.path.join(Path(LastUsedSave).resolve(), "Pinori.ini")
			elif ReturnOne == "Runs": return os.path.join(Path(LastUsedSave).resolve(), "Runs.ini")
			elif ReturnOne == "Inventory": return os.path.join(Path(LastUsedSave).resolve(), "inventory.ini")
			elif ReturnOne == "EnemyPop": return os.path.join(Path(LastUsedSave).resolve(), "EnemyPopulation.ini")