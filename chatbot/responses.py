# chatbot/responses.py
def get_response(text):
    text = text.lower()
    if "price" in text:
        return "The current price is 10 shillings."
    elif "inventory" in text:
        return "We currently have 150 items in stock."
    else:
        return "I'm still learning. Ask me something else, Keiv."

