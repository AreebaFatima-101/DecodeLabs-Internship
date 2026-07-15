# ==========================================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Artificial Intelligence Internship
# Author: Areeba Fatima
# ==========================================================

from datetime import datetime


# ------------------------------
# Display Project Title
# ------------------------------
def display_title():
    print("=" * 60)
    print("               RULE-BASED AI CHATBOT")
    print("=" * 60)
    print("DecodeLabs Artificial Intelligence Internship")
    print("=" * 60)
    print()


# ------------------------------
# Display Help Menu
# ------------------------------
def show_help():
    print("\nAvailable Commands")
    print("-" * 60)
    print("hello")
    print("hi")
    print("hey")
    print("good morning")
    print("good afternoon")
    print("good evening")
    print("how are you")
    print("what is your name")
    print("who created you")
    print("what can you do")
    print("what is ai")
    print("tell me a joke")
    print("motivate me")
    print("tell me a fact")
    print("time")
    print("date")
    print("thank you")
    print("help")
    print("bye")
    print("-" * 60)


# ------------------------------
# Main Program
# ------------------------------
display_title()

name = input("Bot : Hello! What's your name?\nYou : ")

print(f"\nBot : Nice to meet you, {name}!")
print("Bot : Type 'help' to see all available commands.\n")

message_count = 0

while True:

    user = input(f"{name} : ").strip().lower()
    message_count += 1

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print(f"Bot : Hello {name}! Hope you're having a great day.")

    elif user == "good morning":
        print("Bot : Good morning! Have a wonderful day ahead.")

    elif user == "good afternoon":
        print("Bot : Good afternoon! Keep smiling.")

    elif user == "good evening":
        print("Bot : Good evening! Hope your day went well.")

    # Basic Questions
    elif user == "how are you":
        print("Bot : I'm doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot : My name is RuleBot.")

    elif user == "who created you":
        print("Bot : I was created by Areeba Fatima as part of an AI internship project.")

    elif user == "what can you do":
        print("Bot : I can answer simple questions using predefined rules.")

    elif user == "what is ai":
        print("Bot : Artificial Intelligence enables computers to perform tasks that usually require human intelligence.")

    # Fun Commands
    elif user == "tell me a joke":
        print("Bot : Why do programmers prefer dark mode?")
        print("Bot : Because light attracts bugs!")

    elif user == "motivate me":
        print("Bot : Success comes from learning, consistency, and hard work.")

    elif user == "tell me a fact":
        print("Bot : Honey never spoils. Archaeologists have found edible honey in ancient tombs!")

    # Date & Time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot : Current Time:", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's Date:", current_date)

    # Polite Conversation
    elif user == "thank you":
        print(f"Bot : You're welcome, {name}! Happy to help.")

    elif user == "help":
        show_help()

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("\n" + "=" * 60)
        print(f"Bot : Goodbye, {name}!")
        print(f"Bot : Total Messages Exchanged : {message_count}")
        print("Bot : Thank you for chatting with me.")
        print("Bot : Have a wonderful day!")
        print("=" * 60)
        break

    # Unknown Command
    else:
        print("Bot : Sorry, I didn't understand that.")
        print("Bot : Type 'help' to see the available commands.")