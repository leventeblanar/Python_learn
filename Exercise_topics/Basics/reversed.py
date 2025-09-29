#  beépített függvény
#  visszaad egy terátort, ami a megadott sorozatot (lista, string, tuple, range, stb.) fordított sorrendben adja vissza
#  maga az eredmény nem lista, hanem egy reversed objektum -> ezért gyakran list(...)-tel alakítjuk át


def pelda_1():

    szamok = [1, 2, 3, 4, 5]
    print(list(reversed(szamok)))


def pelda_2():

    szo = "python"
    print("".join(reversed(szo)))

def pelda_3():

    for i in reversed(range(1, 6)):
        print(i, end= " ")

