import random
import sys
import argparse

def greeting(name):
    print(f"Hello {name}, Let's play the game\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Give out the name"
    )

    parser.add_argument("-n", "--name", required=True, help="Give out the username")
    args = parser.parse_args()
    greeting(args.name)

    computer_choice = random.choice("123")

    def mynum():
        game_count = 0
        user_wins = 0
        system_wins = 0

        def guess():
            nonlocal game_count
            nonlocal user_wins
            nonlocal system_wins

            user_choice = input(f"Pick the number I am thinking from 1 2 and 3 \n")
            if user_choice not in ["1", "2", "3"]:
                guess()

            print(f"{args.name} you chose {user_choice}")

            print(f"I was thinking about: {computer_choice}")
            nonlocal game_count
            game_count += 1

            if user_choice == computer_choice:
                user_wins += 1
                print(f"{args.name}, you win 🏆")
            elif user_choice != computer_choice:
                system_wins += 1
                print("Sorry try next time!\n")

            print(f"Total game counts: {game_count}\n")
            print(f"user wins: {user_wins}\n")

            percentage = user_wins*100/game_count 

            print(f"system wins: {system_wins}, Your winning percentage is: {percentage}%\n")

            answer = input("Do you want to play again? (y/q)\n")
            if answer.lower() == "y":
                print("Lets Go!")
                guess()
            elif answer.lower() == "q":
                sys.exit("Thanks for playing")
            else:
                print("Invalid input. Please enter 'y' to play again or 'q' to quit.")
        
        guess()
    mynum()
