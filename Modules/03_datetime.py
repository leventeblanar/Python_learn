from datetime import date, datetime, timedelta
from collections import defaultdict

ma = date.today()
maido = datetime.today()
holnap = date.today() + timedelta(days=1)

# dátumot szöveggé alakít
datumszoveg = datetime.now().strftime("%Y-%m-%d")
# fordítva szövegből csinál dátumot
datumszovegbe = datetime.strptime("2026-02-22", "%Y-%m-%d")

def feladat1():
    szuletesnapok = {
    "Anna": "1995-04-12",
    "Béla": "1988-11-03",
    "Csilla": "2001-07-25",
    }

    today = date.today()
    korok = defaultdict(int)

    for nev, datum in szuletesnapok.items():
        datumtodate = datetime.strptime(datum, "%Y-%m-%d")
        age = today.year - datumtodate.year - ((today.month, today.day) < (datumtodate.month, datumtodate.day))
        print(f"{nev} ma {age} éves.")
        korok[nev] = age

    print(max(korok, key=lambda nev: korok[nev]))


def feladat2():

    feladatok = [
    ("Riport elkészítése", "2026-02-25"),
    ("Meetingre felkészülés", "2026-02-22"),
    ("Negyedéves zárás", "2026-03-31"),
    ("Szabadság bejelentése", "2026-02-20"),
    ]

    today = date.today()

    hatralavo_map = {}

    for feladat, hatarido in feladatok:
        hatarido_date = datetime.strptime(hatarido, "%Y-%m-%d").date()
        kulonbseg = hatarido_date - today
        print(f"Feladat: {feladat}, Rendelekzésre álló idő: {kulonbseg.days}")
        hatralavo_map[feladat] = kulonbseg.days

    nem_lejart = {f: n for f, n in hatralavo_map.items() if n >= 0}
    legsurgosebb = min(nem_lejart, key=lambda feladat: nem_lejart[feladat])

    print(f"Legsürgősebb: {legsurgosebb}")

    print("Lejárt határidejű feladatok")
    for hatralevo, napok in hatralavo_map.items():
        if napok < 0:
            print(f"- {hatralevo}")

feladat2()