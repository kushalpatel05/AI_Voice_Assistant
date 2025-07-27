# Custom modules
from voice import speak
from system_control import processcommand
from aiprocess import aiprocess
from security import password_lock

import speech_recognition as sr      # Recognizes voice input and converts it to text 
import sys                           # Used to exit the program, get system-specific info


# MAIN EXECUTION LOOP
if __name__ == "__main__":
    password_lock()
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)

                # ONly active if "jarvis" is spoken
                if word.lower() == "jarvis":
                    speak("Ya")
                    speak("How may I help you?")

                    while True:
                        try:
                            with sr.Microphone() as source:
                                audio = r.listen(source, timeout=3, phrase_time_limit=5)
                                user_input = r.recognize_google(audio)
                                print("You:", user_input)

                                if "exit" in user_input or "stop" in user_input:
                                    speak("Goodbye.")
                                    sys.exit(0)

                                # Try smart commands firs        
                                result = processcommand(user_input)
                                if result == "break":
                                    continue

                                # Otherwise, use AI response                                            
                                if result is None:
                                    response = aiprocess(user_input)
                                    speak(response)

                        except Exception as e:
                            print("Error:", e)
        except Exception as e:
            print("Error:", e)