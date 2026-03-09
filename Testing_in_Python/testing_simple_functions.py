import re
import datetime

def valid_adoszam(adoszam: str) -> bool:

    if not isinstance(adoszam, str):
        return False
    pattern = r"^\d{8}-\d-\d{2}$"
    return bool(re.match(pattern, adoszam))




def valid_partner(partner: dict) -> dict:

    hibak = []

    if not partner.get("Nev"):
        hibak.append("Hiányzó név")
    if not partner.get("Adoszam"):
        hibak.append("Hiányzó adószam")
    elif not valid_adoszam(partner["Adoszam"]):
        hibak.append("Érvénytelen adószám formátum")
    
    if not partner.get("IsVevo") and not partner.get("IsSzallito"):
        hibak.append("Partner sem vevő sem szállító")
    
    return {
        "valid": len(hibak) == 0,
        "hibak": hibak
    }




def szamitsd_fizetesi_hatarido(szamla_datum: str, fizetesi_nap: int) -> str:
    
    szamla_datum_date = datetime.datetime.strptime(szamla_datum, "%Y-%m-%d")
    print(szamla_datum_date)
    fizhat_date = szamla_datum_date + datetime.timedelta(days=fizetesi_nap)
    print(fizhat_date)
    fizhat_date_str = fizhat_date.strftime("%Y-%m-%d")
    print(fizhat_date)

    return fizhat_date_str


szamitsd_fizetesi_hatarido("2026-02-04", 30)