raktar = {
    "nev": "Központi raktár",
    "varos": "Budapest",
    "termekek": [
        {
            "cikkszam": "A001",
            "nev": "Laptop",
            "kategoria": "elektronika",
            "ar": {
                "netto": 150000,
                "brutto": 190500
            },
            "keszlet": 12
        },
        {
            "cikkszam": "B042",
            "nev": "Egér",
            "kategoria": "elektronika",
            "ar": {
                "netto": 8000,
                "brutto": 10160
            },
            "keszlet": 85
        },
        {
            "cikkszam": "C017",
            "nev": "Irodaszék",
            "kategoria": "butorok",
            "ar": {
                "netto": 45000,
                "brutto": 57150
            },
            "keszlet": 7
        }
    ],
    "kapcsolattarto": {
        "nev": "Kiss Márton",
        "email": "kiss.marton@ceg.hu"
    }
}

# minden feladatnál írd a választ a print()-be, majd futtasd le és nézd meg az eredményt

# # 1. Kérd le a raktár városát!
# print(raktar["varos"])

# # 2. Hány termék van a raktárban?
# print(raktar["termekek"][0]["keszlet"] + raktar["termekek"][1]["keszlet"] + raktar["termekek"][2]["keszlet"])

# # 3. Kérd le az első termék nevét!
# print(raktar["termekek"][0]["nev"])

# # 4. Kérd le az Egér (B042) bruttó árát!
# print(raktar["termekek"][1]["ar"]["brutto"])

# # 5. Kérd le az utolsó termék cikkszámát negatív indexszel!
# print(raktar["termekek"][-1]["cikkszam"])

# # 6. Kérd le a kapcsolattartó e-mail címét!
# print(raktar["kapcsolattarto"].get("email"))

# # 7. Írd fel azt a kifejezést, ami True-t ad vissza, ha az első termék készlete több mint 10!
# print(raktar["termekek"][0]["keszlet"] > 10)

# # 8. List comprehension: szedd ki az összes termék nevét egy listába!
# print([termek["nev"]] for termek in raktar["termekek"])


termekek = raktar["termekek"]  # hogy ne kelljen mindig kiírni

# -------------------------------------------------------
# alap — [mit for elem in lista]
# -------------------------------------------------------

# 1. Szedd ki az összes termék nevét egy listába!
# elvárt: ['Laptop', 'Egér', 'Irodaszék']
print([termek['nev'] for termek in termekek])

# 2. Szedd ki az összes bruttó árat egy listába!
# elvárt: [190500, 10160, 57150]
print([termek['ar']['brutto'] for termek in termekek])

# 3. Szedd ki az összes cikkszámot egy listába!
# elvárt: ['A001', 'B042', 'C017']
print([termek["cikkszam"] for termek in termekek])

# -------------------------------------------------------
# transzformáció — [valami(elem) for elem in lista]
# -------------------------------------------------------

# 4. Készíts egy listát, ahol minden termék neve NAGYBETŰS!
# hint: str.upper()
# elvárt: ['LAPTOP', 'EGÉR', 'IRODASZÉK']
print([termek['nev'].upper() for termek in termekek])

# 5. Készíts egy listát a nettó árakból, de ezerben kifejezve!
# elvárt: [150.0, 8.0, 45.0]
print([termek['ar']['netto'] / 1000 for termek in termekek])

# -------------------------------------------------------
# szűrés — [elem for elem in lista if feltétel]
# -------------------------------------------------------

# 6. Szedd ki csak az elektronika kategóriájú termékek nevét!
# elvárt: ['Laptop', 'Egér']
print([termek["nev"] for termek in termekek if termek["kategoria"] == "elektronika"])

# 7. Szedd ki azokat a termékeket (az egész dict-et), amelyekből több mint 10 db van raktáron!
# elvárt: [{'cikkszam': 'A001', ...}, {'cikkszam': 'B042', ...}]
print([termek for termek in termekek if termek["keszlet"] > 10])

# 8. Szedd ki azokat a termék neveket, amelyek bruttó ára 50000 felett van!
# elvárt: ['Laptop', 'Irodaszék']
print([termek["nev"] for termek in termekek if termek["ar"]["brutto"] > 50000])