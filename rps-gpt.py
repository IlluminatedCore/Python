import random
import sys

choices = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Pick your choice between Rock, Paper, or Scissors: ").lower()
    if user_choice in choices:
        break
    else:
        print("Pick a valid choice")

print(f"Computer choice is {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations! You won!")
else:
    print("Sorry, computer won!")

play_again = input("Do you want to play again (yes/no)? ").lower()
if play_again != "yes":
    print("Hope you enjoyed")
    sys.exit()
