#  set - olyan, mint egy lista csak egyedi elemeket tartalmaz
#  nincs benne sorrend tehát nem indexelhető úgy mint a listák
#  nagyon gyors a keresés

def pelda_1():

    a = [1, 2, 3, 4, 5]
    s = set(a)
    print(s)


def pelda_2():

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print(a | b) # unió -> {1, 2, 3, 4, 5, 6}
    print(a & b) # metszet -> {3, 4}
    print(a - b) # különbség -> {1, 2}
    print(a ^ b) # szimmetrikus különbség -> {1, 2, 5, 6}


def pelda_3():

    team1 = ["Alex", "Bianka", "Charlie", "Diana"]
    team2 = ["Charlie", "Eric", "Bianka", "Fiona"]

    print(set(team1) | set(team2))
    print(set(team1) & set(team2))
    print(set(team1) - set(team2))


#  ----- GYAKORLÓS -----

def feladat_1():

    nevek = ["Alex", "Bianka", "Alex", "Charlie", "Bianka", "Diana"]

    print(set(nevek))

def feladat_2():

    team1 = {"Alex", "Bianka", "Charlie"}
    team2 = {"Charlie", "Diana", "Eric"}

    print(set(team1) & set(team2))

def feladat_3():

    team1 = {"Alex", "Bianka", "Charlie", "Diana"}
    team2 = {"Charlie", "Eric", "Bianka"}

    print(set(team1) - set(team2))

def feladat_4():

    team1 = {"Alex", "Bianka", "Charlie"}
    team2 = {"Charlie", "Diana", "Eric"}

    print(set(team1) ^ set(team2))

def feladat_5():

    szamok = [1, 2, 3, 2, 4, 1, 5, 3]

    print(list(set(szamok)))


