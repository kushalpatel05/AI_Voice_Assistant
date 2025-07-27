import pyttsx3                        # Converts text into speech (offline TTS)
import speech_recognition as sr       # Recognizes voice input and converts it to text

engine = pyttsx3.init()         # Initialize TTS engine
recognizer = sr.Recognizer()    # Initialize recognizer


def speak(text):
    print("Jarvis:", text)
    engine.say(text)            # Convert text to speech
    engine.runAndWait()         # Play the speech
    print()

# Listen to Microphone Input and convert speech to text 
def listen():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)     