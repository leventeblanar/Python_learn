import random

def count_while():

    szam = 1

    while szam <= 10:
        print(szam)
        szam += 1


def jelszo_csekk():

    jelszo = "python123"
    user_input = ""
    attempts = 0

    while user_input != jelszo:
        user_input = input("Adja meg a jelszót: ")
        if user_input != jelszo:
            attempts += 1
            print("Hibás jelszó, próbálja meg újra.")
            print(f"Még {3-attempts} próbálkozása maradt.")
            if attempts == 3:
                break

    if attempts == 3:
        print("Fiók letiltva.")
    else:
        print("Sikeres bejelentkezés.")

def number_guess():

    print("A csodálatos szám kitalálós játék.")

    random_num = random.randrange(1,10)
    guess = 0
    attempt = 0
    game = True

    while game:
        guess = int(input("Tippeljen egy számra: "))
        if guess == random_num:
            attempt +=1
            print(f"Sikerült. A szám tényleg {random_num}")
            print(f"Tippek száma: {attempt}")
            game = False
        elif guess < random_num:
            attempt +=1
            print(f"Túl alacsony tipp.") 
        elif guess > random_num:
            attempt +=1
            print(f"Túl magas tipp.")

def akasztofa():

    szavak = ['alma', 'körte', 'cseresznye', 'varjú', 'autó', 'szekerce', 'kalapács', 'borjú', 'vitamin', 'kaland', 'szekér', 'sorompó',]
    random_szo = random.choice(szavak)
    talalatok = ["_"] * len(random_szo)
    attempts = 0

    print("Akasztófa játék.")
    print(f"A szó {len(random_szo)} karakterből áll.")
    print(" ".join(talalatok))

    while "_" in talalatok:
        attempts += 1
        tipp = str(input("Tippeljen egy betűt: "))
        for index, karakter in enumerate(random_szo):
            if karakter == tipp:
                talalatok[index] = tipp
        print(" ".join(talalatok))

    print("Gratulálok, kitaláltad!")
    print(f"Tippek száma: {attempts}")


akasztofa()