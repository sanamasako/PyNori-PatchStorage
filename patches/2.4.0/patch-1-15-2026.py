def FakeDiffChanger():
	global PinorINI, RunsINI, InventorINI, EnemyPopINI
	global FakeDiff, sel, important; routegetter = configparser.ConfigParser(); routegetter.read(PinorINI)
	RouteThingity = routegetter["Progress"]; Route = RouteThingity["route"]; ShadoThingityThing = routegetter["Shadorako"]
	if int(ShadoThingityThing['total deaths']) > 0 and ShadoThingityThing['hard'] == "True": typewriter_shado("Too late :)", tone="a"); pause(); return
	elif int(ShadoThingityThing['total deaths']) > 0 and ShadoThingityThing['hard'] != "True": typewriter_shado("You do realise we're already mid-battle, right? Your decision was finalised the moment you started the battle."); pause(); return

	while True:
		newfakediff = input("Choose a new difficulty level. [Hard/Harder/Hell/Impossible]: ").strip().title()
		
		if newfakediff in ["Hard", "Harder", "Hell", "Impossible"]:
			SoundCh.SFX.play(sel)
			
			if newfakediff == "Impossible" and Route == "Omnicide" and FakeDiff != "Impossible":
				i = 0
				while i != 7:
					SoundCh.SFX.play(important); areyousureyouwanttodietodeath = input("Are you sure? [Y/N] ").lower()
					if areyousureyouwanttodietodeath in ["y", "n", "yes", "no", "yeah", "nah", "nope", "sure"]:
						if areyousureyouwanttodietodeath in ["y", "yes", "yeah", "sure"]: i += 1; continue
						elif areyousureyouwanttodietodeath in ["n", "no", "nah", "nope"]:
							print("Thought not."); pause(); routegetter.set("Shadorako", "hard", "False")
							with open(PinorINI, "w") as GrimReaper: routegetter.write(GrimReaper)
							return
				print("Your funeral."); pause()
				routegetter.set("Shadorako", "hard", "True")
				with open(PinorINI, "w") as GrimReaper: routegetter.write(GrimReaper)
			elif newfakediff == "Impossible" and Route != "Omnicide": print("Off limits."); newfakediff = None; continue
			if newfakediff == FakeDiff: print(f"The difficulty remains just as hard ({FakeDiff}). Press any key to return to the suffering personalisation menu."); pause(); return
			else:
				routegetter.set("Shadorako", "hard", "False")
				with open(PinorINI, "w") as GrimReaper: routegetter.write(GrimReaper)
				FakeDiff = newfakediff; print(f"Difficulty updated to: {newfakediff}. Press any key to return to the suffering personalisation menu.") if FakeDiff != "Impossible" else print("Impossible mode activated. Press any key to confirm that you are ready to die."); pause(); return
		else:
			print("Invalid input. Please choose from Hard, Harder, Hell, or Impossible.")
			if Route != "Omnicide": pause(); typewriter_shado("Uh. Forget I said anything about Impossible.", tone="n"); pause()