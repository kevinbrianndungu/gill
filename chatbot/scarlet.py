from chatbot.responses import get_response
from chatbot.tts import speak
from chatbot.stt import listen  # Optional, replace input() for voice mode

# Wake/Kill phrase control
WAKE_PHRASES = ["keiali", "keiali are you there", "hey keiali"]
KILL_PHRASES = ["thank you keiali", "you can stop now", "bye keiali"]

active = False

def handle_command(user_input):
    """Handle activation and routing logic for Keiali."""
    global active
    lower_input = user_input.lower()

    if any(phrase in lower_input for phrase in WAKE_PHRASES):
        active = True
        return "Yes Keiv, I’m here."

    if any(phrase in lower_input for phrase in KILL_PHRASES):
        active = False
        return "Standing down. Say 'Keiali' when you need me again."

    if active:
        return get_response(user_input)

    return None  # No response if not activated

def start_scarlet(use_voice=False):
    """Main loop to run Keiali in either text or voice mode."""
    print("Keiali is listening... (type 'exit' to quit)")

    while True:
        user_input = listen() if use_voice else input("You: ")

        if user_input.lower() in ("exit", "quit"):
            speak("Goodbye, Keiv.")
            break

        response = handle_command(user_input)

        if response:
            print(f"Keiali: {response}")
            speak(response)

