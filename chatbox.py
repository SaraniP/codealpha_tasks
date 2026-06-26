print("🤖 Welcome to CodeAlpha Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: I am CodeAlpha Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")