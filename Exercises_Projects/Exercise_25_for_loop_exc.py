import random

def number_1_10():
    for i in range(1, 11):
        print(i)


def number_even_num():
    for i in range(1, 21):
        if i % 2 == 1:
            continue
        else:
            print(i)


def add_numbers():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)


def szorzo_tabla():
    num = int(input("Adj egy számot: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def add_lista():
    list = [3, 7, 2, 9, 4]

    for i in list:
        print(i)
    print(f"A számok összege: {sum(list)}")


def random_number():
    random_number = random.randint(1, 10)
    game = True

    for i in range(1, 4):
        guess = int(input("Tippelj egy számot: "))
        if guess == random_number:
            print("Talált!")
            break
        else:
            print("Nem talált.")
    else:
        print("Sajnálo, elfogyott a lehetőséged! A szám:", random_number)


def duouble_value():
    list = [1, 3, 5, 7, 9]

    for element in list:
        print(element * 2)


def square():
    numbers = [2, 4, 6, 8, 10]

    for element in numbers:
        print(element ** 2)


def generate_index():
    split_text = "python"

    for index, letter in enumerate(split_text):
        print(f"{index + 1}.", letter)


def find_vowels():
    vowels = ["a","e","i","o","u"]

    user_input = input("Adj egy szöveget: ")

    for letter in user_input:
        if letter in vowels:
            print(letter)

if __name__ == '__main__':
    find_vowels()