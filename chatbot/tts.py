# chatbot/tts.py

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Speed percent
engine.setProperty('volume', 0.9)  # Volume 0-1

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

