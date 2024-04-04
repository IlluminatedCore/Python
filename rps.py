import random
import sys

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)

#user_choice = input("Pick your choice between Rock, Papper or Scissors: ").lower()

while True:
    user_choice = input("Pick your choice between Rock, Papper or Scissors: ").lower()
    if user_choice  in choices:
        break
    else:
        sys.exit("pick a valid choice")

print(f"computer choice is {computer_choice}")

if user_choice == computer_choice:
    print("play again!🤝")
elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" \
    and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
    print("Yayy, user won🏆")
elif user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissors" or \
    user_choice == "scissors" and computer_choice == "rock":
    print("lol computer won!😵‍💫")
sys.exit("Bye")


    

    