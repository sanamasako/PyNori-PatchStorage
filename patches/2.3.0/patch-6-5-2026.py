def P3Menu():
	global HP, MaxHP, ShadorakoHP, ShadorakoMaxHP, inventory, atk, defense, Lvl, deaths, hurt, ShadorakoEarthHP, ShadorakoWaterHP, ShadorakoFireHP, ShadorakoMagicHP, TotalDeaths, Route
	global miss, sel, heal, weak, Route, kick, crit, suhit, uhit, brit, fhit, ShownLowHPWarning, heartbeat
	HealthBars = "no health bars"; Log("Outside of loop on Shadorako Phase 3."); sp3 = None
	while sp3 is None:
		if ShadorakoHP <= 0 and ShadorakoEarthHP <= 0 and ShadorakoWaterHP <= 0 and ShadorakoFireHP <= 0 and ShadorakoMagicHP <= 0: Log("Shadorako death condition triggered."); ShadorakoHP = 1000; deaths = 0; Phase4Intro()
		if HP <= 0: TotalDeaths += 1; deaths += 1; GameOverShado()
		if HP <= (MaxHP/7) and not ShownLowHPWarning: SoundCh.BAT2.play(heartbeat); print(Fore.RED + "You're dying."); pause(); ShownLowHPWarning = True
		DynamicallyReprintMenu()
		try:
			sp3 = int(input("You chose ")); SoundCh.SFX.play(sel)
			if sp3 == 1:
				Log("Player selected 1.")
				BarColours = {}; OtherBars = ["Earth", "Water", "Fire", "Magic"]; Log("Initialised bar colour stuff.")
				for bar in OtherBars: Log(f"Configuring {bar} bar."); BarColours[bar] = Fore.RED if globals()[f"Shadorako{bar}HP"] <= 0 else Fore.WHITE
				Log("Printing attack menu."); print("Which part of Shadorako do you want to attack?\n\n1 - Shadorako\n"+BarColours["Earth"]+"2 - Earth\n"+BarColours["Water"]+"3 - Water\n"+BarColours["Fire"]+"4 - Fire\n"+BarColours["Magic"]+"5 - Magic"+Fore.WHITE+"\n0 - Exit"); ElementAttacker = None
				while ElementAttacker is None:
					Log("Entered attack menu loop.")
					try:
						ElementAttacker = int(input("\nYou chose ")); SoundCh.SFX.play(sel)
						if ElementAttacker == 0: pass
						elif ElementAttacker == 1:
							Log("Trying to attack Shadorako.")
							if not all(power <= 0 for power in [ShadorakoEarthHP, ShadorakoWaterHP, ShadorakoFireHP, ShadorakoMagicHP]): Log("Powers have not been depleted."); print("Shadorako's other powers have not been weakened yet."); pause(); ShadoDamagesYouP3()
							else:
								Log("Powers have been depleted."); print("You tried to attack Shadorako."); time.sleep(3)
								Max = 150 if Route != "Omnicide" else 300
								dmg = random.randint(-1,Max)
								if dmg == 0: SoundCh.BAT2.play(miss)
								elif dmg == -1: SoundCh.SFX.play(heal)
								elif round(dmg) in range(1,19): SoundCh.SFX.play(weak)
								else:
									SoundCh.BAT.play(kick)
									if round(dmg) in range(100,199): SoundCh.BAT2.play(crit)
									elif round(dmg) in range(200,299): SoundCh.SFX.play(suhit)
									elif round(dmg) in range(300,399): SoundCh.SFX.play(uhit)
									elif round(dmg) in range(400,499): SoundCh.SFX.play(brit)
									elif round(dmg) > 499: SoundCh.SFX.play(fhit)
								ShadorakoHP -= dmg
								if dmg not in [-1, 0]:
									print(f"Dealt {dmg} damage to Shadorako!")
									if round(dmg) in range(100,199): print("Critical hit!")
									elif round(dmg) in range(200,299): print("Super hit!")
									elif round(dmg) in range(300,399): print("Ultra hit!")
									elif round(dmg) in range(400,499): print("BRUTAL hit!")
									elif round(dmg) > 499: print(Fore.RED + "FATAL HIT!!!")
								elif dmg == 0: print("The attack missed...")
								elif dmg == -1: print("Shadorako managed to block your hit... she recovered 1 HP.")
								pause(); Log("Damaging player."); ShadoDamagesYouP3()
						elif ElementAttacker == 2:
							if ShadorakoEarthHP > 0:
								print("You tried to decrease Shadorako's Earth power."); time.sleep(3)
								Max = 40 if Route != "Omnicide" else 300
								dmg = int(round(random.randint(5,Max)))
								ShadorakoEarthHP -= dmg
								print(f"Shadorako's Earth power was decreased by {dmg}!"); pause(); ShadoDamagesYouP3()
							else: print("This power has been depleted."); ElementAttacker = None
						elif ElementAttacker == 3:
							if ShadorakoWaterHP > 0:
								print("You tried to decrease Shadorako's Water power."); time.sleep(3)
								Max = 40 if Route != "Omnicide" else 300
								dmg = int(round(random.randint(10,Max)/4))
								ShadorakoWaterHP -= dmg
								print(f"Shadorako's Water power was decreased by {dmg}!"); pause(); ShadoDamagesYouP3()
							else: print("This power has been depleted."); ElementAttacker = None
						elif ElementAttacker == 4:
							if ShadorakoFireHP > 0:
								print("You tried to decrease Shadorako's Fire power."); time.sleep(3)
								Max = 40 if Route != "Omnicide" else 300
								dmg = int(round(random.randint(30,Max)))
								ShadorakoFireHP -= dmg
								print(f"Shadorako's Fire power was decreased by {dmg}!"); pause(); ShadoDamagesYouP3()
							else: print("This power has been depleted."); ElementAttacker = None
						elif ElementAttacker == 5:
							if ShadorakoMagicHP > 0:
								print("You tried to decrease Shadorako's Magic power."); time.sleep(3)
								Max = 40 if Route != "Omnicide" else 300
								dmg = int(round(random.randint(10,Max)))
								ShadorakoMagicHP -= dmg
								print(f"Shadorako's Magic power was decreased by {dmg}!"); pause(); ShadoDamagesYouP3()
							else: print("This power has been depleted."); ElementAttacker = None
						else: print("Invalid input."); ElementAttacker = None
					except ValueError: print("Input was not an integer."); ElementAttacker = None
			elif sp3 == 2:
				print("You struggle to move..."); time.sleep(2)
				print("Shadorako cackles."); ShadoDamagesYouP3()
			elif sp3 == 3: ItemShado()
			elif sp3 == 4: command = Fore.RED if Route == "Omnicide" else Fore.WHITE; print(command + "But there was nothing worth doing with Shadorako."); sp3 = None
			elif sp3 == 5: command = Fore.RED if Route == "Omnicide" else Fore.WHITE; print(command + "You still found yourself unable to spare Shadorako."); sp3 = None
			else: print("Invalid option."); sp3 = None
		except ValueError: print("Input was not an integer."); sp3 = None
		sp3 = None