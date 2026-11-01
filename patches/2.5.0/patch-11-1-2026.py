def ItemUsageMoment(slot, member, ow, ween=False, Yami=False, shadorako=False, Krystal=False):
	global HP, MaxHP, EnemyHP, CurE, VocalPoints, decoded, PlayerStatStorage, Party, defense, heal, crit, hurt, ShadorakoHP, burn, steps, FocusedPlayer, PlayerStatStorage, atk, defense, Lvl, Diff, expShare, healthroat, SpookyTime, Weenventory, WeenSteps
	global caffeine, withdrawal, SleepCounter, LC_is_in_inventory, sheptone_c, tef, inventory, debug, AttackList, Phase, TrueShadoDefense, FakeDiff, ItemCosts, deaths, YamiBossHP, YamiBossMaxHP, KrystalHP, Lightheadedness, AlreadyDecrementedLightheadedness
	FocusedPlayer = "Pinori" if shadorako else FocusedPlayer
	if args.debug: print(Fore.YELLOW + "DEBUG: Item usage function opened.")
	try: ShadoGuards = CurE == "Shadorako's Guards"
	except: CurE = None
	try: PkBoss = CurE in ["Pumpking", "Pumpqueen"]
	except: PkBoss = False
	try:
		if SpookyTime: pass
	except: SpookyTime = False
	if int(slot) not in range(1,4+1) and not (SpookyTime or ween): Cheater("oob slot")
	if args.debug: print(Fore.YELLOW + f"DEBUG: inventory[{member}][f\"slot{slot}\"]: {inventory[member][f'slot{slot}']} (type {type(inventory[member][f'slot{slot}'])})")
	if not SpookyTime: ChosenItem = inventory[member][f"slot{slot}"] # inventory wasn't even in the global scope before I typed this, how the HELL was this working???
	else: ChosenItem = Weenventory[f"slot{slot}"]
	Log("You're using an item."); Log(f"Slot: {slot}\nMember: {member}\nUsing item from overworld: {ow}\nFighting Yami: {Yami}\nFighting Shadorako: {shadorako}\nItem: {ChosenItem}"); hasItems = False
	if args.debug and not (SpookyTime or ween): print(Fore.YELLOW + f"DEBUG: inventory[{member}]: {inventory[member]} (type {type(inventory[member])})\ninventory[{member}].items(): {inventory[member].items()} (type {type(inventory[member].items())})")
	elif args.debug and (SpookyTime or ween): print(Fore.YELLOW + f"DEBUG: Weenventory: {Weenventory} (type {type(Weenventory)})\nWeenventory.items(): {Weenventory.items()} (type {type(Weenventory.items())})")
	for NotTheSlotVariableProvidedByTheFunction, item in (inventory[member] if not SpookyTime else Weenventory).items():
		if args.debug: print(Fore.YELLOW + f"DEBUG: slot: {NotTheSlotVariableProvidedByTheFunction}\nitem: {item}")
		if item != "None":
			if args.debug: print(Fore.YELLOW + f"{member} has items.")
			hasItems = True; Log(f"{member} has items."); break
	Log(f"Has items?: {hasItems}")
	if ChosenItem is None: print(f"{member.title()} has no items. If you do not automatically exit the inventory menu, please type \"E\" to do so.") if not hasItems else print(f"Slot {slot} is empty. Please select another."); return
	if ChosenItem not in ["Unused Ring", "3-Shot Slingshot", "2-Shot Slingshot", "Lucky Charm"] and not (ChosenItem == "Promotion" and Diff == "Tryhard"): inventory[member][f"slot{slot}"] = "None"
	try:
		if SpookyTime and "Pumpkin" not in ChosenItem: Weenventory[f"slot{slot}"] = "None"
	except: pass
	if "-Shot Slingshot" in ChosenItem and ChosenItem[0] != "2": inventory[member][f"slot{slot}"] = f"{int(ChosenItem[0])-1}-Shot Slingshot"
	elif ChosenItem == "2-Shot Slingshot": inventory[member][f"slot{slot}"] = "Upgraded Slingshot"
	elif ChosenItem == "Unused Ring": inventory[member][f"slot{slot}"] = "Ring"
	if ChosenItem == "Unused Ring":
		if CurE == "Shadorako": inventory[member][f"slot{slot}"] = "Ring" # player won't be able to use the Ring on enemies other than Shadorako, so they get to keep it
		print(f"You used the Ring on {CurE}."); time.sleep(3)
		if shadorako and Phase == 1: decoded = "True"; print("The glitching subsides. You can attack now!") # it can only really be used on Shadorako, and only on Phase 1
		elif shadorako and Phase != 1: print("Nothing happened.") # only doable with cheats, since the Unused Ring turns into the Ring after being used in Phase 1, and it MUST be used for attacking to be possible
		else: print("It's useless.")
	elif ChosenItem == "Ring": print("The Ring has already been used. It disintegrates...")
	elif ChosenItem == "Ambersoda":
		SoundCh.SFX.play(heal)
		QuarterHP = int(MaxHP/4)
		if (HP + QuarterHP) > MaxHP: AfterSentence = f"{f"{FocusedPlayer}'s" if FocusedPlayer != "Pinori" else "Your"} HP was maxed out!"; HP = MaxHP
		else: HP += QuarterHP; AfterSentence = f"{FocusedPlayer if FocusedPlayer != "Pinori" else FocusedPlayer} recovered {QuarterHP} HP."
		print(f"The Ambersoda feels like a breath of fresh air. {AfterSentence}")
		if len(Party) > 1:
			for unconscious in Party:
				if unconscious in ["Pinori", "Sana", "Akuron", "Yami"] and unconscious not in [FocusedPlayer, "Millie"]:
					if PlayerStatStorage[unconscious]["HP"] <= 0: PlayerStatStorage[unconscious]["HP"] += 10; print(f"{unconscious} recovered 10 HP!")
	elif ChosenItem == "AUX Cord Energy Drink":
		SoundCh.SFX.play(heal); SoundCh.BAT.play(healthroat); print(f"The AUX Cord Energy Drink makes {"your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} vocal cord feel brand new.\n{"Your" if FocusedPlayer == "Pinori" else "Their"} HP and Vocal Points were maxed out!"); HP = MaxHP
		VocalPoints = PlayerStatStorage[FocusedPlayer]["MaxVP"]
		if not shadorako:
			caffeine += 10
			if caffeine > 79 and withdrawal is not True: withdrawal = True; print("You've consumed too many energy drinks and are now at risk of experiencing caffeine withdrawal.\nYou must continue using AUX Cord Energy Drinks to avoid falling asleep."); pause(); Log(f"Caffeine intake is at {caffeine}.")
			elif caffeine > 0 and SleepCounter > 0 and withdrawal is True: caffeine += 10; print("The caffeine withdrawal continues..."); pause()
		elif shadorako: print("(A strange force prevents the caffeine from affecting your body.)")
	elif ChosenItem == "Key Switch" and not shadorako:
		if "key switch" in AttackList: print("You already know this attack. Why'd you make another?") if len(Party) == 1 else print("Your party already knows this attack. Why'd you make another?")
		else: print("You learned a new attack! Congratulations!") if len(Party) == 1 else print("Your party learned a new attack! Congratulations!"); AttackList["Key Switch"] = 50
	elif ChosenItem == "Key Switch" and shadorako:
		print("You used the Key Switch despite not having access to your normal attacks."); time.sleep(5)
		SoundCh.SFX.play(hurt); SoundCh.BAT2.play(crit); HP, ShadorakoHP = 1, 1; print("Both your and Shadorako's HP were reduced to 1. Sudden death, GO!")
	elif ChosenItem == "Shepard Tone" and not shadorako:
		if "shepard tone" in AttackList: print("You already know this attack. Why'd you make another?") if len(Party) == 1 else print("Your party already knows this attack. Why'd you make another?")
		else: print("You learned a new attack! Congratulations!") if len(Party) == 1 else print("Your party learned a new attack! Congratulations!"); AttackList["Shepard Tone"] = 30
	elif ChosenItem == "Shepard Tone" and shadorako:
		print("You used the Shepard Tone despite not having access to your normal attacks."); time.sleep(5)
		SoundCh.BAT.play(sheptone_c); print("Suddenly, the item begins to glow...!"); time.sleep(3); hits = 0; totaldmg = 0
		while hits < 5:
			hits += 1; dmg = random.randint(0,100); totaldmg += dmg
			if dmg == 0: SoundCh.BAT2.play(miss); print("Miss.")
			else: SoundCh.SFX.play(burn); print(f"Dealt {dmg} damage{"." if dmg in range(1,74) else "!"}")
			if dmg == 100: SoundCh.BAT2.play(crit)
			time.sleep(0.4)
		time.sleep(2); print(f"The Shepard Tone dealt {totaldmg} total damage!"); ShadorakoHP -= totaldmg; time.sleep(4)
	elif ChosenItem == "Enemy Repellant":
		if not Yami and not shadorako and not Krystal:
			word = "You" if FocusedPlayer == "Pinori" else FocusedPlayer
			print(f"{word} proudly presented the Enemy Repellant to {CurE}.")
			if CurE not in ["Clef", "Treble", "???", "Corrupted Soul"]: print(f"{CurE} pouts and retreats automatically.")
			elif CurE in ["Clef", "Treble"]: instrument = "bass" if CurE == "Treble" else "violin"; print(f"{CurE} giggles and stands up, waving goodbye before taking their {instrument} with them.")
			elif CurE != "Clef" and CurE in ["???", "Corrupted Soul"]: print(f"{CurE} disappears into thin air.")
			pause(); BattleWon("spare")
		else:
			if Yami:
				print("You presented the Enemy Repellant to Yami."); pause()
				print("Yami: " + Fore.RED + "Hah. What the hell is that? A counterfeit coin?"); pause()
				print("Yami: " + Fore.RED + "Get that outta my face and square up."); pause()
			elif shadorako:
				print("You presented the Enemy Repellant to Shadorako."); pause()
				print("Shadorako takes a moment to try to comprehend what you're even doing."); pause()
				print("Eventually, she catches on and bursts into laughter, turning your Enemy Repellant to dust."); pause()
				typewriter_shado("If you're such a hero, now's the time to show it. Quit being such a coward, you're making me laugh."); pause()
			elif Krystal:
				print("You presented the Enemy Repellant to Krystal."); pause()
				print("Krystal: Mate... what in the hell be that there?"); pause()
				print("Krystal: Have ye lost yer marbles?"); pause()
				print("Krystal: This here be a quarrel, not show n' tell! En garde!"); pause()
	elif "-Shot Slingshot" in ChosenItem:
		try: InBattle = CurE != None
		except Exception: SoundCh.SFX.play(tef); InBattle = False
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} used one of the shots on the {ChosenItem}.")
		if InBattle:
			if not Yami and not Krystal: EnemyHP -= 10
			elif not Yami and Krystal: KrystalHP -= 10
			else: YamiBossHP -= 10
			print(f"{CurE} lost 10 HP!")
		elif shadorako: ShadorakoHP -= 10; print("Shadorako lost 10 HP!")
		else: print("Nothing happened.")
		print(f"{f'{int(ChosenItem[0])-1} shot{"s" if ChosenItem[0] != "2" else ""}'} left.")
	elif ChosenItem == "Upgraded Slingshot":
		try: InBattle = CurE != None
		except Exception: SoundCh.SFX.play(tef); InBattle = False
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} used the Upgraded Slingshot.")
		if InBattle:
			if not Yami and not Krystal: EnemyHP -= 15
			elif not Yami and Krystal: KrystalHP -= 15
			else: YamiBossHP -= 15
			print(f"{CurE} lost 15 HP!")
		elif shadorako: ShadorakoHP -= 15; print("Shadorako lost 15 HP!")
		else: print("Nothing happened.")
		print(f"The Upgraded Slingshot is out of ammo, so {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} discarded it.")
	elif ChosenItem == "Slingshot":
		try: InBattle = CurE != None
		except Exception: SoundCh.SFX.play(tef); InBattle = False
		CurE = "Shadorako" if shadorako else CurE
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} used the Slingshot..."); time.sleep(2)
		itvsshe = "It" if not Yami else "She"
		theenemyvsname = "the enemy" if not Yami else "Yami"
		if InBattle:
			SlingStrength = random.randint(1,5)
			if SlingStrength == 1: print("The Slingshot broke...")
			elif SlingStrength == 2:
				print(f"The ammo weakly hit {theenemyvsname}.")
				if not Yami and not shadorako: EnemyHP -= 1
				elif shadorako and not Yami: ShadorakoHP -= 1
				else: YamiBossHP -= 1
				print(f"{CurE} lost 1 HP.")
			elif SlingStrength == 2:
				print(f"The ammo hit {theenemyvsname}. {itvsshe} doesn't look so phased.")
				if not Yami: EnemyHP -= 4
				elif shadorako and not Yami: ShadorakoHP -= 4
				else: YamiBossHP -= 4
				print(f"{CurE} lost 4 HP.")
			elif SlingStrength == 3:
				print(f"The ammo hit {theenemyvsname}. {itvsshe} flinched, but aside from that, no reaction.")
				if not Yami: EnemyHP -= 5
				elif shadorako and not Yami: ShadorakoHP -= 5
				else: YamiBossHP -= 5
				print(f"{CurE} lost 5 HP.")
			elif SlingStrength == 4:
				print(f"The ammo hit {theenemyvsname} somewhat strongly. {"The enemy" if not Yami else "Yami"} flinched.")
				if not Yami: EnemyHP -= 10
				elif shadorako and not Yami: ShadorakoHP -= 10
				else: YamiBossHP -= 10
				print(f"{CurE} lost 10 HP.")
			elif SlingStrength == 5:
				print(f"The ammo hit {theenemyvsname} hard. {"The enemy" if not Yami else "Yami"} flinched and said ow.")
				if not Yami: EnemyHP -= 15
				elif shadorako and not Yami: ShadorakoHP -= 15
				else: YamiBossHP -= 15
				print(f"{CurE} lost 15 HP.")
		else: print("It broke. Nice.")
	elif ChosenItem == "Promotion":
		if Diff == "Tryhard": print("Skipping parts of the game is for cowards. You're a tryhard."); pause()
		else:
			try: InBattle = CurE != None
			except Exception: SoundCh.SFX.play(tef); InBattle = False
			if not InBattle: print("You're being promoted!\nThis means you can skip to the next area without taking all the necessary steps.\nPress any key to skip ahead!"); pause(); ProgressMaker(Promotion=True)
			else:
				inventory[member][f"slot{slot}"] = "Promotion" # give the item back because the game defaults to erasing it
				print("You cannot be promoted in battle. Please finish the battle first."); pause()
	elif ChosenItem == "Demotion":
		try: InBattle = CurE != None
		except Exception: SoundCh.SFX.play(tef); InBattle = False
		if not InBattle: print("You're being demoted!\nThis means you can backtrack to the previous area if you have some unfinished business.\nPress any key to backtrack!"); pause(); ProgressDestroyer()
		else:
			inventory[member][f"slot{slot}"] = "Demotion" # same reason as above
			print("You cannot be demoted in battle. Please finish the battle first."); pause()
	elif ChosenItem == "Foreign Stimulant":
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} took the Foreign Stimulant..."); time.sleep(2)
		StimulantType = random.randint(1,9); StimulantWord = {1: "Bad Drug", 2: "Sugar Rush", 3: "Roofie", 4: "Power Burst", 5: "Death Pill", 6: "Defense Boost", 7: "Attack Boost", 8: "Tasteless", 9: "Lightheadedness Pill"}
		Log(f"The Foreign Stimulant was {"a " if StimulantType != 7 else "an " if StimulantType != 8 else ""}{StimulantWord.get(StimulantType)}.")
		if StimulantType == 1: # bad drug
			print("You don't feel so good...") if FocusedPlayer == "Pinori" else print(f"{FocusedPlayer} doesn't feel so good...")
			HP -= 10; print("Lost 10 HP!")
			if HP == 0:
				if shadorako:
					try: deaths += 1
					except: deaths = 1
					GameOverShado(drugs=True)
				else:
					TotalHP = 0; Log("Calculating HP of whole party.")
					for member in Party:
						Log(f"Member: {member}")
						if member == "Millie": Log("Millie cannot battle. Skipping."); continue
						TotalHP += PlayerStatStorage[member]["HP"] if member != FocusedPlayer else HP; Log(f"Total HP is now {TotalHP}.")
					GameOver(cheaterweater=False, drugs=True) if TotalHP <= 0 else SwitchMember(Forced=True)
		elif StimulantType == 2: # sugar rush
			print(f"It was just a piece of candy, apparently.\nThe piece of candy had a lot of caffeine in it.\nNow {"you're" if FocusedPlayer == "Pinori" else f"{FocusedPlayer} is"} having a sugar rush!")
			SoundCh.SFX.play(heal); HP = MaxHP*3; print(f"{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} HP is now 3x {"your" if FocusedPlayer == "Pinori" else "their"} Max HP! Enjoy!")
		elif StimulantType == 3: # roofie
			try: InBattle = CurE != None
			except Exception: SoundCh.SFX.play(tef); InBattle = False
			if FocusedPlayer == "Pinori": word1, word2, word3 = "You", "You'll", "you"
			else: word1, word2, word3 = FocusedPlayer, f"{FocusedPlayer} will", "they"
			print("It was a roofie!")
			if InBattle: SleepCounter += 4; print(f"{word1} fell asleep. {word2} wake up in {SleepCounter} turns.")
			else: word4 = "don't" if FocusedPlayer == "Pinori" else "doesn't"; print(f"{word1} fell asleep... but since you're not in battle, {word3} {word4} need to wait to wake up.\nWith that said... {word1.lower() if word1 == "You" else word1} woke up.")
		elif StimulantType == 4: # power burst
			print("You feel a surge of power flow through your body.") if FocusedPlayer == "Pinori" else print(f"{FocusedPlayer} feels a surge of power flow through their body.")
			MaxHP += 10; print(f"{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} Max HP increased by 10!")
			try:
				if isinstance(globals()["RealMaxHP"], int): RealMaxHP += 10
			except: pass
		elif StimulantType == 5: # SHE FREAKIN DIED!
			HP = 0; print("... and died as a result."); pause()
			if not shadorako:
				if len(Party) == 1 or CurE == "Yami": GameOver(cheaterweater=False, drugs=True) # game over even if others are alive because you're supposed to solo the Yami battle
				else:
					TotalHP = 0; Log("Calculating HP of whole party.")
					for member in Party:
						Log(f"Member: {member}")
						if member == "Millie": Log("Millie cannot battle. Skipping."); continue
						TotalHP += PlayerStatStorage[member]["HP"] if member != FocusedPlayer else HP; Log(f"Total HP is now {TotalHP}.")
					GameOver(cheaterweater=False, drugs=True) if TotalHP <= 0 else SwitchMember(Forced=True)
			else:
				try: deaths += 1
				except: deaths = 1
				GameOverShado(drugs=True)
		elif StimulantType == 6: defense += 1; print("You feel stronger. Your defense increased by 1!") if FocusedPlayer == "Pinori" else print(f"{FocusedPlayer} feels stronger. Their defense increased by 1!") # def boost
		elif StimulantType == 7: atk += 1; print("You feel stronger. Your attack increased by 1!") if FocusedPlayer == "Pinori" else print(f"{FocusedPlayer} feels stronger. Their attack increased by 1!") # atk boost
		elif StimulantType == 8: print("It was tasteless. Nothing happened.") # nothing
		elif StimulantType == 9:
			AlreadyDecrementedLightheadedness = True
			if not Yami or shadorako: Lightheadedness += 10; print(f"{"You're not" if FocusedPlayer == "Pinori" else f"{FocusedPlayer} isn't"} sure WHAT {"you" if FocusedPlayer == "Pinori" else "they"} just consumed, but it's making {"you" if FocusedPlayer == "Pinori" else "them"} feel lightheaded.\nMenus will be unreadable for the next 10 turns!"); AlreadyDecrementedLightheadedness = True
			else: print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} became lightheaded. {"Yami" if Yami else "Shadorako"} waits for {"you" if FocusedPlayer == "Pinori" else "them"} to recover before continuing the battle."); pause(); print("Despite everything, Yami still wants the fight to be fair." if Yami else "Shadorako may be evil, but she knows you need to be able to read the menus if you want to stand a chance."); pause(); print("Eventually, the lightheadedness wears off.")
		pause()
	elif ChosenItem == "Stepper":
		while True:
			try: StepTeleport = int(input("What step would you like to teleport to? "))
			except Exception: print("Input was not an integer."); continue
			if StepTeleport not in range(0,100): print(f"You may not teleport to {"a negative" if StepTeleport < 0 else "that"} step.")
			if StepTeleport in range(0,100+1): break # range includes value a but excludes value b so I have to do stupid stuff like this, it's really annoying
		steps = StepTeleport; print(f"You are now at step {steps}!"); pause()
	elif ChosenItem == "Lucky Charm":
		EraseItem = True
		if HP > MaxHP/2:
			benefits = ["inc atk", "inc def", "vocal point refresh", "vocal point half refresh", "weaken enemy", "weaken enemy but nerfed", "dec enemy def"]; benefit = random.choice(benefits)
			if benefit == "inc atk": thing = random.randint(1,3); atk += thing; reward = f"{word} attack increased by {thing}!"
			elif benefit == "inc def": defense += 1; reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} defense increased by 1!"
			elif benefit == "vocal point refresh": SoundCh.SFX.play(healthroat); VocalPoints = 140 if FocusedPlayer == "Pinori" else 120 if FocusedPlayer == "Akuron" else 150 if FocusedPlayer == "Sana" else 60; reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} Vocal Points were refilled!"
			elif benefit == "vocal point half refresh": SoundCh.SFX.play(healthroat); VocalPoints = 70 if FocusedPlayer == "Pinori" else 60 if FocusedPlayer == "Akuron" else 75 if FocusedPlayer == "Sana" else 30; reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} Vocal Points were half refilled."
			elif benefit == "weaken enemy" and CurE is not None:
				if not Yami and not shadorako: EnemyHP = 1
				elif Yami: YamiBossHP = 1
				else: ShadorakoHP = 1
				reward = "The opponent's HP was reduced to 1!"
			elif benefit == "dec enemy def" and CurE is not None and not Yami:
				thing = random.randint(1,8)
				if not shadorako: EnemyDEF -= thing
				else:
					if Phase == 2: TrueShadoDefense -= thing
				reward = f"The opponent's defense decreased by {thing}!"
			elif benefit == "dec enemy def" and Yami: reward = "Unfortunately, Yami is immune to defense nerfs."; EraseItem = False
			elif benefit in ["weaken enemy", "dec enemy def", "weaken enemy but nerfed"] and CurE is None and not Yami and not shadorako and not Krystal: reward = "It chose a benefit that requires you to be in battle, so nothing happened. (Don't worry, you get to keep the item for now!)"; EraseItem = False
			elif benefit == "weaken enemy but nerfed" and CurE:
				if not shadorako and not Yami: EnemyHP = round(EnemyHP / 2)
				elif Yami: YamiBossHP = round(YamiBossHP / 2)
				else: ShadorakoHP = round(ShadorakoHP / 2)
				reward = "The enemy's HP was halved!"
			print(f"{FocusedPlayer} used the Lucky Charm. {reward}")
		elif HP <= MaxHP/2:
			benefits = ["inc atk", "inc def", "full heal", "vocal point refresh", "weaken enemy", "dec enemy def"] if HP < MaxHP/2 else ["vocal point half refresh", "weaken enemy but nerfed"]; benefit = random.choice(benefits); reward = "But... nothing happened. That's weird."
			try:
				if benefit == "inc atk" and not shadorako: thing = random.randint(1, 3); atk += thing; reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} attack increased by {thing}!"
				elif benefit == "inc atk" and shadorako: reward = "Unfortunately, Shadorako is preventing Pinori from strengthening her attack..." # the real reason is because the Shadorako battle doesn't care about your stats aside from HP lol, the damage is mainly RNG
				elif benefit == "inc def" and not shadorako: defense += 1; reward = f"{word} defense increased by 1!"
				elif benefit == "inc def" and shadorako: reward = "Unfortunately, Shadorako is preventing Pinori from strengthening her defense..."
				elif benefit == "full heal": HP = MaxHP; reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} HP was maxed out!"
				elif benefit == "vocal point refresh" and not shadorako: SoundCh.SFX.play(healthroat); VocalPoints = {"Pinori": 140, "Akuron": 120, "Sana": 150, "Yami": 60}.get(FocusedPlayer, VocalPoints); reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} Vocal Points were refilled!"
				elif benefit == "vocal point refresh" and shadorako: reward = "Unfortunately, Vocal Points are useless in the void."
				elif benefit == "weaken enemy" and CurE is not None:
					if not shadorako and not Yami: EnemyHP = 1
					elif Yami: YamiBossHP = 1
					else: ShadorakoHP = 1
					reward = "The opponent's HP was reduced to 1!"
				elif benefit == "dec enemy def" and CurE is not None and not Yami:
					thing = random.randint(1, 8)
					if not shadorako: EnemyDEF -= thing
					elif Phase == 2: TrueShadorakoDefense -= thing
					if (not shadorako) or (shadorako and Phase == 2): reward = f"The opponent's defense decreased by {thing}!"
					else: reward = "ERROR"
				elif benefit == "dec enemy def" and Yami: reward = "Unfortunately, Yami is immune to defense nerfs."; EraseItem = False
				elif benefit == "vocal point half refresh" and not shadorako: SoundCh.SFX.play(healthroat); VocalPoints = {"Pinori": 70, "Akuron": 60, "Sana": 75, "Yami": 30}.get(FocusedPlayer, VocalPoints); reward = f"{"Your" if FocusedPlayer == "Pinori" or shadorako else f"{FocusedPlayer}'s"} Vocal Points were half refilled."
				elif benefit == "vocal point half refresh" and shadorako: reward = "Unfortunately, Vocal Points are useless in the void."
				elif benefit == "weaken enemy but nerfed" and CurE:
					if not shadorako and not Yami: EnemyHP = round(EnemyHP / 2)
					elif Yami: YamiBossHP = round(YamiBossHP / 2)
					else: ShadorakoHP = round(ShadorakoHP / 2)
					reward = "The enemy's HP was halved!"
			except Exception as e:
				SoundCh.SFX.play(tef); Log(f"Exception when using Lucky Charm manually: {e}")
				if benefit in ["weaken enemy but nerfed", "weaken enemy"]: reward = "It chose a benefit that requires you to be in battle, so nothing happened. (Don't worry, you get to keep the item for now!)"; EraseItem = False
			print(f"{FocusedPlayer} used the Lucky Charm! {reward}")

		if EraseItem is True:
			inventory[member][slot] = "None"
			for slot, item in inventory[member].items(): # no kitty, you cannot has multiple lucky charms
				if item == "Lucky Charm": inventory[member][slot] = "None"; LC_is_in_inventory = False
	elif ChosenItem == "Item Coupon":
		DiscountedItem = random.choice(ItemNames); DiscountCeiling = 20 if Diff == "Hard" else 50 if Diff == "Normal" else 90; OriginalPrice = ItemCosts[DiscountedItem]
		ItemCosts[DiscountedItem] = round(ItemCosts[DiscountedItem] * (random.randint(10,DiscountCeiling)/100)); DiscountPercentage = (OriginalPrice - ItemCosts[DiscountedItem])/OriginalPrice * 100
		print(f"The {DiscountedItem} item now costs {ItemCosts[DiscountedItem]} Sine{"s" if ItemCosts[DiscountedItem] != 1 else ""} ({DiscountPercentage}% off)!\nDiscounts are NOT preserved in your Save Data, so now or never!")
	elif ChosenItem == "EXP Share":
		expshareIncrement = random.randint(2,7)
		if expshareIncrement + expShare > 100: expShare = 100; print(f"Party members {"(except Millie)" if "Millie" in Party else ""} will now earn the same amount of EXP as {FocusedPlayer}!")
		else: expShare += expshareIncrement; print(f"Party members {"(except Millie)" if "Millie" in Party else ""} will now receive {expShare}% of {FocusedPlayer}'s earnings!")
	elif ChosenItem == "Pocket Shop": Shop(Pocket=True) if not shadorako else print("Shadorako forbids you from getting help.") # half bc haha it makes the fight harder and half bc the Sines aren't initialised for the Shadorako battle
	elif ChosenItem == "Small Candy":
		if not SpookyTime: print("Nice try, this only works in the Halloween Event!"); pause()
		else:
			CandyType = random.randint(1,3); print("You used the Small Candy...")
			if CandyType == 1: SoundCh.SFX.play(heal); HP = MaxHP; print("Your HP was maxed out!")
			elif CandyType == 2: SoundCh.SFX.play(healthroat); VocalPoints = MaxVP; print("Your Vocal Points were refilled!")
			elif CandyType == 3: MaxHP += 10; print("Your Max HP increased by 10!")
	elif "Pumpkin" in ChosenItem and ChosenItem != "Grand Pumpkin":
		if not SpookyTime: print("Nice try, this only works in the Halloween Event!"); pause()
		else:
			Merged = False; HasGrandPumpkin = "Grand Pumpkin" in Weenventory.values()
			try:
				for OtherSlot, item in Weenventory.items():
					if f"slot{slot}" != OtherSlot and Weenventory[OtherSlot] == ChosenItem:
						print(f"Found a {ChosenItem} to pair with!"); Merged = True; Weenventory[OtherSlot] = "None"
						if ChosenItem == "Pumpkin": Weenventory[f"slot{slot}"] = "Super Pumpkin"
						elif ChosenItem == "Super Pumpkin": Weenventory[f"slot{slot}"] = "Mega Pumpkin"
						elif ChosenItem == "Mega Pumpkin": Weenventory[f"slot{slot}"] = "Hyper Pumpkin"
						elif ChosenItem == "Hyper Pumpkin": Weenventory[f"slot{slot}"] = "Ultra Pumpkin"
						elif ChosenItem == "Ultra Pumpkin": Weenventory[f"slot{slot}"] = "Giga Pumpkin"
						elif ChosenItem == "Giga Pumpkin" and not HasGrandPumpkin: Weenventory[f"slot{slot}"] = "Grand Pumpkin"
						elif ChosenItem == "Giga Pumpkin" and HasGrandPumpkin: print("There can only be one Grand Pumpkin."); pause(); break
						print(f"Your {ChosenItem}s have become a {Weenventory[f"slot{slot}"]}!")
						if Weenventory[f"slot{slot}"] == "Grand Pumpkin": print("Congratulations! The Pumpking and Pumpqueen will be very pleased.")
						break
				if not Merged: print(f"Couldn't find another {ChosenItem} to pair with.\nPlease collect more pumpkins and try again.")
			except: pass
	elif ChosenItem == "Grand Pumpkin":
		if not SpookyTime: print("Nice try; even if you were in the Halloween Event, this does nothing!"); pause()
		else: print("It's the Grand Pumpkin! Now just make it to the Kameria City Hall before the Pumpking and Pumpqueen arrive."); pause()
	elif ChosenItem == "Rewind":
		if not SpookyTime: print("Nice try, this only works in the Halloween Event!"); pause()
		else: WeenSteps = max(0, WeenSteps-10); print(f"You're now at step {WeenSteps}!"); pause()
	elif ChosenItem == "Booster":
		if not SpookyTime: print("Nice try, this only works in the Halloween Event!"); pause()
		else: WeenSteps = min(WeenSteps+10, 200); print(f"You're now at step {WeenSteps}!"); pause()
	else: print("You'reeeee notttt funnyyyyyyy brooooo!"); time.sleep(1); print("This is not gaming this is cheatingggggggggggggg I don't like cheaters dudeeee"); time.sleep(3); print("D i e"); time.sleep(1); SoundCh.BAT2.play(crit); SoundCh.SFX.play(hurt); print(f"Shirley dealt {HP} damage to you!"); HP = 0; time.sleep(1); GameOver(cheaterweater=True)
	if shadorako:
		if Phase == 1: P1Menu() if FakeDiff != "Impossible" else ImpP1Menu()
		elif Phase == 2: P2Menu() if FakeDiff != "Impossible" else ImpP2Menu()
		elif Phase == 3: P3Menu() if FakeDiff != "Impossible" else ImpP3Menu()
		elif Phase == 4: P4Menu() if FakeDiff != "Impossible" else ImpP4Menu()
		elif Phase == 5: Cheater("phase 5"); os._exit(1)
		elif Phase == 6 and FakeDiff == "Impossible": P6Menu()
		elif Phase == 7 and FakeDiff == "Impossible": P7Menu()
		elif Phase > 7 and FakeDiff == "Impossible": Cheater("phase 8"); os._exit(1)
		else: print("ERROR"); os._exit(1)
	else: 
		if not ween:
			if CurE not in ["Shadorako's Guards", "Shadorako"] and not ShadoGuards: gameThing() if ow else YamiBattleMenu() if Yami else KrystalBattleMenu() if Krystal else BattleMenu()
			elif CurE == "Shadorako": ShadoArchlekiaBattleMenu()
			else: ShadoGuardsBattleMenu() if ShadoGuards and not ow else gameThing()
		else:
			if not PkBoss:
				if CurE: BattleMenu()
				else: WeenOverworld()
			else: WeenBossBattleMenu()