import random

print("Üdv a számkitalálós játékban!")
print("*******************************************")
print("A szabályok:")
print("- A számítógép véletlenszerűen kiválaszt egy számot egy adott tartományban.")
print("- Neked ki kell találnod ezt a számot.")
print("- Minden tipp után megmondjuk, hogy a szám túl magas vagy túl alacsony.")
print("- Összesen 7 próbálkozásod van, hogy eltaláld.")
print("- Ha eltalálod, nyersz! Ha nem, a számítógép felfedi a választ.")
print("*******************************************")



def random_number():
    return random.randint(1, 100)

def get_user_input():
    while True:
        try:
            guess = int(input("Tippelj egy számra 1 és 100 között: "))
            return guess
        except ValueError:
            print("Kérlek, egy számot adj meg")

def check_answer(target, guess):
    if guess < target:
        return "low"
    elif guess > target:
        return "high"
    else:
        return "correct"

def main():
    target = random_number()
    attempts = 0

    while True:
        guess = get_user_input()
        attempts += 1

        result = check_answer(target, guess)

        if result == "low":
            print("A tipped túl alacsony!")
        elif result == "high":
            print("A tipped túl magas!")
        else:
            print(f"Gratulálok! Eltaláltad a számot {attempts} próbálkozás után.")
            break


if __name__ == '__main__':
    main()