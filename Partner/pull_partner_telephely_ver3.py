import requests
import psycopg2
import sys
from collections import defaultdict
import pandas as pd

sys.stdout.reconfigure(encoding="UTF-8")
sys.stderr.reconfigure(encoding="UTF-8")

headers = {"Authorization": "ad815b38-3796-45eb-8a5c-fb935b02fe51"}
kornyezet = "p20"

### ATLAS CONNECTION
def get_conn():

    try:
        conn = psycopg2.connect(
                dbname = "atlas",
                user = "lblanar",
                password = "mUi1vNJUDH74zrh",
                host = "172.20.17.111",
                port = "5432"
            )
        return conn
    except psycopg2.Error as e:
        print(f"Hiba tortént a atlas kapcsolat létrehozása során: {e}")
        return None

### HERMES API LEKÉRÉS - P20
def hermes_api_lekeres():
    url = f"http://{kornyezet}.hermes.csihakft.hu:10002/api/kosar/PartnerTelephely/"
    params = {"$includeleft": "Partner;Cim;Cim.Telepules;Cim.KozteruletJelleg", "$filter": "D=0"}

    hermes_data = requests.get(url, headers=headers, params=params).json()

    hermes_telephely = hermes_data.get("Items", [])

    df = pd.json_normalize(hermes_telephely, sep=".")
    df.to_csv("hermes_telephelyek.csv", index=False, encoding="utf-8-sig")
    print("Hermes api lekérés csv-be exportálva.")

    return hermes_telephely

