import datetime
import random
import string



# Define keyword-response mapping (intent rules)
rules = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
    },

    "help": {
        "keywords": ["help", "assist", "support", "problem"],
        "responses": [
            "I'm here to help. What do you need assistance with?",
            "How can I assist you today?",
            "Sure, tell me your issue."
        ]
    },

    "thanks": {
        "keywords": ["thank", "thanks", "thank you", "appreciate"],
        "responses": ["You're welcome!", "No problem!", "Anytime!", "Glad I could help!"]
    },

    "name": {
        "keywords": ["your name", "who are you"],
        "responses": ["I'm ChatBot, your virtual assistant!", "You can call me ChatBot."]
    },

    "time": {
        "keywords": ["time", "current time", "what time"],
        "responses": [
            f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
        ]
    },

    "date": {
        "keywords": ["date", "today's date", "what date", "todays date"],
        "responses": [
            f"Today's date is {datetime.date.today().strftime('%Y-%m-%d')}"
        ]
    },

    "weather": {
        "keywords": ["weather", "forecast", "rain", "temperature"],
        "responses": [
            "I can't fetch live weather, but I suggest checking a weather app!",
            "Please check weather.com or AccuWeather for updates."
        ]
    }
}



# Fallback/default responses
default_responses = [
    "I'm not sure how to respond to that.",
    "Can you please rephrase?",
    "Hmm, I don't understand. Try asking something else.",
    "Interesting... Can you explain more?"
]



# Function to clean user input
def clean_input(user_input):
    return user_input.lower().translate(
        str.maketrans('', '', string.punctuation)
    )



# Match user input to intent category
def get_intent(user_input):
    cleaned_input = clean_input(user_input)

    for intent, data in rules.items():
        for keyword in data["keywords"]:
            if keyword in cleaned_input:
                return intent

    return None



# Get response based on intent
def get_response(intent):
    if intent:
        return random.choice(rules[intent]["responses"])

    return random.choice(default_responses)



# Main chatbot loop
def chatbot():
    print("ChatBot: Hello! Ask me anything. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break

        intent = get_intent(user_input)
        response = get_response(intent)

        print("ChatBot:", response)



# Run the chatbot
if __name__ == "__main__":
    chatbot()



"""
Output:

ChatBot: Hello! Ask me anything. Type 'exit' to quit.

You: hi
ChatBot: Hey!

You: who are you
ChatBot: I'm ChatBot, your virtual assistant!

You: how are you
ChatBot: Interesting... Can you explain more?

You: todays date
ChatBot: Today's date is 2025-05-30

You: time
ChatBot: The current time is 15:06:30

You: will you help me
ChatBot: How can I assist you today?

You: exit
ChatBot: Goodbye!
"""
