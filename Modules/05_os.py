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


def feladat3():

    parent_dir = os.getcwd()
    new_folder = "project"

    path = os.path.join(parent_dir, new_folder)

    # os.makedirs(path)

    child_folder = ['src', 'tests', 'docs', 'logs']

    for folder in child_folder:
        child_path = os.path.join(path, folder)
        # os.makedirs(child_path)

    check_if_exists = [f"{f} ✅" if os.path.exists(os.path.join(path, f)) else f"{f} ❌" for f in child_folder]
    print(check_if_exists)