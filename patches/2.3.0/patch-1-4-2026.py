def gameThing():
	global location, LocCode, steps, KikuStep, TanpopoStep, NodiumStep, OceanStep, ArchlekiaStep, TanggalStep, DyarixStep, Tones, FocusedPlayer, LocVisits, LocPop, MGtoggle, isnewgame, WeatherEnabled, TempMeasurement, AlreadyDecrementedLightheadedness; AlreadyDecrementedLightheadedness = False
	global Advance, MaxHP, HP, Party, PopFocus, BattleOrNot, probability, overworld, ActiveQuirk, Quirk1, Quirk2, fakeprob, Diff, debug, TotalPossibleKills, population, npckills, LastUsedSave, Lightheadedness, important, inventory, CurrentSavePath, CharTasks
	global sel, Tone, end, bababooey, Route, ToneStates, tef, yamiclear, ShopStats, heal, burn, buzzer, ItemCosts, shado_guards_clear, shado_archlekia_clear, krystalclear, LoreSnippetStates, OWSecretStates, WeirdStuffStates; HealZone, PainZone = False, False
	global thunder, wind, frozen # weather sounds
	if location == "Shadorako's Lair" or LocCode == "Cathedral": cathedralThing()
	try:
		if end: pass
	except: end = False
	try:
		if MGtoggle: pass
	except: MGtoggle = True

	if FocusedPlayer not in Party: SoundCh.SFX.play(bell); print(Fore.RED + "Focused player is not in your party. You are now playing as Pinori."); pause(); SwitchMember(SilentSwitch="Pinori", Forced=True, SwitchingBeforeBoss=True)
	overworld, BattleOrNot, PopFocus, CurPop, probability, areas, AreaData, LocCode, StepsNeeded, RemainingSteps, Advance = DoVeryImportantGameRelatedThings()
	if AdvText == "Shown":
		if len(Party) > 1 and FocusedPlayer != "Pinori": print(f"You're playing as {FocusedPlayer}.{f" {FocusedPlayer} is lightheaded, so you cannot read menus properly." if Lightheadedness > 0 else ""}")
		ScramblePrint(f"You're in {location}. You have been here {LocVisits[LocCode]} time{'s' if LocVisits[LocCode] != 1 else ''} this session. You have taken {steps} step{'s' if steps != 1 else ''} so far." if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2] else f"You're in {location}. You have taken {steps} step{'s' if steps != 1 else ''} so far.")
		if RemainingSteps > 0:
			if steps not in [15, 16] or location != "Archlekia": ScramblePrint(f"You have {RemainingSteps} more step{"s" if RemainingSteps != 1 else ""} to take{" before proceeding to the next area" if location != "Dyarix" else ""}.")
			elif shado_guards_clear and steps in [15, 16] and location == "Archlekia": ScramblePrint(f"The coast is clear.{".. of guards, at least.\n" if population > 0 else " "}(You have {RemainingSteps} more steps to take before proceeding to the next area.)")
			elif not shado_guards_clear and steps == 15 and location == "Archlekia": ShadoGuardBattleIntro()
			# I have NO clue why I have to make an else branch specific to when you're reloading after defeating Shadorako's Guards but oh well
			elif location == "Archlekia" and steps == 16: ScramblePrint(f"The coast is clear.{".. of guards, at least.\n" if population > 0 else " "}(You have {RemainingSteps} more steps to take before proceeding to the next area.)")
		elif RemainingSteps == 0: ScramblePrint(f"You have walked far enough{" to proceed to the next area" if location != "Dyarix" else ""}.")
		elif RemainingSteps < 0 and steps < (StepsNeeded*2): ScramblePrint("You've gone farther than you need to. Not like that's a bad thing.")
		elif RemainingSteps < 0 and steps == (StepsNeeded*2): ScramblePrint("You see a shiny object in the distance.")
		elif RemainingSteps < 0 and steps > (StepsNeeded*2) and population == 0: Yami() if steps == (StepsNeeded*2)+1 and (kills + npckills) >= 5 and location == "Kiku Village" else ScramblePrint("Nothing of interest left here.")
		elif RemainingSteps < 0 and steps > (StepsNeeded*2) and population != 0:
			if RemainingSteps < 0 and steps == ((StepsNeeded*2)+1) and location == "Kiku Village": Yami() if (kills + npckills == 0) or (kills + npckills >= 5) else ScramblePrint("A black-haired girl watches you from a distance. She's not happy.")
			else: ScramblePrint("Unless you're grinding, now would be a good time to move on.")
		else: print("???")
		if Route != "Traditional": ScramblePrint(f"The population is {LocPop[f"Live{LocCode}Pop"]}.", c="red" if Route == "Omnicide" else "white")
	try:
		if end: ScramblePrint(f"Selecting 7 will end your journey.{" You may need a Demotion (item) to continue collecting the Tones." if Route == "Traditional" and Tones != 7 else ""}")
	except (UnboundLocalError, NameError) as e:
		if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2]: Log(f"DUMB THING HAPPENED WITH THE RANDOMISER THINGITY THING: {e}"); SoundCh.SFX.play(tef); end = False
	if AdvText == "Shown": print()
	if args.debug: print(Fore.YELLOW + f"DEBUG: Location: {location}, Location Code: {LocCode}, Steps Taken: {steps}, Steps needed to pass Kiku Village: {KikuStep} (should be 10), Steps needed to pass Tanpopo Town: {TanpopoStep} (should be 12), Steps needed to pass Nodium Valley: {NodiumStep} (should be 20), Steps needed to pass Crystalline Oceanfront: {OceanStep} (should be 25), Steps needed to pass Archlekia: {ArchlekiaStep} (should be 30), Steps needed to pass Tanggal Volcano: {TanggalStep} (should be 35), Steps needed to pass Dyarix: {DyarixStep} (should be 50), MaxHP: {MaxHP}, Able to Advance?: {Advance}, HP: {HP}, Population Focus: {PopFocus}, BattleOrNot (determines whether or not the player enters battle): {BattleOrNot}, probability (the chances of entering battle, BattleOrNot must match this value to trigger a battle): {probability}"); print()
	while BattleOrNot != probability or overworld is None:
		if steps == (StepsNeeded*2)+1 and (kills + npckills) in [0, 5] and location == "Kiku Village": Yami() # I can't believe I have to copypaste everything improtant just because the other bits of code decided they didn't want to work anymore. awesome
		try:
			for opt in ["A - Healing Zone" if HealZone else Fore.RED + "A - Pain Zone" if PainZone else "", "1 - Step Forward", "2 - Items", "3 - Party", "4 - Switch Member", "5 - Save", "6 - Check Progress", "7 - Continue Mission" if Advance else "", "8 - Shiny Object" if steps == StepsNeeded * 2 else "", "0 - Exit"]:
				if not opt: continue
				colour = (Fore.GREEN if "Healing Zone" in opt else Fore.RED if "Pain Zone" in opt else Fore.WHITE)
				if Lightheadedness > 0: text = ''.join(random.sample(opt, len(opt)))
				else: text = opt if ("Healing Zone" not in opt and "Pain Zone" not in opt) else Fore.GREEN + opt if "Pain Zone" not in opt else Fore.RED + opt
				print(colour + text)
			overworld, BattleOrNot, PopFocus, CurPop, probability, areas, AreaData, LocCode, StepsNeeded, RemainingSteps, Advance = DoVeryImportantGameRelatedThings()
			overworld = input("\nYou chose "); overworld = int(overworld) if overworld.isdigit() else overworld; SoundCh.SFX.play(sel); Log(f"Player chose {overworld}."); SkipFunctionality = False
			if Lightheadedness > 0 and not AlreadyDecrementedLightheadedness:
				if Lightheadedness-1 == 0: print(f"{FocusedPlayer} is no longer lightheaded! You can now read clearly again."); pause()
				Lightheadedness -= 1 if Lightheadedness != 0 else 0; AlreadyDecrementedLightheadedness = True
			if overworld == 1:
				if HealZone:
					hz = ""
					while hz.lower() not in ["y", "n", "ye", "nah", "no", "yes", "nope", "yeah", "sure", "nuh-uh", "hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
						hz = input("Are you sure you want to skip the Healing Zone? [Y/N] ").lower()
						if hz in ["y", "ye", "yes", "yeah", "sure"]: break # I don't think things like return, continue, or break can be used to make one-liners so sadly this has to be like this WAAA
						elif hz in ["n", "no", "nope", "nuh-uh", "hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
							if hz in ["hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]: print("You didn't have to be rude about it. Jeez.")
							SkipFunctionality = True
						else: print("Invalid input.")
				elif PainZone: print("Sorry! Pain Zones are mandatory. Please take damage before taking your next step."); continue
				if SkipFunctionality: continue
				for char in Party:
					if char in ["Pinori", "Millie"]: continue
					if CharTasks[char].state == "away": CharTasks[char].UpdateDistance()
				if TimeSpecificBonus() == "0x25" and not LoreSnippetStates[TimeSpecificBonus()] and random.randint(1,5) == 3: LoreSnippetStates[TimeSpecificBonus()] = True; SoundCh.SFX.play(important); print("What's this...? https://pastebin.com/raw/nsSTFgtA"); pause() # I bet you like spoiling secrets don't you? You don't like waiting to encounter these legitimately, do you? Yeah, I caught you red-handed, Cheaty McCheaterson.
				elif TimeSpecificBonus() == "0x27" and not LoreSnippetStates[TimeSpecificBonus()] and random.randint(1,5) == 2: LoreSnippetStates[TimeSpecificBonus()] = True; SoundCh.SFX.play(important); print("What's this...? https://pastebin.com/raw/A1fsgKuy"); pause()
				elif TimeSpecificBonus() == "0x29" and not LoreSnippetStates[TimeSpecificBonus()] and random.randint(1,5) == 4: LoreSnippetStates[TimeSpecificBonus()] = True; SoundCh.SFX.play(important); print("What's this...? https://pastebin.com/raw/DixDFQbc"); pause()
				elif TimeSpecificBonus() == "0x30" and not OWSecretStates[TimeSpecificBonus()] and random.randint(1,10) == 6:
					OWSecretStates[TimeSpecificBonus()] = True; CharInvFull = {c: all(item != "None" for item in inventory[c].values()) for c in Party if c != "Yami"}; Destination = next((c for c, full in CharInvFull.items() if not full), None)
					if not Destination: print(f"You find a Foreign Stimulant sitting on top of a {"flower" if LocCode in ["Kiku", "Tanpopo"] else "stone" if LocCode in ["Nodium", "Archlekia", "Tanggal", "Dyarix"] else "seashell" if LocCode == "Ocean" else "shmunguss"}, but nobody can hold it, so you walked right past it."); pause()
					else:
						for slot, item in inventory[Destination].items():
							if item == "None": inventory[Destination][slot] = "Foreign Stimulant"; print(f"{Destination} found a Foreign Stimulant! They put it in {slot}."); pause(); break
				elif TimeSpecificBonus() == "0x32" and not OWSecretStates[TimeSpecificBonus()] and random.randint(1,10) == 2:
					OWSecretStates[TimeSpecificBonus()] = True; CharInvFull = {c: all(item != "None" for item in inventory[c].values()) for c in Party if c != "Yami"}; Destination = next((c for c, full in CharInvFull.items() if not full), None)
					if not Destination: print(f"You find an Item Coupon sitting on top of a {"flower" if LocCode in ["Kiku", "Tanpopo"] else "stone" if LocCode in ["Nodium", "Archlekia", "Tanggal", "Dyarix"] else "seashell" if LocCode == "Ocean" else "shmunguss"}, but nobody can hold it, so you walked right past it."); pause()
					else:
						for slot, item in inventory[Destination].items():
							if item == "None": inventory[Destination][slot] = "Item Coupon"; print(f"{Destination} found an Item Coupon! They put it in {slot}."); pause(); break
				elif TimeSpecificBonus() == "0x36" and not OWSecretStates[TimeSpecificBonus()] and random.randint(1,10) == 9:
					OWSecretStates[TimeSpecificBonus()] = True; CharInvFull = {c: all(item != "None" for item in inventory[c].values()) for c in Party if c != "Yami"}; Destination = next((c for c, full in CharInvFull.items() if not full), None)
					if not Destination: print(f"You find a Shepard Tone sitting on top of a {"flower" if LocCode in ["Kiku", "Tanpopo"] else "stone" if LocCode in ["Nodium", "Archlekia", "Tanggal", "Dyarix"] else "seashell" if LocCode == "Ocean" else "shmunguss"}, but nobody can hold it, so you walked right past it."); pause()
					else:
						for slot, item in inventory[Destination].items():
							if item == "None": inventory[Destination][slot] = "Shepard Tone"; print(f"{Destination} found a Shepard Tone! They put it in {slot}."); pause(); break
				elif TimeSpecificBonus() == "0x42" and not OWSecretStates[TimeSpecificBonus()] and random.randint(1,10) == 7:
					OWSecretStates[TimeSpecificBonus()] = True; CharInvFull = {c: all(item != "None" for item in inventory[c].values()) for c in Party if c != "Yami"}; Destination = next((c for c, full in CharInvFull.items() if not full), None)
					if not Destination: print(f"You find a Stepper sitting on top of a {"flower" if LocCode in ["Kiku", "Tanpopo"] else "stone" if LocCode in ["Nodium", "Archlekia", "Tanggal", "Dyarix"] else "seashell" if LocCode == "Ocean" else "shmunguss"}, but nobody can hold it, so you walked right past it."); pause()
					else:
						for slot, item in inventory[Destination].items():
							if item == "None": inventory[Destination][slot] = "Stepper"; print(f"{Destination} found a Stepper! They put it in {slot}."); pause(); break
				elif TimeSpecificBonus() == "0x45" and not OWSecretStates[TimeSpecificBonus()] and random.randint(1,10) == 4:
					OWSecretStates[TimeSpecificBonus()] = True; CharInvFull = {c: all(item != "None" for item in inventory[c].values()) for c in Party if c != "Yami"}; Destination = next((c for c, full in CharInvFull.items() if not full), None)
					if not Destination: print(f"You find an AUX Cord Energy Drink sitting on top of a {"flower" if LocCode in ["Kiku", "Tanpopo"] else "stone" if LocCode in ["Nodium", "Archlekia", "Tanggal", "Dyarix"] else "seashell" if LocCode == "Ocean" else "shmunguss"}, but nobody can hold it, so you walked right past it."); pause()
					else:
						for slot, item in inventory[Destination].items():
							if item == "None": inventory[Destination][slot] = "AUX Cord Energy Drink"; print(f"{Destination} found an AUX Cord Energy Drink! They put it in {slot}."); pause(); break
				elif TimeSpecificBonus() == "0x17" and not WeirdStuffStates[TimeSpecificBonus()] and random.randint(1,20) == 16: WeirdStuffStates[TimeSpecificBonus()] = True; AutomatedFauxBattle(); continue
				elif TimeSpecificBonus() == "0x19" and not WeirdStuffStates[TimeSpecificBonus()] and random.randint(1,20) == 17: WeirdStuffStates[TimeSpecificBonus()] = True; print("You take a step to the left..."); time.sleep(2); print("You take a step backward..."); time.sleep(2); print("You take a step to the right..."); time.sleep(2); print("You take a step forward..."); time.sleep(2); print("WOW! It's a miracle!"); time.sleep(2); print("You're not misaligned."); time.sleep(2); print("Anyway..."); time.sleep(2)
				elif TimeSpecificBonus() == "0x1a" and not WeirdStuffStates[TimeSpecificBonus()] and random.randint(1,20) == 18:
					WeirdStuffStates[TimeSpecificBonus()] = True; print("A disembodied voice provides feedback about your current state...")
					if HP >= MaxHP: print("???: You're doing just fine!")
					elif HP >= round(MaxHP*6/7): print("???: You're doing great!")
					elif HP >= round(MaxHP/2): print("???: You're doing okay!")
					elif HP >= round(MaxHP/7): print("???: You could be doing better... consider healing soon!")
					elif HP > 0: print("???: Consider healing soon...")
					elif HP <= 0: print("???: You look terribly out of shape... you're in dire need of a healing item!")
					else: print("???: This is an error... the developer of this game truly is an idiot, isn't she?")
					pause(); print("Before you can ask the disembodied voice what it's talking about, you feel its presence fade out."); pause(); print("What was that...?"); pause()
				elif TimeSpecificBonus() == "0x1f" and not WeirdStuffStates[TimeSpecificBonus()] and random.randint(1,20) == 8:
					OWSecretStates[TimeSpecificBonus()] = True; CharInvFull = {c: all(item != "None" for item in inventory[c].values()) for c in Party if c != "Yami"}; Destination = next((c for c, full in CharInvFull.items() if not full), None)
					if not Destination: print(f"You find a Pocket Shop sitting on top of a {"flower" if LocCode in ["Kiku", "Tanpopo"] else "stone" if LocCode in ["Nodium", "Archlekia", "Tanggal", "Dyarix"] else "seashell" if LocCode == "Ocean" else "shmunguss"}, but nobody can hold it, so you walked right past it."); pause()
					else:
						for slot, item in inventory[Destination].items():
							if item == "None": inventory[Destination][slot] == "Pocket Shop"; print(f"{Destination} found a Pocket Shop! They put it in {slot}."); pause(); break
				elif TimeSpecificBonus() == "0x20" and not WeirdStuffStates[TimeSpecificBonus()] and random.randint(1,20) == 20:
					WeirdStuffStates[TimeSpecificBonus()] = True; print("A disembodied voice comments on your surroundings...")
					if LocCode == "Kiku": print("???: Ahh... chrysanthemums. The most fun flower name to say aloud...")
					elif LocCode == "Tanpopo": print("???: Ahh... dandelions. One of the sillier kinds of flowers...\n???: They have lion in their name, yet they look nothing like lions. I wonder where the name came from...")
					elif LocCode == "Nodium": print("???: Such tall mountains... I wonder what the peaks have in store...\n???: Something? Nothing? The only way to find out is to climb... how mysterious...")
					elif LocCode == "Ocean": print("???: Isn't the beach such a relaxing place? It would be so much better if the wildlife weren't so hostile...")
					elif LocCode == "Archlekia": print("???: Mmmm, Koridya. The home of a certain not-so-friendly Archlekian demon... I'd be careful if I were you...")
					elif LocCode == "Tanggal": print("???: Mmm, being around volcanoes must feel like living in a furnace. I would rather become an ice cube...")
					elif LocCode == "Dyarix": print("???: Hmmm, I hear the Dyarian night sky offers scenery that rivals even the Aurora Borealis...")
					pause(); print("Before you can reply to the disembodied voice's commentary, you feel its presence fade out."); pause(); print("What was that...?"); pause()
				elif TimeSpecificBonus() == "0x22" and not WeirdStuffStates[TimeSpecificBonus()] and random.randint(1,20) == 2:
					WeirdStuffStates[TimeSpecificBonus()] = True; print(f"{"Everyone's inventories shuffle" if len(Party) > 1 else "Your inventory shuffles"} spontaneously!")
					for char, slots in inventory.items():
						vals = list(slots.values()); random.shuffle(vals)
						for key, newval in zip(slots.keys(), vals): slots[key] = newval
				HealZone, PainZone = False, False; steps += 1 if "Speedwalker" not in [ActiveQuirk, Quirk1, Quirk2] else 2; Log(f"Steps: {steps}")
				RemainingSteps = StepsNeeded - steps; Log(f"Remaining steps: {RemainingSteps}")
				Advance = RemainingSteps <= 0; Log(f"Can Advance yet?: {Advance}")
				population = int(CurPop); Log(f"Population: {CurPop}")
				if "Time Crunch" in [ActiveQuirk, Quirk1, Quirk2] and RemainingSteps < 0 and yamiclear and location == "Kiku Village": print("I wouldn't do that if I were you."); return
				if "Time Crunch" in [ActiveQuirk, Quirk1, Quirk2] and RemainingSteps < population: SoundCh.SFX.play(buzzer); print("TIME'S UP!"); time.sleep(1); GameOver(TimeUp=True)
				# iicih
				if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2]: probability, BattleOrNot = 1, 1; BON = "yes" if population != 0 else "no"; Max = 45 if Diff == "Easy" else 10 if Diff == "Hard" else 25
				else:
					coinflip = []; probability = int(round(50 * population / 30)) if population >= 1 else 0
					Log(f"Probability of entering battle (not measured by a particular unit, it's just an integer because of course it is): {probability}"); Max = 45 if Diff == "Easy" else 10 if Diff == "Hard" else 25
					Log(f"Range max is {Max} because the difficulty is set to {Diff}.")
					BattleOrNot = 1 if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] else random.randint(1,Max)
					for _ in range(Max):
						if population != 0:
							if (DualQMode is True and Quirk1 != "Is it crowded in here?" and Quirk2 != "Is it crowded in here?") or (DualQMode is False and ActiveQuirk != "Is it crowded in here?"): YesNo = random.randint(1,Max); coinflip.append("yes" if YesNo in range(1,round(Max/2)) else "no")
							else: coinflip.append("yes") if population > 0 else coinflip.append("no")
						else: coinflip.append("no") # if there's nobody left it'll just spam no in the coinflip list
					BON = "yes" if population != 0 and "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] else "no" if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] and population == 0 else random.choice(coinflip)
					Log(f"Will encounter an enemy this turn: {BON}"); coinflip.clear()
				try:
					if BON == "no": BattleOrNot = 16 if "Money is all you need" in [ActiveQuirk, Quirk1, Quirk2] else random.randint(1,Max)
					else: BattleOrNot = int(random.randint(1, Max))
				except (NameError, UnboundLocalError) as e:
					SoundCh.SFX.play(tef); Log(f"Encountered an error while setting up BattleOrNot: {e}")
					if args.debug: print(Fore.YELLOW + "Failed to setup BattleOrNot.")
					Max = 45 if Diff == "Easy" else 10 if Diff == "Hard" else 25
					BattleOrNot = 1 if "Is it crowded in here?" in [ActiveQuirk, Quirk1, Quirk2] else random.randint(1,Max)
				Log(f"Battle Or Not: {BattleOrNot}")
				fakeprob = 1 if population == 0 else 0
				print("You take a step forward..."); Weather = BuildWeather(Silent=True) if WeatherEnabled else None
				time.sleep(2 if not WeatherEnabled else 0) # loading a website takes a while, so we don't want to add 2 seconds of artificial loading time on top of that
				if Weather:
					try:
						ThunderChance = random.randint(1,15300); WindChance = random.randint(1,5)
						if WeatherEnabled: Log(f"Weather Conditions: {Weather["Conditions"]}")
						if "thunder" in Weather["Conditions"] and ThunderChance == 12345: SoundCh.WTHR.play(thunder); SoundCh.BAT2.play(crit); print(f"{FocusedPlayer} was struck by lightning!!!"); pause(); HP = 0
						elif "thunder" in Weather["Conditions"] and ThunderChance != 12345: Log(f"Thunder Chance: {ThunderChance} (if you're seeing this, you DIDN'T get struck by lightning, you're welcome)")
						if Weather[f"TempState{TempMeasurement[0].upper()}"] in ["mild heat", "moderate heat", "extreme heat"] and WindChance == 1:
							Range = [1,3] if Weather[f"TempState{TempMeasurement[0].upper()}"] == "mild heat" else [2,6] if Weather[f"TempState{TempMeasurement[0].upper()}"] == "moderate heat" else [8,15]
							if HP > 0: HeatDMG = random.randint(Range[0],Range[1]); SoundCh.SFX.play(burn); HP = max(HP-HeatDMG,0); print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} took {HeatDMG} damage from the heat.")
							else: print(f"The heat continues to burden {"you" if len(Party) == 1 or FocusedPlayer == "Pinori" else FocusedPlayer}, but {"you" if FocusedPlayer == "Pinori" else "they"} can't take anymore damage because {"you" if FocusedPlayer == "Pinori" else "they"}'re unconscious...")
						else: Log("No heat effect. You're welcome!") #		the reason I did this is because mild heat isn't included in the conditions for the sunny flag
						if Weather["Wind"] in ["calm", "breezy"] and (Weather[f"TempState{TempMeasurement[0].upper()}"] == "mild heat" or "sunny" in Weather["Conditions"]) and WindChance == 3: Refresher = max(round(int(Wind(BuildWeather(ReturnCurrent=True),ReturnKmph=True)))/2,1); HP = min(HP+round(Refresher),MaxHP); SoundCh.SFX.play(heal); SoundCh.WTHR.play(wind); print(f"The wind feels {"nice" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "mild heat" else "great" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "moderate heat" else "amazing"} in the {Weather[f"TempState{TempMeasurement[0].upper()}"]}. {"You" if FocusedPlayer == "Pinori" else FocusedPlayer}{f" recovered {round(Refresher)} HP" if HP < MaxHP else f"{"r" if FocusedPlayer == "Pinori" else "'s"} HP was maxed out"}!"); pause()
						elif Weather["Wind"] in ["windy", "powerful wind"] and WindChance == 3:
							steps -= max(round(int(Wind(BuildWeather(ReturnCurrent=True),ReturnKmph=True)))/11,1); SoundCh.WTHR.play(wind); print(f"Today's winds are so strong that they managed to push {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} back by {max(round(int(Wind(BuildWeather(ReturnCurrent=True),ReturnKmph=True)))/11,1)} steps!"); pause()
							steps = 0 if steps < 0 else steps
						elif Weather["Wind"] == "deadly wind" and WindChance == 2: steps = 0; SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); print("Today's winds are "+Fore.RED+"DEADLY"+Fore.WHITE+f"!!! The sudden hurricane-like gust sends you{"r party" if len(Party) > 1 else ""} FLYING back to the beginning of the area!"); pause()
						else: Log("No wind effect. You're welcome!")
						if "snow" in Weather["Conditions"]:
							SFP = SnowStepFailCalc(TempMeasurement[0], Weather["Rain"], Weather[f"Temp{globals()["TempMeasurement"][0]}"], Challenge=True); StepFail = random.randint(1,100)
							if StepFail <= SFP: SoundCh.SFX.play(frozen); print(f"Due to the {"freezing " if Weather[f"TempState{TempMeasurement[0]}"] in ["deadly cold", "extreme cold"] else ""}cold, you {"found yourself unable to move" if Weather[f"TempState{TempMeasurement[0]}"] in ["deadly cold", "extreme cold"] else "couldn't move a full step forward"}."); steps -= 1 if steps > 0 else 0; pause(); continue
						else: Log("No snow effect. You're welcome!")
					except Exception as e: SoundCh.SFX.play(tef); Log(f"Weather logic error: {e}")
				if population != 0:
					if BON == "yes": # honestly after that rewrite I doubt the probability thing even matters now (update: apparently it did)
						if args.debug: print(Fore.YELLOW + "DEBUG: Battle time!")
						print("Enemy incoming!"); pause(); Log("Entering battle."); EnterBattle()
					elif BattleOrNot in [8, 16, 32]: # it cannot say yes to a battle and say you spotted a shop on the same step
						if "Money is all you need" in [ActiveQuirk, Quirk1, Quirk2]: coin = True
						else:
							# I love convoluted RNG
							# no seriously WHAT THE HELL AM I DOING LMFAO
							Log("Determining if you will encounter a shop.")
							Max = 45 if Diff == "Easy" else 10 if Diff == "Hard" else 25
							coinmax = random.randint(6,Max); Log(f"Coinflip max is {coinmax}."); coinflip = random.randint(1,coinmax); Log(f"Coin (more like dice) rolled a(n) {coinflip}.")
							rangefloor = round(coinmax/7); Log(f"Range floor is {rangefloor}.")
							if coinflip in range(rangefloor,coinmax): Log(f"{coinflip} is in range {rangefloor}-{coinmax}. You will not encounter a shop."); coin = False
							elif coinflip in range(1,rangefloor): Log(f"{coinflip} is in range 1-{rangefloor}! You will encounter a shop."); coin = True
							else:
								if population != 0: Log("A failsafe went off. You will not encounter a shop."); coin = False
								else: Log("A failsafe went off. You will encounter a shop."); coin = True # what am I doing
						if coin:
							Log("Encountered a shop.")
							if args.debug:
								print(Fore.YELLOW + "DEBUG: Shop time!")
								if BON == "yes" and coin: print(Fore.YELLOW + "DEBUG: DAMN IT")
							shop = ""; TotalPop = 0
							for area in LocPop:
								Log(f"Checking population for area {area}.")
								if area != "LivePneumonoultramicroscopicsilicovolcanoconiosisPop": Log(f"Population is {LocPop[area]}."); TotalPop += LocPop[area]; Log(f"Total population is now {TotalPop}.")
								else: Log("Area is from the April Fools' event. Ignoring.")
							if ShopStats[LocCode] == "banned" and TotalPop > 0:
								word = "Pinori's" if FocusedPlayer != "Pinori" else "your"
								print(f"You spot a shop. However, on the front door is a poster showing {word} face with a no entry sign over it. Yikes.\n(You took a free step forward.)"); overworld = None; continue
							while shop.lower() not in ["y", "n", "ye", "nah", "no", "yes", "nope", "yeah", "sure", "nuh-uh", "hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"] and (ShopStats[LocCode] != "banned" or (ShopStats[LocCode] == "banned" and TotalPop == 0)):
								shop = input("You spot a shop! Do you want to head inside? [Y/N] ").lower() if TotalPop > 0 and ShopStats[LocCode] == "allowed" else input("You spot a shop. You're banned from it, but nobody is alive to stop you from entering. Do you want to? [Y/N] ")

								if shop in ["y", "ye", "yes", "yeah", "sure"]: # twice here cuz I don't wanna play the sound if the input doesn't meet the criteria. ask me why it matters, I dare you
									SoundCh.SFX.play(sel); Log("Entering shop."); Shop()
								elif shop in ["n", "nah", "no", "nope", "nuh-uh", "hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
									Log("You chose to pass the shop."); SoundCh.SFX.play(sel)
									if shop in ["hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
										if Route == "Traditional": print("Damn, okay. Are you scared of items or something?")
										else:
											print("Do you kiss your mother with that mouth?")
											if Route == "Omnicide": pause(); print(Fore.RED + "Well, of course not. She's dead.")
											pause()
										overworld = None
									else:
										print("You chose not to head inside and took a free step forward."); steps += 1
										# (to the tune of "Doofenshmirtz Evil Incorporated!") fixin' bugs when it's past miiiidniiiiiight!
										overworld = None; BattleOrNot = 0; continue
								else: shop = ""
						else:
							Log(f"Step was free. Hello from line {CurLine()}.")
							if population == 0: print("There's nobody left.")
							else:
								print("No enemies to be seen." if population > 0 else "There's nobody left.")
								if steps == 21 and LocCode == "Kiku" and yamiclear == False and (kills + npckills) in [0, 5]: Log("Encountering Yami."); Yami()
								elif steps == 15 and LocCode == "Archlekia" and shado_guards_clear == False: Log("Encountering Shadorako Guards."); ShadoGuardBattleIntro()
								overworld = None
							ZoneRNG = random.randint(1,5); ForbiddenSteps = [10, 12, 20, 24, 25, 30, 35, 50, 60, 70, 100]
							HealZone = ZoneRNG in [3, 5] and steps not in ForbiddenSteps
							PainZone = ZoneRNG == 1 and "EXTREME DEMON" in [Quirk1, Quirk2, ActiveQuirk] and steps not in ForbiddenSteps
							if HealZone or PainZone: Log(f"There's a{" Healing Zone" if ZoneRNG in [3, 5] else " Pain Zone" if PainZone else "n anomaly"} here!")
							if not HealZone: Log(f"A Healing Zone failed to appear because {"the D5 die didn't land on 3 or 5" if ZoneRNG != 3 else "you're on a forbidden step" if steps in ForbiddenSteps else "an error occurred"}!")
							if "EXTREME DEMON" in [ActiveQuirk, Quirk1, Quirk2] and not PainZone: Log(f"A Pain Zone failed to appear because {"the D5 die didn't land on 1" if ZoneRNG != 1 else "you're on a forbidden step" if steps in ForbiddenSteps else "an error occurred"}!")
					else:
						Log(f"Step was free. Hello from line {CurLine()}.")
						if population == 0: print("There's nobody left.")
						else:
							print("No enemies to be seen." if population > 0 else "There's nobody left.")
							if steps == 21 and LocCode == "Kiku" and yamiclear == False and (kills + npckills) in [0, 5]: Log("Encountering Yami."); Yami()
							elif steps == 15 and LocCode == "Archlekia" and shado_guards_clear == False: Log("Encountering Shadorako Guards."); ShadoGuardBattleIntro()
						MinigameRNG = random.randint(1,20); ForbiddenSteps = [10, 12, 20, 24, 25, 30, 35, 50, 60, 70, 100]
						MinigameTimeVar = MinigameRNG == 16 and steps not in ForbiddenSteps
						if MinigameTimeVar and MGtoggle: Log("Yah! It's minigame time!"); MinigameTime()
						elif not MGtoggle: print("(You have minigames disabled, so this step is free.)")
						overworld = None
				else:
					Log("Determining if you will encounter a shop.")
					Max = 45 if Diff == "Easy" else 10 if Diff == "Hard" else 25
					coinmax = random.randint(6,Max); Log(f"Coinflip max is {coinmax}."); coinflip = random.randint(1,coinmax); Log(f"Coin (more like dice) rolled a(n) {coinflip}.")
					rangefloor = round(coinmax/7)
					Log(f"Range floor is {rangefloor}.")
					if coinflip in range(rangefloor,coinmax): Log(f"{coinflip} is in range {rangefloor}-{coinmax}. You will not encounter a shop."); coin = False
					elif coinflip in range(1,rangefloor): Log(f"{coinflip} is in range 1-{rangefloor}! You will encounter a shop."); coin = True
					else:
						if population != 0: Log("A failsafe went off. You will not encounter a shop."); coin = False
						else: Log("A failsafe went off. You will encounter a shop."); coin = True # what am I doing
					if coin:
						Log("Encountered a shop.")
						if args.debug:
							print(Fore.YELLOW + "DEBUG: Shop time!")
							if BON == "yes" and coin: print(Fore.YELLOW + "DEBUG: DAMN IT")
						shop = ""
						while shop.lower() not in ["y", "n", "ye", "nah", "no", "yes", "nope", "yeah", "sure", "nuh-uh", "hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
							shop = input("You spot a shop! Do you want to head inside? [Y/N] ").lower()

							if shop in ["y", "ye", "yes", "yeah", "sure"]: # twice here cuz I don't wanna play the sound if the input doesn't meet the criteria. ask me why it matters, I dare you
								SoundCh.SFX.play(sel); Log("Entering shop."); Shop()
							elif shop in ["n", "nah", "no", "nope", "nuh-uh", "hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
								Log("You chose to pass the shop."); SoundCh.SFX.play(sel)
								if shop in ["hell no", "bitch no", "shut up", "stfu", "sybau", "kick rocks", "gfys", "kys", "fuck you"]:
									if Route != "Omnicide": print("Damn, okay. Are you scared of items or something?")
									else:
										print("Do you kiss your mother with that mouth?")
										if Route == "Omnicide": pause(); print(Fore.RED + "Well, of course not. She's dead.")
										pause()
									overworld = None
								else:
									print("You chose not to head inside and took a free step forward."); steps += 1
									# (to the tune of "Doofenshmirtz Evil Incorporated!") fixin' bugs when it's past miiiidniiiiiight!
									overworld = None; BattleOrNot = 0; continue
							else: shop = ""
					else:
						MinigameRNG = random.randint(1,20); ForbiddenSteps = [10, 12, 15, 20, 21, 24, 25, 40, 50]
						MinigameTimeVar = MinigameRNG == 16 and steps not in ForbiddenSteps
						if MinigameTimeVar and MGtoggle: Log("Yah! It's minigame time!"); MinigameTime()
						elif not MGtoggle: print("(You have minigames disabled, so this step is free.)")
					if population == 0 and BattleOrNot == fakeprob: print("You spot something!"); pause(); Log("Pretending to enter battle."); EnterFauxBattle() # this stays the same despite the rewrite
					else:
						Log(f"Step was free. Hello from line {CurLine()}."); Log("Calculating total population."); TotalPop = 0
						for area in LocPop:
							Log(f"Checking population for area {area}.")
							if area != "LivePneumonoultramicroscopicsilicovolcanoconiosisPop": Log(f"Population is {LocPop[area]}."); TotalPop += LocPop[area]; Log(f"Total population is now {TotalPop}.")
							else: Log("Area is from the April Fools' event. Ignoring.")
						if TotalPop != 0: Log("Omnicide has not been achieved."); print("There's nobody left.") # nobody left in the area, not nobody left at all
						else:
							Log("Omnicide has been achieved."); print(Fore.RED + "There's nothing left.")
							if steps == 21 and LocCode == "Kiku" and yamiclear == False and (kills + npckills) in [0, 5]: Log("Encountering Yami."); Yami()
							elif steps == 15 and LocCode == "Archlekia" and shado_guards_clear == False: Log("Encountering Shadorako Guards."); ShadoGuardBattleIntro()
				overworld = None; continue
			elif overworld == 2:
				if len(Party) > 1:
					pmem = input("Whose inventory would you like to check? ").title()
					if pmem != "Yami" and pmem:
						if pmem in Party: SoundCh.SFX.play(sel); Log(f"Checking inventory for {pmem}."); Inventory(pmem, overworld=True)
						else: print(f"{pmem} is not a valid party member.")
					elif pmem == "Yami" and pmem: print("Yami cannot hold items." if "Yami" in Party else "Yami is not a valid party member.")
				else: Inventory("Pinori", overworld=True)
				overworld = None
			elif overworld == 3: Log("Listing party members."); PartyMenu(); overworld = None
			elif overworld == 4: Log("Switching members from overworld."); SwitchMember(); overworld = None
			elif overworld == 5: Log("Saving the game."); Save(RemainingSteps); overworld = None
			elif overworld == 6:
				if AdvText == "Shown":
					if len(Party) > 1 and FocusedPlayer != "Pinori": print(f"You're playing as {FocusedPlayer}.")
					ScramblePrint(f"You're in {location}. You have been here {LocVisits[LocCode]} time{'s' if LocVisits[LocCode] != 1 else ''} this session. You have taken {steps} step{'s' if steps != 1 else ''} so far." if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2] else f"You're in {location}. You have taken {steps} step{'s' if steps != 1 else ''} so far.")
					if RemainingSteps > 0:
						if steps not in [15, 16] or location != "Archlekia": ScramblePrint(f"You have {RemainingSteps} more step{"s" if RemainingSteps != 1 else ""} to take{" before proceeding to the next area" if location != "Dyarix" else ""}.")
						elif shado_guards_clear and steps in [15, 16] and location == "Archlekia": ScramblePrint(f"The coast is clear.{".. of guards, at least.\n" if population > 0 else " "}(You have {RemainingSteps} more steps to take before proceeding to the next area.)")
						# I have NO clue why I have to make an else branch specific to when you're reloading after defeating Shadorako's Guards but oh well
						elif location == "Archlekia" and steps == 16: ScramblePrint(f"The coast is clear.{".. of guards, at least.\n" if population > 0 else " "}(You have {RemainingSteps} more steps to take before proceeding to the next area.)")
					elif RemainingSteps == 0: ScramblePrint(f"You have walked far enough{" to proceed to the next area" if location != "Dyarix" else ""}.")
					elif RemainingSteps < 0 and steps < (StepsNeeded*2): ScramblePrint("You've gone farther than you need to. Not like that's a bad thing.")
					elif RemainingSteps < 0 and steps == (StepsNeeded*2): ScramblePrint("You see a shiny object in the distance.")
					elif RemainingSteps < 0 and steps > (StepsNeeded*2) and population == 0: Yami() if steps == (StepsNeeded*2)+1 and (kills + npckills) >= 5 and location == "Kiku Village" else ScramblePrint("Nothing of interest left here.")
					elif RemainingSteps < 0 and steps > (StepsNeeded*2) and population != 0:
						if RemainingSteps < 0 and steps == ((StepsNeeded*2)+1) and location == "Kiku Village": Yami() if (kills + npckills == 0) or (kills + npckills >= 5) else ScramblePrint("A black-haired girl watches you from a distance. She's not happy.")
						else: ScramblePrint("Unless you're grinding, now would be a good time to move on.")
					else: print("???")
					if Route != "Traditional": ScramblePrint(f"The population is {LocPop[f"Live{LocCode}Pop"]}.")
					try:
						if end: ScramblePrint(f"Selecting 7 will end your journey.{" You may need a Demotion (item) to continue retrieving Tones." if Route == "Traditional" and Tones != 7 else ""}")
					except (UnboundLocalError, NameError) as e:
						if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2]:
							Log(f"DUMB THING HAPPENED WITH THE RANDOMISER THINGITY THING: {e}"); SoundCh.SFX.play(tef); end = False
					if Route != "Traditional": ScramblePrint(f"The population is {LocPop[f"Live{LocCode}Pop"]}.", c="red" if Route == "Omnicide" else "white")
					print()
				else:
					if Lightheadedness > 0: print("(Despite your condition, you can still read this properly!)")
					print(f"Steps taken: {steps}/{StepsNeeded}")
					print(f"You're in {location}. The population is {LocPop[f'Live{LocCode}Pop']}.")
					if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2]: plural = "s" if int(LocVisits[LocCode]) > 1 else ""; print(f"You've been here {LocVisits[LocCode]} time{plural} this session.")
					if Route != "Traditional": ScramblePrint(f"The population is {LocPop[f"Live{LocCode}Pop"]}.", c="red" if Route == "Omnicide" else "white")
				overworld = None
			elif overworld == 7 and Advance is True:
				Log(f"LocCode: {LocCode} | Location: {location}")
				# future me note: it is VERY important that this remains unchanged, reverting it to "npckills != 1" triggers ifinitYami so don't do that!!!
				if LocCode == "Kiku" and population == 0 and yamiclear == False and "Yami" not in Party: # Yami is important to Omnicide so if the player doesn't want to walk the steps and they've already killed the 5 monsters in Kiku Village they can cut to the chase instead of having to raise their step count to 21
					if AdvText == "Shown":
						print("You hear a girl yell towards your direction. She demands you turn around and come to her."); pause()
						print("You decide it's worth slightly deviating from your mission and face the direction the yell came from, walking towards the source of the sound."); pause()
					YamiBattleIntro()
				elif LocCode == "Kiku" and "Yami" in Party and population == 0 and yamiclear == False: YamiAltBattleIntro()
				elif LocCode == "Ocean" and not krystalclear:
					if AdvText == "Shown":
						print("You see a medium-sized pirate ship approaching in the distance..."); pause()
						print(f"Interested, you wait for the ship to arrive. Once it does, an old woman in purple pirate apparel pulls out a sword and points it towards you{"r party" if len(Party) > 1 else ""}."); pause()
					KrystalBattleIntro()
				elif LocCode == "Archlekia": ShadoLairIntro()
				else: ProgressMaker()
				overworld = None
			elif overworld == 7 and Advance is False: print("You have not taken enough steps."); overworld = None
			elif overworld == 8 and steps < (StepsNeeded*2): print("...?"); overworld = None
			elif overworld == 8 and steps == (StepsNeeded*2):
				# dynamically checks if the current area's Tone has been collected
				if ToneStates[LocCode] is False:
					if args.debug: print(Fore.YELLOW + "DEBUG: Tone not collected yet.")
					print("You approach the shiny object..."); time.sleep(3)
					print("It's a Tone! Press any key to collect it."); pause()
					if Tones in range(0,6) or Tones + 1 == 7:
						SoundCh.FARE.play(Tone); ToneCollectedYet = True; Tones += 1; ToneStates[LocCode] = True; print(f"= TONE GET = {Tones}/7 =")
						while pygame.mixer.get_busy(): time.sleep(0)
						print("Press any key to continue."); pause()
						print("After collecting the Tone, you took a free step forward.")
					else: print("All Tones collected or player is on NewGame+. Please disregard this message.")
					pause(); steps += 1
				elif ToneStates[LocCode] is True:
					if args.debug: print(Fore.YELLOW + "DEBUG: Tone already collected.")
					print("You already got the Tone in this area.")
					if Tones > 7: print(Fore.RED + "So stop trying to exploit, god damn it.")
				else:
					if args.debug: print(Fore.YELLOW + "DEBUG: Tone variable undefined.")
					BadCodeSong()
				overworld = None
			elif overworld == 8 and steps > (StepsNeeded*2):
				try:
					if ToneCollectedYet:
						print("You already got the Tone in this area.")
						if Tones > 7: print(Fore.RED + "So stop trying to exploit, god damn it.")
					else: print("You've passed the Tone. Hopefully your save can help.") if Route == "Traditional" else print("You missed the Tone. Nice going, now you have to reload your save.")
				except UnboundLocalError: SoundCh.SFX.play(tef); print("...")
				overworld = None
			elif overworld == 0:
				CurrentSavePath = LastUsedSave
				if os.path.exists(GetCustomFilePath("SavePaths.ini")):
					quickSP = configparser.ConfigParser(); quickSP.read("SavePaths.ini")
					quickSP.set("Last Used", "path", str(LastUsedSave))
					with open(GetCustomFilePath("SavePaths.ini"), "w") as asdfasdf: quickSP.write(asdfasdf); Log("Updated last used Save Data group.")
				if not isnewgame or (steps != 0 or location != "Kiku Village"): SavedProgress = CheckIfProgressSaved()
				else: SavedProgress = True
				if SavedProgress is False:
					if not isnewgame: print("You have made progress that hasn't been saved yet.\nIf you quit now, you will lose said progress (and all sales will end)!\nOnly select yes if you are trying to undo a mistake.")
					else: print("")
					returntotitle = ""
					while returntotitle.lower() not in ["y", "n", "yes", "no"]:
						SoundCh.SFX.play(important); returntotitle = str(input("\nAre you sure you want to return to the title screen? [Y/N] "))
						if returntotitle.lower() in ["y", "n", "yes", "no"]: break
						else: returntotitle = ""
					if returntotitle.lower() in ["y", "yes"]: ItemCosts = {"Ambersoda": 5, "Slingshot": 4, "Enemy Repellant": 10, "Foreign Stimulant": 1, "AUX Cord Energy Drink": 20, "3-Shot Slingshot": 15, "Promotion": 30, "Demotion": 20, "Shepard Tone": 90, "Stepper": 250, "Lucky Charm": 50, "EXP Share": 500, "Pocket Shop": 100}; TitleScreen()
					else: overworld = None
				else: ItemCosts = {"Ambersoda": 5, "Slingshot": 4, "Enemy Repellant": 10, "Foreign Stimulant": 1, "AUX Cord Energy Drink": 20, "3-Shot Slingshot": 15, "Promotion": 30, "Demotion": 20, "Shepard Tone": 90, "Stepper": 250, "Lucky Charm": 50, "EXP Share": 500, "Pocket Shop": 100}; TitleScreen()
			elif overworld in ["A", "a"] and HealZone:
				print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} encountered a Healing Zone!")
				HP = HP+10 if HP+10 <= MaxHP else MaxHP; SoundCh.SFX.play(heal); HP = MaxHP if TimeSpecificBonus() == 17 else HP # Healing Zones heal you fully if the Time Specific Bonus hex is set to 17
				print(f"{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} HP was maxed out!") if HP == MaxHP else print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} recovered 10 HP!")
				print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} took a free step forward."); steps += 1; HealZone = False
				for char in Party:
					if char in ["Pinori", "Millie"]: continue
					if CharTasks[char].state == "away": CharTasks[char].UpdateDistance()
			elif overworld in ["A", "a"] and PainZone:
				print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} encountered a Pain Zone!")
				HP -= 10; SoundCh.SFX.play(hurt)
				print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} took 10 damage!")
				print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} took a free step forward."); steps += 1; PainZone = False
				for char in Party:
					if char in ["Pinori", "Millie"]: continue
					if CharTasks[char].state == "away": CharTasks[char].UpdateDistance()
			elif overworld in ["A", "a"] and not HealZone and not PainZone:
				YourPCName = getpass.getuser(); UseAn = YourPCName[0].lower() in ["a", "e", "i", "o", "u"]
				randomremarks = ["No touchy!", "It's not time yet.", "Nothing to see here.", "B\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ", "Ooh! What does THIS button do?", "A little bird told me that this option doesn't do anything right now.", "Hold your horses.", "403 Forbidden", "Try again later.", f"How much A would {"a" if not UseAn else "an"} {YourPCName} press if {"a" if not UseAn else "an"} {YourPCName} could press A?", "I'm Press A-nsen, and this is How to Catch a Press-A-tor.", "very a, much press", "You should probably play the game now.", "Invalid input. (Just kidding, you found a secret.)", "Outvalid output.", "An occur has errored.", f"Polly want a{random.choice(["n AUX Cord Energy Drink", " Foreign Stimulant", "n Ambersoda"])}?", f"This is getting way too long, I should probably stop adding entries to it. Hey wait, this isn't a comment! Uh... hi, {YourPCName}!", "Nuh-uh!", "Adolph Blaine Charles David Earl Frederick Gerald Hubert Irvin John Kenneth Lloyd Martin Nero Oliver Paul Quincy Randolph Sherman Thomas Uncas Victor William Xerxes Yancy Zeus Wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswessenschafewarenwohlgepflegeundsorgfaltigkeitbeschutzenvorangreifendurchihrraubgierigfeindewelchevoralternzwolfhunderttausendjahresvorandieerscheinenvonderersteerdemenschderraumschiffgenachtmittungsteinundsiebeniridiumelektrischmotorsgebrauchlichtalsseinursprungvonkraftgestartseinlangefahrthinzwischensternartigraumaufdersuchennachbarschaftdersternwelchegehabtbewohnbarplanetenkreisedrehensichundwohinderneuerassevonverstandigmenschlichkeitkonntefortpflanzenundsicherfreuenanlebenslanglichfreudeundruhemnitchteinfurchtvorangreifenvorandererintelligentgeschopfsvonhinzwischensternartigraum Sr.", "Nothing to see here. But while you're sending inputs that do nothing at the moment, you should spend those inputs subscribing to the PyNori YouTube channel. Yes, that exists. https://youtube.com/@pynori", "YOU SHALL NOT HEAL!", "PLEASE SHIRLEY I NEED THIS, MY CHARACTER IS KINDA HEALTHLESS", "Are you pressing A when you're not supposed to? That's naughty! Keep that up and I'll make sure you get coal for Pressmas!", "os.remove(\"C:\\Windows\\System32\")" if sys.platform == "win32" else "sudo rm -rf /*"]
				print(random.choice(randomremarks))
			else: print("Invalid input.")
			if overworld in [1,2,3,4,5,6,7,8,9,0,"A","a"]: AlreadyDecrementedLightheadedness = False
		except ValueError as e:
			if args.debug: print(Fore.YELLOW + f"DEBUG: {e}")
			print("Input was not an integer.")
	overworld = None; print("whoopsies the script ain't supposed to get here")