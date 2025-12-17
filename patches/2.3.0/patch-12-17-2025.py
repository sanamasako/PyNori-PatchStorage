def CheckForPatches():
	global nopatches, CurVer; CurVerPieces = list(map(int, CurVer.split("."))); PatchCheckURL = f"https://raw.githubusercontent.com/sanamasako/PyNori-PatchStorage/main/patches/{CurVerPieces[0]}.{CurVerPieces[1]}.0/manifest.json"
	if nopatches or args.nopatches: print("You chose to skip checking for patches. Press any key to continue game startup."); pause(); return
	try: print(Fore.WHITE+"Checking for patches..."); response = requests.get(PatchCheckURL); FileList = response.json()
	except Exception as e: print(f"Could not check for patches at this time: {e}\nPyNori will still function, but bug fixes (if any) are currently unavailable.\n(If you're REALLY desperate, you COULD apply the patch by hand...)"); pause(); return
	Log(f"File list for v{CurVer}: {FileList}"); Patches = FileList["active_patches"]; Log(f"Patches for v{CurVer}: {Patches}")
	if Patches == {}: print(f"There are no patches for v{CurVer} at this time. Press any key to continue game startup."); pause(); return
	else:
		MissingPatches, PendingPatches = 0, 0; MissingPatchNames = []; DownloadedPatches = []
		for patch in Patches.keys():
			if not os.path.exists(os.path.join(os.getcwd(), "patches", patch)) and not FileInFile(f"https://raw.githubusercontent.com/sanamasako/PyNori-PatchStorage/main/patches/{CurVerPieces[0]}.{CurVerPieces[1]}.0/{patch}", "game.py"): MissingPatches += 1; MissingPatchNames.append(patch)
			elif os.path.exists(os.path.join(os.getcwd(), "patches", patch)) and not FileInFile(os.path.join(os.getcwd(), "patches", patch), "game.py"): PendingPatches += 1; DownloadedPatches.append(patch)
		if MissingPatches + PendingPatches == 0: print("Congratulations! Your copy of PyNori is all patched up! Press any key to continue game startup."); pause(); return
		else:
			print(f"There {"are" if MissingPatches+PendingPatches > 1 else "is"} {MissingPatches+PendingPatches} patch{"es" if MissingPatches+PendingPatches > 1 else ""} available{f" ({PendingPatches} of which were found locally but not yet installed)" if PendingPatches > 0 else ""}.\nPatches are bugfixes that can be automatically applied to your copy of PyNori without updating the game."); patchOpt = ""
			while True:
				patchOpt = input("Would you like to patch the game? [Y/N] ").lower()
				if patchOpt in ["y", "yes", "n", "no"]: break
			if patchOpt in ["n", "no"]: print("Suit yourself. Enjoy the bugs!"); pause(); return
			print(f"Fetching manifest for v{CurVerPieces[0]}.{CurVerPieces[1]}.0..."); checksums = {}
			try:
				for patch in Patches.keys(): checksums[patch] = Patches[patch]["checksum"].split(":", 1)[1]
			except Exception as e: print(f"Encountered an error when collecting checksums: {e}")
			if MissingPatchNames != []: print("Downloading missing patches...")
			for patch in MissingPatchNames:
				if patch in FileList["skipped_patches"]: print(f"{patch} is outdated, so it will not be downloaded."); continue
				try:
					print(f"Downloading {patch}..."); os.makedirs("patches", exist_ok=True)
					response = requests.get(f"https://raw.githubusercontent.com/sanamasako/PyNori-PatchStorage/main/patches/{CurVerPieces[0]}.{CurVerPieces[1]}.0/{patch}")
					if response.status_code == 200:
						with open(os.path.join(os.getcwd(), "patches", patch), "wb") as f: f.write(response.content)
						print(f"{patch} finished downloading!"); DownloadedPatches.append(patch)
					elif response.status_code == 404: print("The patch could not be located on the repository.")
					else: print(f"The patch could not be downloaded (HTTP {response.status_code}).")
				except OSError as e:
					SoundCh.SFX.play(error)
					if e.errno == 28: print("The drive you are running PyNori from is full. Please free up space and reload the game.")
					elif e.errno == 5: print("The patch could not be downloaded due to an input/output error. Consider moving the game to a different drive if possible, then reload the game.")
					elif e.errno == 30: print("The patch could not be downloaded because the current directory is read-only.\nPlease change the directory settings to allow writing to it, or move the game elsewhere and reload it.")
					elif e.errorno == 2: print("The patch could not be downloaded because PyNori couldn't figure out where to save it. Most likely, this is a result of you trying to \"import game\" within Python itself instead of trying to run it from the terminal your OS provides you. If you need assistance running the game properly, see = OPEN ME IN NOTEPAD =.txt.")
					else: print(f"The patch could not be downloaded due to an error: {e}\nIf the error isn't about a failed connection, please try running the game from a different directory or drive. If (non-internet) errors continue to occur, there may be something wrong with your device.")
			print("Verifying checksums of downloaded patches...")
			try:
				for patch in os.listdir("patches"):
					if f"sha256:{GetChecksum(os.path.join(os.getcwd(), "patches", patch))}" != Patches[patch]["checksum"]: print(f"The checksum for {patch} doesn't match the one on the server. This patch will not be installed."); os.remove(os.path.join(os.getcwd(), "patches", patch)); DownloadedPatches.remove(patch)
			except Exception as e: print(f"Encountered an error while verifying checksums: {e}")
			if DownloadedPatches:
				print("Applying patches..."); PatchErrors = 0
				for patch in DownloadedPatches: PatchErrors += 1 if not ApplyPatch(patch) else 0
				print("Cleaning up...")
				for patch in os.listdir("patches"): os.remove(os.path.join(os.getcwd(), "patches", patch))
				print(f"Finished patching{f" with {PatchErrors} errors" if PatchErrors > 0 else ""}! Please restart the game."); os._exit(0)
			else:
				print("There are no valid patches to apply. Cleaning up...")
				for patch in os.listdir("patches"): os.remove(os.path.join(os.getcwd(), "patches", patch))