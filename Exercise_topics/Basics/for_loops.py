def szamlalo():
    for item in range(1,11):
        print(item)
        
        
def paros_szam_szamlalo():
    
    osszeg = 0
    
    for num in range(1,101):
        if num % 2 == 0:
            osszeg += num
    
    print(f"A páros számok összege {osszeg}")


def karakter_szamolo():
    
    szoveg = "Alma a fa alatt"
    szamlalo = 0
    
    for c in szoveg:
        if c == "a" or c == "A":
            szamlalo += 1
            
    print(szamlalo)


def szoszamlalo():
    
    szoveg = "ez egy laza kis feladat"
    szoszam = 0
    
    for c in szoveg:
        if c == " ":
            szoszam += 1
            
    szoszam += 1 # ez amiatt mert a mondat végén nem lesz szóköz, de muszáj adni plusz egyet, mert az utolsó szót nem fogja számolni.
            
    print(f"A példaszöveg: '{szoveg}'")
    print(szoszam)
    
    
    
def mag_mas_szamlalo():
    
    szoveg = "Ez egy egyszerű szöveg."
    maganhangzok = 0
    massalhangzok = 0
    
    mag_hang = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű",]
    irasjelek = [".", ",", "!", "?", " "]

    for c in szoveg.lower():
        if c in mag_hang:
            maganhangzok += 1
        elif c in irasjelek:
            continue 
        else:
            massalhangzok += 1
            
    print(f"Magánhangzók száma: {maganhangzok}")
    print(f"Mássalhangzók száma: {massalhangzok}")
    


# enumerate() = automatikusan létrehoz egy sorszámot (indexet), és mellé az adott elemet

def nagybet_alakít():
    
    szoveg = "Szeretek pythonban programozni, de azt azért nem mondanám, hogy ez az életem haverom. Csak, hogy értsd az utalást. Szólj, ha észrevetted, hogy ezt neked írtam direktben."
    uj_szoveg = ""

    for index, c in enumerate(szoveg, start=0):
        if index % 2 == 1:
            uj_szoveg += c.lower()
        elif index % 2 == 0:
            uj_szoveg += c.upper()
            
    print(uj_szoveg)
            
            
            
def count_word_five():
    
    szoveg = "Szeretek pythonban programozni, de azt azért nem mondanám, hogy ez az életem haverom."
    szavak = szoveg.split()
    
    

    for index, szo in enumerate(szavak):
        szo = szo.strip(".,?!")
        if len(szo) >=5:
            print(index, szo)
        

def short_word_count():
    
    szoveg = "Ez itt egy újabb próba, ami segít gyakorolni az enumerate használatát Pythonban."
    szavak = szoveg.split()
    
    for index, szo in enumerate(szavak):
        szo = szo.strip(".,?!")
        if len(szo) <= 3:
            print(index, szo)



def clean_words():
    
    szoveg = "Ez egy próba-szöveg! Tisztán@ kellene látnunk, mi marad meg?"

    szavak = szoveg.split()

    for szo in szavak:
        szo = szo.strip(",.?!@")
        if szo.isalpha():
            print(szo)
            
clean_words()