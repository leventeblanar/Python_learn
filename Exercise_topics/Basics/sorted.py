#  sorted - it is not a list method, but a built in function that gives back a new list that is sorted based on a certain criteria

def example_1():

    a = (1, 11, 2)
    x = sorted(a, reverse=True)
    print(x)


def example_2():

    a = ("Jenifer", "Sally", "Jane")
    x = sorted(a, key=len)
    print(x)


#  the key parameter can handle functions as well

def example_3():

    def myfunc(n):
        return abs(10-n)

    a = (5, 3, 1, 11, 2, 12, 17)
    x = sorted(a, key=myfunc)
    print(x)


#  ----- Gyakorlós -----

def feladat_1():

    szavak = ["alma", "banán", "körte", "szilva"]
    print(sorted(szavak))
    print(sorted(szavak, reverse=True))
    print(sorted(szavak, key=len))


def feladat_2():

    dolgozok = [
    {"nev": "Alex", "kor": 25, "fizetes": 300000},
    {"nev": "Bianka", "kor": 19, "fizetes": 250000},
    {"nev": "Charlie", "kor": 32, "fizetes": 450000},
    {"nev": "Diana", "kor": 28, "fizetes": 220000},
    {"nev": "Eric", "kor": 41, "fizetes": 500000},
    ]

    print(sorted(dolgozok, key=lambda x: x['kor']))

def feladat_3():

    dolgozok = [
    {"nev": "Alex", "kor": 25, "fizetes": 300000},
    {"nev": "Bianka", "kor": 19, "fizetes": 250000},
    {"nev": "Charlie", "kor": 32, "fizetes": 450000},
    {"nev": "Diana", "kor": 28, "fizetes": 220000},
    {"nev": "Eric", "kor": 41, "fizetes": 500000},
    {"nev": "Frank", "kor": 28, "fizetes": 400000},
    ]

    print(sorted(dolgozok, key=lambda x: (x['kor'], -x['fizetes'])))


def feladat_4():

    nevek = ["alex", "Bianka", "charlie", "Diana", "eric", "Frank"]


    print(sorted(nevek, key=lambda x: x.lower()))


def feladat_5():

    konyvek = [
    {"cim": "Python kezdőknek", "szerzo": "Kiss Péter", "ev": 2021},
    {"cim": "Haladó SQL", "szerzo": "Nagy Anna", "ev": 2019},
    {"cim": "Adatbázisok", "szerzo": "Kiss Péter", "ev": 2018},
    {"cim": "Algoritmusok", "szerzo": "Tóth Béla", "ev": 2020},
    {"cim": "Python mesterfokon", "szerzo": "Kiss Péter", "ev": 2023},
    ]

    print(sorted(konyvek, key=lambda x: (x['szerzo'], -x['ev'])))

feladat_5()