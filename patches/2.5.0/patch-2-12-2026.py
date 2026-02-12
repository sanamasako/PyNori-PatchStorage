def newGame():
	global location, LocCode, steps, kills, spares, npckills, Route, HP, MaxHP, MaxVP, Lvl, atk, defense, AttackList, ActiveQuirk, population, Tones, Sines, VocalPoints, isnewgame, MultipleSaves, CurrentSavePath, ShowHPBars
	global PlayerStatStorage, FocusedPlayer, Party, bababooey, inventory, caffeine, withdrawal, SleepCounter, yamiclear, exp, Lightheadedness, shado_guards_clear, shado_archlekia_clear, krystalclear, lairFloor, lairRoom, lairSteps, roomPuzzleSolved, bleedCounter
	global LocPop, LiveKikuPop, LiveTanpopoPop, LiveNodiumPop, LiveOceanPop, LiveArchlekiaPop, LiveTanggalPop, LiveDyarixPop, ToneStates, ShopStats, EnemyPop, satisfaction, dissatisfaction; satisfaction, dissatisfaction = 0, 0 # no more interaction bugs :3
	global bell, error, tef, CharTasks, CurE; cls(); CurE = None
	global PinorINI, RunsINI, InventorINI, EnemyPopINI
	if MultipleSaves is True: Log(f"CURRENT SAVE PATH BEFORE CALLING MULTISAVE HELPER: {CurrentSavePath}"); PinorINI, RunsINI, InventorINI, EnemyPopINI = MultisaveHelper(PredefinedSavePath=CurrentSavePath)
	else: PinorINI, RunsINI, InventorINI, EnemyPopINI = GetPinorINIPath(), GetRunsINIPath(), GetInventorINIPath(), GetEnemyPopINIPath(); Log(f"MULTIPLE SAVES DISABLED, USING ROOT DIRECTORY"); CurrentSavePath = os.getcwd()
	NotFound = []
	for f in [PinorINI, RunsINI, InventorINI, EnemyPopINI]:
		if not os.path.exists(f): NotFound.append(f)
	if NotFound != []: GameLoadError("MissingData", MissingINIs=NotFound)

	RunCheck = configparser.ConfigParser(); RunCheck.read(RunsINI)
	if "Runs" in RunCheck: RunConvert() # if Runs.ini is in pre-1.5 format (not sorted by difficulty) force the player to convert their runs or send them back to the title screen
	isnewgame = CheckIfNewGame(); Log(f"PINORI.INI AFTER RUNNING NEW GAME CHECK: {PinorINI}"); Log("Initialising configparser.")
	config = configparser.ConfigParser(); config.read(PinorINI); Log(f"Configparser initialised. (Pinori.ini: {PinorINI})")
	if cheating == "YES": Log("Oh, you're cheating. Well then."); Victory(cheating=True)

	if 'Shop States' in config and isnewgame is False:
		shopstat = config['Shop States']; Log("Loading shop states."); ShopStats = {}
		ShopStats["Kiku"] = shopstat['kiku']; Log("Loaded Shop state for Kiku Village.")
		ShopStats["Tanpopo"] = shopstat['tanpopo']; Log("Loaded Shop state for Tanpopo Town.")
		ShopStats["Nodium"] = shopstat['nodium']; Log("Loaded Shop state for Nodium Valley.")
		ShopStats["Ocean"] = shopstat['ocean']; Log("Loaded Shop state for Crystalline Oceanfront.")
		ShopStats["Archlekia"] = shopstat['archlekia']; Log("Loaded Shop state for Archlekia.")
		ShopStats["Tanggal"] = shopstat['tanggal']; Log("Loaded Shop state for Tanggal Volcano.")
		ShopStats["Dyarix"] = shopstat['dyarix']; Log("Loaded Shop state for Dyarix.")
	else:
		ShopStats = {}
		for code in ["Kiku", "Tanpopo", "Nodium", "Ocean", "Archlekia", "Tanggal", "Dyarix"]: ShopStats[code] = "allowed"

	if 'Global' in config and isnewgame is False:
		gl = config['Global']; Log("Loading global data.")
		ShowHPBars = gl.getboolean('healthbars', True); Log(f"Health Bars?: {ShowHPBars}")
		gamecorrupted = gl.getboolean('gamecorrupted', 'False')
		if gamecorrupted: FinalBattle()
		Tones = int(gl.get('Tones', 0)); Log("Loaded Tones."); Sines = int(gl.get('Sines', 0)); Log("Loaded Sines.")
		ToneStates["Kiku"] = gl.getboolean('Kiku Tone', False); Log("Loaded Tone state for Kiku Village.")
		ToneStates["Tanpopo"] = gl.getboolean('Tanpopo Tone', False); Log("Loaded Tone state for Tanpopo Town.")
		ToneStates["Nodium"] = gl.getboolean('Nodium Tone', False); Log("Loaded Tone state for Nodium Valley.")
		ToneStates["Ocean"] = gl.getboolean('Ocean Tone', False); Log("Loaded Tone state for Crystalline Oceanfront.")
		ToneStates["Archlekia"] = gl.getboolean('Archlekia Tone'); Log("Loaded Tone state for Archlekia.")
		ToneStates["Tanggal"] = gl.getboolean('Tanggal Tone', False); Log("Loaded Tone state for Tanggal Volcano.")
		ToneStates["Dyarix"] = gl.getboolean('Dyarix Tone', False); Log("Loaded Tone state for Dyarix.")
		for state in ToneStates:
			if isinstance(ToneStates[state], str): Log(f"Converted Tone state {state} to bool because it was still a string when loaded.")
			if ToneStates[state] == "False": ToneStates[state] = False
			elif ToneStates[state] == "True": ToneStates[state] = True
			else:
				if isinstance(ToneStates[state], str):
					SoundCh.SFX.play(error)
					if args.debug: print(Fore.YELLOW + f"DEBUG: {state} IS NOT BEING PROCESSED PROPERLY (VALUE {ToneStates[state]} OF TYPE {type(ToneStates[state]).__name__}, CONFIG VALUE {gl[f'{state} Tone']} OF TYPE {type(gl[f'{state} Tone']).__name__})")
					ToneStates[state] = False; Log(f"{state} IS NOT BEING PROCESSED PROPERLY (VALUE {ToneStates[state]} OF TYPE {type(ToneStates[state]).__name__}, CONFIG VALUE {gl[f'{state} Tone']} OF TYPE {type(gl[f'{state} Tone']).__name__})\nSet Tone state {state} to bool as a failsafe. Please check ini contents for errors.")
		# I don't need to load the Kill System setting because I have a separate function to check it whenever I want
	else:
		Tones, Sines = 0, 0; LocList = ["Kiku", "Tanpopo", "Nodium", "Ocean", "Archlekia", "Tanggal", "Dyarix"]
		for code in LocList: ToneStates[code] = False; Log(f"Set Tone state for location code {code} to False.")

	if 'Progress' in config and isnewgame is False:
		Log("Loading progress."); progress = config['Progress']
		location = progress.get('Location', "Kiku Village"); Log(f"Location set to {location}.")
		steps = int(progress.get('Steps Taken', 0)); Log("Loaded steps.")
		kills = int(progress.get('Kills', 0)); Log("Loaded kills.")
		npckills = int(progress.get('NPC Kills', 0)); Log("Loaded NPC kills.")
		spares = int(progress.get('Spares', 0)); Log("Loaded spares.")
		Route = str(progress.get('Route', "Traditional")); Log(f"Route set to {Route}.")
		Lair = config['Shadorako\'s Lair']; Log("Loading Shadorako's Lair exclusive data.")
		lairFloor = int(Lair.get("floor", 1)); Log("Loaded lair floor.")
		lairRoom = int(Lair.get("room", 1)); Log("Loaded lair room.")
		lairSteps = int(Lair.get("steps", 0)); Log("Loaded lair steps.")
		bleedCounter = int(Lair.get("bleed", 0)); Log("Loaded bleed counter.")
		roomPuzzleSolved = False # puzzle data doesn't get saved, deal with it
	else:
		Log(f"Progress section not found or game is new. Data for this section will be set to their starting values.")
		location, Route = "Kiku Village", "Traditional"
		steps, kills, npckills, spares = 0, 0, 0, 0; lairFloor, lairRoom, lairSteps, bleedCounter = 1, 1, 0, 0
		if not isnewgame: Log("Progress values set to their defaults. If the Progress section existed in the ini prior to loading a game and this message still appeared, please try to recreate what the ini looked like and check it for errors (if possible).")
	InDeBeninging = (location == "Kiku Village" and steps+spares == 0 and (kills+npckills) == 0)
	ngTryhard = InDeBeninging and Diff == "Tryhard"; TrueNewGame = CountRuns("all", "all")

	if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2]:
		global LocVisits, LocCode
		rqbearer = "ActiveQuirk" if ActiveQuirk == "Randomiser" else "Quirk1" if Quirk1 == "Randomiser" else "Quirk2" if Quirk2 == "Randomiser" else "ERROR"
		Log(f"Randomiser quirk is active under {rqbearer}. {"Please double-check the code!" if rqbearer == "ERROR" else ""}")
		LocVisits = {"Kiku": 0, "Tanpopo": 0, "Nodium": 0, "Ocean": 0, "Archlekia": 0, "Tanggal": 0, "Dyarix": 0}
		if location == "Kiku Village": LocCode = "Kiku"
		elif location == "Tanpopo Town": LocCode = "Tanpopo"
		elif location == "Nodium Valley": LocCode = "Nodium"
		elif location == "Crystalline Oceanfront": LocCode = "Ocean"
		elif location == "Archlekia": LocCode = "Archlekia"
		elif location == "Shadorako's Lair": LocCode = "Cathedral" # NOT an area in the normal sense, it's more of a sub-area
		elif location == "Tanggal Volcano": LocCode = "Tanggal"
		elif location == "Dyarix": LocCode = "Dyarix"
		else: LocCode = "VOID"
		LocVisits[LocCode] = 1 if LocCode not in ["VOID", "Cathedral"] else 0; Log(f"Set visits to {LocCode} to 1.")
		if LocCode == "VOID": Log("Please double-check the code!")

	if 'Party' in config:
		Log("Loading your party."); party = config['Party']; Party = ["Pinori"]; partynames = ["akuron", "sana", "yami", "millie"]; battle = config['Battle']; Log(f"Your party currently looks like this: {Party}")
		for member in partynames:
			if member in party and party[member] == "True" and member.title() not in Party:
				if member == "akuron": # I just realised I can't optimise this... [insert spongebob boowomp]
					PlayerStatStorage["Akuron"]["MaxHP"] = int(battle.get('akuronmaxhp', 70 if Diff != "Tryhard" else 45)) if not ngTryhard else 45
					PlayerStatStorage["Akuron"]["HP"] = int(battle.get('akuronhp', 70 if Diff != "Tryhard" else 45)) if not ngTryhard else 45
					PlayerStatStorage["Akuron"]["Lvl"] = int(battle.get('akuronlevel', 5 if Diff != "Tryhard" else 2)) if not ngTryhard else 2
					PlayerStatStorage["Akuron"]["atk"] = int(battle.get('akuronatk', 15 if Diff != "Tryhard" else 6)) if not ngTryhard else 6
					PlayerStatStorage["Akuron"]["defense"] = int(battle.get('akurondef', 10 if Diff != "Tryhard" else 5)) if not ngTryhard else 5
					PlayerStatStorage["Akuron"]["VocalPoints"] = int(battle.get('akuron vp', 120 if Diff != "Tryhard" else 60)) if not ngTryhard and not TrueNewGame else 60
					PlayerStatStorage["Akuron"]["MaxVP"] = int(battle.get('akuron max vp', 120 if Diff != "Tryhard" else 60)) if not ngTryhard and not TrueNewGame else 60
					PlayerStatStorage["Akuron"]["Caffeine"] = int(battle.get('akuroncaffeine', 0))
					PlayerStatStorage["Akuron"]["Withdrawal"] = battle.getboolean('akuronwithdrawal', False)
					PlayerStatStorage["Akuron"]["Sleep"] = int(battle.get('akuronsleep', 0))
					PlayerStatStorage["Akuron"]["EXP"] = int(battle.get('akuronexp', 350 if Diff != "Tryhard" else 50)) if not ngTryhard else 50
					PlayerStatStorage["Akuron"]["Lightheadedness"] = int(battle.get('akuron lightheadedness', 0))
					Log("Akuron loaded.")
				elif member == "sana":
					PlayerStatStorage["Sana"]["MaxHP"] = int(battle.get('sanamaxhp', 100)) if not ngTryhard else 50
					PlayerStatStorage["Sana"]["HP"] = int(battle.get('sanahp', 100)) if not ngTryhard else 50
					PlayerStatStorage["Sana"]["Lvl"] = int(battle.get('sanalevel', 7)) if not ngTryhard else 3
					PlayerStatStorage["Sana"]["atk"] = int(battle.get('sanaatk', 5)) if not ngTryhard else 2
					PlayerStatStorage["Sana"]["defense"] = int(battle.get('sanadef', 9)) if not ngTryhard else 4
					PlayerStatStorage["Sana"]["VocalPoints"] = int(battle.get('sana vp', 150)) if not ngTryhard and not TrueNewGame else 75
					PlayerStatStorage["Sana"]["MaxVP"] = int(battle.get('sana max vp', 150)) if not ngTryhard and not TrueNewGame else 75
					PlayerStatStorage["Sana"]["Caffeine"] = int(battle.get('sanacaffeine', 0))
					PlayerStatStorage["Sana"]["Withdrawal"] = battle.getboolean('sanawithdrawal', False)
					PlayerStatStorage["Sana"]["Sleep"] = int(battle.get('sanasleep',0))
					PlayerStatStorage["Sana"]["EXP"] = int(battle.get('sanaexp', 700)) if not ngTryhard else 120
					PlayerStatStorage["Sana"]["Lightheadedness"] = int(battle.get('sana lightheadedness', 0))
					Log("Sana loaded.")
				elif member == "yami":
					PlayerStatStorage["Yami"]["MaxHP"] = int(battle.get('yamimaxhp', 120)) if not ngTryhard else 60
					PlayerStatStorage["Yami"]["HP"] = int(battle.get('yamihp', 120)) if not ngTryhard else 60
					PlayerStatStorage["Yami"]["Lvl"] = int(battle.get('yamilevel', 11)) if not ngTryhard else 5
					PlayerStatStorage["Yami"]["atk"] = int(battle.get('yamiatk', 25)) if not ngTryhard else 12
					PlayerStatStorage["Yami"]["defense"] = int(battle.get('yamidef', 5)) if not ngTryhard else 3
					PlayerStatStorage["Yami"]["VocalPoints"] = int(battle.get('yami vp', 60)) if not ngTryhard and not TrueNewGame else 30
					PlayerStatStorage["Yami"]["MaxVP"] = int(battle.get('yami max vp', 60)) if not ngTryhard and not TrueNewGame else 30
					PlayerStatStorage["Yami"]["Caffeine"] = int(battle.get('yamicaffeine', 0))
					PlayerStatStorage["Yami"]["Withdrawal"] = battle.getboolean('yamiwithdrawal', False)
					PlayerStatStorage["Yami"]["Sleep"] = int(battle.get('yamisleep', 0))
					PlayerStatStorage["Yami"]["EXP"] = int(battle.get('yamiexp', 2000)) if not ngTryhard else 350
					PlayerStatStorage["Yami"]["Lightheadedness"] = int(battle.get('yami lightheadedness', 0))
					Log("Yami loaded.")
				elif member == "millie": # this doesn't matter I'm just loading it to load it lol
					PlayerStatStorage["Millie"]["MaxHP"] = 0
					PlayerStatStorage["Millie"]["HP"] = 0
					PlayerStatStorage["Millie"]["Lvl"] = 0
					PlayerStatStorage["Millie"]["atk"] = -1
					PlayerStatStorage["Millie"]["defense"] = 999999999999999999
					PlayerStatStorage["Millie"]["VocalPoints"] = 0
					PlayerStatStorage["Millie"]["MaxVP"] = 0
					PlayerStatStorage["Millie"]["Caffeine"] = -100
					PlayerStatStorage["Millie"]["Withdrawal"] = False
					PlayerStatStorage["Millie"]["Sleep"] = 999999999999999999
					PlayerStatStorage["Millie"]["EXP"] = 0
					PlayerStatStorage["Millie"]["Lightheadedness"] = 999999999999999999
					Log("Millie loaded.")
				if member.title() not in Party: Party.append(member.title()); Log(f"{member.title()} added to your party."); Log(f"Your party now looks like this: {Party}")
			# old functionality

			#elif member in party and member not in partynames and party[member] == "True" and member != "pinori" and member not in Party: # the system will think Pinori is an imaginary friend because of the way I set it up lol
			#	Log(f"Imaginary friend detected! Loading stats for {member.title()}.")
			#	PlayerStatStorage[member] = {}
			#	PlayerStatStorage[member]["MaxHP"] = 0
			#	PlayerStatStorage[member]["HP"] = 0
			#	PlayerStatStorage[member]["Lvl"] = 0
			#	PlayerStatStorage[member]["atk"] = -1
			#	PlayerStatStorage[member]["defense"] = 999999999999999999
			#	PlayerStatStorage[member]["VocalPoints"] = 0
			#	PlayerStatStorage[member]["Caffeine"] = -100
			#	PlayerStatStorage[member]["Withdrawal"] = False
			#	PlayerStatStorage[member]["Sleep"] = 999999999999999999
			#	Log(f"{member.title()} loaded.")
			#	if member not in Party:
			#		Party.append(member.title())
			#		Log(f"{member.title()} added to your party.")
			#		Log(f"Your party now looks like this: {Party}")
			if member in Party and party[member] == "False": Party.remove(member.title()); Log(f"{member.title()} was removed from your party because they weren't supposed to be there."); Log(f"Your party now looks like this: {Party}")
	else: Log("Party section does not exist."); GameLoadError("GenericHalt")
	Party = list(set(Party)); Log("If there were any duplicates in the Party (which there shouldn't have been), there aren't anymore."); CharTasks = {}
	try: assert Party[0] == "Pinori", "THE PARTY LOADED OUT OF ORDER AGAIN I'M SOBBING"
	except AssertionError as e: Log(f"{e}"); Party.remove("Pinori"); Party.insert(0, "Pinori"); Log("Pinori should now be at ID 0. AS INTENDED. SOBBING EMOJI. I don't even know why this bug is inconsistent tbh but it pmo")
	for member in Party: CharTasks[member] = CharacterTasks(member, CanCommand=(True if member not in ["Pinori", "Millie"] else False))

	if "Character Tasks" in config:
		taskstuff = config["Character Tasks"]
		for character in ["Akuron", "Sana", "Yami"]:
			if character not in Party: continue
			CharTasks[character].task = taskstuff[f"{character.lower()} task"] or None # holds the task (duh)
			CharTasks[character].state = taskstuff[f"{character.lower()} state"] or None # tells the game whether they're present or not
			CharTasks[character].TaskSteps = int(taskstuff[f"{character.lower()} distance"]) or 0 # if not present, tells the game how far away the character is in steps
			CharTasks[character].retrieve = taskstuff[f"{character.lower()} purchase"] or None # for the item task, holds which item the character should buy
			CharTasks[character].WaitLoc = taskstuff[f"{character.lower()} meetup"] or None # for the "promote" or "demote" task, holds the location to wait in
	else:
		Log("Character Tasks section not found. Is your copy of Pinori.ini from 2.2.0 or older?")
		for character in ["Akuron", "Sana", "Yami"]:
			if character not in Party: continue
			CharTasks[character].task = None
			CharTasks[character].state = "present"
			CharTasks[character].TaskSteps = 0
			CharTasks[character].retrieve = None
			CharTasks[character].WaitLoc = None

	PlayerCheated = False
	if 'Battle' in config and isnewgame is False:
		Log("Loading battle statistics."); battle = config['Battle']; FocusedPlayer = battle.get('focused player', "Pinori")
		if FocusedPlayer == "Millie":
			Log("Focused player is Millie. Berating player for cheating."); SoundCh.SFX.play(error)
			print("Hi. I noticed you manually changed the Focused Player to Millie."); pause()
			print("Don't do that. Ever again. Got it?"); pause()
			print("It doesn't even benefit you. The game will just force you to switch characters once you start a battle."); pause()
			CanonMillie = {"MaxHP": "0", "HP": "0", "Lvl": "0", "atk": "-1", "defense": "999999999999999999", "VocalPoints": "0", "Caffeine": "-100", "Withdrawal": "False", "EXP": "0"}
			SavedMillie = {"MaxHP": battle["milliemaxhp"], "HP": battle["milliehp"], "Lvl": battle["millielevel"], "atk": battle["millieatk"], "defense": battle["milliedef"], "VocalPoints": battle["millie vp"], "Caffeine": battle["milliecaffeine"], "Withdrawal": battle["milliewithdrawal"], "EXP": battle["millieexp"]}
			print("Or at least I'd assume so, given you tried to change her stats too. Nice try, bucko." if SavedMillie != CanonMillie else "So stop wasting your time. Just play by my rules. It's not hard."); pause(); FocusedPlayer = "Pinori"
			print("I've set the Focused Player back to Pinori. I'd better not catch you doing this again."); pause()
			print(f"Have a good day, {getpass.getuser()}."); pause(); PlayerCheated = True
		if FocusedPlayer == "Pinori":
			Log("Focused player is Pinori. Setting her stats using the default variables.")
			HP = 5 if ngTryhard else int(battle.get('hp', 10))
			MaxHP = 5 if ngTryhard else int(battle.get('maxhp', 10)); Log(f"Pinori's HP: {HP}/{MaxHP}")
			Lvl = int(battle.get('level', 1)); Log(f"Pinori is level {Lvl}.")
			atk = 1 if ngTryhard else int(battle.get('atk', 2)); Log(f"Pinori's attack is {atk}.")
			defense = 3 if ngTryhard else int(battle.get('def', 6)); Log(f"Pinori's defense is {defense}.")
			VocalPoints = 70 if ngTryhard else int(battle.get('vp', 140))
			MaxVP = 70 if ngTryhard and TrueNewGame else int(battle.get('max vp', 140)); Log(f"Pinori's VP: {VocalPoints}/{MaxVP}")
			caffeine = int(battle.get('caffeine', 0)); Log(f"Pinori's caffeine intake: {caffeine}")
			SleepCounter = int(battle.get('sleep', 0)); Log(f"Pinori's sleep counter: {SleepCounter}")
			withdrawal = battle.getboolean('withdrawal', False); Log(f"Pinori's Caffeine Withdrawal state: {withdrawal}")
			exp = int(battle.get('exp', 0)); Log(f"Pinori has {exp} EXP." if KillSystemSwitch(task="check") == "EXP" else "Player is using 8K Kill System. EXP is currently irrelevant.")
			Lightheadedness = int(battle.get('lightheadedness', 0)); Log(f"Pinori's Lightheadedness: {Lightheadedness}")
			PlayerStatStorage["Pinori"]["HP"] = HP
			PlayerStatStorage["Pinori"]["MaxHP"] = MaxHP
			PlayerStatStorage["Pinori"]["Lvl"] = Lvl
			PlayerStatStorage["Pinori"]["atk"] = atk
			PlayerStatStorage["Pinori"]["defense"] = defense
			PlayerStatStorage["Pinori"]["VocalPoints"] = VocalPoints
			PlayerStatStorage["Pinori"]["MaxVP"] = MaxVP; Log(f"MAX VOCAL POINTS IS {MaxVP}!!!")
			PlayerStatStorage["Pinori"]["Caffeine"] = caffeine
			PlayerStatStorage["Pinori"]["Withdrawal"] = withdrawal
			PlayerStatStorage["Pinori"]["Sleep"] = SleepCounter
			PlayerStatStorage["Pinori"]["EXP"] = exp
			PlayerStatStorage["Pinori"]["Lightheadedness"] = Lightheadedness; Log("Saved Pinori's stats to Player Stat Storage.")
		else:
			Log("Focused player is not Pinori. Setting her stats using the Player Stat Storage.")
			PlayerStatStorage["Pinori"]["HP"] = 5 if ngTryhard else int(battle.get("HP", 10))
			PlayerStatStorage["Pinori"]["MaxHP"] = 5 if ngTryhard else int(battle.get("maxhp", 10)); Log(f"Pinori's HP: {PlayerStatStorage["Pinori"]["HP"]}/{PlayerStatStorage["Pinori"]["MaxHP"]}")
			PlayerStatStorage["Pinori"]["Lvl"] = int(battle.get("level", 1)); Log(f"Pinori is level {PlayerStatStorage["Pinori"]["Lvl"]}.")
			PlayerStatStorage["Pinori"]["atk"] = 1 if ngTryhard else int(battle.get("atk", 2)); Log(f"Pinori's attack is {PlayerStatStorage["Pinori"]["atk"]}.")
			PlayerStatStorage["Pinori"]["defense"] = 3 if ngTryhard else int(battle.get("def", 6)); Log(f"Pinori's defense is {PlayerStatStorage["Pinori"]["defense"]}.")
			PlayerStatStorage["Pinori"]["VocalPoints"] = 70 if ngTryhard else int(battle.get("vp", 140))
			PlayerStatStorage["Pinori"]["MaxVP"] = 70 if ngTryhard and TrueNewGame else int(battle.get("max vp", 140)); Log(f"Pinori's VP: {PlayerStatStorage["Pinori"]["VocalPoints"]}/{PlayerStatStorage["Pinori"]["MaxVP"]}")
			PlayerStatStorage["Pinori"]["Caffeine"] = int(battle.get("caffeine", 0)); Log(f"Pinori's caffeine intake: {PlayerStatStorage["Pinori"]["Caffeine"]}")
			PlayerStatStorage["Pinori"]["Sleep"] = int(battle.get("sleep", 0)); Log(f"Pinori's sleep counter: {PlayerStatStorage["Pinori"]["Sleep"]}")
			PlayerStatStorage["Pinori"]["Withdrawal"] = battle.getboolean("withdrawal", False); Log(f"Pinori's Caffeine Withdrawal state: {PlayerStatStorage["Pinori"]["Withdrawal"]}")
			PlayerStatStorage["Pinori"]["EXP"] = int(battle.get("exp", 0)); Log(f"Pinori has {PlayerStatStorage["Pinori"]["EXP"]} EXP." if KillSystemSwitch(task="check") == "EXP" else "Player is using 8K Kill System. EXP is currently irrelevant.")
			PlayerStatStorage["Pinori"]["Lightheadedness"] = int(battle.get("lightheadedness", 0)); Log(f"Pinori's Lightheadedness counter: {PlayerStatStorage["Pinori"]["Lightheadedness"]}")
			Log("Setting main stat variables to the focused player's stats.")
			HP = PlayerStatStorage[FocusedPlayer]["HP"]
			MaxHP = PlayerStatStorage[FocusedPlayer]["MaxHP"]; Log(f"{FocusedPlayer}'s HP: {PlayerStatStorage[FocusedPlayer]["HP"]}/{PlayerStatStorage[FocusedPlayer]["MaxHP"]}")
			Lvl = PlayerStatStorage[FocusedPlayer]["Lvl"]; Log(f"{FocusedPlayer} is level {PlayerStatStorage[FocusedPlayer]["Lvl"]}.")
			atk = PlayerStatStorage[FocusedPlayer]["atk"]; Log(f"{FocusedPlayer}'s attack is {PlayerStatStorage[FocusedPlayer]["atk"]}.")
			defense = PlayerStatStorage[FocusedPlayer]["defense"]; Log(f"{FocusedPlayer}'s defense is {PlayerStatStorage[FocusedPlayer]["defense"]}")
			VocalPoints = PlayerStatStorage[FocusedPlayer]["VocalPoints"]
			MaxVP = PlayerStatStorage[FocusedPlayer]["MaxVP"]; Log(f"{FocusedPlayer}'s VP: {PlayerStatStorage[FocusedPlayer]["VocalPoints"]}/{PlayerStatStorage[FocusedPlayer]["MaxVP"]}")
			caffeine = PlayerStatStorage[FocusedPlayer]["Caffeine"]; Log(f"{FocusedPlayer}'s caffeine intake: {PlayerStatStorage[FocusedPlayer]["Caffeine"]}")
			SleepCounter = PlayerStatStorage[FocusedPlayer]["Sleep"]; Log(f"{FocusedPlayer}'s sleep counter{" (WHAT)" if FocusedPlayer == "Sana" else ""}: {PlayerStatStorage[FocusedPlayer]["Sleep"]}")
			withdrawal = PlayerStatStorage[FocusedPlayer]["Withdrawal"]; Log(f"{FocusedPlayer}'s Caffeine Withdrawal state: {PlayerStatStorage[FocusedPlayer]["Withdrawal"]}")
			exp = PlayerStatStorage[FocusedPlayer]["EXP"]; Log(f"{FocusedPlayer} has {PlayerStatStorage[FocusedPlayer]["EXP"]} EXP." if KillSystemSwitch(task="check") == "EXP" else "Player is using 8K Kill System. EXP is currently irrelevant.")
			Lightheadedness = PlayerStatStorage[FocusedPlayer]["Lightheadedness"]; Log(f"{FocusedPlayer}'s Lightheadedness counter: {Lightheadedness}")

		if FocusedPlayer not in Party: SoundCh.SFX.play(bell); print(Fore.RED + "Focused player is not in your party. You are now playing as Pinori."); pause(); SwitchMember(SilentSwitch="Pinori", Forced=True, SwitchingBeforeBoss=True) # bell instead of error because this can only happen if you're cheating, unless I REALLY messed something up in the code.
	else:
		if Diff != "Tryhard": MaxHP, HP = 10, 10; Lvl, atk, defense = 1, 2, 6; VocalPoints, MaxVP = 140, 140
		else: MaxHP, HP = 5, 5; Lvl, atk, defense = 1, 1, 3; VocalPoints, MaxVP = 70, 70
		FocusedPlayer = "Pinori"; caffeine, exp, Lightheadedness = 0, 0, 0; withdrawal = False
		Log("Statistics set to their defaults.")

	if 'Pinori Attacks' in config and isnewgame is False:
		Log("Loading attacks."); AttackList = {}
		for attack, cost in config['Pinori Attacks'].items(): AttackList[attack.title()] = int(cost); Log(f"{attack.title()} loaded.")
	else: Log("Attacks not found. They have been manually set to their intended defaults."); AttackList = {"Treble Punch": 10, "Kick": 0}
	if os.path.exists(InventorINI):
		Log("Inventory ini file exists. Loading inventories.")
		config.read(InventorINI)
		Log(f"Current party: {Party}")
		for member in Party:
			Log(f"Next member: {member} (if this is Yami they won't be loaded)")
			if member in config and member != "Yami" and member in ["Pinori", "Millie", "Akuron", "Sana"]:
				invconf = config[member]
				for slot, item in invconf.items(): inventory[member][slot] = item if item != "None" else "None" # do I need to do this? no. am I doing it anyway? yes. shut up. I'm tired of the inventory bugging out
				Log(f"{member} loaded.")
			else: Log("Invalid character (or character is Yami)! Skipping.")
	Log("Loading EXP Share percentage."); LoadEXPShare()

	if (DualQMode is False and ActiveQuirk == "God Mode") or (DualQMode is True and (Quirk1 == "God Mode" or Quirk2 == "God Mode")):
		MaxHP = 9999999999999999999999999999999999; HP = MaxHP
		atk, defense, Lvl = 999, 999, 999
		Log("God mode activated for Pinori.")
	#elif (DualQMode is False and ActiveQuirk == "Glass Soul") or (DualQMode is True and (Quirk1 == "Glass Soul" or Quirk2 == "Glass Soul")): MaxHP = 1; HP = MaxHP; Lvl, atk, defense = 1, 1, 1
	if location == "Kiku Village": LocCode = "Kiku"
	elif location == "Tanpopo Town": LocCode = "Tanpopo"
	elif location == "Nodium Valley": LocCode = "Nodium"
	elif location == "Crystalline Oceanfront": LocCode = "Ocean"
	elif location == "Archlekia": LocCode = location
	elif location == "Tanggal Volcano": LocCode = "Tanggal"
	elif location == "Dyarix": LocCode = "Dyarix"
	else: LocCode = "VOID"

	Pop = configparser.ConfigParser(); Pop.read(PinorINI)
	if "Progress" in Pop:
		Log("Continuing to load your progress.")
		Loc = Pop["Progress"]
		yamiclear = Loc.getboolean("yami defeated", False); Log("Loaded Yami defeat state.")
		krystalclear = Loc.getboolean("krystal defeated", False); Log("Loaded Krystal O'Shin defeat state.")
		shado_guards_clear = Loc.getboolean("shado guards defeated", False); Log("Loaded Shadorako Guards defeat state.")
		shado_archlekia_clear = Loc.getboolean("shado archlekia defeated", False); Log("Loaded Shadorako defeat state (Archlekia).")
		population = int(Loc.get(f"{location} population", 0)); Log("Loaded population for current area.")
		LiveKikuPop = int(Loc.get("kiku village population", 0)); Log("Loaded Kiku Village population.")
		LiveTanpopoPop = int(Loc.get("tanpopo town population", 0)); Log("Loaded Tanpopo Town population.")
		LiveNodiumPop = int(Loc.get("nodium valley population", 0)); Log("Loaded Nodium Valley population.")
		LiveOceanPop = int(Loc.get("crystalline oceanfront population", 0)); Log("Loaded Crystalline Oceanfront population.")
		LiveArchlekiaPop = int(Loc.get("archlekia population", 0)); Log("Loaded Archlekia population.")
		LiveTanggalPop = int(Loc.get("tanggal volcano population", 0)); Log("Loaded Tanggal Volcano population.")
		LiveDyarixPop = int(Loc.get("dyarix population", 0)); Log("Loaded Dyarix population.")
		LocPop["LiveKikuPop"] = LiveKikuPop
		LocPop["LiveTanpopoPop"] = LiveTanpopoPop
		LocPop["LiveNodiumPop"] = LiveNodiumPop
		LocPop["LiveOceanPop"] = LiveOceanPop
		LocPop["LiveArchlekiaPop"] = LiveArchlekiaPop
		LocPop["LiveTanggalPop"] = LiveTanggalPop
		LocPop["LiveDyarixPop"] = LiveDyarixPop
		Log("Transferred populations into a dictionary.")
	else: Log("An error occurred!"); GameLoadError("GenericHalt")

	if "Yami" in Party and yamiclear is True: Date = datetime.datetime.now(); year = Date.year; Party.remove("Yami"); print(f"You cheaters are so funny. Seriously? How can Yami be in your party if you killed her earlier?\nIf you're gonna be a lame cheater in the big {max(2021, year)}, at least be good at it, for the love of God.\nOr, you know, alternatively, stop cheating. The world would be a better place if you did that, you know."); pause(); PlayerCheated = True

	if os.path.exists(EnemyPopINI) and os.path.exists(GetCustomFilePath("Enemy.json")):
		Log(f"Loading enemy populations from {EnemyPopINI}.")
		with open(GetCustomFilePath("Enemy.json"), 'r', encoding='utf-8') as enemypop: Enemies = json.load(enemypop)
		EnemyNames = Enemies.keys(); EnemyPopPart2 = configparser.ConfigParser(); EnemyPopPart2.read(EnemyPopINI); EnemyPop = {}
		for name in EnemyNames:
			if name.lower() in ["skelepound", "vampiper", "mortis", "reminiscer", "hellhoward", "skid", "pump", "kin", "zomblaire", "frances"]: continue
			EnemyPop[name.title() if name not in ["Hot Tin Can't", "Tin Can't", "Pam the Clam"] else "Hot Tin Can't" if name.title() == "Hot Tin Can'T" else "Tin Can't" if name.title() == "Tin Can'T" else "Pam the Clam" if name.title() == "Pam The Clam" else name.title()] = int(EnemyPopPart2["Enemy"][name.title()])
			Log(f"{name.title() if name not in ["Hot Tin Can't", "Tin Can't", "Pam the Clam"] else "Hot Tin Can't" if name.title() == "Hot Tin Can'T" else "Tin Can't" if name.title() == "Tin Can'T" else "Pam the Clam" if name.title() == "Pam The Clam" else name.title()} has a population of {EnemyPopPart2["Enemy"][name.title()]}. {f"{name.title()} is extinct." if [name.title() if name not in ["Hot Tin Can't", "Tin Can't", "Pam the Clam"] else "Hot Tin Can't" if name.title() == "Hot Tin Can'T" else "Tin Can't" if name.title() == "Tin Can'T" else "Pam the Clam" if name.title() == "Pam The Clam" else name.title()] == 0 else ""}")

	if Route == "Traditional" and (kills + npckills) >= 12 and (LiveKikuPop + LiveTanpopoPop + spares) == 0 and location != "Tanpopo Town":
		if args.debug: print(Fore.YELLOW + "DEBUG: Route was set to Traditional when it should be set to Omnicide. My bad.")
		Route = "Omnicide"; Log("Route was incorrectly configured. You're on Omnicide.")

	if args.debug: print(Fore.YELLOW + f"""DEBUG:
You have {Tones} Tones!
Tone States:
Kiku: {ToneStates["Kiku"]}
Tanpopo: {ToneStates["Tanpopo"]}
Nodium: {ToneStates["Nodium"]}
Ocean: {ToneStates["Ocean"]}
Archlekia: {ToneStates["Archlekia"]}
Tanggal: {ToneStates["Tanggal"]}
Dyarix: {ToneStates["Dyarix"]}
You have {Sines} Sines!
You have {VocalPoints} Vocal Points!
You've taken {steps} steps in {location}!
You've killed {kills} monsters and {npckills} NPCs!
You've spared {spares} times!
You are on the {Route} route!
HP: {HP}/{MaxHP}
You're level {Lvl} with an attack of {atk} and a defense of {defense}!
The populations of each location (named by code) are as follows:
Kiku: {LiveKikuPop}
Tanpopo: {LiveTanpopoPop}
Nodium: {LiveNodiumPop}
Ocean: {LiveOceanPop}
Archlekia: {LiveArchlekiaPop}
Tanggal: {LiveTanggalPop}
Dyarix: {LiveDyarixPop}
Your party is {len(Party)} member(s) big!"""); pause()
	MaxVP = PlayerStatStorage[FocusedPlayer]["MaxVP"] if not ngTryhard or not TrueNewGame else int(PlayerStatStorage[FocusedPlayer]["MaxVP"]/2); Log(f"MAX VOCAL POINTS IS {MaxVP}!!!")
	if PlayerCheated: Save(0, Silent=True); print("Oh, and by the way, I've autosaved my changes, so you won't see this message again unless you go out of your way to do exactly what I just told you not to.\nBut you won't, right? Because you're a good player. At least I hope so. Anyway, I'll leave you be now, to play my game as intended. Cough cough."); pause()
	if bababooey: Log("Starting \"game\"."); fakeGame()
	else: Log("Starting game."); gameThing()