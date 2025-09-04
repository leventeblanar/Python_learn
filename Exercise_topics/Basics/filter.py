#  filter() - used to extract elements from an iterable (list, tuple, set) that satisfy a given condition
#  It works by applying a function to each element and keeping only those for which function return True

def example_1():
    def even(n):
        return n% 2 == 0

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = filter(even, a)
    print(list(b))


def example_2():
    
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = filter(lambda x: x % 2 == 0, a)
    print(list(b))


def example_3():

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = filter(lambda x: x % 2 == 0, a)
    c = map(lambda x: x * 2, b)
    print(list(c))


def example_4():

    a = ["apple", "banana", "cherry", "kiwi", "grape"]
    b = filter(lambda w: len(w) > 5, a)
    print(list(b))


def example_5():

    L = ["apple", "", None, "banana", 0, "cherry"]
    A = filter(None, L)
    print(list(A))


#  ------- GYAKORLÓS --------


def feladat_1():

    szamok = [3, 8, 15, 22, 29, 40]
    greater_10 = filter(lambda x: x > 10 and x % 2 == 0, szamok)
    print(list(greater_10))


def feladat_2():

    adatok = ["alma", "", "banán", None, "szilva", "", "körte"]
    not_none = filter(None, adatok)
    print(list(not_none))


def feladat_3():

    szamok = list(range(1, 31))
    filtered_num = filter(lambda x: x % 3 == 0 and x % 2 != 0, szamok)
    print(list(filtered_num))


def feladat_4():

    szavak = ["alma", "banán", "kiwi", "ananász", "szilva", "körte"]

    longer_than_5 = filter(lambda x: len(x) < 5, szavak)
    print(list(longer_than_5))


def feladat_5():

    dolgozok = [
    {"nev": "Alex", "kor": 25, "fizetes": 300000},
    {"nev": "Bianka", "kor": 19, "fizetes": 250000},
    {"nev": "Charlie", "kor": 32, "fizetes": 450000},
    {"nev": "Diana", "kor": 28, "fizetes": 220000},
    {"nev": "Eric", "kor": 41, "fizetes": 500000},
    ]

    older_than_25 = filter(lambda x: x['kor'] >= 25 and x['fizetes'] > 300000, dolgozok)
    print(list(older_than_25))
