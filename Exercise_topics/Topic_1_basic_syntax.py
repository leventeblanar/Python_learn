import random
import re

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

# print("Ez a csodálatos kő-papír-olló játék.")

# while True:
#     gep_valaszt = random.choice(["kő", "papír", "olló"])
#     print(f"A gép választása: {gep_valaszt}")
#     ember_valaszt = input("Te milyen kézjelet dobsz bro? ").lower()

#     if ember_valaszt not in ["kő", "papír", "olló"]:
#         print("Haver, mit mutogatsz? Kő-Papír-Olló! Mit nem értesz?")
#         continue

#     print(f"A gép kéznélkül ezt mutassa: {gep_valaszt}")

#     nyeresi_helyzetek = [("kő", "papír"), ("papír", "olló"), ("olló", "kő")]

#     if (gep_valaszt, ember_valaszt) in nyeresi_helyzetek:
#         print("Nyertél Tes!")
#     elif gep_valaszt == ember_valaszt:
#         print("Ez egy erős döntetlen!")
#     else:
#         print("Vesztettél te Gyász!")
    
#     tovabb = input("Akarsz még játszani te Nyomorult? (igen/nem) ").lower()
#     if tovabb != "igen":
#         print("Jól van bradám, majd legközelebb!")
#         break


### FELADAT 6.

# szamok = input("Adj meg számokat, hogy kiszámolhassam neked az átlagát: ")

# szam_lista = szamok.split(",")

# szam_lista = [float(szam.strip()) for szam in szam_lista]

# atlag = sum(szam_lista) / len(szam_lista)

# print(f"A megadott számok átlaga: {round(atlag, 2)}")


### FELADAT 7.

# szamok = input("Adj meg számokat, hogy megkereshessem a legnagyobb és legkisebbet köztük: ")

# szam_lista = szamok.split(",")

# szam_lista = [int(szam.strip()) for szam in szam_lista]

# max_szam = max(szam_lista)
# min_szam = min(szam_lista)

# print("A legnagyobb szám: ", max_szam)
# print("A legnagyobb szám: ", min_szam)


### FELADAT 8.

# userInput = input("Adj meg több azonos számot, kiszűrjük belőle a duplikációkat: ")

# szamok = userInput.split(",")
# szamok = [int(szam.strip()) for szam in szamok]

# s = []
# for num in szamok:
#     if num not in s:
#         s.append(num)

# print(s)

### ALTERNATÍV MEGOLDÁS

# userInput = input("Adj meg több azonos számot, kiszűrjük belőle a duplikációkat: ")

# szamok = userInput.split(",")
# szamok = [int(szam.strip()) for szam in szamok]

# egyedi_szamok = sorted(set(szamok))

# print("Számok listája a duplikációk kiszűrése után: ", egyedi_szamok)


### FELADAT 9.

# szoveg_input = input("Írj be egy szöveget, megnézem palindróm-e: ")

# szoveg = szoveg_input.replace(" ", "")

# szoveg = szoveg.lower()
# forditott_szoveg = szoveg[::-1]

# if forditott_szoveg == szoveg:
#     print("Palindrom")
# else:
#     print("Nem palindrom")


### FELADAT 10.

# szam_sor = input("Adj meg egy növekvő számsorozatot vesszővel elválasztva, amiben hiányzik egy szám: ")

# szamok = [int(szam.strip()) for szam in szam_sor.split(",")]

# for szam in range(1, len(szamok)):
#     if szamok[szam] - szamok[szam - 1] > 1:
#         hianyzo = szamok[szam - 1] + 1
#         print(f"A hiányzó szám: {hianyzo}")
#         break


### FELADAT 11.

# szamok = input("Adj be pár számot, megnézem hogy melyik van többször és ha van hányor: ")

# szam_list = [int(szam.strip()) for szam in szamok.split(",")]

# szamlalo = {}

# for szam in szam_list:
#     if szam in szamlalo:
#         szamlalo[szam] += 1
#     else:
#         szamlalo[szam] = 1

# print("Ismétlődő számok:")
# for szam, darabszam in szamlalo.items():
#     if darabszam > 1:
#         print(f"{szam} -> {darabszam}-szor")

### FELADAT 12.

# inputSzoveg = input("Adj meg egy szöveget: ")

# szoveg_clean = re.sub(r'[^a-zA-Z]', '', inputSzoveg.lower()) # r = raw string - speciális karaktereket nem értelmezi kódként a python

# szamlalo = {}

# for betu in szoveg_clean:
#     if betu in szamlalo:
#         szamlalo[betu] += 1
#     else:
#         szamlalo[betu] = 1

# print("Ismétlődő betűk: ")
# for betu, darabszam in szamlalo.items():
#     if darabszam > 1:
#         print(f"{betu} - > {darabszam}-szor")

# leggyakoribb_betu = max(szamlalo, key=szamlalo.get)
# print(f"\n A Leggyakoribb betű: {leggyakoribb_betu}")

szamok = input("Adj meg egy számsort: ")

szam_list = [int(szam.strip()) for szam in szamok.split(",")]

print(szam_list)