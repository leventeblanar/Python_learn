from collections import Counter
from collections import defaultdict

# normal dict, list, tuple is not always enough for certain tasks
# collections helps with some bit cleverer datastructures

# Counter - counts anything in an iterable object
# defaultdict - a dict where you don't get a KeyError if a key doesn't exist yet - automatically creates a value
# deque - double-ended queue, a list where yu an add an item to the end or the beginning
# namedtuple - tuple that has named spaces, miniclass without boilerplate

szavak = ["alma", "körte", "alma", "szilva", "alma", "körte"]
szamlalo = Counter(szavak)

# print(szamlalo)
# print(szamlalo.most_common(2))

mondat = "a macska az asztalon ült a macska szereti az almát az alma piros"
mondatszavak = mondat.split(" ")
# print(mondatszavak)

mondatszavakeloford = Counter(mondatszavak)
# print(mondatszavakeloford)
# print(mondatszavakeloford.most_common(5))
# print(sorted(mondatszavakeloford))

# defaultict automatikusan létrehozza az alapértéket ha nincs a hozzáadás során kulcs
# Ez KeyErrort dob
# d = {}
# d["alma"] += 1

# Így már nem dobna azt
d = defaultdict(int)


def feladat0():
    vasarlasok = [
        ("Anna", "alma"),
        ("Béla", "körte"),
        ("Anna", "kenyér"),
        ("Béla", "tej"),
        ("Anna", "alma"),
        ("Csilla", "kenyér"),
        ("Béla", "alma"),
        ("Csilla", "tej"),
    ]

    vasarlasokszotar = defaultdict(list)
    for vasarlo, item in vasarlasok:
        vasarlasokszotar[vasarlo].append(item)
    # print(f"Anna vásárlása: {vasarlasokszotar['Anna']}")
    # print(max(vasarlasokszotar, key=lambda vasarlo: len(vasarlasokszotar[vasarlo])))

def feladat1():
    jegyek = [
        ("Anna", 5),
        ("Béla", 3),
        ("Anna", 4),
        ("Csilla", 5),
        ("Béla", 2),
        ("Anna", 3),
        ("Csilla", 4),
        ("Béla", 5),
        ("Csilla", 3),
    ]

    jegyeklista = defaultdict(list)
    for diak, jegy in jegyek:
        jegyeklista[diak].append(jegy)
    print(jegyeklista)
    # jegyek összege elosztva a jegyek számával
    atlagok = {}
    for diak, jegyek in jegyeklista.items():
        atlag = round(sum(jegyek)/len(jegyek), 2)
        print(f"{diak}: {atlag}")
        atlagok.update({f'{diak}': atlag})

    print(max(atlagok, key=lambda diak: atlagok[diak]))


def feladat2():
    # lista, amiben tupleök vannak
    meccsek = [
    ("Fradi", "MTK", 3, 1),
    ("Újpest", "Fradi", 2, 2),
    ("MTK", "Újpest", 1, 0),
    ("Fradi", "Újpest", 1, 0),
    ("MTK", "Fradi", 0, 2),
    ("Újpest", "MTK", 3, 1),
    ]

    csapatgol = defaultdict(list)
    for hazai, vendeg, hazai_gol, vendeg_gol in meccsek:
        csapatgol[hazai].append(hazai_gol)
        csapatgol[vendeg].append(vendeg_gol)

    print(csapatgol)

    for csapat, gol in csapatgol.items():
        print(f"{csapat} összes lőtt góljának összege: {sum(gol)}")
    
    print(max(csapatgol, key=lambda csapat: sum(csapatgol[csapat])))



feladat2()