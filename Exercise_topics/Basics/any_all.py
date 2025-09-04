#  any() and all() - are two built-in functions provided in Python used for successive AND/OR. 
#  Any() - return true if any of the items is True and returns False if empty or all are f = open('myfile.txt', 'w')
#  All() - returns true if all of the items are True


def example_any_1():

    print(any([False, False, False, False, False]))
    print(any([True, False, False, False, False]))
    print(any([False, False, True, False, False]))


def example_any_2():

    list1 = []
    list2 = []

    for i in range(1, 11):
        list1.append(4*i)
    
    for i in range(0,10):
        list2.append(list1[i]%5==0)
    
    print('See whether at least on number is divisible by 5 in list 1=>')
    print(any(list2))


def example_all_1():

    print(all([True, True, True, True, True]))
    print(all([True, False, False, False, False]))
    print(all([False, False, True, False, False]))


def example_all_2():

    list1 = []
    list2 = []

    for i in range(1, 21):
        list1.append(4*i-3)
    
    for i in range(0,20):
        list2.append(list1[i]%2==1)
    
    print('See whether all numbers in list1 are odd =>')
    print(all(list2))


#  ---------- Gyakorlós ----------

def feladat_1():

    projektek = [
    ["done", "done", "done"],
    ["done", "in_progress", "done"],
    ["todo", "todo", "todo"],
    ]

    for index, projekt in enumerate(projektek, start=1):
        if all(x == "done" for x in projekt) == True:
            print(f"Projekt {index}: Kész")
        elif any(x == "in_progress" for x in projekt) == True:
            print(f"Projekt {index}: Folyamatban")
        else:
            print(f"Projekt {index}: Nincs elkezdve")


def feladat_2():

    szamok = [3, -5, 7, 10, -2, 0]

    if all(szam > 0 for szam in szamok):
        print("Minden pozitív")
    if any(szam < 0 for szam in szamok):
        print("Van negatív")
    if any(szam == 0 for szam in szamok):
        print("Van nulla")
    if not all(szam > 0 for szam in szamok) and not any(szam < 0 for szam in szamok) and not any(szam == 0 for szam in szamok):
        print("Vegyes lista")


def feladat_3():

    diakok = {
    "Alex": [3, 4, 5],
    "Bianka": [2, 2, 3],
    "Charlie": [5, 5, 5],
    "Diana": [3, 0, 4],
    }

    for nev, jegyek in diakok.items():
        if all(jegy >= 2 for jegy in jegyek):
            status = "Átment"
        elif any(jegy < 2 for jegy in jegyek):
            status = "Megbukott"
        else:
            status = "Vegyes"

        van_jeles = "van jeles" if any(jegy == 5 for jegy in jegyek) else "nincs jeles"

        print(f"{nev}: {status}, {van_jeles}")


def feladat_4():

    autok = {
    "BMW": ["ok", "ok", "ok"],
    "Audi": ["ok", "hiba", "ok"],
    "Lada": ["hiba", "hiba", "hiba"],
    "Tesla": ["ok", "ok", "hiba"],
    }

    for auto, statusok in autok.items():
        if all(status == "ok" for status in statusok):
            status = "Minden rendben"
        elif all(status == "hiba" for status in statusok):
            status = "Roncs"
        elif any(status == "hiba" for status in statusok):
            status = "Van hiba"
        
        minden_ok = "Minden ok" if all(status == "ok" for status in statusok) else "Valami nem ok"

        print(f"{auto} - {status} - Oké? - {minden_ok}")

feladat_4()