import os

def feladat1():

    # megmutatja hogy hol vagy az adott futtatáskor
    jelenlegi_path = os.getcwd()
    print(jelenlegi_path)

    #  mappa tartalmának kilistázása
    mappa_tartalma = os.listdir()
    print(mappa_tartalma)

    # letezik-e az adott folder, fájl
    letezik_e = os.path.exists("Basics_course")
    print(letezik_e)

    # os.path.isfile()/os.path.isdir() -> fájl vagy mappa
    # os.path.join() -> pathok joinolása ("Modules", "03_datetime.py") -> "Modules/03_datetime.py"
    # os.makedirs() -> mappa létrehozása ("uj_mappa", exists_ok=True)


def feladat2():

    aktualis_mappa_konyvtar = os.getcwd()
    
    fajlok = os.listdir(aktualis_mappa_konyvtar)

    py_fajlok = [f for f in fajlok if f.endswith(".py")]

    nulla_fajlok = [f for f in fajlok if f.startswith("0")]

    eleresi_utak = [os.path.join(aktualis_mappa_konyvtar, f) for f in nulla_fajlok]

    for gyoker, mappak, fajlok in os.walk("."):
        print(gyoker)
        print(fajlok)


feladat2()


