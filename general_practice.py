import pandas as pd

def enumerate_1():

    gyumolcsok = ["alma", "banán", "szilva"]

    for idx, gyumolcs in enumerate(gyumolcsok, start=1):
        print(f"{idx}. {gyumolcs}")


def isintance_1():

    adatok = [42, "hello", [1, 2, 3], {"nev": "Alex"}]

    for adat in adatok:
        if isinstance(adat, int):
            print(f"{adat} egy int")
        if isinstance(adat, str):
            print(f"{adat} egy string")
        if isinstance(adat, float):
            print(f"{adat} egy float")
        if isinstance(adat, list):
            print(f"{adat} egy list")
        if isinstance(adat, dict):
            print(f"{adat} egy dict")


def zip_1():

    nevek = ["Alex", "Bianka", "Charlie"]
    korok = [25, 19, 32]

    for nev, kor in zip(nevek, korok):
        print(f"{nev} -> {kor}")


def map_1():

    szamok = [1, 2, 3, 4]

    power2 = map(lambda x: x**2, szamok)
    print(list(power2))


def any_all_1():

    jegyek = [3, 4, 5, 2]

    if any(jegy == 1 for jegy in jegyek):
        print("Megbukott")
    elif all(jegy  >= 2 for jegy in jegyek):
        print("Átment")


def sorted_1():

    diakok = [
    {"nev": "Alex", "kor": 25},
    {"nev": "Bianka", "kor": 19},
    {"nev": "Charlie", "kor": 32}
    ]

    print(sorted(diakok, key=lambda x: x['kor']))


def set_1():

    team1 = ["Alex", "Bianka", "Charlie"]
    team2 = ["Charlie", "Diana", "Eric"]

    print(set(team1) & set(team2))


def loc_iloc_1():

    import pandas as pd

    df = pd.DataFrame({
        "nev": ["Alex", "Bianka", "Charlie"],
        "kor": [25, 19, 32]
    })

    print(df.loc[1, 'nev'])
    print(df.iloc[1, 0])


def typecast_1():

    df = pd.DataFrame({
    "ar": ["100", "200", "x", ""],
    "datum": ["2021-01-01", "rossz", "2021/02/15", ""],
    "ido": ["2:30:00", "90m", "rossz", ""]
    })

    df['ar_tn'] = (pd.to_numeric(df['ar'], errors='coerce'))
    df['datum_dt'] = (pd.to_datetime(df['datum'], errors='coerce'))
    df['ido_td'] = (pd.to_timedelta(df['ido'], errors='coerce'))

    print(df["ar_tn"])
    print(df["datum_dt"])
    print(df["ido_td"])
