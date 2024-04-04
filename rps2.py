import random
import sys

choices = ["rock", "paper", "scissors"]



#user_choice = input("Pick your choice between Rock, Papper or Scissors: ").lower()

#Play_again = True

while True:
    user_choice = input("Pick your choice between Rock, Papper or Scissors: ").lower()
    

    if user_choice not in choices:
        continue

    computer_choice = random.choice(choices)

    print(f"computer choice is {computer_choice}")

    if user_choice == computer_choice:
        print("Its a tie!🤝")
    elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" \
        and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
        print("Yayy, user won🏆")
    elif user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissors" or \
        user_choice == "scissors" and computer_choice == "rock":
        print("lol computer won!😵‍💫")
    
    Play_again = input("Do you want to play again?(Y/N)\n")
    if Play_again.lower() != "y":
        break

sys.exit("Thanks for Playing!❤️")