def ProgressDestroyer(): # for the Demotion item
	global location, steps, LocCode, ToneCollectedYet, debug, DualQMode, ActiveQuirk, Quirk1, Quirk2, LocVisits, Advance, tef; ToneCollectedYet = False; Log("Backtracking time!")
	try: DebugPrint(f"Location: {location}, Steps Taken: {steps}"); DebugPrint(f"DEBUG: ActiveQuirk: {ActiveQuirk}" if not DualQMode else f"DEBUG: Quirk1: {Quirk1}, Quirk2: {Quirk2}")
	except ValueError:
		SoundCh.SFX.play(tef)
		if args.debug: debugFail()
	if "Randomiser" in [ActiveQuirk, Quirk1, Quirk2]: ProgressMaker(Demotion=True) # the randomisation is no different so just do the normal thing
	else:
		if location == "Kiku Village": print("... nothing changed."); pause()
		elif location == "Tanpopo Town": location, LocCode = "Kiku Village", "Kiku"
		elif location == "Nodium Valley": location, LocCode = "Tanpopo Town", "Tanpopo"
		elif location == "Crystalline Oceanfront": location, LocCode = "Nodium Valley", "Nodium"
		elif location == "Archlekia": location, LocCode = "Crystalline Oceanfront", "Ocean"
		elif location == "Tanggal Volcano": location, LocCode = "Archlekia", "Archlekia"
		elif location == "Dyarix": location, LocCode = "Tanggal Volcano", "Tanggal"
	Advance = False; steps = 0; Log("Progress has NOT been made! Hell yeah!"); gameThing()