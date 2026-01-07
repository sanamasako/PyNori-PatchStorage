def PreStartup():
	try:
		VictoryCheck()
		if sys.platform in ["win32", "darwin", "linux", "linux2"]:
			if not skip_rpc:
				Log("Setting up Discord Rich Presence."); threading.Thread(target=UpdatePresence, daemon=True).start()
				try: PyNoriRPC_ClientID = bytes.fromhex("31343538353436333831393836393838323033").decode(); RPC = Presence(str(PyNoriRPC_ClientID)); RPC.connect()
				except DiscordNotFound: print("Discord is either not installed or not running. Discord Rich Presence will not function.\nPress any key to continue game startup."); pause()
				except ConnectionRefusedError: print("Discord Rich Presence failed to initialise. You can still play the game, but it will not show up as an Activity.\nPress any key to continue game startup."); pause()
			else: print("You chose to skip Discord Rich Presence, so it will not function for this session. Press any key to continue game startup."); pause()
			Log("Initialising checksum analyser."); global checksum_thread; checksum_thread = CheckForChanges(sys.argv[0]); checksum_thread.start()
			Log("Initialising Lucky Charm thread."); LCThread = LuckyCharmThread(); LCThread.start()
			if os.path.exists(os.path.join(os.getcwd(), "weatherconfig.ini")):
				StartupWeatherChecker = configparser.ConfigParser(); StartupWeatherChecker.read(GetCustomFilePath("weatherconfig.ini")); WeatherCustoms = StartupWeatherChecker["Customisation"]
				Log("Setting up weather." if WeatherCustoms["weather events"] == "True" else "You have Weather Events disabled, so the weather will not build."); Weather = BuildWeather() if WeatherCustoms["weather events"] == "True" else None
			try:
				free = shutil.disk_usage(__file__).free
				if free < 1000000: raise OSError(28, "No space left on device")
			except OSError as e:
				SoundCh.SFX.play(error)
				if e.errno == 28: print("The drive you are running PyNori from is full. Please free up space and reload the game.")
				elif e.errno == 5: print("An input/output error occurred when checking the free space on the current drive. Please consider running the game from a different drive.")
				elif e.errno == 30: print("PyNori could not start because the current directory is read-only.\nPlease change the directory settings to allow writing to it, or move the game elsewhere and reload it.")
				else: print(f"PyNori could not start due to an error: {e}\nPlease try running the game from a different directory or drive. If errors continue to occur, there may be something wrong with your device.")
				while pygame.mixer.get_busy(): continue
				os._exit(1)
			except MemoryError:
				SoundCh.SFX.play(error); print("Your device does not have enough free memory to run PyNori. If you have other apps open (especially resource intensive ones), close those and try again.")
				while pygame.mixer.get_busy(): continue
				os._exit(1)
			AttemptStartup()
		else: Lockout()
	except Exception: sys.excepthook(*sys.exc_info())