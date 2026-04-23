

class Auto:
    # class atribute
    kerekek_szama = 4
    gyartott_darab = 0

    # constructor
    def __init__(self, marka, szin, km):
        # instance attribute
        self.marka = marka
        self.szin = szin
        self.km = km


    def car_rides(self):
        print(f"The {self.marka} car rides")

    def tankol(self, liter):
        print(f"{self.marka} tankolt {liter} litert.")

    def km_hozzaad(self, megtett):
        self.km += megtett


class Termek:
    afa_kulcs = 0.27
    termekek_szama = 0

    def __init__(self, nev, netto_ar):
        self.nev = nev
        self.netto_ar = netto_ar
        Termek.termekek_szama += 1

    # classmethod - jellemzően classra vonatkozó metódusokra használjuk, Ezzel szignózzuk, hogy jelenleg nem a példányra hanem magára a classra vonatkozik az adott metódus
    @classmethod
    def print_darabszam(cls):
        print(f"Jelenlegi darabszám: {cls.termekek_szama}")

    @classmethod
    def brutto_szamol(cls, netto):
        print((cls.afa_kulcs * netto) + netto )

    @classmethod
    def brutto_arból(cls, nev, brutto_ar):
        netto = brutto_ar / (1 + cls.afa_kulcs)
        return cls(nev, netto)
    
    @staticmethod
    def afa_info():
        print("Az ÁFA kulcs Magyarországon általánosan 27%.")

alma = Termek("Alma", 15)
alma2 = Termek.brutto_arból("Alma", 127)

Termek.print_darabszam()
Termek.brutto_szamol(18)