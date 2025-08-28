# zip() - egyszerre több listátjárunk be - összecsatoljuk őket és az elemek sorrendje szerint megyünk

def pelda_1():
    nevek = ["Anna", "Béla", "Csaba"]
    korok = [25, 30, 22]

    for nev, kor in zip(nevek, korok):
        print(f"{nev} {kor} éves.")


def pelda_2():

    print(list(zip([1,2,3], ["a", "b"])))


def pelda_3():
    nevek = ["Anna", "Béla", "Csaba"]
    korok = [25, 30, 22]

    for i, (nev, kor) in enumerate(zip(nevek, korok)):
        print(f"{i}. {nev} - {kor} év")



#  GYAKORLÓ


def feladat_1():

    diakok = ["Alex", "Bianka", "Charlie", "Diana"]
    jegyek = [5, 4, 3, 5]

    for diak, jegy in zip(diakok, jegyek):
        print(f"{diak}: {jegy }")



def feladat_2():

    import statistics

    diakok = ["Alex", "Bianka", "Charlie", "Diana"]
    matek = [5, 4, 3, 2]
    tori  = [4, 5, 4, 3]
    info  = [5, 5, 5, 4]

    tantargyak = ["matek", "tori", "info"]
    jegyek_list = list(zip(matek, tori, info))

    

    for diak, jegyek in zip(diakok, jegyek_list):
        atlag = round(statistics.mean(jegyek), 2)
        max_index = jegyek.index(max(jegyek))
        legjobb_targy = tantargyak[max_index]
        legjobb_jegy = max(jegyek)
        print(f"{diak} -> {list(jegyek)}, átlag: {atlag}")
        print(f"legjobb: {legjobb_targy}({legjobb_jegy})")

def feladat_3():

    futok = ["Alex", "Bianka", "Charlie", "Diana"]
    idok  = [15.2, 14.8, 16.5, 14.8]

    for futo, ido in zip(futok, idok):
        print(f"{futo}: {ido}")

    legjobb_ido = min(idok)
    min_index = idok.index(min(idok))
    legjobb_futo = [f for f,i in zip(futok, idok) if i == legjobb_ido]

    print(f"A legjobb időt futotta: {legjobb_futo} - {legjobb_ido}")



def zip_gyakorlas():

    diakok = ["Alex", "Bianka", "Charlie", "Diana"]
    jegyek = [5, 4, 3, 5]

    for diak, jegy in zip(diakok, jegyek):
        print(f"{diak} -> {jegy}")

zip_gyakorlas()