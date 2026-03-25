# modul ami fájl- és mappaútvonalakat objektumként kezeli, nem sima stringként
# sokkal olvashatóbb és kevésbé hibázós, mint a régi os.path

from pathlib import Path
def alapok():
    p = Path("/Users/levente_blanar/GitHub/Python_learn")
    # ez már nem csak egy string - hanem egy objektum aminek vannak tulajdonságai is
    print(p.name) # -> fájlnév
    print(p.stem) # -> fájlnév kiterjesztés nélkül
    print(p.suffix) # -> csak kiterjesztés
    print(p.parent) # -> szülőmappa
    print(p.parts) # -> elemek

    fajl = p / "Modules"
    # további elem hozzáadás a / operátorral. (os verzió bonyolultabb -> os.path.join(base, "reports")

    print(fajl)

    print(p.exists()) # -> létezik-e
    print(p.is_file()) # -> fájl-e
    print(p.is_dir()) # -> mappa-e
    print(Path.cwd()) # -> ahol most vagy
    print(__file__) # -> annak a fájlnak az útvonala ami éppen fut


def feladat1():

    cwd = Path.cwd()
    print(cwd)
    cwd_kieg = cwd / "Modules" / "08_pathlib.py"
    print(cwd_kieg)

    print(cwd_kieg.name)
    print(cwd_kieg.suffix)
    print(cwd_kieg.parent)
    
    if cwd_kieg.exists():
        print(f"{cwd_kieg.parts[-1]} létezik.")
    else:
        print(f"{cwd_kieg.parts[-1]} nem létezik.")

feladat1()