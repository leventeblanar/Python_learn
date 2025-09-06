def enumerate_re():

    gyumolcsok = ["alma", "banán", "körte"]

    for index, gyumolcs in enumerate(gyumolcsok):
        print(f"{index}: {gyumolcs}")


def isnstance_re():

    adatok = [42, "hello", [1, 2], {"nev": "Alex"}]

    for adat in adatok:
        if isinstance(adat, int):
            print(f"Ez egy int: {adat}")
        elif isinstance(adat, str):
            print(f"Ez egy str: {adat}")
        elif isinstance(adat, float):
            print(f"Ez egy float: {adat}")
        elif isinstance(adat, dict):
            print(f"Ez egy dict: {adat}")
        else:
            print("This is something else.")


def zip_re():

    nevek = ["Alex", "Bianka", "Charlie"]
    korok = [25, 19, 32]

    for nev, kor in zip(nevek, korok):
        print(f"{nev} -> {kor}")


def map_re():

    szamok = [1, 2, 3, 4]

    szamok_4 = list(map(lambda x: x**2, szamok))

    print(szamok_4)


def filter_re():

    szamok = [5, 12, 7, 20, 3, 18]

    tiz_felett = list(filter(lambda x: x > 10, szamok))

    print(tiz_felett)


def any_all():

    jegyek = [3, 4, 5, 2]

    atment = 'Átment' if all(jegy >= 2 for jegy in jegyek) else "Nem ment át"
    print(atment)
    megbukott = "Megbukott" if any(jegy == 1 for jegy in jegyek) else "Nem bukott meg"
    print(megbukott)


def sorted_re():

    diakok = [
    {"nev": "Alex", "kor": 25},
    {"nev": "Bianka", "kor": 19},
    {"nev": "Charlie", "kor": 32}
    ]

    print(sorted(diakok, key=lambda x: x["kor"]))