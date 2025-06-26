def select_emails():

    adatok = [
    "peter@gmail.com",
    "nememail.com",
    "hello@valami",
    "teszt@abc.hu",
    "ez.sem.jo",
    "no@dot"
    ]

    valid_emails = [s for s in adatok if "@" in s and "." in s.split("@")[-1]]
    print(valid_emails)



def capitelize_institution_names():

    adatok = [
        "moricz zsigmond általános iskola",
        "szegedi tudomany egyetem"
    ]

    for adat in adatok:
        adat_split = (adat.split(" "))
        capitelized =( [s.capitalize() for s in adat_split])
        uj_nev = " ".join(capitelized)
        print(uj_nev)
        

def normalize_words():

    tantargyak = [
    "matek",
    "fizika",
    "foldrajz",
    "testneveles",
    "irodalom",
    "tortenelem",
    "kemia",
    "biologia",
    "informatika",
    "enektanctestneveles"
    ]

    kulcsszavak = [
        "enek", "tanc", "testneveles", "matek", "fizika", "foldrajz",
        "irodalom", "tortenelem", "kemia", "biologia", "informatika"
    ]


    eredmeny = []
    
    for szo in tantargyak:
        i = 0
        while i<len(szo):
            talalat = False
            for kulcs in sorted(kulcsszavak, key=len, reverse=True):
                if szo[i:].startswith(kulcs):
                    eredmeny.append(kulcs)
                    i+=len(kulcs)
                    talalat = True
                    break
            if not talalat:
                i+=1
    
    nagybetusek = []
    
    for item in eredmeny:
        nagybetusek.append(item.capitalize())

    print(nagybetusek)

def create_normal_form():

    rovidites_szo = {
    "elte": "eötvös loránd tudományegyetem",
    "bme": "budapesti műszaki és gazdaságtudományi egyetem",
    "szte": "szegedi tudományegyetem",
    "ttk": "természettudományi kar",
    "ikt": "informatikai kar",
    "info": "informatika",
    "irod": "irodalom",
    "bio": "biológia",
    "kem": "kémia",
    "matek": "matematika",
    "tesi": "testnevelés"
    }
    
    eredmeny = []

    for rovid, hosszu in rovidites_szo.items():
        eredmeny.append(hosszu.title())

    print(eredmeny)



def short_form():

    intezmenyek = [
    "eotvos lorand tudomanyegyetem",
    "budapesti muszaki es gazdasagtudomanyi egyetem",
    "szegedi tudomanyegyetem",
    "informatikai kar",
    "informatika",
    "matematika",
    "biologia",
    "ismeretlen egyetem"
    ]

    hosszu_to_rovid = {
        "eotvos lorand tudomanyegyetem": "elte",
        "budapesti muszaki es gazdasagtudomanyi egyetem": "bme",
        "szegedi tudomanyegyetem": "szte",
        "termeszettudomanyi kar": "ttk",
        "informatikai kar": "ikt",
        "informatika": "info",
        "irodalom": "irod",
        "biologia": "bio",
        "kemia": "kem",
        "matematika": "matek",
        "testneveles": "tesi"
    }

    for hosszu, rovid in hosszu_to_rovid.items():
        if hosszu in intezmenyek:
            print(rovid)
        else:
            print(f"No match for {hosszu}")

    for nev in intezmenyek:
        rovidites = hosszu_to_rovid.get(nev, "???")
        print(f"{nev.title()} -> {rovidites.upper()}")

short_form()





