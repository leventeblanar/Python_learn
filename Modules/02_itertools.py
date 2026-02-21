from itertools import product

def feladat1():
    csapatok = ["Fradi", "Újpest", "MTK", "Honvéd"]

    meccsekszama = 0
    for hazai, vendeg in product(csapatok, csapatok):
        if hazai != vendeg:
            print(f"{hazai} - {vendeg}")
            meccsekszama += 1

    print(meccsekszama)

feladat1()