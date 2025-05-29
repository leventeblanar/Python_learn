def split_string():
    szoveg = "Ez egy próba-szöveg! Tisztán@ kellene, látnunk: mi marad meg?"

    szavak = szoveg.split()

    for szo in szavak:
        szo = szo.strip("-.,:!?@")
        if szo.isalpha():
            print(szo)



def sentences_string():

    mondatok = [
    "Alma esik az ágról.",
    "Banán sárga gyümölcs.",
    "Ablak előtt áll egy autó.",
    "Éjszaka hideg van.",
    "Aranyos a kutyád."
    ]


    for mondat in mondatok:
        mondat = mondat.lower()
        if mondat.startswith("a"):
            print(mondat.replace("a", "@", 1))



def filter_count_join():

    elemek = ["123", "alma", "456", "Python", "789", "körte", "0", "Banán"]

    szamok = 0
    nem_szamok = []

    for elem in elemek:
        if elem.isdigit():
            szamok += 1
        else:
            nem_szamok.append(elem.upper())

    print(f"Szám típusúak: {szamok}")
    print("Nem szám elemek nagybetűvel:", " ".join(nem_szamok))

filter_count_join()