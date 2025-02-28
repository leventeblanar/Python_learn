import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def  guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        if any(color not in COLORS for color in guess):
            print("Invalid colors detected. Try again!")
            continue

        return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        color_counts[color] = color_counts.get(color, 0) + 1

    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            color_counts[guess[i]] -= 1

    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
            incorrect_pos += 1
            color_counts[guess[i]] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)


    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()