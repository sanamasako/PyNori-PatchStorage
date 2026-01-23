def OptionsMenu():
	global config, AdvText, Diff, debug, cheating, cheatymccheatcheat, BatStat, sisas, OGsfx, MGtoggle, SplashText, PStoggle, MultipleSaves, ShowHPBars, PinorINI, RunsINI, InventorINI, EnemyPopINI
	try:
		if MultipleSaves: pass
	except: MultiSaveToggle()
	if not os.path.exists(PinorINI): print("Pinori.ini could not be found in the last used directory. Did you attempt to load an invalid Save Path?\nYour settings will be loaded from the default path to prevent the game from crashing.\nPress any key to continue."); PinorINI, RunsINI, InventorINI, EnemyPopINI = MultisaveHelper(LoadPrompt=False, LastUsed=True, ReturnPathOnly=True, PredefinedSavePath=os.getcwd()); pause()
	while True:
		cls(); CurrentKS = KillSystemSwitch(task="check"); checkStats(); print("= Options =\n")
		print(f"A - Weather Configuration\nB - Toggle Splash Texts (Currently {SplashText}.)\nC - Toggle Powerscaling (Currently {PStoggle}.)\nD - Toggle Multi-Save (Currently {MultipleSaves}.)\nE - Toggle Health Bars (Currently {ShowHPBars}.)")
		print(f"1 - Change Difficulty (Currently {Diff}.)")
		print(f"2 - Toggle Adventure Text (Currently {AdvText}.)")
		print(f"3 - Toggle Battle Stats (Currently {BatStat}.)")
		print("4 - I would like to skip to the end of the game because I haven't cheated enough today" if cheatymccheatcheat else "You are already cheating. Reload the game to disable cheating." if cheating == "YES" else "4 - I would like to cheat")
		print(f"5 - Toggle Debug Mode (Currently {debug}.)")
		print(f"6 - Change Kill System (Currently {CurrentKS}.)")
		print(f"7 - Show Innocence Score After Shadorako (SISAS) (Currently {sisas}.)")
		print(f"8 - Original Sound Effects (Currently {OGsfx}.)")
		print(f"9 - Toggle Minigames (Currently {MGtoggle}.)")
		print("0 - Return to Title Screen\n")
		try:
			OptInp = input("You chose "); SoundCh.SFX.play(sel)
			if OptInp in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]: OptInp = int(OptInp)
			if OptInp in ["a", "b", "c", "d", "e"]: OptInp = OptInp.upper()
			if OptInp not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "a", "B", "b", "C", "c", "D", "d", "E", "e"]: raise ValueError
		except ValueError: print("Please choose either A/B/C/D/E or a single digit number."); pause(); continue
		options = {"A": WeatherOptions, "B": SplashTextToggle, "C": PowerscaleToggle, "D": MultiSaveToggle, "E": HealthBarsToggle, 1: DiffChanger, 2: AdvTextToggle, 3: BatStatToggle, 4: CheatChance if cheating == "NO" else lambda: print("You are already cheating."), 5: lambda: not debug, 6: KillSystemSwitch, 7: SISAS, 8: ogSFX, 9: ToggleMG, 0: TitleScreen}
		if OptInp in options:
			if OptInp not in [5, 6]:
				if options[OptInp].__code__.co_argcount > 0: options[OptInp](config) # ChatGPT is crazy good, I had no idea this existed whatttt
				else: options[OptInp]()
			elif OptInp == 6: KillSystemSwitch(task="toggle")
			else: debug = not debug
		else: print("Please choose a single digit number."); pause()