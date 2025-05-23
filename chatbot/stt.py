# chatbot/stt.py

import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def listen() -> str:
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech service is unavailable right now."

