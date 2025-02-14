import random

print("Szókirakó játék")
print("*******************************************")
print("Szabályok: ")
print("- Csak annyit kell tenned, hogy kitalálod, melyik szó") 
print("van megjelenítve a képernyőn.")
print("- Minden helyes találat egy pontot ér.")
print("- A sikeres teljesítéshez 70%-ot kell elérned.")
print("*******************************************")

def load_words():
    return [
    "alma", "körte", "szilva", "eper", "málna", "programozás", "python", "kód", "lista", "szótár", "függvény", "változó", "ciklus", "string", "számológép", "adatbázis", "számítógép", "internet", "szerver", "algoritmus", "hibakeresés", "fejlesztés",
    "optimalizálás", "különbség", "számolás", "megoldás", "felhasználó", "hardver", "szoftver", "elágazás", "modul", "parancs", "karakterlánc", "hálózat", "kapcsolat", "adat", "folyamat", "konstans", "válasz", "kiértékelés", "véletlen", "generátor",
    "gyakorlás", "kihívás", "érdekes", "feladat", "megértés", "tanulás", "játék", "kihívó", "logika", "szabály"
]


def get_random_word(words):
    return random.choice(words)

def display_word(words):
    
    word = get_random_word(words)
    shuffled_letters = list(word)
    random.shuffle(shuffled_letters)
    task = "".join(shuffled_letters)

    user_answer = input(f"Melyik szó lehet eredetileg a {task}? ").strip().lower()
    return user_answer, word

def check_answer(user_answer, word):
    return user_answer == word

def main():
    words = load_words()
    points = 0

    for _ in range(10):
        user_answer, original_word = display_word(words)

        if check_answer(user_answer, original_word):
            points += 1
            print("Helyes! Szereztél egy pontot!")
        else:
            print(f"Nem talált! A helyes válasz: {original_word}")

    total_questions = 10
    passing_score = total_questions * 0.70
    print(f"A játék véget ért! Az összpontszámod: {points}/{total_questions}.")

    if points >= passing_score:
        print("Gratulálok! Sikeresen teljesítetted a kvízt! 🎉")
    else:
        print("Sajnos nem érted el a szükséges pontszámot. Próbáld újra!")
    

if __name__ == "__main__":
    main()