def fakeGame():
	global sel, steps, HP, MaxHP, AdvText, RemainingSteps, ActiveQuirk, Quirk1, Quirk2, DualQMode, LocCode, Route, tef, caffeine, withdrawal, FocusedPlayer, encounter, Lightheadedness
	LocCode = "Pneumonoultramicroscopicsilicovolcanoconiosis"; Route = "Traditional"; population = 999999999 # HAHA hardcoded
	StepsNeeded = 100 if "Megalopolis" not in [Quirk1, Quirk2, ActiveQuirk] else 200; fakeoverworld = None; FocusedPlayer = "Pinori"
	BattleOrNot = 16; probability = random.randint(2,7); caffeine = 0; withdrawal = False; Lightheadedness = 0

	if AdvText == "Shown":
		print(f"You're in Pneumonoultramicroscopicsilicovolcanoconiosis Plateau. You have taken {steps} step{"s" if steps != 1 else ""} so far.")
		if RemainingSteps > 1: print(f"You have {RemainingSteps} more steps to take before ending your journey.")
		elif RemainingSteps == 1: print("You have 1 more step to take before ending your journey.")
		elif RemainingSteps == 0: print("You have made it to the end.")
		elif RemainingSteps < 0 and steps < (StepsNeeded*2): print("You've gone farther than you need to. That's a bad thing.")
		elif RemainingSteps < 0 and steps == (StepsNeeded*2): print("You see an object in the distance.")
		elif RemainingSteps < 0 and steps > (StepsNeeded*2): print("If you're grinding, now would be a good time to give up.")
		else: print("???")

	while BattleOrNot != probability:
		Advance = RemainingSteps <= 0
		try:
			print("\n1 - Step Forward\n2 - Items\n3 - Party\n4 - Switch Member\n5 - Save\n6 - Check Progress")
			if Advance is True: print("7 - End Journey")
			if steps == (StepsNeeded*2): print("8 - Object")
			fakeoverworld = int(input("\nYou chose ")); SoundCh.SFX.play(sel)
			if fakeoverworld == 1:
				steps += 1 if "Speedwalker" not in [ActiveQuirk, Quirk1, Quirk2] else 2; RemainingSteps = StepsNeeded - steps; Advance = RemainingSteps <= 0
				if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2]: probability, BattleOrNot = 1, 1; BON = "yes" if population != 0 else "no"
				else:
					coinflip = []; probability = int(round(50 * population / 30)) if population >= 1 else 0
					if Diff == "Easy": Max = 45
					elif Diff == "Hard": Max = 10
					elif Diff == "Tryhard": Max = 5
					elif Diff == "Normal": Max = 25
					BattleOrNot == 1 if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] else random.randint(1,Max)
					for _ in range(Max):
						if (DualQMode and ("Is it crowded in here?" not in [Quirk1, Quirk2])) or (DualQMode is False and ActiveQuirk != "Is it crowded in here?"):
							YesNo = random.randint(1,Max)
							if Max == 45: coinflip.append("yes") if YesNo in range(1,22) else coinflip.append("no")
							elif Max == 25: coinflip.append("yes") if YesNo in range(1,12) else coinflip.append("no")
							elif Max == 10: coinflip.append("yes") if YesNo in range(1,5) else coinflip.append("no")
						else: coinflip.append("yes") if population > 0 else coinflip.append("no")
					BON = "yes" if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] else random.choice(coinflip)
					coinflip.clear()
				try:
					if BON == "no": BattleOrNot = 16 if "Money is all you need" in [ActiveQuirk, Quirk1, Quirk2] else random.randint(1,Max)
					else: BattleOrNot = int(random.randint(1, Max))
				except (NameError, UnboundLocalError):
					SoundCh.SFX.play(tef); DebugPrint("Failed to setup BattleOrNot."); Max = 30 if Diff == "Easy" else 25 if Diff == "Normal" else 10 if Diff == "Hard" else 5
					BattleOrNot == 1 if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] else random.randint(1,Max)
				print("You take a step forward..."); time.sleep(2)
				if population != 0:
					if BON == "yes": DebugPrint("Battle time!"); SoundCh.SFX2.play(incoming); print("Enemy incoming!"); pause(); SoundCh.SFX2.stop(); EnterBattle()
					elif BattleOrNot in [8, 16, 32]: # it cannot say yes to a battle and say you spotted a shop on the same step
						if "Money is all you need" in [ActiveQuirk, Quirk1, Quirk2]: coin = True
						else: coinflip = random.randint(1,6); coin = coinflip in range(1,4) or population == 0
						print("You spot a shop, but it's closed. Aw man!") if coin else print("No enemies to be seen."); fakeoverworld = None
					elif BON == "no": print("No enemies to be seen."); fakeoverworld = None
					else: print("No enemies to be seen."); fakeoverworld = None
				else: print("No enemies to be seen."); fakeoverworld = None
			elif fakeoverworld == 2:
				pmem = input("Whose inventory would you like to check? "); print("Oh wait... you don't have an inventory." if pmem == getpass.getuser() else f"{pmem} is not a valid party member.")
			elif fakeoverworld == 3: print(f"Your party:\n{username}")
			elif fakeoverworld == 4: print("You're alone.")
			elif fakeoverworld == 5: print("Nuh-uh... what do you think you're doing?")
			elif fakeoverworld == 6:
				if AdvText == "Shown": fakeGame()
				else:
					print(f"Steps taken: {steps}/{StepsNeeded}")
					print(f"You're in Pneumonoultramicroscopicsilicovolcanoconiosis Plateau.\nThe population is infinite.")
					if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2]: print("The randomiser doesn't work here, dumbass.")
			elif fakeoverworld == 7 and Advance is True: AprilFoolEnd()
			elif fakeoverworld == 7 and Advance is False: print("You have not taken enough steps.")
			elif fakeoverworld == 8 and steps < (StepsNeeded*2): print("Hold your damn horses! Jeez! Didn't you play the tutorial???")
			elif fakeoverworld == 8 and steps == (StepsNeeded*2):
				print("You approach the object..."); time.sleep(3)
				print("... but instead of a joke, you got hit with a bunch of dead memes!"); time.sleep(4)
				Date = datetime.datetime.now(); year = Date.year; global crit
				deadmemes = ["DEEZ NUTS!", "DORITOS MTN DEW AIRHORN MLG", "360 NO SCOPE", f"VEGAS PRO 12 CRACK WORKING {year+random.randint(1,3)} (NOT CLICKBAIT)", "SPARTA NO BGM REMIX", "CAILLOU CRASHES HIS DAD'S CAR INTO A TREE (GROUNDED)", f"KLASKYKLASKYKLASKYKLASKY WINDOWS XP EDITED VERSION EFFECTS {random.randint(1,20)} SPONSORED BY PREVIEW 2B WINDOWS XP", "HAWK TUAH! SPIT ON THAT THANG!", "GEDAGEDIGEDAGEDAGO, I BEEN MARRIED A LONG TIME AGO! WHERE DID YOU COME FROM, WHERE DID YOU GO? WHERE DID YOU COME FROM, COTTON EYED JOE?", "BRRRR SKIBIDI DOP DOP DOP YES YES, SKIBIDI DOBIDI DIP DIP!", "RAISE YOUR YAYAYA!", "FREE FORTNITE VBUCKS TUTORIAL", "TRALALERO TRALALA", "WHEN THE IMPOSTOR IS... SUSSY???"]
				for i in range(12): SoundCh.BAT2.play(crit); print(random.choice(deadmemes)); time.sleep(0.1)
				time.sleep(3); print("Oh my God. The cringe is real. The cringe is so real that you didn't just take a free step forward, you took 10 FREE STEPS forward."); steps += 10; pause()
			elif overworld == 8 and steps > (StepsNeeded*2): print("No.")
		except ValueError as e: DebugPrint(e); randomBS = ["Input was not very cash money.", "Input did not compute.", "Input did not spit on my thang.", "Input was not a word from today's sponsor.", "Instructions unclear, accidentally built 12 shelves.", "Input was not a multistage aerobic capacity test that progressively gets more difficult as it continues.", "Input was not the bite of '87.", "Input was not an intern. I mean, integer.", "All this chitchat about integers, but nobody gives a damn about outegers. What's up with that???"]; print(random.choice(randomBS))
	fakeoverworld = None