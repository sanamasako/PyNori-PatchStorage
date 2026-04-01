def TitleScreen():
	global ThereIsSave, LoadErrors, sel, debug, EnemyPop, EnemyPopINI; EnemyPopINI = MultisaveHelper(ReturnOne="EnemyPop", ReturnPathOnly=True, LastUsed=True)
	global Quirk1, Quirk2, ActiveQuirk, DualQMode; ReprintOGTS() # how about instead of two versions of the same title screen, there be ONE title screen?
	global CurrentSavePath; CurrentSavePath = None
	while True:
		try:
			tsChoice = input("You chose number ")
			if tsChoice not in ["4r", "4R"]: UnixForceCanon(); tsChoice = int(tsChoice)
			SoundCh.SFX.play(sel)
		except (ValueError, UnboundLocalError): print("Please select a number. Press any key to retry."); pause()
		except KeyboardInterrupt: print("\nSending keyboard interrupts is disallowed here to prevent breaking the game.\nIf you would like to quit, please select 0. Press any key to continue."); pause()
		else:
			if tsChoice not in [1, 2, 3, 4, 5, 6, 7, 0, "4r", "4R"]: print("Please select a number from 1-6. Press any key to retry."); pause()
			elif tsChoice == 1:
				global RemainingSteps, bababooey, aprilfool, nospook, SpookyTime; SpookyTime = False
				RemainingSteps = 100 if not "Megalopolis" in [Quirk1, Quirk2, ActiveQuirk] else 200
				Date = datetime.datetime.now(); month = Date.month; day = Date.day
				if month == 4 and day == 1 and aprilfool and (no_fool is False): # IT'S APRIL FOOOOOOOOL
					correctanswer = "yes" if random.randint(1,2) == 1 else "no"; answer = ""
					if args.debug: print(Fore.YELLOW + f"DEBUG: the answer is {correctanswer} you dingus how could you get that wrong")
					while answer.lower() not in ["y", "yes", "yeah", "n", "no", "nah", "nope"]: answer = input("!? [Y/N] ")
					if (answer.lower() in ["y", "yes", "yeah"] and correctanswer == "yes") or (answer.lower() in ["n", "no", "nah", "nope"] and correctanswer == "no"):
						bababooey = True; global HP, MaxHP, atk, defense, VocalPoints, Lvl
						if "God Mode" not in [ActiveQuirk, Quirk1, Quirk2]: MaxHP = 300; HP = MaxHP; Lvl, atk, defense = 1, 15, 20; VocalPoints = 200
						else: MaxHP = 9999999999999999999999999999999999; HP = MaxHP; atk, defense, Lvl = 999, 999, 999; VocalPoints = 10000000

						if os.path.exists(EnemyPopINI) and os.path.exists(GetCustomFilePath("Enemy.json")):
							Log("Loading enemy populations.")
							with open(GetCustomFilePath("Enemy.json"), 'r', encoding='utf-8') as enemypop: Enemies = json.load(enemypop)

							EnemyNames = Enemies.keys(); EnemyPop = {}
							for name in EnemyNames: EnemyPop[name.title() if name not in ["Hot Tin Can't", "Tin Can't", "Pam the Clam"] else "Hot Tin Can't" if name.title() == "Hot Tin Can'T" else "Tin Can't" if name.title() == "Tin Can'T" else "Pam the Clam" if name.title() == "Pam The Clam" else name.title()] = -1
							for name in EnemyPop:
								if name in ["Hot Tin Can't", "Tin Can't", "Pam the Clam", "Treble"]: EnemyPop[name] = 1
						fakeGame()
					else: print("You must be fun at parties."); pause(); bababooey = False
				elif (month == 10 and day == 31 and (not nospook)): # ISSA SPOOKY... DAY
					print("Despite the game not having started yet, you hear the wind call your name..."); answer = ""
					while answer not in ["y", "yes", "yeah", "n", "no", "nah", "nope"]: answer = input("(Will you listen to the wind?) [Y/N] ").lower()
					if answer in ["y", "yes", "yeah"]: print("Suddenly, you feel like you're being teleported somewhere...!"); pause(); SpookyTime = True; cls(); HalloInstructions()
					else: print("You ignore the wind and stick to playing the main game."); pause()
				newGame(); print("what"); os._exit(0)
			elif tsChoice == 2: OptionsMenu()
			elif tsChoice == 3: cred()
			elif tsChoice == 4: Log(f"{os.path.join(Path(LastUsedSave), "VICTOR.Y")}: {str(os.path.exists(os.path.join(Path(LastUsedSave), "VICTOR.Y")))}"); randQuirk() if not os.path.exists(os.path.join(Path(LastUsedSave).resolve(), "VICTOR.Y")) else randQuirk_dual()
			elif tsChoice in ["4r", "4R"]: # can't use .lower() because it'll crash if tsChoice is an integer
				if not (ActiveQuirk == "NONE" and Quirk1 == "NONE" and Quirk2 == "NONE"): ActiveQuirk, Quirk1, Quirk2 = "NONE", "NONE", "NONE"; print("All quirks have been turned off.")
				else: print("Quirks are already off.")
			elif tsChoice == 5: SaveOverview()
			elif tsChoice == 6: PlayMinigamesForFun()
			elif tsChoice == 7: DailyChallengeMenu()
			elif tsChoice == 0: os._exit(0)