def BuildWeather(Silent=True, ReturnCurrent=False):
	def CompareHours():
		global hour; Date = datetime.datetime.now(); CurHour = Date.hour; SameHour = CurHour == hour # condition set here so the line below this one doesn't cause the return to say "yes, it's still that hour"
		if CurHour != hour: hour = CurHour
		Log(f"Current hour and old hour are identical?: {SameHour}"); return SameHour
	try:
		if os.path.exists(GetCustomFilePath("weatherconfig.ini")): GetHemi = configparser.ConfigParser(); GetHemi.read(GetCustomFilePath("weatherconfig.ini")); WeatherConf = GetHemi["Customisation"]; SavedHemi = WeatherConf["hemisphere"]; Log(f"Hemisphere setting: {SavedHemi}")
		else: SavedHemi = "Auto"
		Loc = PlayerLocation(); Log("Loading hemisphere."); hemi = hemisphere(float(Loc["latitude"])) if SavedHemi == "Auto" else SavedHemi; Log(f"Hemisphere: {hemi}"); season = Season(hemi); Log(f"Season: {season}")
		if (not Loc["latitude"]) or (not Loc["longitude"]) or (Loc["latitude"] in [None, ""]) or (Loc["longitude"] in [None, ""]): Log("Coordinates were not retrieved. The weather will not build."); return None
		Log("Player location and hemisphere set. (This data is NOT being sent anywhere! Check the code for proof.)")
		try: response = requests.get(f"https://wttr.in/{PlayerLocation(ReturnCoords=True)}?format=j1"); Log("Got response from wttr.in.")
		except Exception as e: Log(f"EXCEPTION WHEN ACCESSING WEATHER: {e}")
		try: WeatherD = response.json(); Log("Weather Data parsed successfully.")
		except ValueError: print(f"Weather Data parsing failed.\nResponse: {response.text}"); pause(); return None
		current = WeatherD["current_condition"][0]; Log(f"Weather Description: {current}")
		if ReturnCurrent: return current
		Fahrenheit = int(current.get("temp_F", 0)); Celsius = int(current.get("temp_C", 0))
		TempTypeF = TempFetchFahrenheit(Fahrenheit); TempTypeC = TempFetchCelsius(Celsius); Log("Temperature set successfully.")
		humid = Humidity(current); wind = Wind(current); precip = Precipitation(current, NoLog=Silent); Log("Humidity, wind, and precipitation set successfully.")
		condition = current.get("weatherDesc", [{}])[0].get("value", "").lower()
		if not Silent: Log(f"Weather description: {condition}")
		flags = []
		if "rain" in condition or "storm" in condition and precip != "none": flags.append("rain")
		if "snow" in condition: flags.append("snow")
		if "thunder" in condition: flags.append("thunder")
		if TempTypeF in ["moderate heat", "extreme heat"] or TempTypeC in ["moderate heat", "extreme heat"]: flags.append("sunny")
		if wind != "calm": flags.append("wind")
		Log("Weather JSON is ready to be returned.")
		Weather = {
			"TempF": Fahrenheit, "TempC": Celsius,
			"TempStateF": TempTypeF, "TempStateC": TempTypeC,
			"Humidity": humid, "Rain": precip,
			"Wind": wind, "Season": season,
			"Conditions": flags
		}; Log("Weather built successfully."); return Weather
	except Exception as e:
		if not Silent: print(f"Weather data could not be compiled: {e}\nWeather-based events will not run. Aside from that, the game will operate as normal.\nPress any key to continue."); pause()
		return None