#  map() - fog egy függvényt és egy iterálható dolgot (pl. lista) és végigfuttatja a függvényt minden elemre

def pelda_1():

    # map(function, iterable)

    szamok = [1, 2, 3, 4]

    duplak = map(lambda x: x*2, szamok)
    print(list(duplak))


def pelda_2():

    szavak = ["python", "rocks", "big", "time"]

    hosszak = map(len, szavak)
    print(list(hosszak))


def pelda_3():

    a = [1, 2, 3]
    b = [10, 20, 30]

    osszeg = map(lambda x, y: x + y, a, b)
    print(list(osszeg))


#  GYAKORLÓ


def feladat_1():

    szamok = [3, 6, 9, 12]

    negyzet = map(lambda x: x**2, szamok)
    print(list(negyzet))


def feladat_2():

    diakok = ["Alex", "Bianka", "Charlie"]
    jegyek = [3, 5, 4]

    eredmeny = list(map(lambda x, y: f"{x} -> {y}", diakok, jegyek))
    print(eredmeny)



def feladat_3():

    nevek = ["Alex", "Bianka", "Charlie", "Diana"]

    karakterek = map(len, nevek)
    print(list(karakterek))



def final_boss():

    diakok = ["Alex", "Bianka", "Charlie"]
    matek  = [5, 3, 4]
    tori   = [4, 4, 5]
    info   = [5, 5, 3]

    jegyek_list = list(zip(matek, tori, info))
    
    for index, (diak, jegyek) in enumerate(zip(diakok, jegyek_list), start=1):
        atlag = list(map(lambda x: round(sum(x)/len(x), 2), [jegyek]))
        print(f"{index} - {diak}: jegyek={list(jegyek)}, átlag={atlag}")

final_boss()