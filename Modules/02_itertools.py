from itertools import product, combinations

def feladat1():
    csapatok = ["Fradi", "Újpest", "MTK", "Honvéd"]

    meccsekszama = 0
    for hazai, vendeg in product(csapatok, csapatok):
        if hazai != vendeg:
            print(f"{hazai} - {vendeg}")
            meccsekszama += 1

    print(meccsekszama)

def feladat2():
    jatekosok = ["Anna", "Béla", "Csilla", "Dani"]

    validcsapat = 0

    for jatekos in combinations(jatekosok, 2):
        validcsapat += 1
        print(jatekos)

    print(f"Lehetséges csapat: {validcsapat}")

feladat2()