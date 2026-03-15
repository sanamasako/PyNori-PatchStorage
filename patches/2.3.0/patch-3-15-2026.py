def FightEnem(Yami=False):
	global Satisfied, FocusedPlayer, VocalPoints, MaxVP, atk, Lvl, HP, MaxHP, CurE, EnemD, EnemyHP, EnemyMaxHP, EnemyLvl, EnemyATK, EnemyDefense, defense, AttackList, Diff, pronoun1, pronoun2, pronounBelonging, YamiBossHP, YamiBossMaxHP, CritChance; AvailableAttacks = []; atk_name = ""
	global hurt, weak, crit, sel, burn, mumiss, kick, kickcrit, trePunch, trePunchcrit, sheptone_c, sheptone_b, sheptone_bcrit, kickweak, kickmiss, trePunchweak, trePunchmiss, sheptone_bweak, sheptone_bmiss, tef, block, thunder; BlownAway = False
	global FoughtYami, bababooey, HasFoughtYet, DeathByDeerGod, DeathByBurn, YamiTraumatised, CantUseThisAttack, Quirk1, Quirk2, ActiveQuirk, DualQMode, DeathByDeerGodAlt, SleepCounter, ShadoArchHP, ShadoArchMaxHP, AlreadyPrayed, AlreadyDecrementedSleep, KrystalHP, KrystalMaxHP, Lightheadedness
	global wind, thunder; CritMSG = False
	if Yami: EnemyMaxHP = YamiBossMaxHP
	if not bababooey:
		if Yami: CurE = "Yami"
		ScramblePrint("= Attacks = Case sensitive, be careful! = Type \"exit\" to return. =")
		try:
			if "Invulnerable" in [ActiveQuirk, Quirk1, Quirk2]: ScramblePrint("= Attacks that say (FUTILE) cannot be used! =")
		except: pass
		ScramblePrint(f"\nVocal Points: {VocalPoints}/{MaxVP}")
		for attack in AttackList:
			try:
				if attack != CantUseThisAttack: ScramblePrint(f"{attack} - {AttackList[attack]} VP", c="red" if VocalPoints < AttackList[attack] else "white")
				else: ScramblePrint(f"{attack} - {AttackList[attack]} VP (FUTILE)", c="blue")
			except: ScramblePrint(f"{attack} - {AttackList[attack]} VP", c="red" if VocalPoints < AttackList[attack] else "white")
			AvailableAttacks.append(attack)
		while True:
			while atk_name not in AvailableAttacks:
				try:
					if CurE is None: print(Fore.RED+"CORPSE ENCOUNTER ALERT! IF THIS WAS NOT TRIGGERED BY A CTRL+C, PLEASE SEND A SCREENSHOT OF YOUR TERMINAL TO THE DEVELOPER IMMEDIATELY."); return
					atk_name = input(f"\n{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} chose "); VPCost = AttackList.get(atk_name)
					if atk_name.lower() == "exit": return
					if atk_name in AvailableAttacks:
						SoundCh.SFX.play(sel); HasFoughtYet = True; CritMSG = False
						if VPCost is not None:
							if (VocalPoints - VPCost) < 0: print(f"{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} throat is too sore to use this attack.")
							else:
								CritSound = kickcrit if atk_name == "Kick" else trePunchcrit if atk_name == "Treble Punch" else sheptone_bcrit if atk_name == "Shepard Tone" else kickcrit
								if CurE == "Shadorako":
									sys.stdout.write("\033[1A\033[K")
									AttackMSG = "\rYou chose {}...\n".format(atk_name) if FocusedPlayer == "Pinori" else "{} chose {}...\n".format(FocusedPlayer, atk_name)
									print(f"\r{AttackMSG}\n", end="")
									if atk_name == "Shepard Tone": SoundCh.BAT.play(sheptone_c)
									time.sleep(2); VocalPoints -= VPCost; Weather = BuildWeather(Silent=True) if WeatherEnabled else None
									if "Invulnerable" in [ActiveQuirk, Quirk1, Quirk2] and atk_name == CantUseThisAttack: SoundCh.SFX.play(block); print(f"{CurE} was unaffected!"); DamageOut = 0
									else:
										atkPerformance = random.randint(0,6); DamageOut = abs(OutDamage(atk_name, Lvl*(random.randint(1,3) if FocusedPlayer == "Pinori" and Lvl < 4 else 1), atk*(random.randint(2,15) if FocusedPlayer == "Pinori" and Lvl < 4 else 1), 10, 10, atkPerformance, VPCost, Diff))
										if DamageOut >= round(ShadoArchMaxHP/2): print("Critical hit!"); SoundCh.BAT2.play(crit); SoundCh.SFX.play(CritSound); CritMSG = True
										if DamageOut > 19 and not CritMSG: SoundCh.BAT.play(kick) if atk_name == "Kick" else SoundCh.BAT.play(trePunch) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_b) if atk_name == "Shepard Tone" else time.sleep(0)
										elif DamageOut in range(1,19): SoundCh.BAT.play(kickweak) if atk_name == "Kick" else SoundCh.BAT.play(trePunchweak) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_bweak) if atk_name == "Shepard Tone" else time.sleep(0)
										else: SoundCh.BAT.play(kickmiss) if atk_name == "Kick" else SoundCh.BAT.play(trePunchmiss) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_bmiss) if atk_name == "Shepard Tone" else time.sleep(0)
										dnamething = "You" if FocusedPlayer == "Pinori" else FocusedPlayer; dnamething2 = "r" if FocusedPlayer == "Pinori" else "'s"
										ShadoArchHP -= DamageOut; print(f"{dnamething} dealt {DamageOut} damage to {CurE}.") if DamageOut > 0 else print(f"{dnamething}{dnamething2} attack missed."); SoundCh.BAT2.play(miss) if DamageOut == 0 else SoundCh.SFX.play(weak) if round(DamageOut) in range(1,19) and not (CritChance == 23 or (DamageOut >= (round(ShadoArchMaxHP/2)))) else time.sleep(0)
									pause()
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
											else: Log("No heat effect. You're welcome!")
											if Weather["Wind"] in ["calm", "breezy"] and Weather[f"TempState{TempMeasurement[0].upper()}"] in ["mild heat", "moderate heat", "extreme heat"] and WindChance == 3: Refresher = max(round(int(Wind(BuildWeather(ReturnCurrent=True),ReturnKmph=True)))/2,1); HP = min(HP+round(Refresher),MaxHP); SoundCh.SFX.play(heal); SoundCh.WTHR.play(wind); print(f"The wind feels {"nice" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "mild heat" else "great" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "moderate heat" else "amazing"} in the {Weather[f"TempState{TempMeasurement[0].upper()}"]}. {"You" if FocusedPlayer == "Pinori" else FocusedPlayer}{f" recovered {round(Refresher)} HP" if HP < MaxHP else f"{"r" if FocusedPlayer == "Pinori" else "'s"} HP was maxed out"}!"); pause()
											elif Weather["Wind"] in ["windy", "powerful wind"] and WindChance == 3 or Weather["Wind"] == "deadly wind" and WindChance == 2: SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); print("A gust of wind knocks you on your side. Shadorako, however, is unaffected."); pause()
											else: Log("No wind effect. You're welcome!")
										except Exception as e: SoundCh.SFX.play(tef); Log(f"Weather logic error: {e}")
									if ShadoArchHP > 0 and HP > 0:
										ShadoArchCasualAttacks = {"Pessimistic Punch": 1, "Traumatic Triple": 1.1 if Route == "Omnicide" else 1, "Grip of Grief": 1.2, "Bleak Blast": 1.8 if Route == "Omnicide" else 1.4, "Jaded Jab": 1.5}; ShadoArchAttack = random.choice(list(ShadoArchCasualAttacks.keys())); JabSleep = random.randint(1,10) == 2; DMGShield = random.randint(0,5)
										print(f"Shadorako chose {Fore.MAGENTA+f"{ShadoArchAttack}"+Fore.WHITE}..."); time.sleep(2); dmgMult = ShadoArchCasualAttacks[ShadoArchAttack]; dmg = round(random.randint(10,25 if Route == "Omnicide" else 16)*dmgMult)
										if Lvl < 4 and DMGShield > 1: dmg /= DMGShield; dmg = round(dmg); print(f"You braced yourself. Incoming damage divided by {DMGShield}!"); pause()
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
								elif CurE == "Krystal":
									sys.stdout.write("\033[1A\033[K")
									AttackMSG = "\rYou chose {}...\n".format(atk_name) if FocusedPlayer == "Pinori" else "{} chose {}...\n".format(FocusedPlayer, atk_name)
									print(f"\r{AttackMSG}\n", end="")
									if atk_name == "Shepard Tone": SoundCh.BAT.play(sheptone_c)
									time.sleep(2); VocalPoints -= VPCost; Weather = BuildWeather(Silent=True) if WeatherEnabled else None
									if "Invulnerable" in [ActiveQuirk, Quirk1, Quirk2] and atk_name == CantUseThisAttack: SoundCh.SFX.play(block); print(f"{CurE} was unaffected!"); DamageOut = 0
									else:
										atkPerformance = random.randint(0,6); DamageOut = abs(OutDamage(atk_name, Lvl, atk, 8, 6, atkPerformance, VPCost, Diff))
										if DamageOut >= round(KrystalMaxHP/2): print("Critical hit!"); SoundCh.BAT2.play(crit); SoundCh.SFX.play(CritSound); CritMSG = True
										if DamageOut >= 19 and not CritMSG: SoundCh.BAT.play(kick) if atk_name == "Kick" else SoundCh.BAT.play(trePunch) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_b) if atk_name == "Shepard Tone" else time.sleep(0)
										elif DamageOut in range(1,19): SoundCh.BAT.play(kickweak) if atk_name == "Kick" else SoundCh.BAT.play(trePunchweak) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_bweak) if atk_name == "Shepard Tone" else time.sleep(0)
										else: SoundCh.BAT.play(kickmiss) if atk_name == "Kick" else SoundCh.BAT.play(trePunchmiss) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_bmiss) if atk_name == "Shepard Tone" else time.sleep(0)
										KrystalHP -= DamageOut; print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} dealt {DamageOut} damage to Krystal.") if DamageOut > 0 else print(f"{"Your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} attack missed."); SoundCh.BAT2.play(miss) if DamageOut == 0 else SoundCh.SFX.play(weak) if round(DamageOut) in range(1,19) and not (CritChance == 23 or (DamageOut >= (round(KrystalMaxHP/2)))) else time.sleep(0)
									pause(); AkuronSwing = random.randint(1,5)
									if AkuronSwing == 3 and FocusedPlayer == "Akuron":
										print("Akuron swung his sword at Krystal!"); time.sleep(3); Succeed = random.randint(1,3) != 1
										if Succeed: KrystalHP -= 5; SoundCh.BAT.play(kick); print("Krystal took 5 damage!"); pause(); print("Krystal: Nice swing, lad!"); pause()
										else: SoundCh.SFX.play(block); print("Krystal blocked his swing with her sword!"); pause()
									else: Succeed = False # crash prevention
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
											else: Log("No heat effect. You're welcome!")
											if Weather["Wind"] in ["calm", "breezy"] and Weather[f"TempState{TempMeasurement[0].upper()}"] in ["mild heat", "moderate heat", "extreme heat"] and WindChance == 3: Refresher = max(round(int(Wind(BuildWeather(ReturnCurrent=True),ReturnKmph=True)))/2,1); HP = min(HP+round(Refresher),MaxHP); SoundCh.SFX.play(heal); SoundCh.WTHR.play(wind); print(f"The wind feels {"nice" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "mild heat" else "great" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "moderate heat" else "amazing"} in the {Weather[f"TempState{TempMeasurement[0].upper()}"]}. {"You" if FocusedPlayer == "Pinori" else FocusedPlayer}{f" recovered {round(Refresher)} HP" if HP < MaxHP else f"{"r" if FocusedPlayer == "Pinori" else "'s"} HP was maxed out"}!"); pause()
											elif Weather["Wind"] in ["windy", "powerful wind"] and WindChance == 3 or Weather["Wind"] == "deadly wind" and WindChance == 2: SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); print("A gust of wind knocks you on your side. Krystal, however, somehow stands her ground."); pause()
											else: Log("No wind effect. You're welcome!")
										except Exception as e: SoundCh.SFX.play(tef); Log(f"Weather logic error: {e}")
									if KrystalHP > 0 and HP > 0:
										DamageIn = InDamage(Lvl, 14, defense, Yami=False); HP -= DamageIn
										SoundCh.BAT2.play(miss) if DamageIn == 0 else SoundCh.SFX.play(hurt)
										print(f"Krystal dealt {DamageIn} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer}.") if DamageIn > 0 else print(f"Krystal's attack missed{" as well" if DamageOut <= 0 else ""}."); pause()
										if DamageIn + DamageOut == 0 and not Succeed: SoundCh.BAT2.play(mumiss); print("It's a mutual miss!")
								else:
									FoughtYami = True if Yami else False # don't lock the player out of the "prayer ending" just for selecting fight even if they don't attack
									sys.stdout.write("\033[1A\033[K")
									AttackMSG = "\rYou chose {}...\n".format(atk_name) if FocusedPlayer == "Pinori" else "{} chose {}...\n".format(FocusedPlayer, atk_name)
									print(f"\r{AttackMSG}\n", end="")
									if atk_name == "Shepard Tone": SoundCh.BAT.play(sheptone_c)
									time.sleep(2); OP_Enemies = ["Corrupted Soul", "???"] # enemies that are (intentionally) completely broken
									# non-broken enemies that still need an attack buff to defeat
									Lesser_OP_Enemies = ["Shark"] # there's only this left because Yatta and Zetta Bite were removed :sob:
									VocalPoints -= VPCost; Weather = BuildWeather(Silent=True) if WeatherEnabled else None
									if "Invulnerable" in [ActiveQuirk, Quirk1, Quirk2] and atk_name == CantUseThisAttack: SoundCh.SFX.play(block); print(f"{CurE} was unaffected!"); DamageOut = 0 # the unindented pause will work here
									else:
										atkPerformance = random.randint(0,6); DamageOut = abs(OutDamage(atk_name, Lvl, atk, EnemyLvl, EnemyDEF, atkPerformance, VPCost, Diff))
										if DamageOut > 500 and (CurE not in OP_Enemies or Lvl < 10): # might have to adjust this later but yes there will be a point where the damage cap is removed, I've decided
											if args.debug: print(Fore.YELLOW + "DEBUG: Attack damage was limited because it was too overpowered."); print(Fore.YELLOW + f"DEBUG: Unhinged damage: {DamageOut}")
											Log(f"Attack damage was limited because it was too overpowered. Unhinged damage was {DamageOut}."); DamageOut = random.randint(480,500)
										if CurE in OP_Enemies: DamageOut *= random.randint(317,482)
										# TRADE OFFER | I get: extremely high defense enemies because oooo scary | you get: to beat the absolute life out of them because the values I input are unbalanced as hell and I'm too lazy to fine-tune them
										elif CurE in Lesser_OP_Enemies: DamageOut *= random.randint(20,30)
										if Yami: YamiBossHP -= DamageOut
										else: EnemyHP -= DamageOut
										if not CritMSG and CritChance == 23 and DamageOut != 0:
											CritMSG = True; SoundCh.SFX.play(CritSound)
											Crit_Criteria = (DamageOut >= (round((YamiBossMaxHP if Yami else EnemyMaxHP)/2))) or round(DamageOut) in range(100,199)
											Suhit_Criteria = ((DamageOut >= (round((YamiBossMaxHP if Yami else EnemyMaxHP)/4))*3) and not (DamageOut >= (round((YamiBossMaxHP if Yami else EnemyMaxHP)/5))*4)) or round(DamageOut) in range(200,299)
											Uhit_Criteria = (DamageOut >= (round((YamiBossMaxHP if Yami else EnemyMaxHP)/5))*4) and not (DamageOut >= (round((YamiBossMaxHP if Yami else EnemyMaxHP)/8))*7) or round(DamageOut) in range(300,399)
											Brit_Criteria = (DamageOut >= (round((YamiBossMaxHP if Yami else EnemyMaxHP)/8))*7) and not (DamageOut >= (YamiBossMaxHP if Yami else EnemyMaxHP)) or round(DamageOut) in range(400,499)
											Fhit_Criteria = DamageOut >= (YamiBossMaxHP if Yami else EnemyMaxHP) or round(DamageOut) > 499
											Log(f"= HIT CRITERIA =\n\nCritical: {Crit_Criteria}\nSuper: {Suhit_Criteria}\nUltra: {Uhit_Criteria}\nBrutal: {Brit_Criteria}\nFatal: {Fhit_Criteria}")
											if Fhit_Criteria: Log("Hit was FATAL!"); SoundCh.BAT2.play(fhit); print(Fore.RED+f"FATAL HIT!{"!!" if CritChance == 23 else ""}")
											elif Brit_Criteria: Log("Hit was brutal!"); SoundCh.BAT2.play(brit); print((Fore.YELLOW if CritChance == 23 else Fore.WHITE)+"Brutal hit!!!!")
											elif Uhit_Criteria: Log("Hit was ultra."); SoundCh.BAT2.play(uhit); print((Fore.YELLOW if CritChance == 23 else Fore.WHITE)+"Ultra hit!!!")
											elif Suhit_Criteria: Log("Hit was super."); SoundCh.BAT2.play(suhit); print((Fore.YELLOW if CritChance == 23 else Fore.WHITE)+"Super hit!!")
											elif Crit_Criteria: Log("Hit was only critical."); SoundCh.BAT2.play(crit); print((Fore.YELLOW if CritChance == 23 else Fore.WHITE)+"Critical hit!")
										if DamageOut >= 19 and not CritMSG: SoundCh.BAT.play(kick) if atk_name == "Kick" else SoundCh.BAT.play(trePunch) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_b) if atk_name == "Shepard Tone" else time.sleep(0)
										elif DamageOut in range(1,19): SoundCh.BAT.play(kickweak) if atk_name == "Kick" else SoundCh.BAT.play(trePunchweak) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_bweak) if atk_name == "Shepard Tone" else time.sleep(0)
										elif DamageOut <= 0: SoundCh.BAT.play(kickmiss) if atk_name == "Kick" else SoundCh.BAT.play(trePunchmiss) if atk_name == "Treble Punch" else SoundCh.BAT.play(sheptone_bmiss) if atk_name == "Shepard Tone" else time.sleep(0)
										print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} dealt {DamageOut} damage to {CurE}.") if DamageOut > 0 else print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer}{"r" if FocusedPlayer == "Pinori" else "'s"} attack missed."); SoundCh.BAT2.play(miss) if DamageOut == 0 else SoundCh.SFX.play(weak) if round(DamageOut) in range(1,19) and not (CritChance == 23 or (DamageOut >= (round(EnemyMaxHP/2)))) else time.sleep(0)
									pause()
									if "Hot" in CurE: print(f"{"The" if FocusedPlayer == "Pinori" else "Your"} opponent is piping hot. Attacking it dispersed a lot of heat, slightly burning {"you" if FocusedPlayer == "Pinori" else FocusedPlayer}. {"You" if FocusedPlayer == "Pinori" else FocusedPlayer} took 1 damage!"); SoundCh.SFX.play(burn); HP -= 1; DeathByBurn = True
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
											else: Log("No heat effect. You're welcome!")
											if Weather["Wind"] in ["calm", "breezy"] and Weather[f"TempState{TempMeasurement[0].upper()}"] in ["mild heat", "moderate heat", "extreme heat"] and WindChance == 3: Refresher = max(round(int(Wind(BuildWeather(ReturnCurrent=True),ReturnKmph=True)))/2,1); HP = min(HP+round(Refresher),MaxHP); SoundCh.SFX.play(heal); SoundCh.WTHR.play(wind); print(f"The wind feels {"nice" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "mild heat" else "great" if Weather[f"TempState{TempMeasurement[0].upper()}"] == "moderate heat" else "amazing"} in the {Weather[f"TempState{TempMeasurement[0].upper()}"]}. {"You" if FocusedPlayer == "Pinori" else FocusedPlayer}{f" recovered {round(Refresher)} HP" if HP < MaxHP else f"{"r" if FocusedPlayer == "Pinori" else "'s"} HP was maxed out"}!"); pause()
											elif Weather["Wind"] in ["windy", "powerful wind"] and WindChance == 3 or Weather["Wind"] == "deadly wind" and WindChance == 2:
												if not Yami: SoundCh.WTHR.play(wind); print("A gust of wind blew the enemy away!"); pause(); BlownAway = True; break
												else: SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); SoundCh.WTHR.play(wind); print("A gust of wind knocks you on your side. Yami, however, jams her sword deep into the ground and grips the handle for dear life.\nAfter the gust of wind ceases, she pulls her sword out of the ground and wipes it clean."); pause()
											else: Log("No wind effect. You're welcome!")
										except Exception as e: SoundCh.SFX.play(tef); Log(f"Weather logic error: {e}")
						else: print(Fore.RED + "???")
						if Yami:
							if YamiBossHP > 0:
								dmg = InDamage(Lvl, 34, defense, Yami=True); HP -= dmg if dmg != 0.01 else 0 # 0.01 is my little code for "nothing happens" cuz of the early exit code in case Yami does a Melee+
								SoundCh.SFX.play(hurt) if dmg not in [0, 0.01] else time.sleep(0) if dmg != 0 else SoundCh.BAT2.play(miss)
								print(f"{"C" if not YamiTraumatised else "Inc"}onsistently, Yami dealt {dmg} damage to you.") if dmg not in [0, 0.01] else print("Surprisingly, Yami's attack missed. Yami flinches from surprise and sweats briefly.") if dmg != 0.01 else time.sleep(0); pause()
						elif CurE not in ["Shadorako", "Krystal"]:
							if EnemyHP > 0:
								DamageIn = InDamage(Lvl, EnemyATK, defense, Yami=False)
								if CurE not in ["Clef", "Treble"] or (CurE == "Clef" and not ClefHappy): HP -= DamageIn
								else: HP = min(HP + DamageIn, MaxHP)
								if DamageIn != 0 and DamageIn > 0 and CurE != "Clef": SoundCh.SFX.play(hurt)
								else:
									if CurE in ["Clef", "Treble"]: SoundCh.SFX.play(heal) if DamageIn != 0 else SoundCh.BAT2.play(miss)
									else: SoundCh.BAT2.play(miss)
								if CurE not in ["Clef", "Treble"] or (CurE in ["Clef", "Treble"] and not ClefHappy):
									if DamageIn > 0: print(f"{CurE} dealt {DamageIn} damage to you.") if FocusedPlayer == "Pinori" else print(f"{CurE} dealt {DamageIn} damage to {FocusedPlayer}.")
									else:
										try: SentenceEnd = "." if (DamageOut + DamageIn) != 0 else " as well."
										except Exception: SentenceEnd = "."
										print(f"{CurE}'s attack missed{SentenceEnd}")
									try:
										if isinstance(DamageIn, int) and isinstance(DamageOut, int) and (DamageIn + DamageOut) == 0 and (not "Hot" in CurE): # only do this if an attack actually happened (yay no more dumb crashes I hope)
											pause(); SoundCh.BAT2.play(mumiss); print("It's a mutual miss!")
									except Exception: pass # it's fine if this throws an error
								else: print(f"{CurE} returned {DamageIn} HP to {'you' if FocusedPlayer == 'Pinori' else FocusedPlayer}." if DamageIn >= 1 and HP != MaxHP else f"{CurE} maxed out {'your' if FocusedPlayer == 'Pinori' else f'{FocusedPlayer}\'s'} HP." if DamageIn >= 1 else f"{CurE} was unable to return any of {'your' if FocusedPlayer == 'Pinori' else f'{FocusedPlayer}\'s'} HP.")
								pause()
						AlreadyPrayed = False
						if HP > 0: YamiBattleMenu() if Yami else BattleMenu() if CurE not in ["Krystal", "Shadorako"] else ShadoArchlekiaBattleMenu() if CurE == "Shadorako" else KrystalBattleMenu()
						elif HP <= 0 and Yami: GameOver()
						else:
							PlayerStatStorage[FocusedPlayer]["HP"] = HP; TotalHP = 0; PartyMembersAsString = ", ".join(map(str, Party))
							Log(f"Party: {PartyMembersAsString}"); validnames = ["Pinori", "Akuron", "Sana", "Yami"]
							for member in Party:
								if member not in validnames: continue
								Log(f"Adding {member}'s HP.")
								if args.debug: print(Fore.YELLOW + f"DEBUG: {member}'s HP is {PlayerStatStorage[member]['HP']}.")
								if PlayerStatStorage[member]['HP'] <= 0:
									if args.debug: print(Fore.YELLOW + f"DEBUG: {member} is literally dead lol")
								else:
									if member != FocusedPlayer: TotalHP += int(PlayerStatStorage[member]['HP']); Log(f"Total HP is now at {TotalHP}.")
									else: Log(f"Assessed character is focused player. Total HP remains at {TotalHP}.")
							Log("That's everyone. The consensus is...")
							if TotalHP <= 0 or len(Party) == 1: Log("Gaming over! Damn! Crud! Fiddlesticks! That just sucks."); GameOver() # only game over if everyone is unconscious
							else: Log("Someone's still alive! Good for them!"); print(f"{FocusedPlayer} is unconscious!"); pause(); SwitchMember(Forced=True); return # this can't trigger if Pinori is alone
					else: print(f"Invalid attack. {"Remember, case sensitive!" if atk_name.title() in AvailableAttacks else ""}")
				except (IndexError, ValueError) as DUMBTHINGLOL: SoundCh.SFX.play(tef); Log(f"EXCEPTION (except why the hell would this of all things break): {DUMBTHINGLOL}"); print("Invalid attack."); continue
		if BlownAway: BattleWon("flee", FleeText=False)
	else:
		print(f"You forgot how to attack, so you did what you could to deal damage to {CurE}."); time.sleep(4)
		dmg = OutDamage("Shepard Tone", Lvl, atk, EnemyLvl, random.randint(5,16), random.randint(0,6), (random.randint(1,4)*10), "Harder")
		if dmg <= 0: SoundCh.BAT2.play(miss); print("Nothing happened.")
		else:
			if dmg > 80: SoundCh.BAT2.play(crit)
			EnemyHP -= dmg; SoundCh.BAT.play(kick); print(f"You dealt {dmg} damage to {CurE}.") # April Fools' event is always in Pinori's pov so this remains unchanged too
		pause()
		if "Hot" in CurE: print(f"Your opponent is piping hot. Attacking it dispersed a lot of heat, slightly burning you. You took 1 damage!"); SoundCh.SFX.play(burn); HP -= 1; DeathByBurn = True
		if EnemyHP >= 1:
			TheEnemyStrikes = InDamage(Lvl, EnemyATK, defense, Yami=False); HP -= TheEnemyStrikes
			if (HP - TheEnemyStrikes) < 0: HP = 0
			if TheEnemyStrikes <= 0: SoundCh.BAT2.play(miss); print(f"{CurE}'s attack missed.")
			else:
				if TheEnemyStrikes > ((HP/7)*4): SoundCh.BAT2.play(crit)
				SoundCh.SFX.play(hurt); print(f"{CurE} dealt {TheEnemyStrikes} damage to you.")
			if dmg + TheEnemyStrikes <= 0: pause(); SoundCh.BAT2.play(mumiss); RandomUnnecessaryTaunt = ["Get good.", "Try harder.", "Have you tried turning it off and on again?", "Weakling.", "1, 2, 3 strikes you're out at the old ball game.", "Pneumonoultramicroscopicsilicovolcanoconi-oh-damn.", "Your keyboard looks like it needs a kiss.", "One miss, two miss, no miss, mutual miss.", "Foul ball!", "If you miss this next attack I'm going to spam you with brainrot. (I'm kidding, but imagine.)", "That tracks.", "Baseball, huh?"]; print(f"It's a mutual miss! ({random.choice(RandomUnnecessaryTaunt)})")
			pause()
		if HP <= 0: GameOverAprilFool()