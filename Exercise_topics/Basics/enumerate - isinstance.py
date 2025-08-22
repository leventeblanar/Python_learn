from datetime import datetime, timedelta

#  enumerate() - akkor jön jól, ha végig akarunk menni egy listán és közben kell az index is
def enumerate_pelda():

    nevek = ["Anna", "Béla", "Csaba"]

    for index, nev in enumerate(nevek):
        print(index, nev)



#  isinstance() - ellenőrzi a változó típusát
def isinstance_pelda():
    adatok = [1, "hello", [1, 2, 3]]

    for a in adatok:
        if isinstance(a, int):
            print(a, "-> int")
        elif isinstance(a, str):
            print(a, "-> string")
        elif isinstance(a, list):
            print(a, "-> lista")



#  kombinalva a kettő

def enumerate_isinstance_pelda():
    adatok = [1, "hello", [1, 2, 3]]

    for i, a in enumerate(adatok):
        if isinstance(a, int):
            print(f"{i}. elem: {a} (int)")
        elif isinstance(a, str):
            print(f"{i}. elem: {a} (string)")
        elif isinstance(a, list):
            print(f"{i}. elem: {a} (list)")
        else:
            print(f"{i}. elem: {a} (ismeretlen)")



def enumerate_feladat_1():

    words = ["python", "rocks", "big", "time"]

    for index, word in enumerate(words):
        print(f"Index: {index}, Word: {word}")



def isinstance_feladat_1():

    adatok = [1, "hi", [1,2], "python", 5]

    int_szamlalo = 0
    str_szamlalo = 0
    list_szamlalo = 0

    for adat in adatok:
        if isinstance(adat, int):
            print(adat, "-> int")
            int_szamlalo += 1 
        elif isinstance(adat, str):
            print(adat, "-> string")
            str_szamlalo += 1
        elif isinstance(adat, list):
            print(adat, "-> lista")
            list_szamlalo += 1
    
    print(f"int={int_szamlalo}")
    print(f"str={str_szamlalo}")
    print(f"list={list_szamlalo}")

        
def kezeld(adat):
    if isinstance(adat, dict):
        print("This is a dict, number of keys:", len(adat))
    elif isinstance(adat, list):
        print("This is a list, number of items:", len(adat))
    else:
        print("This is something else.", adat)



#  1st type_checker

def type_checker(adat):
    if isinstance(adat, list):
        print("This is a list, number of items:", len(adat))
    elif isinstance(adat, dict):
        print("This is a dict, number of keys:", len(adat))
    elif isinstance(adat, str):
        print("This is a string:", adat)
    else:
        print("This is an unknown type:", adat)

# type_checker([1, 2, 3])
# type_checker({"name": "Zsolt", "age": 30, "game": "LOL"})
# type_checker("Dinosaurs are cool!")
# type_checker(4)


#  2nd normalize_rows(row, headers)



def normalize_rows(row, headers):

    headers = ["name", "age", "city"]

    if isinstance(row, dict):
        return [row.get(h, "") for h in headers]
    elif isinstance(row, (list, tuple)):
        lst = list(row)
        if len(lst) < len(headers):
            lst = lst + [""] * (len(headers) - len(lst))
        else:
            lst = lst[:len(headers)]
        return lst
    else:
        raise ValueError("Unsupported row type.")
    
# print(normalize_rows({"name": "Anna", "city": "Paris"}, headers))
# print(normalize_rows(["Bob", 25], headers))
# print(normalize_rows(("Eve", 22, "London", "extra"), headers))
# print(normalize_rows("Hello", headers))


def normalize_all(adatok, headers):

    eredmeny = []
    for adat in adatok:
        if isinstance(adat, dict):
            sor = [adat.get(h, "") for h in headers]
        elif isinstance(adat, (list, tuple)):
            lst = list(adat)
            if len(lst) < len(headers):
                lst = lst + [""] * (len(headers) - len(lst))
            else:
                lst = lst[:len(headers)]
            sor = lst
        else:
            raise ValueError("Unsupported row type.")
        eredmeny.append(sor)
    return eredmeny
        
headers = ["name", "age", "city"]      
adatok = [
    {"name": "Anna", "city": "Paris"},
    ["Bob", 25],
    ("Eve", 22, "London", "extra"),
    {"name": "John", "age": 40, "city": "Berlin"},
    "Ez itt hibás típus",
    12345
]

# print(normalize_all(adatok, headers))


def clean_and_normalize(adatok, headers, fill="-"):

    eredmeny = []
    hibas = []

    for adat in adatok:
        if isinstance(adat, dict):
            sor = [adat.get(h, fill) for h in headers]
            eredmeny.append(sor)

        elif isinstance(adat, (list, tuple)):
            lst = list(adat)
            if len(lst) < len(headers):
                lst += [fill] * (len(headers) - len(lst))
            else:
                lst = lst[:len(headers)]
            eredmeny.append(lst)
        else:
            print(f"Hibás típus.")
            sor = adat
            hibas.append(sor)

    print(f"Megfelelő sorok száma: {len(eredmeny)}")
    print(f"Hibás sorok száma: {len(hibas)}")
    return eredmeny

# print(clean_and_normalize(adatok, headers))
    





