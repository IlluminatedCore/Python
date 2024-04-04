import random
import sys

# def greeting(name='Player One'):
#     print(f"{name} Choose the arcade game")
# greeting('Manideep')


def play_game(name='Player One'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game(name)
        
        welcome_back = True

        if playerchoice == "1":
            print("rps")
        elif playerchoice == "2":
            print("gmn")
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")
     
play_game('Manideep')