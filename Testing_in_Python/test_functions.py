from testing_simple_functions import valid_partner, valid_adoszam, szamitsd_fizetesi_hatarido


def test_valid_adoszam_helyes_formatum():
    assert valid_adoszam("32454460-4-06") == True

def test_valid_adoszam_hibas_formatum():
    assert valid_adoszam("32454460-4-") == False

def test_valid_adoszam_ures_string():
    assert valid_adoszam(" ") == False

def test_valid_adoszam_none():
    assert valid_adoszam(None) == False



def test_valid_partner_valid_partner():
    eredmeny = valid_partner({"Nev": "Lajos", "Adoszam": "23232323-2-23", "IsVevo": True})
    assert eredmeny["valid"] == True
    assert eredmeny["hibak"] == []

def test_valid_partner_hianyzo_nev():
    eredmeny = valid_partner({"Adoszam": "23232323-2-23", "IsVevo": True})
    assert eredmeny["valid"] == False
    assert eredmeny["hibak"] == ["Hiányzó név"]



def test_szamitsd_fizetesi_hatarido_valid_days():
    eredmeny = szamitsd_fizetesi_hatarido("2026-05-04", 45)
    assert eredmeny == "2026-06-18"

def test_szamitsd_fizetesi_hatarido_0():
    eredmeny = szamitsd_fizetesi_hatarido("2026-05-04", 0)
    assert eredmeny == "2026-05-04"