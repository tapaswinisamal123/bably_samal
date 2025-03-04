import random

def chatbot():
    print("Hello! I'm your chatbot. Ask me anything or type 'exit' to end the chat.")
    
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "your name": "I'm a chatbot created using Python.",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure about that. Can you ask something else?"
    }
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = responses.get(user_input, responses["default"])
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()