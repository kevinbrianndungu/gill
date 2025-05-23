# chatbot/scarlet.py

from chatbot.responses import get_response
from chatbot.tts import speak
from utils.analytics import generate_summary_metrics
from utils.reporter import keiali_response
import json

WAKE_PHRASES = ["keiali", "keiali are you there", "hey keiali"]
KILL_PHRASES = ["thank you keiali", "you can stop now", "bye keiali"]

active = False

def load_mock_transactions():
    with open("data/mock_transactions.json", "r") as f:
        return json.load(f)

def load_mock_customers():
    with open("data/mock_customers.json", "r") as f:
        return json.load(f)

def handle_voice_command(user_input):
    global active

    lower_input = user_input.lower()

    if any(wake in lower_input for wake in WAKE_PHRASES):
        active = True
        return "Yes Keiv, I’m here."
    
    if any(kill in lower_input for kill in KILL_PHRASES):
        active = False
        return "Standing down. Say 'Keiali' when you need me again."

    if active:
        if "how are sales" in lower_input:
            transactions = load_mock_transactions()
            customers = load_mock_customers()
            metrics = generate_summary_metrics(transactions, customers)
            return keiali_response(metrics)
        return get_response(user_input)
    else:
        return None

def start_scarlet():
    while True:
        user_input = input("You: ")
        response = handle_voice_command(user_input)
        if response:
            print(f"Keiali: {response}")
            speak(response)
        if user_input.lower() in ("exit", "quit", "bye"):
            speak("Goodbye, Keiv.")
            break

