import random

### FELADAT 1. ask for userinput and output something using it
# userinput = int(input("Adj meg egy számot: "))
# output = userinput * 15
# print(output)

### FELADAT 2. 
# name = str(input("Név: "))
# output = len(name)
# print(output)

### FELADAT 3.
# szam = int(input("Adj meg egy számot: "))

# if szam % 2 == 0:
#     print("A szám páros")
# else:
#     print("A szám páratlan")

### FELADAT 4. - random szám 

# gep_gondol = random.randint(1, 10)
# fut = True

# while fut:
#     tipp = int(input("Tippelj haver: "))
#     if gep_gondol == tipp:
#         print("Eltaláltad haver!")
#         fut = False
#     elif gep_gondol > tipp:
#         print("Túl alacsony bradám, próbáld újra.")
#     elif gep_gondol < tipp:
#         print("Túl magas testvérem, fuss neki még egyszer")

### FELADAT 5. - kő papír olló

print("Ez a csodálatos kő-papír-olló játék.")

while True:
    gep_valaszt = random.choice(["kő", "papír", "olló"])
    print(f"A gép választása: {gep_valaszt}")
    ember_valaszt = input("Te milyen kézjelet dobsz bro? ").lower()

    if ember_valaszt not in ["kő", "papír", "olló"]:
        print("Haver, mit mutogatsz? Kő-Papír-Olló! Mit nem értesz?")
        continue

    print(f"A gép kéznélkül ezt mutassa: {gep_valaszt}")

    nyeresi_helyzetek = [("kő", "papír"), ("papír", "olló"), ("olló", "kő")]

    if (gep_valaszt, ember_valaszt) in nyeresi_helyzetek:
        print("Nyertél Tes!")
    elif gep_valaszt == ember_valaszt:
        print("Ez egy erős döntetlen!")
    else:
        print("Vesztettél te Gyász!")
    
    tovabb = input("Akarsz még játszani te Nyomorult? (igen/nem) ").lower()
    if tovabb != "igen":
        print("Jól van bradám, majd legközelebb!")
        break