def atlas_lekeres():

    conn = get_conn()
    if conn is None:
        print("Sikertelen Atlas kapcsolat.")
        return []
    
    ## pt.id-t updateljük be Hermes külsőID-nak
    partner_query = """
    SELECT
    p.id as atlas_partner_id,
    pt.nev,
    pt.id as partner_telephely_id,
    t.nev as telepules, 
    pt.kozterulet_neve as kozterulet_nev, 
    kj.nev as kozterulet_jelleg, 
    pt.hazszam, 
    pt.epulet, 
    pt.lepcsohaz, 
    pt.emelet,
    pt.szekhely,
    pt.ajto, 
    pt.helyrajzi_szam 
    FROM atlas.partner_telephely pt
    LEFT JOIN atlas.partner p ON pt.partner_id = p.id and p.d = 0
    LEFT JOIN atlas.telepules t ON pt.telepules_id = t.id and t.d = 0
    LEFT JOIN atlas.kozterulet_jelleg kj ON pt.kozterulet_jelleg_id = kj.id and kj.d = 0
    WHERE pt.d = 0;
    """

    try:
        with conn.cursor() as cur:
            cur.execute(partner_query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            atlas_adatok = [dict(zip(columns, row)) for row in rows]
            return atlas_adatok
    except psycopg2.Error as e:
        print(f"Hiba történt a lekérdezés során: {e}")
        return []
    finally:
        conn.close()

def check_hermes_id_in_atlas():
    
    hermes_telephely = hermes_api_lekeres() ## itt még list of tuples ---> Ezzel fogom matchelni az atlas_match_tp-t
    atlas_telephely = atlas_lekeres() ## itt még list of tuples

    kulso_ids = set()

    ### Itt szedem ki a kulso_id-kat a hermes_api-s lekérésből
    for telephely in hermes_telephely:
        kulso_id = telephely.get("Partner", {}).get("KulsoId")
        if kulso_id:
            kulso_ids.add(int(kulso_id))


    # with open('kulsoId_hermes.txt', "w") as file:
    #     file.write(str(kulso_ids))
    ### Csekkolom az atlas partner Id-kat a kulso_ids listában
    atlas_match_tp = []

    for atl_teleph in atlas_telephely:
        if atl_teleph['atlas_partner_id'] in kulso_ids:
            atlas_match_tp.append(atl_teleph)
        
    print(len(atlas_match_tp))
    atlas_df = pd.DataFrame(atlas_match_tp)
    atlas_df.to_csv("atlas_partner_id_select.csv", index=False)
    print("Atlas adatok Partner Id alapján matchelve.")
    return atlas_match_tp

def normalize(value):
    ### Üres fieldek "" üres stringé alakítása
    if value is None:
        return ""

    return str(value)

def check_cim_egyezes(hermes_telephely, atlas_match_tp):
    egyezesek = []

    a = {}
    b = {}

    for hermes_tp in hermes_telephely:
        partner_id = int(hermes_tp.get("Partner", {}).get("KulsoId", 0))
        partner_telephely_id = int(hermes_tp.get("Id"))
        partner_telephely_kulso_id = (hermes_tp.get("KulsoId"))
        cim = hermes_tp.get("Cim", {})
        partner_nev = hermes_tp.get("Partner", {}).get("Nev")


        hermes_cim = {
            "nev": hermes_tp.get("Nev"),
            "partner_nev": partner_nev,
            "telepules": cim.get("Telepules", {}).get("Nev"),
            "kozterulet_nev": cim.get("KozteruletNev"),
            "kozterulet_jelleg": cim.get("KozteruletJelleg", {}).get("Nev"),
            "hazszam": cim.get("Hazszam"),
            "epulet": cim.get("Epulet"),
            "lepcsohaz": cim.get("Lepcsohaz"),
            "emelet": cim.get("Szint"),
            "ajto": cim.get("Ajto"),
            "helyrajzi_szam": cim.get("Hrsz")
        }

        for atlas_tp in atlas_match_tp:
            atlas_cim_a = {
                "nev": normalize(atlas_tp.get("nev")),
                "partner_nev": normalize(atlas_tp.get("partner_nev")),
                "telepules": normalize(atlas_tp.get("telepules")),
                "kozterulet_nev": normalize(atlas_tp.get("kozterulet_nev")),
                "kozterulet_jelleg": normalize(atlas_tp.get("kozterulet_jelleg")),
                "hazszam": normalize(atlas_tp.get("hazszam")),
                "epulet": normalize(atlas_tp.get("epulet")),
                "lepcsohaz": normalize(atlas_tp.get("lepcsohaz")),
                "emelet": normalize(atlas_tp.get("emelet")),
                "ajto": normalize(atlas_tp.get("ajto")),
                "helyrajzi_szam": normalize(atlas_tp.get("helyrajzi_szam"))
            }

            atlas_cim_b = {
                "nev":atlas_tp.get("nev"),
                "partner_nev": atlas_tp.get("partner_nev"),
                "telepules":atlas_tp.get("telepules"),
                "kozterulet_nev": atlas_tp.get("kozterulet_nev"),
                "kozterulet_jelleg": atlas_tp.get("kozterulet_jelleg"),
                "hazszam": atlas_tp.get("hazszam"),
                "epulet": atlas_tp.get("epulet"),
                "lepcsohaz": atlas_tp.get("lepcsohaz"),
                "emelet": atlas_tp.get("emelet"),
                "ajto": atlas_tp.get("ajto"),
                "helyrajzi_szam": atlas_tp.get("helyrajzi_szam"),
            }

            key = f"{normalize(hermes_cim['nev'])},{normalize(hermes_cim['telepules'])},{normalize(hermes_cim['kozterulet_nev'])},{normalize(hermes_cim['kozterulet_jelleg'])},{normalize(hermes_cim['hazszam'])},{normalize(hermes_cim['epulet'])},{normalize(hermes_cim['ajto'])},{normalize(hermes_cim['helyrajzi_szam'])}"
            
            if hermes_cim['nev'] == atlas_cim_a['nev'] and hermes_cim['telepules'] == atlas_cim_a['telepules'] and hermes_cim['kozterulet_nev'] == atlas_cim_a['kozterulet_nev'] and hermes_cim['kozterulet_jelleg'] == atlas_cim_a['kozterulet_jelleg'] and hermes_cim['hazszam'] == atlas_cim_a['hazszam'] and hermes_cim['epulet'] == atlas_cim_a['epulet'] and hermes_cim['ajto'] == atlas_cim_a['ajto'] and hermes_cim['helyrajzi_szam'] == atlas_cim_a['helyrajzi_szam']:
                a[key] = {
                    "atlas_telephely_id": atlas_tp["partner_telephely_id"],
                    "partner/külső_id": partner_id,
                    "hermes_telephely_id": partner_telephely_id,
                    "partner_telephely_kulso_id": partner_telephely_kulso_id,
                    "partner_nev_hermes": hermes_tp["Partner"]["Nev"],
                    "telepules_hermes": hermes_cim["telepules"],
                    "kozterulet_nev_hermes": hermes_cim["kozterulet_nev"],
                    "kozterulet_jelleg_hermes": hermes_cim["kozterulet_jelleg"],
                    "hazszam_hermes": hermes_cim["hazszam"],
                }

            if hermes_cim['nev'] == atlas_cim_b['nev'] and hermes_cim['telepules'] == atlas_cim_b['telepules'] and hermes_cim['kozterulet_nev'] == atlas_cim_b['kozterulet_nev'] and hermes_cim['kozterulet_jelleg'] == atlas_cim_b['kozterulet_jelleg'] and hermes_cim['hazszam'] == atlas_cim_b['hazszam'] and hermes_cim['epulet'] == atlas_cim_b['epulet'] and hermes_cim['ajto'] == atlas_cim_b['ajto'] and hermes_cim['helyrajzi_szam'] == atlas_cim_b['helyrajzi_szam']:
                b[key] = {
                    "atlas_telephely_id": atlas_tp["partner_telephely_id"],
                    "partner/külső_id": partner_id,
                    "hermes_telephely_id": partner_telephely_id,
                    "partner_telephely_kulso_id": partner_telephely_kulso_id,
                    "partner_nev_hermes": hermes_tp["Partner"]["Nev"],
                    "telepules_hermes": hermes_cim["telepules"],
                    "kozterulet_nev_hermes": hermes_cim["kozterulet_nev"],
                    "kozterulet_jelleg_hermes": hermes_cim["kozterulet_jelleg"],
                    "hazszam_hermes": hermes_cim["hazszam"],
                }

    x = a | b
    egyezesek = [i for i in x.values()]
                

    ossz_egyez_df = pd.DataFrame(egyezesek)
    ossz_egyez_df.to_csv(f"kornyezet_csv/egyezesek_{kornyezet}.csv", index=False, encoding="utf-8-sig")


    



def hermes_api_put(hermes_telephely_id, kulso_id):

    url = f"http://{kornyezet}.hermes.csihakft.hu:10002/api/kosar/PartnerTelephely/{hermes_telephely_id}"
    params = {"$includeleft": "Partner;Cim;Cim.Telepules;Cim.KozteruletJelleg", "$filter": "D=0"}

    hermes_data = requests.get(url, headers=headers, params=params).json()
    hermes_data['KulsoId'] = kulso_id

    resp = requests.put(url, headers=headers, json=hermes_data)

    print(resp.status_code)
    

if __name__ == "__main__":
    hermes__telephely = hermes_api_lekeres()
    atlas_telephely = check_hermes_id_in_atlas()

    check_cim_egyezes(hermes__telephely, atlas_telephely)

    egyezesek_df = pd.read_csv(f"kornyezet_csv/egyezesek_{kornyezet}.csv")

    for idx, row in egyezesek_df.iterrows():
        hermes_telephely_id = int(row["hermes_telephely_id"])
        kulso_id = str(row["atlas_telephely_id"])

        print(f"HermesID = {hermes_telephely_id} , Atlas KulsoId = {kulso_id}")
        # hermes_api_put(hermes_telephely_id, kulso_id)
    
    print("Futtatás vége.")