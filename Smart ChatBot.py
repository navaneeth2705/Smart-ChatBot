import random
import wikipedia
import time


def bot_type(text):
    """"Typing animmation for bot"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

print("="*45)
bot_type("Smart Campus Companion Bot")
bot_type("Type 'exit' to end the chat")
print("="*45)


name = input("Bot: What is your name? \nYou: ")

print(f"Bot: Nice to meet you, {name}! How are you feeling today?")

while True:
    user_input = input(f"{name}: ").lower()

    # Exit
    if user_input == "exit":
        print(f"Bot: Goodbye {name}! Take care")
        break

    # Mood detection

    elif "happy" in user_input or "good" in user_input or "great" in user_input:
        responses = [
            "That's wonderful to hear!!",
                ]
        print("Bot:", random.choice(responses))

    elif "internship" in user_input:
        print("Bot: Internships help you gain real-world experience. Start with small projects and apply early")

    elif "motivate me" in user_input:
        print("Bot: You’re doing better than you think. Keep going, one step at a time")

    elif "exam fear" in user_input:
        print("Bot: Exams can be stressful. Make a simple timetable and revise daily ")

    elif "project" in user_input:
        print("Bot: Projects improve your resume. This chatbot itself is a great start ")

    elif "I am sad" in user_input or "tired" in user_input or "bad" in user_input:
        responses = [
            "Take a deep breath. Things will get better "
                ]

    # College info
    elif "course" in user_input:
        print("Bot: Available courses are BCA, BSc, and BCom.")

    elif "timing" in user_input:
        print("Bot: College timing is from 9:00 AM to 4:00 PM.")

    elif "help" in user_input:
        print("Bot: I can help you with mood support, college info, and general chat.")

    else:
        try:
            summary = wikipedia.summary(user_input, sentences=2)
            print("Bot:", summary)
        except wikipedia.exceptions.DisambiguationError:
            print("Bot: Please be more specific.")
        except wikipedia.exceptions.PageError:
            print("Bot: I couldn’t find information on that.")
        except:
            print("Bot: Something went wrong. Try again.")



