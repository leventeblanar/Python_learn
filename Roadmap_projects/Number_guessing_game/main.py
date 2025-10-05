import random
from rich import print

print("***** Random Number Guessing game *****")
print("Rules: ")
print("- You get a random number")
print("- Your job is to guess it in 10 tries\n")

def play_game():
    random_num = int(random.randrange(1, 100))
    num_guess = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            num_guess += 1
            if user_guess > random_num:
                print("Too High!") 
            elif user_guess < random_num:
                print("Too low!")
            elif user_guess == random_num:
                print(f"YOU WON! It only took you {num_guess} attempts to get it!")
                break

            elif num_guess == 10:
                    print("Sorry, you lost!")
                    break
                    
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing!")
        break


    
