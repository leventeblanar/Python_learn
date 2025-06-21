class Konyv:
    def __init__(self, cim, szerzo, oldalszam, read):
        self.cim = cim
        self.szerzo = szerzo
        self.oldalszam = oldalszam
        self.read = read

    def konyv_info(self):
        print(f"A könyv címe: {self.cim}")
        print(f"A könyv szerzője: {self.szerzo}")
        print(f"Oldalszám: {self.oldalszam}")
        if self.read:
            print(f"Már elolvastad a {self.cim} című könyvet.")
        else: 
            print(f"Még nem olvastad el a {self.cim} című könyvet.")
        print("\n")

class Hangoskonyv(Konyv):
    def __init__(self, cim, szerzo, oldalszam, read, narrator):
        super().__init__(cim, szerzo, oldalszam, read)
        self.narrator = narrator

    def konyv_info(self):
        super().konyv_info()
        print(f"Feolvasta: {self.narrator}")
        print("\n")


class Konyvtar:
    def __init__(self, nev):
        self.nev = nev
        self.konyvek = []

    def hozzaad_konyv(self, konyv):
        self.konyvek.append(konyv)

    def listaz_konyvek(self):
        print(f"\n{self.nev} könyvtár könyvei: ")
        for k in self.konyvek:
            k.konyv_info()
    
    def keres_cim_szerint(self, keresett_cim):
        print(f"\nKeresés: {keresett_cim}")
        talalat = False
        for k in self.konyvek:
            if k.cim.lower() == keresett_cim.lower():
                k.konyv_info()
                talalat = True

        if not talalat:
            print("Nincs ilyen című könyv a könyvtárban.")




konyv1 = Konyv('Gyűrűk ura', 'J. R. R. Tolkien', 1500, True)
hangoskonyv2 = Hangoskonyv('Harry Potter', 'J.K.Rowling', 2000, False, "Kulka János")
konyv2 = Konyv("Állatfarm", "George Orvwell", 500, True)

kvt = Konyvtar("Városi")

kvt.hozzaad_konyv(konyv1)
kvt.hozzaad_konyv(hangoskonyv2)
kvt.hozzaad_konyv(konyv2)

kvt.listaz_konyvek()

kvt.keres_cim_szerint("Állatfarm")
kvt.keres_cim_szerint("Forest Gump")