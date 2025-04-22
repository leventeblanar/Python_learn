import requests
import json

header = {"Authorization": "8b6c9926-c544-4a1d-980f-06ace5ebda4e"}
param = {}

# class Cikk:
#     def __init__(self, nev: str, cikkszam: str, kulsoid: str, istapadog: bool):
#         self.nev = nev
#         self.cikkszam = cikkszam
#         self.kulsoid = kulsoid
#         self.istapadog = istapadog
    
#     @classmethod
#     def from_json(cls, data):
#         nev = data.get("Nev", "")
#         cikkszam = data.get("Cikkszam", "")
#         kulsoid = data.get("KulsoId", "")
#         istapadog = data.get("IsTapadoGongyoleg", "")
#         return cls(nev, cikkszam, kulsoid, istapadog)
    
#     def print_info(self):
#         print(f"Név: {self.nev}")
#         print(f"Cikkszám: {self.cikkszam}")
#         print(f"KülsőId: {self.kulsoid}")
#         print(f"Tapadógöngyöleg: {self.istapadog}")
#         print("_" * 40)

# def fetch_cikk():
#     url = "<place_link"
#     response = requests.get(url, headers=header, params=param)

#     if response.status_code == 200:
#         cikk_data = response.json().get("Items", [])
#         print(type(cikk_data))
#         if isinstance(cikk_data, dict):
#             print("Kulcsok:", list(cikk_data.keys()))
#         return[Cikk.from_json(cikk) for cikk in cikk_data]
#     else:
#         print("Hiba történt a lekérdezéskor.")
#         return []

# if __name__ == '__main__':
#     cikkek = fetch_cikk()

#     for cikk in cikkek:
#         cikk.print_info()


class Partner:
    def __init__(self, nev: str, partnerid: int, szekhely: bool, id:int, edt: str):
        self.nev = nev
        self.partnerid = partnerid
        self.szekhely = szekhely
        self.id = id
        self.edt = edt

    @classmethod
    def from_json(cls, data):
        nev = data.get("Nev", "")
        partnerid = data.get("PartnerId", "")
        szekhely = data.get("IsSzekhely", "")
        id = data.get("Id", "")
        edt = data.get("EDt", "")
        return cls(nev, partnerid, szekhely, id, edt)

    def print_info(self):
        print("__Telephely adatok__")
        print(f"Név: {self.nev}")
        print(f"PartnerId: {self.partnerid}")
        print(f"Székhely: {self.szekhely}")
        print(f"Id: {self.id}")
        print(f"Utolsó módosítás: {self.edt}")
        print("_" * 40)

def fetch_data():
    url = "<paste link>"
    response = requests.get(url, headers=header, params=param)

    if response.status_code == 200:
        partnertelephely_data = response.json().get("Items", [])
        return [Partner.from_json(partnertelep) for partnertelep in partnertelephely_data]
    else:
        print("A lekérdezés nem sikerült")
        return []
    

def save_to_json(partner_list, filename):

    data = []
    for partner in partner_list:
        data.append({
            "Nev": partner.nev,
            "PartnerId": partner.partnerid,
            "IsSzekhely": partner.szekhely,
            "Id": partner.id,
            "EDt": partner.edt
        })

    with open(filename, "w", encoding="utf-8") as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)

    print(data)


if __name__ == '__main__':

    partnertelephelyek = fetch_data()

    for partnertelephely in partnertelephelyek:
        partnertelephely.print_info()

    save_to_json(partnertelephelyek, 'partner_telephelyek.json')