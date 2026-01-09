def EnterBattle(Challenge=None):
	global Route, LocCode, LocCodes, location, npc_battle, CurE, EnemD, spares, EnemyHP, EnemyMaxHP, NeedsInteract, Satisfied, EnemyLvl, EnemyATK, EnemyDEF, IsbattleNPC, satisfaction, ActiveQuirk, Quirk1, Quirk2, DualQMode, EXP, EnemyPop, AlreadyDecrementedSleep, AlreadyDecrementedCaffeine, PStoggle, EnemyPopINI
	global ClefHappy, InBattle, bababooey, BattleOrNot, overworld, HasFoughtYet, tef, ShownLowHPWarning, DeathByDeerGod, DeathByBurn, AttackList, CantUseThisAttack, VocalPoints, weak, CanInteract, Dissatisfied, dissatisfaction, EnemyAsleep, DeathByDeerGodAlt, SeeSimi, PrevState, Weather, WeatherEnabled, TempMeasurement
	ClefHappy = True if Route != "Omnicide" else False; satisfaction, dissatisfaction = 0, 0; LocCode = "Challenge" if Challenge else LocCode; global EnemPowAmped, EnemPowNerfed; EnemPowAmped, EnemPowNerfed = False, False
	Satisfied, HasFoughtYet, EnemyAsleep, StartBattle, AlreadyDecrementedSleep, AlreadyDecrementedCaffeine = False, False, False, False, False, False; AquaticEnemyWarning = False
	AquaticEnemies = ["Shark", "Dolphin", "Lionfish", "Fishenstein", "Pam the Clam", "Investigator", "Fish"]
	try:
		if Weather: pass
	except: Weather = None
	
	if "Invulnerable" in [ActiveQuirk, Quirk1, Quirk2] and "Enemies Fear You" not in [ActiveQuirk, Quirk1, Quirk2] and not Challenge:
		Attacks = []
		for attack in AttackList: Attacks.append(attack)
		CantUseThisAttack = random.choice(Attacks); SoundCh.SFX.play(weak); print(f"WARNING! Your opponent will be immune to your {CantUseThisAttack}!")
		if VocalPoints == 0 and CantUseThisAttack == "Kick": print("If you have no AUX Cord Energy Drinks, you may have to flee this battle.")
		pause()

	if ActiveQuirk == "Enemies Fear You" or (DualQMode and (Quirk1 == "Enemies Fear You" or Quirk2 == "Enemies Fear You")) and not Challenge: Log("Whoops! You're very scary so no battles for you."); print("Huh? The enemy ran away..."); spares += 1; pause(); overworld = None; BattleOrNot = 16
	else:
		try:
			npc_battle = random.randint(0, 40); Log(f"NPC battle variable: {npc_battle}")
			if npc_battle == 16 and not Challenge:
				Log("Ooooo you're battling an innocent character, don't do anything I wouldn't do"); pool = EnemyPool[LocCode]["NPC"]; IsbattleNPC = True
				if debug and npc_battle == 16: print(Fore.YELLOW + "DEBUG: NPC BATTLE!")
				elif debug and npc_battle != 16: print(Fore.YELLOW + "DEBUG: Computers really are a lot dumber than they seem."); pool = EnemyPool[LocCode]["Traditional"]
				if npc_battle != 16: Log("Compooter had a brainfart"); pool = EnemyPool[LocCode]["Traditional"]
			else:
				Log("You're battling a regular enemy."); IsbattleNPC = False
				if Route == "Traditional" or Challenge: pool = EnemyPool[LocCode]["Traditional"]; Log(f"The enemy will come from the {LocCode} Traditional enemy pool."); Log(f"{LocCode} Traditional Enemy Pool: {EnemyPool[LocCode]["Traditional"]}")
				elif Route == "Omnicide":
					ERandom = random.randint(0, 3); RandomCode = random.choice(LocCodes); PoolTypes = ["Traditional", "Omnicide", "NPC"]; RPoolType = random.choice(PoolTypes); RPool = ""
					if ERandom == 0:
						Log("RNG has decided that further RNG will randomise the pool and location in which your opponent will come from.")
						if args.debug: print(Fore.YELLOW + "DEBUG: THE RANDOMISER IS REAL!"); RPool = dpt(RPoolType, npc_battle)
						
						if RPool:
							if RandomCode: pool = EnemyPool[RandomCode][RPoolType]; Log(f"Your enemy will come from the {RandomCode} {RPoolType} enemy pool.")
							else: pool = EnemyPool[LocCode][RPoolType]; Log(f"Your enemy will come from your current location's {RPoolType} enemy pool.")
							IsBattleNPC = True if RPool == "NPC" else False
						else: pool = EnemyPool[LocCode]["Omnicide"]; Log("RNG has decided that the enemy pool will not be scrambled this time.")
					else: pool = EnemyPool[LocCode][RPoolType]; Log(f"Your enemy will come from your current location's {RPoolType} enemy pool.")
				else:Log("Shirley made a humongous oops! Time to try to find the bug for 2 months only to find out the solution was as simple as adding/removing a conditional branch."); BadCodeSong()
			BattleLoadError = False; Extinct = [""]; CurE = ""
			if Challenge not in ["ow", "battle"]:
				while StartBattle is False:
					while CurE in Extinct: CurE = random.choice(pool)
					Log(f"Current opponent choice is {CurE}.")
					CurE_PopCheck = configparser.ConfigParser()
					try: CurE_PopCheck.read(EnemyPopINI)
					except Exception as e: Log(f"An error occurred when reading EnemyPopulation.ini. The battle has been aborted.\nDetails: {e}"); SoundCh.SFX.play(tef); BattleLoadError = True; break
					try:
						if int(CurE_PopCheck["Enemy"][CurE.lower()]) == 0 or EnemyPop[CurE] == 0: Log(f"{CurE} is extinct. Choosing an enemy that's not {CurE}."); Extinct.append(CurE)
						else: StartBattle = True # enemies with a positive population will be encounterable until their population reaches 0; enemies with a negative population are intended to spawn until the area population is exhausted
					except Exception as e: Log(f"An error occurred when checking the population of {CurE}: {e}\nEnemyPop: {EnemyPop}"); SoundCh.SFX.play(tef); BattleLoadError = True
				if BattleLoadError: BattleWon("error")
			else: CurE = random.choice(pool)
			Log(f"Your opponent is {CurE}.")
			EnemStat = InitEnemStat(CurE); Log(f"Enemy Stats (raw): {EnemStat}")
			EnemyMaxHP = EnemStat.get('health', 0)
			EXP = int(EnemStat.get('EXP', 0)); Log("Loaded your opponent's EXP.")
			EnemyHP = EnemyMaxHP; Log("Loaded your opponent's HP.")
			EnemyATK = EnemStat.get('attack', 0); Log("Loaded your opponent's attack.")
			EnemyDEF = EnemStat.get('defense', 0); Log("Loaded your opponent's defense.")
			EnemyLvl = EnemStat.get('level', 0); Log("Loaded your opponent's level."); LvlDiff = abs(Lvl-EnemyLvl)
			if not Challenge and EnemStat["Powerscaling"]["enabled"] == "True" and EnemStat["Powerscaling"]["mode"] not in [None, "null"] and LvlDiff//int(EnemStat["Powerscaling"]["ratio"].split(":")[-1]) > 0 and PStoggle:
				PowerscaleMode = EnemStat["Powerscaling"]["mode"]; PowerscaleType = EnemStat["Powerscaling"]["method"]; Log(f"{CurE} allows powerscaling {PowerscaleMode if PowerscaleMode != "bidi" else "bidirectionally"} with type {PowerscaleType}.")
				PowerscaleMultiplier, MultPerLevel = EnemStat["Powerscaling"]["ratio"].split(":"); PowerscaleMultiplier, MultPerLevel = float(PowerscaleMultiplier), int(MultPerLevel); Log(f"Powerscale ratio is {PowerscaleMultiplier}x per {MultPerLevel} level{"s" if MultPerLevel != 1 else ""}.")
				ScaleCount = LvlDiff//MultPerLevel; Log(f"The powerscale will be performed {ScaleCount} time{"s" if ScaleCount != 1 else ""}.\nEnemy stats: {EnemyMaxHP} HP, {EnemyATK} ATK {EnemyDEF} DEF")
				if ScaleCount > 0: print(f"You're at a{" dis" if EnemyLvl > Lvl else "n "}advantage, so your opponent has become {"weak" if EnemyLvl > Lvl else "strong"}er!"); pause()
				for _ in range(ScaleCount):
					if PowerscaleType == "mult" and EnemyLvl < Lvl and PowerscaleMode in ["up", "bidi"]:
						EnemyLvl *= PowerscaleMultiplier; EnemyLvl = round(EnemyLvl)
						EnemyMaxHP *= PowerscaleMultiplier; EnemyMaxHP = round(EnemyMaxHP); EnemyHP = EnemyMaxHP
						EnemyATK *= PowerscaleMultiplier; EnemyATK = round(EnemyATK)
						EnemyDEF *= PowerscaleMultiplier; EnemyDEF = round(EnemyDEF); EnemPowAmped = True
					elif PowerscaleType == "mult" and EnemyLvl > Lvl and PowerscaleMode in ["down", "bidi"]:
						EnemyLvl /= PowerscaleMultiplier; EnemyLvl = max(round(EnemyLvl), 1)
						EnemyMaxHP /= PowerscaleMultiplier; EnemyMaxHP = round(EnemyMaxHP); EnemyHP = EnemyMaxHP
						EnemyATK /= PowerscaleMultiplier; EnemyATK = round(EnemyATK)
						EnemyDEF /= PowerscaleMultiplier; EnemyDEF = round(EnemyDEF); EnemPowNerfed = True
					elif PowerscaleType == "add" and EnemyLvl > Lvl and PowerscaleMode in ["down", "bidi"]:
						ELvlBonus = round(EnemyLvl*(PowerscaleMultiplier-1)); EnemyLvl -= ELvlBonus
						EMaxHPBonus = round(EnemyMaxHP*(PowerscaleMultiplier-1)); EnemyMaxHP -= EMaxHPBonus; EnemyHP = EnemyMaxHP
						EATKBonus = round(EnemyATK*(PowerscaleMultiplier-1)); EnemyATK -= EATKBonus
						EDEFBonus = round(EnemyDEF*(PowerscaleMultiplier-1)); EnemyDEF -= EDEFBonus; EnemPowNerfed = True
					elif PowerscaleType == "add" and EnemyLvl < Lvl and PowerscaleMode in ["up", "bidi"]:
						ELvlBonus = round(EnemyLvl*(PowerscaleMultiplier-1)); EnemyLvl += ELvlBonus
						EMaxHPBonus = round(EnemyMaxHP*(PowerscaleMultiplier-1)); EnemyMaxHP += EMaxHPBonus; EnemyHP = EnemyMaxHP
						EATKBonus = round(EnemyATK*(PowerscaleMultiplier-1)); EnemyATK += EATKBonus
						EDEFBonus = round(EnemyDEF*(PowerscaleMultiplier-1)); EnemyDEF += EDEFBonus; EnemPowAmped = True
					elif PowerscaleType == "level" and EnemyLvl < Lvl and PowerscaleMode in ["up", "bidi"]: EnemyLvl += 1; EnemyMaxHP += random.randint(5,15); EnemyHP = EnemyMaxHP; EnemyATK += random.randint(1,3); EnemyDEF += 1; EnemPowAmped = True
					elif PowerscaleType == "level" and EnemyLvl > Lvl and PowerscaleMode in ["down", "bidi"]: EnemyLvl = max(EnemyLvl-1,1); EnemyMaxHP -= random.randint(5,15); EnemyMaxHP = max(EnemyMaxHP,1); EnemyHP = EnemyMaxHP; EnemyATK -= random.randint(1,3); EnemyATK = max(EnemyATK,1); EnemyDEF = max(EnemyDEF-1,1); EnemPowNerfed = True
					Log(f"Enemy stats after powerscale {_+1}: {EnemyMaxHP} HP, {EnemyATK} ATK {EnemyDEF} DEF")
			else: Log("No powerscaling allowed because someone (you or the enemy) disallowed it, you're about equal in power, or you're doing a Daily Challenge.")
			if Challenge not in ["ow", "battle"] and not Weather: Weather = BuildWeather(Silent=True) if WeatherEnabled else None
			if Weather:
				if CurE in AquaticEnemies and "rain" in Weather["Conditions"]:
					AquaticEnemyWarning = True; print(f"Because you're encountering an aquatic enemy in the rain, they've become 1.1x more powerful!{"\nDue to this, their EXP value has also increased by the same amount." if KillSystemSwitch(task="check") == "EXP" else ""}"); pause()
					EXP *= 1.1; EnemyHP *= 1.1; EnemyMaxHP *= 1.1; EnemyATK *= 1.1; EnemyDEF *= 1.1; EnemyLvl *= 1.1
					EXP, EnemyHP, EnemyMaxHP, EnemyATK, EnemyDEF, EnemyLvl = round(EXP), round(EnemyHP), round(EnemyMaxHP), round(EnemyATK), round(EnemyDEF), round(EnemyLvl); EnemPowAmped = True
				if "Hot" in CurE and "sunny" in Weather["Conditions"]:
					print("Additionally, the enemy is hot, so they've received another 1.1x strength buff.\nSounds tough... good luck!" if AquaticEnemyWarning else f"Because you're encountering a hot enemy in the heat, they've become 1.1x more powerful!{"\nDue to this, their EXP value has also increased by the same amount." if KillSystemSwitch(task="check") == "EXP" else ""}"); pause()
					EXP *= 1.1; EnemyHP *= 1.1; EnemyMaxHP *= 1.1; EnemyATK *= 1.1; EnemyDEF *= 1.1; EnemyLvl *= 1.1
					EXP, EnemyHP, EnemyMaxHP, EnemyATK, EnemyDEF, EnemyLvl = round(EXP), round(EnemyHP), round(EnemyMaxHP), round(EnemyATK), round(EnemyDEF), round(EnemyLvl); EnemPowAmped = True
			NI = EnemStat.get('NeedsInteractionToSpare', "False"); CI = EnemStat.get('CanInteract', "False"); Log("Loaded interaction conditions.")
			pronoun1 = EnemStat.get('pronoun1', 'It'); pronoun2 = EnemStat.get('pronoun2', 'Its'); pronounBelonging = EnemStat.get('pronounBelonging', 'Its'); Log("Loaded enemy pronouns (yes, that's an official thing LOL).")
			NeedsInteract = True if NI == "True" else False; CanInteract = True if CI == "True" else False
			if NI in ["True", "False"]: Log(f"Interact condition is {NeedsInteract}.")
			if CI in ["True", "False"]: Log(f"Optional interactions?: {CanInteract}")
			Satisfied, Dissatisfied = False, False
			if args.debug: print(Fore.YELLOW + f"DEBUG: Enemy is {CurE}")
			if npc_battle == 16 and debug: print(Fore.YELLOW + "DEBUG: Enemy is NPC")
			else:
				if args.debug: print(Fore.YELLOW + "DEBUG: Enemy is not NPC")
		except (KeyError, UnboundLocalError) as e:
			SoundCh.SFX.play(tef)
			Log(f"AN ERROR OCCURRED WHILE LOADING THE BATTLE: {e}")
			if args.debug: print(Fore.YELLOW + f"DEBUG: {e}")
			print("Huh...? That's weird, I swear there was someone approaching. Oh well."); pause(); return
	if args.debug: print(Fore.YELLOW + f"DEBUG: Route: {Route}, Location Code: {LocCode}, NPC Battle? (16 = True): {npc_battle}")
	if ActiveQuirk == "Enemies Fear You" or (DualQMode and (Quirk1 == "Enemies Fear You" or Quirk2 == "Enemies Fear You")) and not Challenge: return
	else:
		ShownLowHPWarning = False; DeathByDeerGod, DeathByDeerGodAlt, DeathByBurn = False, False, False
		SeeSimi, PrevState = (True, True) if CurE == "Simi" else (True, False)
		BattleMenu() if Challenge not in ["ow", "battle"] else OWChallengeBattleMenu() if Challenge == "ow" else BChallengeBattleMenu()