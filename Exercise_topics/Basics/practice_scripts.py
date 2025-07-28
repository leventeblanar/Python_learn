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





def create_list_to_read_from():

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

    for kulcsszo in kulcsszavak:
        if kulcsszo in tantargyak:
            eredmeny.append(kulcsszo)
    
    print(eredmeny)



def filter_invalid_usernames():

    usernames = [
    "peter123",
    "anna",
    "béla",
    "Juli",
    "ka",
    "rozi!",
    "endre",
    "viola"
    ]

    valid_usernames = []

    for name in usernames:
        if (
            len(name) >= 3 and
            name.isalpha() and
            name.islower() and
            all(ord(c) < 128 for c in name)
        ):
            valid_usernames.append(name)

    print(valid_usernames)

def normalize_phone_numbers():

    szamok = [
    "+36 30 123 4567",
    "06301234567",
    "30-123-4567",
    "06 1 234 5678",
    "0670123456",
    "1234567890",
    "06-70-1234-567"
    ]

    valid_phone_numbers = []

    for szam in szamok:
        szam_onlydigits = szam.replace("-", "").replace(" ", "").replace("+", "").strip("")

        if szam_onlydigits.startswith("36") and len(szam_onlydigits) == 11:
            szam_onlydigits = "0" + szam_onlydigits[1:]

        if len(szam_onlydigits) == 11 and szam.startswith("06"): 
            format_szam = f"+36 {szam_onlydigits[2:4]} {szam_onlydigits[4:7]} {szam_onlydigits[7:11]}"
            valid_phone_numbers.append(format_szam)

        print(szam_onlydigits)

    print(valid_phone_numbers)

normalize_phone_numbers()