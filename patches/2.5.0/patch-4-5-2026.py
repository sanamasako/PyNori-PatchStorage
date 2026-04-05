def Interaction(enemy, interaction):
	global VocalPoints, atk, Lvl, HP, MaxHP, CurE, EnemD, EnemyHP, EnemyMaxHP, defense, AttackList, Diff, pronoun1, pronoun2, pronounPossessive, FocusedPlayer, PlayerStatStorage, Party, Route, ActiveQuirk, Quirk1, Quirk2; DivideOrNah = 2 if Route == "Omnicide" else 1
	global bababooey, satisfaction, Satisfied, ClefHappy, ATKperform_enemy, tef, location, dissatisfaction, Dissatisfied, DeathByDeerGod, DeathByDeerGodAlt, EnemyAsleep, inventory, SpookyTime; DeathByDeerGodAlt = False; BAD = False
	name = "You" if FocusedPlayer == "Pinori" else FocusedPlayer; AtkAmount = 1 if not "Double or Nothing" in [ActiveQuirk, Quirk1, Quirk2] else 2
	DisSatisMath = None; ShadoGuards = CurE == "Shadorako's Guards"; Krystal = CurE == "Krystal"
	EnemyHP = globals()["KrystalHP"] if Krystal else globals()["ShadoGuard1HP"] if ShadoGuards else EnemyHP
	EnemyMaxHP = globals()["KrystalMaxHP"] if Krystal else globals()["ShadoGuard1MaxHP"] if ShadoGuards else EnemyMaxHP
	# so I don't have to retype "Pessimistick" or "Hot Pessimistick" whether they got the regular or hot variant
	if enemy in ["Pessimistick", "Hot Pessimistick"] and interaction == "1": # Pessimistick Cheer Up
		print(f"{name} told {CurE} that it's valuable and to hang in there."); time.sleep(4)
		if EnemyHP > EnemyMaxHP/7: SatisMath = random.randint(1,20); print(f"{CurE} appreciated that. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		else: SatisMath = 0; print(f"{CurE} is confused. If {name.lower() if name == "You" else name} really thought so... why are {name.lower() if name == "You" else "they"} fighting it?")
	elif enemy in ["Pessimistick", "Hot Pessimistick"] and interaction == "2": # Pessimistick Reassure
		print(f"{name} told {CurE} that everything is going to be okay."); time.sleep(4)
		if EnemyHP > EnemyMaxHP/7: SatisMath = random.randint(2,10); print(f"{CurE} appreciated that. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		else: SatisMath = 0; print(f"{CurE} assumes you're making fun of it and ignores your comment.")
	elif enemy in ["Pessimistick", "Hot Pessimistick"] and interaction == "3": # Pessimistick Put Down
		print(f"{name} told {CurE} that it's as invaluable as it thinks it is."); time.sleep(4); BAD = True
		SatisMath = random.randint(-20,-10); DisSatisMath = random.randint(1,20)
		if satisfaction > 0: print(f"{CurE} feels lied to. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
		else: print(f"{CurE}, despite already knowing this, feels hurt. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy in ["Pessimistick", "Hot Pessimistick"] and interaction == "4": # Pessimistick It's Over
		print(f"{name} told {CurE} that there's no purpose it can serve in this world."); time.sleep(4); BAD = True
		SatisMath = random.randint(-25,-5); DisSatisMath = random.randint(15,30)
		if satisfaction > 0: print(f"{CurE} feels lied to. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
		else: print(f"{CurE} nods sadly, struggling to give eye contact. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Megan Bite" and interaction == "1": # Megan Bite Floppy Disks
		print(f"{name} informed Megan Bite that floppy disks exist and that they only use 1.44 of her."); time.sleep(4)
		SatisMath = random.randint(10,20); print(f"Megan Bite smiles. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Megan Bite" and interaction == "2": # Megan Bite Kilobytes
		print(f"{name} reminded Megan Bite that there are units of computer storage thousands to millions of times smaller than her."); time.sleep(4)
		SatisMath = random.randint(25,30); print(f"Megan Bite remembers Keero Bite and Bayet, thinking about how much greater she is. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Megan Bite" and interaction == "3": # Megan Bite Opportunities
		print(f"{name} told Megan Bite that back in the day, you could do a lot with her. {"You" if FocusedPlayer == "Pinori" else "They"} added that that's still the case."); time.sleep(4)
		SatisMath = random.randint(10,15); print(f"Megan Bite looks excited. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Megan Bite" and interaction == "4": # Megan Bite You're Small
		print(f"{name} reminded Megan Bite that there are units of computer storage thousands to millions of times larger than her."); time.sleep(4); BAD = True
		SatisMath = random.randint(-30,-15); DisSatisMath = random.randint(15,30)
		print(f"Megan Bite remembers Yatta Bite and Zetta Bite, thinking about how much greater they are. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Megan Bite" and interaction == "5": # Megan Bite Optical Media is the future
		print(f"{name} told Megan Bite that a special type of disk is being developed that will be able to store hundreds of thousands of petabytes of data."); time.sleep(4); BAD = True
		SatisMath = random.randint(-30,-15); DisSatisMath = random.randint(30,45)
		print(f"Megan Bite feels obsolete. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	# same reason as the Pessimistick situation
	elif enemy in ["Tin Can't", "Hot Tin Can't"] and interaction == "1": # Tin Can't Storage
		print(f"{name} suggested that since {"Hot" if "Hot" in CurE else  ""}Tin Can't hold anything inside it, maybe it should open a storage business so it could help others hold things instead."); time.sleep(3)
		SatisMath = random.randint(10,15); print(f"{CurE} deny that the idea was pretty good. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy in ["Tin Can't", "Hot Tin Can't"] and interaction == "2": # Tin Can't Relate
		print(f"{name} said a human can't store anything inside itself either."); time.sleep(3)
		SatisMath = random.randint(10,25); print(f"{CurE} believe it never thought of that. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy in ["Tin Can't", "Hot Tin Can't"] and interaction == "3": # Tin Can't Razz
		print(f"{name} made fun of {CurE} because it has no limbs or facial features."); time.sleep(3); BAD = True
		SatisMath = random.randint(-15,-10); DisSatisMath = random.randint(10,15)
		print(f"{CurE} believe {"you" if FocusedPlayer == "Pinori" else "they"} said that. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 or satisfaction > 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy in ["Tin Can't", "Hot Tin Can't"] and interaction == "4": # Tin Can't Kick
		print(f"{name} kicked {CurE} as hard as {"you" if FocusedPlayer == "Pinori" else "they"} could."); BAD = True
		PringlesCant = pygame.mixer.Sound(GetCustomFilePath("Pringles Can't.wav", subdir1="sfx")); SoundCh.SFX.play(PringlesCant)
		SoundCh.BAT2.play(crit); time.sleep(3); SatisMath, DisSatisMath = 0, 0; print("... wow. Just wow."); EnemyHP = 0; pause()
	elif enemy == "Ore Gano" and interaction == "1": # Ore Gano Recipe
		print(f"{name} gave a recipe to Ore Gano."); time.sleep(2)
		SatisMath = random.randint(10,25); print(f"Ore Gano appreciates the effort and reads the recipe thoroughly before putting it in their pocket. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Ore Gano" and interaction == "2": # Ore Gano Suggest
		foods = ["Rigatoni", "Spaghetti", "Pizza", "Macaroni and Cheese", "Yogurt", "Pineapple Upside Down Cake", "Lasagna", "Corn Chowder", "Red Velvet Cookies", "Egg Fried Rice"]; food = random.choice(foods)
		print(f"{name} suggested that Ore Gano make: {food}."); time.sleep(3)
		if food in ["Rigatoni", "Spaghetti", "Lasagna", "Egg Fried Rice"]: SatisMath = random.randint(15,30); print(f"Ore Gano really appreciated the suggestion! {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		elif food in ["Pizza", "Corn Chowder", "Macaroni and Cheese"]: SatisMath = random.randint(5,10); print(f"Ore Gano decides it's worth trying to make something they haven't often tried before. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		elif food in ["Pineapple Upside Down Cake", "Yogurt", "Red Velvet Cookies"]: SatisMath = 1; print("Ore Gano is confused, but they agree to try it when they're feeling snacky. Satisfaction increased by 1%.")
		else: SatisMath = 1; print("Ore Gano appreciates the suggestion. Satisfaction increased by 1%.")
	elif enemy == "Ore Gano" and interaction == "3": # Ore Gano Heckle
		print(f"{name} heckled Ore Gano."); time.sleep(2); BAD = True
		SatisMath = random.randint(-20,-15); DisSatisMath = random.randint(15,20)
		print(f"Ore Gano frowns. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 or satisfaction > 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Ore Gano" and interaction == "4": # Ore Gano Negative Suggestion
		print(f"{name} suggested Ore Gano give up their dream of being a chef."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -50, 50; print(f"Ore Gano is appalled that such a thing could even be said. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 or satisfaction > 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Spyder" and interaction == "1": # Spyder Personal Space
		print(f"{name} reminded Spyder that personal space exists."); time.sleep(2)
		SatisMath = random.randint(15,30); print(f"Spyder really wants to follow this concept. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Spyder" and interaction == "2": # Spyder Respect Boundaries
		print(f"{name} respected Spyder's boundaries..."); time.sleep(2)
		SatisMath = random.randint(20,25); print(f"Spyder wants to do the same for you. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Spyder" and interaction == "3": # Spyder Disrespect Boundaries
		print(f"{name} invaded Spyder's personal space."); time.sleep(3); BAD = True
		SatisMath = random.randint(-25,-20); DisSatisMath = random.randint(20,25)
		print(f"Spyder already regrets spying on you. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Spyder" and interaction == "4": # Spyder Death Stare
		print(f"{name} stared Spyder down while narrowing {"your" if FocusedPlayer == "Pinori" else "their"} eyes."); time.sleep(3); BAD = True
		SatisMath = random.randint(-50,-25); DisSatisMath = random.randint(25,50)
		print(f"Spyder understands how you must have felt when they were spying on you. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Deer God" and interaction == "1": # Deer God Worship
		print(f"{name} worshipped the Deer God."); time.sleep(2)
		SatisMath = random.randint(8,10); print(f"Deer God is pleased. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%." if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Deer God" and interaction == "2": # Deer God Research Deerism
		print(f"{name} asked the Deer God to tell a story about the history of Deerism."); time.sleep(3)
		print("Deer God agrees to do so."); time.sleep(2)
		print("It takes a long time for everything to be explained..."); time.sleep(3)
		print(f"... but {"you" if FocusedPlayer == "Pinori" else "they"} listened all the way through with nothing but interest in {"your" if FocusedPlayer == "Pinori" else "their"} eyes."); time.sleep(4)
		SatisMath = random.randint(30,50); print(f"Deer God is very pleased by {"your" if FocusedPlayer == "Pinori" else f"{FocusedPlayer}'s"} dedication. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%." if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Deer God" and interaction == "3": # Deer God Offer to Pet
		print(f"{name} offered to pet the Deer God..."); time.sleep(3); SatisMath = 0; print("Deer God politely declined.")
	elif enemy == "Deer God" and interaction == "4": # Deer God You're not God
		print(f"{name} told the Deer God that it's not the \"real God\"."); time.sleep(3); SatisMath, DisSatisMath = 0, 0
		SoundCh.BAT2.play(crit); SoundCh.SFX2.play(burn); SoundCh.SFX.play(hurt); print(f"Deer God smote {name.lower() if name == "You" else name}! {name} took {HP} damage and became unconscious!"); HP = 0; DeathByDeerGodAlt = True; DeathByDeerGod = False
	elif enemy == "Deer God" and interaction == "5": # Deer God Razz
		print(f"{name} made fun of the Deer God's appearance."); time.sleep(3); SatisMath, DisSatisMath = 0, 0; print("The Deer God was unaffected by the comment."); BAD = True
	elif enemy == "Deer God" and interaction == "6": # Deer God Threaten to tug fur
		print(f"{name} threatened to tug the Deer God's fur."); time.sleep(3); SatisMath, DisSatisMath = 0, 0; print("The Deer God seems unphased by your threat."); BAD = True
	elif enemy == "Investigator" and interaction == "1": # Investigator Cooperate
		print(f"{name} cooperated with the Investigator."); time.sleep(2)
		SatisMath = random.randint(20,30); print(f"Investigator is surprised. He appreciates your cooperation. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Investigator" and interaction == "2": # Investigator Flip your pockets and put your hands up
		print(f"{name} flipped {"your" if FocusedPlayer == "Pinori" else "their"} pockets inside out and put {"your" if FocusedPlayer == "Pinori" else "their"} hands up."); time.sleep(2)
		SatisMath = random.randint(30,60); print(f"Investigator appreciates the extreme effort to cooperate. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Investigator" and interaction == "3": # Investigator Don't cooperate
		print(f"{name} refused to provide any details about {"yourself" if FocusedPlayer == "Pinori" else "themself"}."); time.sleep(3); BAD = True
		SatisMath = random.randint(-40,-20); DisSatisMath = random.randint(20,40)
		print(f"Investigator gives you a dirty look. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 or satisfaction > 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Investigator" and interaction == "4": # Investigator Be Secretive
		print(f"{name} plead{"" if FocusedPlayer == "Pinori" else "ed"} the fifth."); time.sleep(3); BAD = True
		SatisMath = random.randint(-60,-30); DisSatisMath = random.randint(30,60)
		print(f"Investigator is very suspicious of you, though he already has the details he needs to prove you're guilty. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 or satisfaction > 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Kame Dee" and interaction == "1": # Kame Dee Idea
		print(f"{name} gave an idea for a skit to Kame Dee."); time.sleep(2)
		SatisMath = random.randint(15,20); print(f"Kame Dee likes your idea and promises to make a skit inspired by it! {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Kame Dee" and interaction == "2": # Kame Dee Different kinds of humour
		print(f"{name} suggested that Kame Dee try different forms of humour."); time.sleep(3)
		SatisMath = random.randint(20,25); print(f"Kame Dee is interested and wants to give this a try. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Kame Dee" and interaction == "3": # Kame Dee Heckle
		print(f"{name} heckled Kame Dee."); time.sleep(2); BAD = True
		SatisMath = random.randint(-25,-20); DisSatisMath = random.randint(20,25)
		print(f"Kame Dee gives {name.lower() if FocusedPlayer == "Pinori" else name} an unamused stare. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Kame Dee" and interaction == "4": # Kame Dee Negative Idea
		print(f"{name} suggested Kame Dee just give up their career as a Kame-Dee-an."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -50, 50; print(f"Kame Dee doesn't know how to respond, so they don't. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Bayet" and interaction == "1": # Bayet I've got your back
		print(f"{name} told Bayet that you've got their back."); time.sleep(2)
		SatisMath = random.randint(10,15); print(f"Bayet feels less uncomfortable. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Bayet" and interaction == "2": # Bayet You'll be in good hands
		print(f"{name} told Bayet that they'll be taken care of soon."); time.sleep(3)
		SatisMath = random.randint(5,10); print(f"Bayet feels like that could have been worded better, but understood what you meant. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Bayet" and interaction == "3": # Bayet Your siblings are nearby
		print(f"{name} told Bayet that Megan and the others are nearby."); time.sleep(3)
		SatisMath = random.randint(20,75); print(f"Bayet smiles brightly and starts fidgeting. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Bayet" and interaction == "4": # Bayet It's friendly out here
		print(f"{name} told Bayet that {location.title()} is a friendly place."); time.sleep(3)
		if bababooey: location = "Pneumonoultramicroscopicsilicovolcanoconiosis Plateau"
		# BEHOLD. an interaction that changes based on where you're at.
		# it's more possible to get every outcome if you're on Omnicide cuz Bayet won't be everywhere, so yeah good luck trying to get every single area.
		if location in ["Kiku Village", "Tanpopo Town", "Dyarix"]: SatisMath = random.randint(25,50); print(f"Bayet agrees with you. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		elif location in ["Nodium Valley", "Crystalline Oceanfront"]: SatisMath = random.randint(10,20); print(f"Bayet can't deny the truth. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		elif location in ["Archlekia", "Tanggal Volcano"]: SatisMath = random.randint(1,5); print(f"Bayet respectfully disagrees. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		elif location == "Pneumonoultramicroscopicsilicovolcanoconiosis Plateau": SatisMath = random.randint(5,40); print(f"Bayet laughs, wondering how you pronounced that so smoothly. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Bayet" and interaction == "5": # Bayet You're not safe
		print(f"{name} told Bayet that it's not safe out here."); time.sleep(3); BAD = True
		SatisMath = random.randint(-40,-20); DisSatisMath = random.randint(20,40)
		print(f"Bayet believes {"you" if FocusedPlayer == "Pinori" else "them"}, but only because {"you" if FocusedPlayer == "Pinori" else "they"}'re here. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Bayet" and interaction == "6": # Bayet Your siblings are gone
		print(f"{name} told Bayet that Megan, Grega, Terry, and all the others are gone."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -75, 75; print(f"Bayet's heart sinks. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Bayet" and interaction == "6": # Bayet You should run
		print(f"{name} suggested that Bayet start running."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -75, 75; print(f"Bayet really wants to, but can't because enemies fleeing wasn't programmed into the game. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Terry Bite" and interaction == "1": # Terry Bite Admire
		print(f"{name} admired the 1TB hard drive."); time.sleep(3)
		SatisMath = random.randint(10,15); print(f"Terry Bite smiles. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Terry Bite" and interaction == "2": # Terry Bite Envy
		print(f"{name} envied Terry Bite for having such great storage space."); time.sleep(3)
		SatisMath = random.randint(10,15); print(f"Terry Bite wishes he could give you a hard drive this size, but he doubts you have the Sines to buy it. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Terry Bite" and interaction == "3": # Terry Bite Ignore
		print(f"{name} ignored the 1TB hard drive."); time.sleep(3); BAD = True
		SatisMath = random.randint(-15,-10); DisSatisMath = random.randint(10,15)
		print(f"Terry Bite looks disappointed. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Terry Bite" and interaction == "4": # Terry Bite Heckle
		print(f"{name} heckled Terry Bite."); time.sleep(3); BAD = True
		SatisMath = random.randint(-30,-15); DisSatisMath = random.randint(15,30)
		print(f"Terry Bite looks uncomfortable. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy in ["Stickicidal Pessimistick", "Stickicidal Hot Pessimistick"] and interaction == "1": # Stickicidal Pessimistick End it
		print(f"{name} told Pessimistick to give up so it doesn't have to suffer anymore."); time.sleep(3); BAD = True
		print("Pessimistick pulls a Foreign Stimulant out of nowhere and takes it."); time.sleep(3)
		SatisMath, DisSatisMath = -100, 100
		FSType = random.randint(1,2)
		if FSType == 1:
			print("It was toxic."); EnemyHP = 0; time.sleep(3)
			print(Fore.RED + "Pessimistick is dead."); time.sleep(3)
			print(Fore.RED + "And it's all your fault."); time.sleep(3)
			if "Hot" in CurE: print(Fore.RED + "The scent of a burning stick invades your lungs as a result."); time.sleep(3)
		else: print("It was a roofie."); time.sleep(3); print("That was close."); time.sleep(3); EnemyAsleep = True
	elif enemy == "Siwi" and interaction == "1": # Siwi Give another kiwi
		print(f"{name} gave {CurE} another kiwi."); SatisMath = 100; time.sleep(3); print(f"{CurE} is ecstatic! Satisfaction increased by 100%!")
	elif enemy == "Siwi" and interaction == "2": # Siwi Snatch kiwi
		print(f"{name} confiscated {CurE}'s kiwi."); SatisMath, DisSatisMath = -100, 100; time.sleep(3); BAD = True
		print(f"{CurE} looks devastated. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Stranger" and interaction == "1": # Stranger Get to know
		print(f"{name} gave a fact about {"your" if FocusedPlayer == "Pinori" else "them"}self in exchange for a fact about the Stranger."); time.sleep(3)
		SatisMath = random.randint(10,20); print(f"Truly a riveting exchange of details. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Stranger" and interaction == "2": # Stranger Pickpocket
		print(f"{name} tried to pickpocket the Stranger..."); time.sleep(3); BAD = True; FreeSlots = []
		for slot, item in inventory[FocusedPlayer].items():
			FreeSlots.append(slot) if item == "None" else time.sleep(0)
			if FreeSlots: break # only need to scan for one slot, which will end up in entry 0 (FreeSlots[0])
		if not FreeSlots: print(f"... but {"your" if FocusedPlayer == "Pinori" else "their"} inventory is full."); SatisMath, DisSatisMath = 0, 0
		else:
			PotentialItem = ["Ambersoda", "Upgraded Slingshot", "Promotion", "Foreign Stimulant", "None", "None", "None", "None"] # the 4 Nones gives it a fair chance of failing which... makes sense, right? Right?
			StolenItem = random.choice(PotentialItem); inventory[FocusedPlayer][FreeSlots[0]] = StolenItem
			print("... and failed.") if StolenItem == "None" else print(f"... and stole {"a" if StolenItem in ["Promotion", "Foreign Stimulant"] else "an"} {StolenItem}.")
			print("(Press any key to continue.)"); pause()
			SatisMath = random.randint(-25,-20); DisSatisMath = random.randint(20,25)
			print(f"{f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Stray Cat" and interaction == "1": # Stray Cat Take it slow
		print(f"{name} slowly approached the Stray Cat."); time.sleep(3)
		if dissatisfaction == 0: SatisMath = random.randint(5,10); print(f"The Stray Cat doesn't feel alarmed. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		else: SatisMath = 0; print(f"The Stray Cat backs away.")
	elif enemy == "Stray Cat" and interaction == "2": # Stray Cat Offer treat
		print(f"{name} offered the Stray Cat a treat."); time.sleep(3); SatisMath = 0
		if not Dissatisfied and not Satisfied: print("The Stray Cat doesn't seem to want one, but doesn't seem unamused.") if dissatisfaction == 0 else print("The Stray Cat knows you're playing some sort of mind game with it.")
		elif Dissatisfied: print(f"The Stray Cat ignores {"your" if FocusedPlayer == "Pinori" else "their"} offer.")
		elif Satisfied: print(f"The Stray Cat accepts {"your" if FocusedPlayer == "Pinori" else "their"} offer and eats the treat. Yummy!")
		else: print("The Stray Cat just stares at the treat. (This is only an error message if you consider it one.)") # not supposed to trigger but it's not the end of the world if it does ig
	elif enemy == "Stray Cat" and interaction == "3": # Stray Cat Try to pet
		print(f"{name} tried to pet the Stray Cat."); time.sleep(3)
		SatisMath = random.randint(5,10) if dissatisfaction == 0 and not Satisfied else 0
		if dissatisfaction == 0: print(f"The Stray Cat sheepishly tries to let you pet it. This is quite the step out of the comfort zone. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		elif Satisfied: print("The Stray Cat nuzzles your hand and purrs quietly.")
		elif not Dissatisfied: print("The Stray Cat folds its ears back and backs away from you.")
		else: print("The Stray Cat hisses at you. Now's probably a good time to leave.")
	elif enemy == "Stray Cat" and interaction == "4": # Stray Cat Shoo
		print(f"{name} shooed the Stray Cat away."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -100, 100; print(f"The Stray Cat jolts up and backs a few feet away from {"you" if FocusedPlayer == "Pinori" else "them"}. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Feral Cat" and interaction == "1": # Feral Cat Shoo
		print(f"{name} shooed the Feral Cat away."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = 0, 0; print(f"The Feral Cat backs a few feet away from {"you" if FocusedPlayer == "Pinori" else "them"}.")
	elif enemy == "Miyu" and interaction == "1": # Miyu Voice Training Tip
		if not Dissatisfied:
			print(f"{name} gave Miyu a tip for voice training."); time.sleep(3)
			SatisMath = random.randint(20,30); print(f"Miyu is excited to follow {"your" if FocusedPlayer == "Pinori" else "their"} advice. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		else: print("..."); SatisMath = 0
	elif enemy == "Miyu" and interaction == "2": # Miyu Miyu (yeah, you read that right LOL)
		if not Dissatisfied:
			print(f"{name} miyu'd at Miyu. Miyu!"); time.sleep(3)
			SatisMath = random.randint(20,30); print(f"Miyu miyus back. Miyu! {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
		else: print("..."); SatisMath = 0
	elif enemy == "Miyu" and interaction == "3": # Miyu Give Up
		BAD = True
		if not Dissatisfied:
			print(f"{name} told Miyu to give up voice training because it's too difficult."); time.sleep(3)
			SatisMath, DisSatisMath = -100, 100; print(f"Miyu doesn't know what to say. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
		else: print("..."); SatisMath, DisSatisMath = 0, 0
	elif enemy == "Miyu" and interaction == "4": # Miyu Invalidate
		print(f"{name} told Miyu she will never be a woman."); time.sleep(3); BAD = True
		if not Dissatisfied: SatisMath, DisSatisMath = -200, 200; print(f"Miyu freezes up from pure shock. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
		else: print(Fore.RED + "Miyu: No need to say it twice, asshole."); SatisMath, DisSatisMath = 0, 0
	elif enemy == "Tan Papa" and interaction == "1": # Tan Papa Compliment Tan
		print(f"{name} told Tan Papa he has a nice tan."); time.sleep(3)
		SatisMath = random.randint(10,15); print(f"Tan Papa appreciated that. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Tan Papa" and interaction == "2": # Tan Papa Directions to the store
		print(f"{name} told Tan Papa how to get to the store so he can buy the milk and return home."); time.sleep(3)
		SatisMath = random.randint(30,50); print(f"Tan Papa really appreciated the assistance. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Tan Papa" and interaction == "3": # Tan Papa Insult Tan
		print(f"{name} mocked Tan Papa's tan."); time.sleep(3); BAD = True
		SatisMath = random.randint(-30,-20); DisSatisMath = random.randint(20,30)
		print(f"Tan Papa gives you an \"Are you serious?\" look. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Tan Papa" and interaction == "4": # Tan Papa Misdirect
		print(f"{name} gave Tan Papa the wrong directions to the store on purpose to prevent him from buying the milk."); time.sleep(3); BAD = True
		SatisMath = random.randint(-30,-20); DisSatisMath = random.randint(20,30)
		print(f"Tan Papa knows you're lying and gives you a dirty look. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Tan Papa" and interaction == "5": # Tan Papa Lie about the children
		print(f"{name} told Tan Papa the kids are in danger."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -50, 50; print(f"Tan Papa knows you're likely jesting, but worries anyway. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Tan Papa" and interaction == "6": # Tan Papa Bad Dad
		print(f"{name} told Tan Papa he's a bad father."); time.sleep(3); BAD = True
		SatisMath = random.randint(-30,-20); DisSatisMath = random.randint(20,30)
		print(f"Tan Papa responds by saying you don't know him, nor do you have proof. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Optimistick" and interaction == "1": # Optimistick How to escape pessimism?
		print(f"{name} asked Optimistick how to escape pessimism."); time.sleep(3)
		SatisMath = random.randint(20,25); print(f"Optimistick just responds with the word \"hope\". {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Optimistick" and interaction == "2": # Optimistick Congratulate
		print(f"{name} congratulated Optimistick on escaping pessimism."); time.sleep(3)
		SatisMath = random.randint(25,50); print(f"Optimistick thanks {"you" if FocusedPlayer == "Pinori" else "them"} for congratulating it. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Optimistick" and interaction == "3": # Optimistick Degrade
		print(f"{name} told Optimistick that it's foolish for having hopes in this world."); time.sleep(3); BAD = True
		SatisMath, DisSatisMath = -25, 25; print(f"Optimistick feels hurt. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Optimistick" and interaction == "4": # Optimistick No Point
		print(f"{name} told Optimistick that there's no point in having hope in a world where bad thrives."); time.sleep(3); BAD = True
		SatisMath = random.randint(-75,-50); DisSatisMath = random.randint(50,75)
		print(f"Optimistick understands your point of view. {f"Satisfaction decreased by {abs(SatisMath)}%." if satisfaction+SatisMath >= 0 else Fore.RED + f"Dissatisfaction increased by {DisSatisMath}%."}")
	elif enemy == "Shadorako's Guards" and interaction == "1": # Shadorako's Guards I/We come in peace
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} tell{"s" if FocusedPlayer != "Pinori" else ""} Shadorako's Guards that you come in peace."); time.sleep(3)
		SatisMath = random.randint(1,5); typewriter_shadoguard("Yeah, sure...", guard=random.randint(1,2)); pause()
		print(f"{f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}"); pause()
	elif enemy == "Shadorako's Guards" and interaction == "2": # Shadorako's Guards Suggest joining your party
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} suggest{"s" if FocusedPlayer != "Pinori" else ""} the guards join your party."); time.sleep(3)
		SatisMath = random.randint(1,8); print("The guards genuinely give the offer some thought."); time.sleep(2); GuardRemarks = ["Eh... Her Darkness was always pretty harsh with her demands...", "How much will you pay us?", "What's in it for us?", "Maybe...", "I dunno if we can do that."]
		typewriter_shadoguard(random.choice(GuardRemarks), guard=random.randint(1,2)); pause()
		print(f"{f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}"); pause()
	elif enemy == "Shadorako's Guards" and interaction == "3": # Shadorako's Guards Refuse to fight
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} refused to fight the guards."); time.sleep(2)
		SatisMath = 1; typewriter_shadoguard("Hey, there's no backing out now.", guard=random.randint(1,2)); pause()
		print("Satisfaction increased by 1%."); pause()
	elif enemy == "Krystal" and interaction == "1": # Krystal Ambersine
		print(f"{"You tell" if FocusedPlayer == "Pinori" else f"{FocusedPlayer} tells"} Krystal {"s" if FocusedPlayer != "Akuron" else ""}he knows she's from Ambersine, and that the Tone must be returned."); time.sleep(4)
		SatisMath = random.randint(10,20); print(f"Krystal sighs and nods yes. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Krystal" and interaction == "2": # Krystal Stand still
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} stand{"s" if FocusedPlayer != "Pinori" else ""} still and refuse{"s" if FocusedPlayer != "Pinori" else ""} to fight."); time.sleep(3)
		SatisMath = random.randint(1,8); print(f"Krystal doesn't feel inclined to end the battle early, but understands what {"you" if FocusedPlayer == "Pinori" else "they"}'re doing. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Krystal" and interaction == "3": # Krystal Shadorako
		print(f"{"You" if FocusedPlayer == "Pinori" else FocusedPlayer} remind{"s" if FocusedPlayer != "Pinori" else ""} Krystal about Shadorako.\n{"You" if FocusedPlayer == "Pinori" else "He" if FocusedPlayer == "Akuron" else "She"} also tell{"s" if FocusedPlayer != "Pinori" else ""} her that by keeping the Tone, Krystal would be helping her."); time.sleep(5)
		SatisMath = random.randint(10,30); print(f"Krystal growls after hearing Shadorako's name. She's warming up to the idea of helping {"you" if FocusedPlayer == "Pinori" else "your party"}. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Skelepound" and interaction == "1": # Skelepound Weight
		if satisfaction == 0:
			print("You ask Skelepound about its weight."); time.sleep(3) # forced first person because this is a Halloween Event enemy
			SatisMath = 1; print("Skelepound says it only weighs a pound. That's quite light! Satisfaction increased by 1%.")
		elif satisfaction == 1:
			print("You point out how light Skelepound is, expressing surprise."); time.sleep(3)
			SatisMath = 1; print("Skelepound seems more frustrated with itself. Satisfaction increased by 1%.")
		elif satisfaction == 2:
			print("You ask why Skelepound is mad at itself."); time.sleep(3)
			SatisMath = 1; print("Skelepound says it's because other skeletons weigh more than it does. Satisfaction increased by 1%.")
		elif satisfaction == 3:
			print("You point out that just because Skelepound is far lighter, that doesn't mean it's less valued."); time.sleep(3)
			SatisMath = 1; print("Skelepound responds by saying it still wishes it weighed a ton. Satisfaction increased by 1%.")
		elif satisfaction == 4:
			print("You point out that if Skelepound weighed a ton, it wouldn't be able to move."); time.sleep(3)
			SatisMath = 1; print("Skelepound asks why all the other skeletons can move just fine. Satisfaction increased by 1%.")
		elif satisfaction == 5:
			print("You remind Skelepound that skeletons don't weigh a ton."); time.sleep(3)
			SatisMath = 1; print("Skelepound seems surprised. Satisfaction increased by 1%.")
		elif satisfaction == 6:
			print("You reiterate that it's fine for Skelepound to be underweight."); time.sleep(3)
			SatisMath = 94; print("Skelepound shrugs and agrees with you. Satisfaction increased by 94%!")
		else:
			print("You tell Skelepound you're happy it's no longer upset about its weight."); time.sleep(3)
			SatisMath = 0; print("Skelepound responds by saying it is too.")
	elif enemy == "Mortis" and interaction == "1": # Mortis Poke
		global PlayingDead; print("You try to poke Mortis."); time.sleep(3)
		if not PlayingDead: SatisMath = 0; print("Mortis forbids you from doing so.")
		else:
			SatisMath = 0
			if random.randint(1,5) == 3: PlayingDead = False; print("Mortis gets up like nothing happened.")
			else: print("Nothing happens.")
	elif enemy == "Hellhoward" and interaction == "1": # Hellhoward Offer treat
		if not Satisfied:
			accept = random.randint(1,5) == 3; print("You offer Hellhoward a treat."); time.sleep(3)
			if accept: SatisMath = 100; print("Hellhoward accepts and eats the treat. Satisfaction increased by 100%!")
			else: SatisMath = 0; print("Hellhoward ignores your offer and continues focusing on you.")
		else: print("You already gave Hellhoward a treat.")
	elif enemy in ["Skid", "Pump"] and interaction == "1": # Skid/Pump Do the Spooky Dance
		print(f"You do the Spooky Dance with {enemy}."); time.sleep(3)
		SatisMath = 100; print(f"{enemy} is LOVING IT! {"Satisfaction increased by 100%!" if not Satisfied else ""}")
	elif enemy == "Kin" and interaction == "1": # Kin Encourage to do the Spooky Dance
		print("You encourage Kin to do the Spooky Dance."); time.sleep(3) # this is like, the ONLY Halloween Event enemy whose SatisMath isn't hardcoded LOL
		SatisMath = random.randint(5,20); print(f"Kin tries and fails, then sighs. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")
	elif enemy == "Pumpqueen" and interaction == "1": # Pumpqueen Apologise about the Grand Pumpkin
		print("You apologise to the Pumpqueen about the Grand Pumpkin, explaining that it's not your fault it had to be replaced."); time.sleep(3)
		SatisMath = random.randint(8,25); print(f"{"The Pumpqueen nods understandingly, but keeps her guard up for now." if satisfaction+SatisMath < 100 else "The Pumpqueen sighs and looks back at the Pumpking, who still seems miffed."} Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%.")
	else: # placeholder thing in case somehow the thingy breaks lol
		print(f"{name} did a thing."); time.sleep(2)
		SatisMath = random.randint(1,30); print(f"That was cool. {f"Satisfaction increased by {round(SatisMath/DivideOrNah)}%!" if dissatisfaction-SatisMath < 0 else Fore.RED + f"Dissatisfaction decreased by {round(SatisMath/DivideOrNah)}%."}")	
	SatisMath = round(SatisMath/DivideOrNah) # positive interactions mean less on Omnicide
	if not BAD and SatisMath >= 0: # for positive interactions
		if dissatisfaction > 0:
			if abs(SatisMath) <= dissatisfaction:
				dissatisfaction -= SatisMath; dissatisfaction /= DivideOrNah; dissatisfaction = round(dissatisfaction); print(Fore.RED + f"Dissatisfaction: {dissatisfaction}%")
				if DivideOrNah == 2: print(Fore.RED+f"({CurE} is having difficulty trusting you, so the deduction was halved.)")
			else:
				leftover = abs(SatisMath - dissatisfaction); dissatisfaction = 0
				satisfaction = min(100, satisfaction + leftover); print(f"Satisfaction: {satisfaction}%"); # Now, apply the remaining positive amount to satisfaction.
				if DivideOrNah == 2: print(Fore.RED+f"({CurE} is having difficulty trusting you, so the added percentage was halved.)")
		else:
			satisfaction = min(100, satisfaction + SatisMath); print(f"Satisfaction: {satisfaction}%") # If there's no dissatisfaction, simply increase satisfaction.
			if DivideOrNah == 2: print(Fore.RED+f"({CurE} is having difficulty trusting you, so the added percentage was halved.)")
		
		if satisfaction >= 100 or ((enemy in ["Clef", "Treble"]) and ClefHappy): Satisfied, Dissatisfied = True, False; print(f"{enemy} {"is" if CurE != "Shadorako's Guards" else "are"} {"satisfied" if enemy != "Deer God" else "pleased"}.")
	else: # For negative interactions
		if satisfaction > 0:
			if (satisfaction - DisSatisMath) >= 0: satisfaction -= DisSatisMath; print(f"Satisfaction: {satisfaction}%")
			else:
				overflow = abs(satisfaction - DisSatisMath); satisfaction = 0; dissatisfaction = min(100, dissatisfaction + overflow); print(Fore.RED + f"Dissatisfaction: {dissatisfaction}%")
				if dissatisfaction >= 100: Satisfied, Dissatisfied = False, True; print(Fore.RED + f"{enemy} is {"dissatisfied" if enemy != "Deer God" else "displeased"}.") # no is/are logic because you can't manually dissatisfy the guards, they're only automatically dissatisfied if you're fighting them on Omnicide
		else:
			try: DisSatisMath = -SatisMath if not DisSatisMath else DisSatisMath
			except: DisSatisMath = -SatisMath if not isinstance(DisSatisMath, int) else DisSatisMath
			if int(dissatisfaction + DisSatisMath) > 100: dissatisfaction = 100
			elif int(dissatisfaction + DisSatisMath) < 0: satisfaction = abs(dissatisfaction + DisSatisMath); dissatisfaction = 0
			else: dissatisfaction += DisSatisMath
			print(Fore.RED + f"Dissatisfaction: {dissatisfaction}%")
			if dissatisfaction >= 100: Satisfied, Dissatisfied = False, True; print(Fore.RED + f"{enemy} is dis{"satisfied" if enemy != "Deer God" else "pleased"}.")
	pause(); PendingDamage = 0
	if Satisfied and not ShadoGuards and not Krystal: BattleMenu()
	elif Satisfied and ShadoGuards: ShadoGuardsBattleMenu()
	elif Satisfied and Krystal: KrystalBattleMenu()
	elif CurE not in ["Shadorako's Guards", "Krystal"] and not InitEnemStat(CurE)["docile"]:
		try:
			if CurE == "Mortis" and PlayingDead: AtkAmount = 0
		except: pass
		for hohsisjoj in range(AtkAmount):
			if EnemyHP >= 1 and HP >= 1:
				if CurE not in ["Clef", "Treble"]: DamageIn = round(int(InDamage(Lvl, EnemyATK, defense, Yami=False))/4) if not BAD else round(int(InDamage(Lvl, EnemyATK, defense, Yami=False)))
				else: DamageIn = round(int(InDamage(Lvl, EnemyATK, defense, Yami=False))*2)
				if CurE not in ["Clef", "Treble"]:
					if hohsisjoj+1 == AtkAmount and DamageIn+PendingDamage > 0: HP -= DamageIn+PendingDamage
					elif DamageIn <= 0: SoundCh.SFX.play(miss); print(f"{CurE}'s attack missed."); pause(); break
					elif DamageIn > 0: PendingDamage += DamageIn; print(f"{CurE}'s first attack landed."); pause(); continue
				else:
					if hohsisjoj+1 == AtkAmount: HP = min(HP+DamageIn, MaxHP)
					else: PendingDamage += DamageIn; print(f"{CurE}'s first heal landed!"); pause(); continue
				if DamageIn >= 1 and CurE not in ["Clef", "Treble"]:
					try:
						if DamageIn >= (MaxHP/2) or ATKperform_enemy == 5: SoundCh.BAT2.play(crit)
					except Exception as e:
						SoundCh.SFX.play(tef); Log(f"EXCEPTION when doing damage things: {e}")
						if DamageIn >= (MaxHP/2): SoundCh.BAT2.play(crit)
					SoundCh.SFX.play(hurt)
				else: SoundCh.BAT2.play(miss if DamageIn <= 0 and CurE not in ["Clef", "Treble"] else heal)
				if CurE not in ["Clef", "Treble"] or (CurE in ["Clef", "Treble"] and not ClefHappy):
					PronounSet = {"Millie": ["she", "her", "her"],
						"Yami": ["they", "them", "their"],
						"Akuron": ["he", "him", "his"],
						"Sana": ["she", "her", "her"],
						"Pinori": ["you", "your", "your"]} # whenever it's Pinori it's always in first person perspective because you usually play as Pinori who is the main character, but you knew that I hope
					# povmod 1 - 3 and everything else was used for the Shadorako cutscene, I'm just copypasting what I need everywhere else
					povmod4 = "you" if FocusedPlayer == "Pinori" else PronounSet[FocusedPlayer][1]
					povmod5 = "you're" if FocusedPlayer == "Pinori" else "they're"
					povmod6 = FocusedPlayer if FocusedPlayer != "Pinori" else "you"
					if DamageIn >= 1:
						CritMSG = False; print(f"{CurE} dealt {DamageIn+PendingDamage} damage to {povmod4}.")
						if DamageIn >= (MaxHP/2): print("It was a critical hit!"); CritMSG = True
						try:
							if ATKperform_enemy == 5 and not CritMSG: print("It was a critical hit!") # don't display crit message twice
						except Exception: SoundCh.SFX.play(tef)
						if not BAD: print(f"(The damage was quartered{f" because {CurE} acknowledged {povmod5} trying to help." if not Dissatisfied else "."})")
					else: print(f"({CurE} couldn't muster enough strength to deal damage.)" if "Tin Can't" not in CurE else f"({CurE} bring itself to damage you.)") # miss; in the case of Tin Can't, this is another one of those cases where the name is part of a joke, so it'll say "Tin Can't bring itself to damage you". Hot Tin Can't is included here, hence why I wrote the line this way.
				else: print(f"{CurE} returned {DamageIn+PendingDamage} HP to {povmod6}.") if HP < MaxHP else print(f"{CurE} maxed out {PronounSet[FocusedPlayer][2]} HP.")
				pause()
		PendingDamage = 0
		if HP > 0 and not ShadoGuards and not bababooey: DeathByDeerGodAlt = False; BattleMenu()
		elif HP > 0 and ShadoGuards and not bababooey: DeathByDeerGodAlt = False; ShadoGuardsBattleMenu()
		else: GameOverAprilFool() if bababooey else GameOver()
	elif CurE == "Shadorako's Guards":
		for hohsisjoj in range(AtkAmount):
			if (ShadoGuard1HP >= 1 or ShadoGuard2HP >= 1) and HP >= 1:
				OtherGuard = 2 if ShadoGuard1HP <= 0 else 1
				DamageIn = round(InDamage(Lvl, 11 if Route != "Omnicide" else 14, defense, Yami=False)/4)
				if hohsisjoj+1 == AtkAmount and DamageIn > 0: HP -= DamageIn
				elif DamageIn > 0: PendingDamage += DamageIn; print(f"Shadorako{"'s Guards'" if ShadoGuard1HP >= 1 or ShadoGuard2HP >= 1 else f" Guard {OtherGuard}'s"} first attack landed."); pause(); continue
				else: SoundCh.SFX.play(miss); print(f"Shadorako{"'s Guards'" if ShadoGuard1HP >= 1 or ShadoGuard2HP >= 1 else f" Guard {OtherGuard}'s"} attack missed."); pause(); break
				if DamageIn >= MaxHP/2: SoundCh.BAT2.play(crit); print("Critical hit!")
				SoundCh.SFX.play(hurt if DamageIn > 0 else miss); print(f"Shadorako{"'s Guards collaboratively" if ShadoGuard1HP >= 1 or ShadoGuard2HP >= 1 else f" Guard {OtherGuard}"} dealt {DamageIn} damage to {"you" if FocusedPlayer == "Pinori" else FocusedPlayer}.") if DamageIn >= 1 else print(f"Shadorako{"'s Guards'" if ShadoGuard1HP >= 1 or ShadoGuard2HP >= 1 else f" Guard {OtherGuard}'s"} attack missed.")
				if DamageIn > 0: print(f"(The damage was quartered because {CurE} acknowledged {"you're" if FocusedPlayer == "Pinori" else "they're"} trying to help.)"); pause()
		PendingDamage = 0
		if HP > 0: DeathByDeerGodAlt = False; ShadoGuardsBattleMenu()
		else:
			TotalHP = 0; PartyMembersAsString = ", ".join(map(str, Party)); Log(f"Party: {PartyMembersAsString}"); validnames = ["Pinori", "Akuron", "Sana", "Yami"]
			for member in Party:
				if member not in validnames: continue
				Log(f"Adding {member}'s HP."); DebugPrint(f"{member}'s HP is {PlayerStatStorage[member]['HP']}.")
				if PlayerStatStorage[member]['HP'] <= 0: DebugPrint(f"{member} is literally dead lol")
				else:
					if member != FocusedPlayer: TotalHP += int(PlayerStatStorage[member]['HP']); Log(f"Total HP is now at {TotalHP}.")
					else: Log(f"Assessed character is focused player. Total HP remains at {TotalHP}.")
			Log("That's everyone. The consensus is...")
			if TotalHP <= 0 or len(Party) == 1: Log("Gaming over! Damn! Crud! Fiddlesticks! That just sucks."); GameOver() # only game over if everyone is unconscious
			else: Log("Someone's still alive! Good for them!"); print(f"{FocusedPlayer} is unconscious!"); pause(); SwitchMember(Forced=True)
	elif CurE == "Krystal":
		for hohsisjoj in range(AtkAmount):
			if KrystalHP >= 1 and HP >= 1:
				DamageIn = round(InDamage(Lvl, 14, defense, Yami=False)/4)
				if hohsisjoj+1 == AtkAmount and DamageIn > 0: HP -= DamageIn
				elif DamageIn > 0: PendingDamage += DamageIn; print("Krystal's first attack landed."); pause(); continue
				else: SoundCh.SFX.play(miss); print("Krystal's attack missed."); pause(); break
				if DamageIn >= MaxHP/2: SoundCh.BAT2.play(crit); print("Critical hit!")
				SoundCh.SFX.play(hurt) if DamageIn > 0 else SoundCh.SFX2.play(miss); print(f"Krystal dealt {DamageIn} damage to {"you" if FocusedPlayer != "Pinori" else FocusedPlayer}.") if DamageIn > 0 else print("(Krystal couldn't bring herself to damage you during your moment of reasoning.)")
				if DamageIn > 0: print(f"(The damage was quartered{f" because Krystal acknowledged {"you're" if FocusedPlayer == "Pinori" else "they're"} trying to help" if Route != "Omnicide" else ""}.)"); pause()
		PendingDamage = 0
		if HP > 0: DeathByDeerGodAlt = False; KrystalBattleMenu()
		else:
			TotalHP = 0; PartyMembersAsString = ", ".join(map(str, Party)); Log(f"Party: {PartyMembersAsString}"); validnames = ["Pinori", "Akuron", "Sana", "Yami"]
			for member in Party:
				if member not in validnames: continue
				Log(f"Adding {member}'s HP."); DebugPrint(f"{member}'s HP is {PlayerStatStorage[member]['HP']}.")
				if PlayerStatStorage[member]['HP'] <= 0: DebugPrint(f"{member} is literally dead lol")
				else:
					if member != FocusedPlayer: TotalHP += int(PlayerStatStorage[member]['HP']); Log(f"Total HP is now at {TotalHP}.")
					else: Log(f"Assessed character is focused player. Total HP remains at {TotalHP}.")
			Log("That's everyone. The consensus is...")
			if TotalHP <= 0 or len(Party) == 1: Log("Gaming over! Damn! Crud! Fiddlesticks! That just sucks."); GameOver() # only game over if everyone is unconscious
			else: Log("Someone's still alive! Good for them!"); print(f"{FocusedPlayer} is unconscious!"); pause(); SwitchMember(Forced=True)
	elif InitEnemStat(CurE)["docile"]:
		print((Fore.RED if Route == "Omnicide" else Fore.WHITE)+f"{CurE} is docile."); pause() # we don't have to worry about the logic for the bosses because the bosses are very CLEARLY not docile
		if HP > 0: DeathByDeerGodAlt = False; BattleMenu()
		else: GameOverAprilFool() if bababooey else GameOver()