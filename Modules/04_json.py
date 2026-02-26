import json

def pelda1():
    # json.loads() -> JSON szövegből csinál python dictet

    szoveg = '{"nev": "Anna", "kor": 30}'
    adat = json.loads(szoveg)
    print(adat['nev'])

def pelda2():
    # json.dumps() -> python dict-ből csinál szöveget

    adat = {"nev": "Anna", "kor": 30}
    szoveg = json.dumps(adat, indent=2)
    print(szoveg)

def pelda3():

    # json fájlból olvasás
    with open("adat.json", "r") as f:
        adat = json.load(f)

    # python dictet fájlba ír
    with open("adat.json", "w") as f:
        json.dump(adat, f, indent=2)



def feladat1():

    adat = '''
    [
        {"nev": "Anna", "osztaly": "fejlesztés", "fizetes": 850000},
        {"nev": "Béla", "osztaly": "marketing", "fizetes": 720000},
        {"nev": "Csilla", "osztaly": "fejlesztés", "fizetes": 920000},
        {"nev": "Dani", "osztaly": "marketing", "fizetes": 680000},
        {"nev": "Eszter", "osztaly": "fejlesztés", "fizetes": 780000}
    ]
    '''

    adat_list = json.loads(adat)

    for item in adat_list:
        print(item['nev'] + ": " + f"{item['fizetes']:,}".replace(",", " ") + "Ft")

    fejlesztes = [item['fizetes'] for item in adat_list if item['osztaly'] == "fejlesztés"]
    atlag = sum(fejlesztes) / len(fejlesztes)

    print(atlag)

    print(max(adat_list, key=lambda alkalmazott: alkalmazott['fizetes']))


feladat1()