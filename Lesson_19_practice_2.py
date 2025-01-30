# Python ROCK - PAPER - SCISSORS

import random

choices = ("rock", "paper", "scissors")
playing = True

while playing:

    computer = random.choice(choices)
    player = None

    while player not in choices:    # this section just says that the player's choice has to align with the options in the options list
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    
    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing")