# listákat indexxel tudunk elérni
gyumolcsok = ["alma", "körte", "szilva", "barack"]

print(gyumolcsok[1]) #adott index
print(gyumolcsok[-1]) #hátulról indexel
print(gyumolcsok[1:3]) # range
print(gyumolcsok[:2]) # to
print(gyumolcsok[2:]) # from


# dict - kulcs érték párok -> a kulcs neve alapján érjük el az értékét
felhasznalo = {
    "nev":   "Kovács Péter",
    "kor":   34,
    "varos": "Budapest"
}

print(felhasznalo["nev"])
print(felhasznalo["kor"])
print(felhasznalo["varos"])

# .get() - biztonságos elérés - ha nincs olyan kulcs akkor None-t ad vissza
print(felhasznalo.get("nev"))

# tuple - olyan mint a lista de nem változtatható, indexel érjük el
koordinata = (47.497, 19.040)

print(koordinata[0])

# set - egyedi elemeg halmaza, nincs sorrend, nem indexelhető
primes = {2, 3, 5, 7, 11}

print(7 in primes)
print(4 in primes)


# nested struktúrák
# dicten belül dict - befelé haladunk -> elősz9r a dict1 aztán dict2-re hivatkozunk
termek = {
    "nev": "Laptop",
    "ar": {
        "netto":  150000,
        "brutto": 190500
    }
}

print(termek["ar"]["brutto"])

# list of dicts
dolgozok = [
    {"nev": "Anna", "fizetes": 400000},
    {"nev": "Béla", "fizetes": 380000}
]

print(dolgozok[0])
print(dolgozok[0]["nev"])

# dictben lista érték
osztaly = {
    "tanulo": "Kati",
    "jegyek": [5, 4, 5, 3, 4]
}

print(osztaly["jegyek"])
print(osztaly["jegyek"][0])

# nested list
matrix = [
    [1, 2, 3],   # sor 0
    [4, 5, 6],   # sor 1
    [7, 8, 9]    # sor 2
]

print(matrix[0][2])