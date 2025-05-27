class Auto:
    def __init__(self, marka, evjarat):
        self.marka = marka
        self.evjarat = evjarat
        
    def info(self):
        print(f"Az auto márkája: {self.marka}")
        print(f"Az auto évjárata: {self.evjarat}")
        
        
auto1 = Auto("Toyota", 2012)
auto1.info()