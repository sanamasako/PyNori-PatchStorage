def SkipTurn(Challenge=None, Shado=False):
	if args.debug: print(Fore.YELLOW+f"DEBUG: Shadorako?: {Shado}")
	global CurE, ClefHappy, HP, MaxHP, Lvl, EnemyATK, defense, FocusedPlayer, Party, SleepCounter, hurt, heal, crit, miss, AlreadyDecrementedSleep, AlreadyDecrementedCaffeine, ActiveQuirk, Quirk1, Quirk2; AtkAmount = 1 if "Double or Nothing" not in [ActiveQuirk, Quirk1, Quirk2] else 2
	AlreadyDecrementedCaffeine, AlreadyDecrementedSleep = False, False; PendingDamage = 0; ShadoGuards = CurE == "Shadorako's Guards"
	if FocusedPlayer in ["Yami", "Sana"]: pronoun = "her"; pronoun2 = "her"
	elif FocusedPlayer == "Akuron": pronoun = "his"; pronoun2 = "him"
	elif FocusedPlayer == "Millie": Cheater("millie battle")
	else: pronoun = "you"; pronoun2 = "you"
	yourvsnames = "your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"
	print("You skipped your turn.") if len(Party) == 1 or FocusedPlayer == "Pinori" else print(f"{FocusedPlayer} skipped {pronoun} turn.")
	try:
		if InitEnemStat(CurE)["docile"]: print((Fore.RED if Route == "Omnicide" else Fore.WHITE)+f"{CurE} is docile."); pause()
	except: pass
	try:
		AttackAllowed = (not InitEnemStat(CurE)["docile"]) or Shado or ShadoGuards
	except: AttackAllowed = Shado or ShadoGuards
	if AttackAllowed:
		for hohsisjoj in range(AtkAmount):
			DamageIn = InDamage(Lvl, EnemyATK, defense, Yami=False) if not Shado else 0
			if CurE not in ["Clef", "Treble", "Shadorako", "Krystal", "Pumpking", "Pumpqueen", "Shadorako's Guards"] or (CurE in ["Clef", "Treble"] and not ClefHappy) and (not Shado):
				if hohsisjoj+1 == AtkAmount:
					HP -= DamageIn
					if DamageIn != 0: SoundCh.SFX.play(hurt); print(f"{CurE} dealt {DamageIn} damage to {pronoun2}.")
					else: SoundCh.BAT2.play(miss); print(f"{CurE}'s attack missed.")
				elif DamageIn > 0: PendingDamage += DamageIn; print(f"{CurE}'s first attack landed."); pause(); continue
				else: SoundCh.SFX.play(miss); print(f"{CurE}'s attack missed."); pause(); break
			elif CurE in ["Clef", "Treble"] and ClefHappy and (not Shado):
				if hohsisjoj+1 == AtkAmount:
					if DamageIn != 0:
						if (HP + DamageIn) <= MaxHP: HP += DamageIn; print(f"{CurE} returned {DamageIn} HP to {pronoun2}.")
						else: HP = MaxHP; print(f"{CurE} maxed out {yourvsnames} HP.")
					elif DamageIn < 0: HP = min(HP+abs(DamageIn), MaxHP); print(f"{CurE} returned {DamageIn} HP to {pronoun2}.") if HP != MaxHP else print(f"{CurE} maxed out {yourvsnames} HP.")
					else: print(f"{CurE} was unable to return any of {yourvsnames} HP.")
					SoundCh.SFX.play(heal) if DamageIn != 0 else SoundCh.BAT2.play(miss)
				elif DamageIn > 0: PendingDamage += DamageIn; print(f"{CurE}'s first heal landed!"); pause(); continue
				else: SoundCh.SFX.play(miss); print(f"{CurE} was unable to return any of {yourvsnames} HP."); pause(); break
			elif Shado or CurE == "Shadorako":
				ShadoArchCasualAttacks = {"Pessimistic Punch": 1, "Traumatic Triple": 1.1, "Grip of Grief": 1.2, "Bleak Blast": 1.8, "Jaded Jab": 1.5}; ShadoArchAttack = random.choice(list(ShadoArchCasualAttacks.keys())); JabSleep = random.randint(1,10) == 2; DMGShield = random.randint(0,5)
				print(f"Shadorako chose {Fore.MAGENTA+f"{ShadoArchAttack}"+Fore.WHITE}..."); time.sleep(2); dmgMult = ShadoArchCasualAttacks[ShadoArchAttack]; dmg = round(random.randint(10,25)*dmgMult)
				if Lvl < 4 and DMGShield > 1: dmg /= DMGShield; dmg = round(dmg); print(f"You braced yourself. Incoming damage divided by {DMGShield}!"); pause()
				if hohsisjoj+1 == AtkAmount and dmg > 0:
					if ShadoArchAttack != "Traumatic Triple": SoundCh.SFX.play(hurt); HP -= round(dmg/max((defense/2),1))
					if ShadoArchAttack == "Pessimistic Punch": print(f"Shadorako dealt {round(dmg/max((defense/2),1))} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} with a punch!\n{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} feel{"s" if FocusedPlayer != "Pinori" else ""} less confident in defeating her.")
					elif ShadoArchAttack == "Grip of Grief":
						defense -= 1 if DMGShield != 0 and Lvl < 4 else -1; print(f"Shadorako dealt {round(dmg/max((defense/2),1))} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} with a tight grip! (Then she threw {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} a few feet away from her.)\n{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} defense {"de" if not (DMGShield > 2 and Lvl < 4) else "in"}creased by 1{" because you braced yourself" if DMGShield > 2 and Lvl < 4 else ""}!")
						if defense < 1: defense = 0; print(f"{FocusedPlayer} is vulnerable!")
					elif ShadoArchAttack == "Bleak Blast": print(f"Shadorako dealt {round(dmg/max((defense/2),1))} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} with a blast of dark magic!\n{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} feel{"s" if FocusedPlayer != "Pinori" else ""} like the future isn't looking so good.")
					elif ShadoArchAttack == "Jaded Jab": print(f"Shadorako dealt {round(dmg/max((defense/2),1))} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} with a jab.\n{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} feel{"s" if FocusedPlayer != "Pinori" else ""} a little tired...")
					elif ShadoArchAttack == "Traumatic Triple":
						parries = 0
						for _ in range(3):
							parry = random.randint(1,3) == 1 if not (DMGShield > 2 and Lvl < 4) else False
							if not parry:
								divisor = random.randint(3,6); HP -= round(dmg/divisor)
								if round(dmg/divisor) > 0: SoundCh.SFX.play(hurt); print(f"Shadorako dealt {round(dmg/divisor)} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer} with a punch! ({_+1}/3)")
								else: SoundCh.BAT2.play(miss); print("Shadorako's aim was a little too off. The punch missed!")
								time.sleep(0.25)
							else: SoundCh.BAT2.play(miss); print(f"({"You" if FocusedPlayer == "Pinori" else FocusedPlayer} parried this punch!)"); parries += 1; time.sleep(0.25)
							if parries == 3: print(Fore.YELLOW+f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} parried all 3 punches! "+Fore.WHITE+f"{f"{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} HP was maxed out." if HP+10 >= MaxHP else f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} recovered 10 HP."}"); SoundCh.SFX.play(heal); HP = min(HP+10, MaxHP)
							if ShadoArchAttack == "Jaded Jab" and JabSleep: SleepCounter += random.randint(1,2); AlreadyDecrementedSleep = True
				elif hohsisjoj+1 != AtkAmount and dmg > 0: PendingDamage += dmg; print(f"Shadorako's first attack landed."); pause(); continue
				elif dmg <= 0: SoundCh.SFX.play(miss); print("Somehow, Shadorako's attack missed."); pause(); break
			elif CurE == "Krystal" and KrystalHP > 0 and HP > 0:
				DamageIn = InDamage(Lvl, 14, defense, Yami=False)
				if FocusedPlayer != "Akuron": Succeed = False # anti-crash
				if sis+1 == AtkAmount and DamageIn > 0:
					HP -= DamageIn+PendingDamage if DamageIn > 0 else 0; SoundCh.BAT2.play(miss) if DamageIn == 0 else SoundCh.SFX.play(hurt)
					print(f"Krystal dealt {DamageIn+PendingDamage} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer}.") if DamageIn > 0 else print(f"Krystal's attack missed{" as well" if DamageOut <= 0 else ""}."); pause()
				elif DamageIn > 0: PendingDamage += DamageIn; print("Krystal's first attack landed!"); pause(); continue
				else:
					print(f"Krystal's attack missed{" as well" if PlayerMiss else ""}."); SoundCh.SFX.play(miss); pause()
			elif CurE in ["Pumpking", "Pumpqueen"] and PumpHP > 0 and HP > 0:
				DamageIn = InDamage(Lvl, 9, defense, Yami=False)
				if sis+1 == AtkAmount and DamageIn > 0:
					HP -= DamageIn+PendingDamage if DamageIn > 0 else 0; SoundCh.BAT2.play(miss) if DamageIn == 0 else SoundCh.SFX.play(hurt)
					print(f"The {CurE} dealt {DamageIn+PendingDamage} damage to you." if DamageIn > 0 else f"The {CurE}'s attack missed."); pause()
				elif DamageIn > 0: PendingDamage += DamageIn; print(f"The {CurE}'s first attack landed!"); pause(); continue
				else: print(f"The {CurE}'s attack missed{" as well" if PlayerMiss else ""}."); SoundCh.SFX.play(miss); pause()
			elif ShadoGuards:
				PendingDamage = 0
				for sis in range(AtkAmount):
					if globals()["ShadoGuard2HP"] > 0 or globals()["ShadoGuard1HP"] > 0:
						N = "Shadorako's Guards" if not (globals()["ShadoGuard1HP"] > 0 and globals()["ShadoGuard2HP"] > 0) else "Shadorako Guard 1" if globals()["ShadoGuard2HP"] <= 0 else "Shadorako Guard 2"
						DamageIn = InDamage(Lvl, 11 if Route != "Omnicide" else 14, defense, Yami=False)
						if sis+1 == AtkAmount and DamageIn > 0:
							HP -= DamageIn; SoundCh.SFX.play(hurt) if DamageIn > 0 else SoundCh.BAT2.play(miss)
							if DamageIn > 0: print(f"{N}{" collaboratively" if N == "Shadorako's Guards" else ""} dealt {DamageIn} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer}.")
							else: print(f"{N}'{"s" if N[-1].lower() != "s" else ""} attack missed."); pause(); break
						elif DamageIn > 0: print(f"{N}'{"s" if N[-1].lower() != "s" else ""} first attack landed."); pause(); PendingDamage += DamageIn; continue
						else: SoundCh.SFX.play(miss); print(f"{N}'{"s" if N[-1].lower() != "s" else ""} attack missed."); PendingDamage = 0
						pause()
					else:
						if globals()["ShadoGuard1HP"] <= 0 and globals()["ShadoGuard2HP"] > 0: OtherGuard = 2
						elif globals()["ShadoGuard2HP"] <= 0 and globals()["ShadoGuard1HP"] > 0: OtherGuard = 1
						if globals()["ShadoGuard1HP"] <= 0 and globals()["ShadoGuard2HP"] <= 0: break
						if globals()[f"ShadoGuard{OtherGuard}HP"] > 0:
							if Lightheadedness <= 0:
								typewriter_shadoguard("You... you killed her...", guard=OtherGuard); pause()
								typewriter_shadoguard("That was my best friend.", guard=OtherGuard); pause()
								typewriter_shadoguard("We knew each other for as long as I can remember.", guard=OtherGuard); pause()
								typewriter_shadoguard("And you just took her away from me.", guard=OtherGuard); pause()
								typewriter_shadoguard("I... I...", guard=OtherGuard); pause(); Dissatisfied = True
							else: print("(The other guard looks pretty upset that you killed her teammate.)"); pause(); Dissatisfied = True
							if Route != "Omnicide": SoundCh.SFX.play(DGS); print(Fore.RED + f"Shadorako Guard {OtherGuard} is dissatisfied."); pause()
							break
			if not ShadoGuards: pause()
	if not Challenge and CurE not in ["Krystal", "Pumpking", "Pumpqueen"]: ShadoGuardsBattleMenu() if CurE == "Shadorako's Guards" else BattleMenu() if CurE != "Shadorako" else ShadoArchlekiaBattleMenu()
	elif not Challenge and CurE in ["Pumpking", "Pumpqueen"]: WeenBossBattleMenu()
	elif not Challenge and CurE == "Krystal": KrystalBattleMenu()
	else: OWChallengeBattleMenu() if Challenge == "ow" else BChallengeBattleMenu()