# chatbot/scarlet.py
from chatbot.responses import get_response
from chatbot.tts import speak
from chatbot.stt import listen  # Optional

def start_scarlet():
    while True:
        user_input = input("You: ")  # Replace with `listen()` for voice input
        if user_input.lower() in ("exit", "quit", "bye"):
            speak("Goodbye, Keiv.")
            break
        response = get_response(user_input)
        print(f"Scarlet: {response}")
        speak(response)

