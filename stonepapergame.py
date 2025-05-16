import random
import time

# List of possible choices
choices = ["scissor", "stone", "paper"]

# Ask the user for their name
name = input("Please enter your name: ")

# Predefined sarcastic winner and loser messages
winner = [
    "Don’t get cocky. Even a broken clock is right twice a day.",
    "Thanks for participating. Enjoy your consolation prize — silence.",
    "Let me know when you finally win something. I’ll pretend to be surprised."
]

looser = [
    "Maybe gaming’s not for you. Try something easier... like breathing. 😬",
    "Once a loser, always a loser. Accept it. Embrace it. Live it. 💩",
    "This isn't just a loss — it's a career-ending performance."
]

# Initialize win counters
computer_win = 0
user_win = 0


# Function to simulate computer thinking delay
def sleep_time():
    print("Computer is Thinking.....")
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)


# Function to display the current scorecard
def scorecard():
    print("#### CURRENT SCORECARD  ######")
    print(f"""{name} = {user_win} 
computer = {computer_win}
###############################
""")


# Function to show the result of each round
def show_result(winner):
    gap()
    if winner == "tie":
        print("IT'S A TIE ")
    elif winner == "computer":
        print("Computer wins...")
    elif winner == "user":
        print("Hurray You Win...*******")
    gap2()


# Function to display choices and spacing after countdown
def gap():
    sleep_time()
    print()
    print()
    print(f"Computer choice : {computer_choice}")
    print()
    print()


# Function to add spacing and show the scorecard
def gap2():
    print()
    print()
    scorecard()


# Function to get user input and return corresponding choice
def player_choice():
    choice = ""
    user_choice = int(input(f"Hey {name}, it's your turn:  \n\t 1. Stone \n\t 2. Paper \n\t 3. Scissor\nPlease enter your choice: "))
    if user_choice == 1:
        choice = "stone"
    elif user_choice == 2:
        choice = "paper"
    elif user_choice == 3:
        choice = "scissor"
    return choice


# Main game loop
while True:
    if computer_win >= 2 or user_win >= 2:
        break

    # Randomly select the computer's choice
    computer_choice = random.choice(choices)

    # Get user's choice
    user_choice = player_choice()

    # Validate user input
    if user_choice not in choices:
        print("Invalid input..")
        continue
    else:
        # Check for tie
        if user_choice == computer_choice:
            show_result("tie")
            continue

        # Check if computer wins
        elif (user_choice == "scissor" and computer_choice == "stone") or \
             (user_choice == "paper" and computer_choice == "scissor") or \
             (user_choice == "stone" and computer_choice == "paper"):
            computer_win += 1
            show_result("computer")
            continue

        # Otherwise, user wins
        else:
            user_win += 1
            show_result("user")
            continue


# Final result announcement
if computer_win > user_win:
    print(random.choice(looser))
    print()
    print()

elif user_win > computer_win:
    print(random.choice(winner))
    print()
    print()
