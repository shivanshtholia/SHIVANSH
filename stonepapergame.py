import random
import time

choices=["scissor","stone","paper"]
name=input("Please enter ur name : ")

winner=["Don’t get cocky . Even a broken clock is right twice a day.",
        "Thanks for participating. Enjoy your consolation prize — silence.",
        "Let me know when you finally win something. I’ll pretend to be surprised."]


looser=["Maybe gaming’s not for you. Try something easier... like breathing. 😬",
        "Once a loser, always a loser. Accept it. Embrace it. Live it. 💩",
        " This isn't just a loss — it's a career-ending performance."]


computer_win=0
user_win=0


def sleep_time():
    print("Computer is Thinking.....")
    for i in range (3,0,-1):
     time.sleep(1)
     print(i)


def scorecard():
    print("#### CURRENT SCORECARD  ######")
    print(f"""{name} = {user_win} 
computer = {computer_win}
###############################
""")


def show_result(winner):
    gap()
    if winner == "tie":
        print("IT'S A TIE ")
    elif winner == "computer":
        print("Computer wins...")
    elif winner == "user":
        print("Hurray You Win...*******")
    gap2()


def gap():
    sleep_time()
    print()
    print()
    print(f"Computer choice : {computer_choice}")
    print()
    print()

def gap2():
    print()
    print()
    scorecard()

def player_choice():
    choice=""
    user_choice=int(input(f"Hey {name}, its your turn:  \n\t 1. Stone \n\t 2. Paper \n\t 3. Scissor\n Please enter your choice:  "))
    if user_choice==1:
        choice="stone"
    elif user_choice==2:
        choice="paper"
    elif user_choice==3:
        choice="scissor"
    return choice


while True:
    if computer_win>=2 or user_win>=2:
        break
    computer_choice=random.choice(["scissor","stone","paper"])
    user_choice=player_choice()

    if user_choice not in choices:
        print("invalid input..")
        continue
    else:
        if user_choice==computer_choice:
            show_result("tie")
            continue
        elif (user_choice=="scissor" and computer_choice=="stone") or (user_choice=="paper" and computer_choice=="scissor") or user_choice=="stone" and computer_choice=="paper":
            computer_win+=1
            show_result("computer")
            continue
        else :
           user_win+=1
           show_result("user")
           continue
if computer_win>user_win:
    print(random.choice(looser))
    print()
    print()
elif user_win>computer_win:
    print(random.choice(winner))
    print()
    print()


