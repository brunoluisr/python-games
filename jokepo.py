import random

while True:
    user_choice = input("Choose between: rock, paper, or scissors\n")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a TIE")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win! :)")
        else:
            print("Paper cover rock! You lose. :(")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper cover rock! You win. :)")
        else:
            print("Scissors cut paper! You lose :(")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper. You win!")
        else:
            print("Rock smashes scissors! You lose!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
                    

