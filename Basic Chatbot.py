# Basic Chatbot Program

print("🤖 Hello! I am a Simple Chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi dear!")

    elif user_input == "how are you":
        print("Bot: I'm fine , thanks!")

    elif user_input == "what is your name":
        print("Bot: I am a Python Chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
