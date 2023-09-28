import random
import time

def respond(message) -> str:
    ms = message.lower()
    if ms == "hi" or ms == "hello":
        return "Hey there! I am Optimus. How can I help you?"
    
    elif ms == "how are you?" or ms == "how are you doing?":
        return "I'm fine, thanks for asking!"
    
    elif ms == "what is your name?" or ms == "what's your name?":
        return f'My name is Optimus.'
    
    elif ms == "what is your age?" or ms == "what's your age?" or ms == "how old are you?":
        return 'I was created in 2023'

    elif ms == "diceroll":
        return str(random.randint(1, 6))
    
    elif ms == "coinflip":
        return random.choice(["Heads", "Tails"])
    
    elif ms == "what is the time" or ms == "what's the time" or ms == "what time is it?" or ms == "time":
        return time.strftime("%H:%M:%S")
    
    elif ms == "rickroll":
        return "https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713"
    
    elif ms == "help":
        return "```I can do the following:\n1. hi: Greet you\n2. diceroll: Roll a dice -> diceroll\n3. coinflip: Flip a coin\n4. time: Tell you the time\n5. rickroll: Never gonna give you up!\n6. Tell you my name\n7. Tell you my age\n8. Tell you how I am doing 9. weather 'city': Tell you how is the weather ```"

    else:
        return ""
