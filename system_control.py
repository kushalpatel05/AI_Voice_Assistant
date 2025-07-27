# User defined module
from voice import speak, listen
from weather import get_weather         

# Different modules
import os                # Used to execute system-level commands like shutdown, restart
import sys               # Used to exit the program, get system-specific info
import subprocess        # Helps to open external software like Notepad, Word
import re                # Regular Expressions - used for pattern matching in strings
import webbrowser        # Opens websites in your default browser
import pyautogui         # Used to control the keyboard/mouse (media controls)
import screen_brightness_control as sbc         # For brightness control
import requests                                 # Used for API calls (weather, news)

# Volume control using pycaw (Windows only)
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # For controlling volume
from ctypes import cast, POINTER          # Required for COM interaction
import comtypes                          # Required by pycaw

# Date and Time
from datetime import datetime            # Get current system time
import pytz                              # Handle timezone (IST)


# Get current IST date and time
def get_current_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    return current_time.strftime("%B %d, %Y, %I:%M %p")  # Example: July 22, 2025, 02:30 PM

# Handle all kinds of commands in one function 
def processcommand(c):
    c = c.lower()

    # Volume Control
    if "volume up" in c or "volume down" in c:
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            current = volume.GetMasterVolumeLevelScalar()
            change = 0.1 if "up" in c else -0.1
            volume.SetMasterVolumeLevelScalar(max(0.0, min(current + change, 1.0)), None)
            speak(f"Volume {'increased' if change > 0 else 'decreased'}.")
        except:
            speak("Sorry, I couldn't control the volume.")
        return "break"

    # Brightness Control
    if "brightness high" in c or "brightness low" in c:
        try:
            current = sbc.get_brightness()[0]
            change = 10 if "high" in c else -10
            sbc.set_brightness(max(0, min(current + change, 100)))
            speak(f"Brightness {'increased' if change > 0 else 'decreased'}.")
        except:
            speak("Sorry, I couldn't control the brightness.")
        return "break"

    # System Commands
    sys_commands = {
        "shutdown": ("Shutting down the computer.", "shutdown /s /t 1"),
        "restart": ("Restarting the computer.", "shutdown /r /t 1"),
        "logout": ("Logging out.", "shutdown /l"),
        "sleep": ("Putting the computer to sleep.", "rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    }
    for key, (msg, cmd) in sys_commands.items():
        if key in c:
            speak(msg)
            os.system(cmd)       # Execute system-level command
            sys.exit(0)          # Exit the program after execution

    # App Launcher
    apps = {
        "notepad": "notepad.exe",
        "vs code": r"C:\Users\KUSHAL\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        "paint": "mspaint.exe",
        "settings": "start ms-settings:"
    }
    for app, path in apps.items():
        if f"start {app}" in c:
            speak(f"Opening {app.capitalize()}.")
            subprocess.Popen(path, shell=(app == "settings"))      # Use shell=True only for settings
            return "break"

    # Music Control using media keys(Youtube Music or other platforms)
    if "play music" in c or "pause music" in c:
        pyautogui.press("playpause")
        speak("Music paused.")
        return "break"
    if "next song" in c:
        pyautogui.press("nexttrack")
        speak("Playing next song.")
        return "break"
    if "previous song" in c:
        pyautogui.press("prevtrack")
        speak("Playing previous song.")
        return "break"

    # Open Websites
    websites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "linkedin": "https://linkedin.com",
        "hotstar": "https://hotstar.com",
        "chrome": "https://chrome.com"
    }
    if c.startswith("open"):
        site = c.replace("open", "").strip()   # Extract Website name
        if site in websites:
            speak(f"Opening {site}.")
            webbrowser.open(websites[site])    # Launch browser with URL
        else:
            speak("Sorry, I don't have that website in my library.")
        return "break"

    # Search music on YouTube Music
    if "play" in c and "youtube music" in c:
        song = c.replace("play", "").replace("on youtube music", "").strip()        # Extract song name
        if song:
            speak(f"Playing {song} on YouTube Music.")
            url = f"https://music.youtube.com/search?q={song.replace(' ', '+')}"    # From search URL
            webbrowser.open(url)
        else:
            speak("Please specify the song name to play on YouTube Music.")
        return "break"

    # Get current Time and Date
    if "time" in c or "date" in c:
        current_time = get_current_ist_time()      # Get current time in IST
        speak(f"The current date and time is {current_time}")
        return "break"

    # News
    if "news" in c:
        newsapi = "2639d05cab4e465daab6bddde129d5a1"    # News API key
        speak("Getting the latest top news.")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            for article in data.get('articles', [])[:3]:     # Read top 3 headlines
                speak(article['title'])
        return "break"

    # Weather
    if "weather" in c:
        match = re.search(r"weather in ([a-zA-Z ]+)", c)      # Extract city from command
        if match:
            city = match.group(1).strip()
            get_weather(city)    # Fetch weather using city
        else:
            speak("Which city's weather would you like to check?")
            city = listen()   # Ask user to say the city name
            get_weather(city)
        return "break"