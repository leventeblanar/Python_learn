#  Pytest gyak.
import pytest
from datetime import datetime
from unittest.mock import MagicMock

def pelda1(a, b):
    return a + b

# def test_osszeadas():
#     assert pelda1(2, 3) == 5



def normalize_amount(value):
    if value <= 0:
        raise ValueError("Amount must be positive")

    value_float = float("{:.2f}".format(value))

    return value_float


# def test_normalize_amount_valid():
#     assert normalize_amount(36.683) == 36.68

# def test_normalize_amount_zero():
#     with pytest.raises(ValueError):
#         normalize_amount(0)

# def test_normalize_amount_negativ():
#     with pytest.raises(ValueError):
#         normalize_amount(-5)


def validald_szamla_datum(kelt: str, teljesites: str, fizetesi_hatarido: str) -> dict:

    hibak = []

    try:
        kelt_dt = datetime.strptime(kelt, "%Y-%m-%d")
    except ValueError:
        hibak.append("Hibás kelt formátum")
        return {"valid": False, "hibak": hibak}
    
    try:
        teljesites_dt = datetime.strptime(teljesites, "%Y-%m-%d")
    except ValueError:
        hibak.append("Hibás teljesítés formátum")
    
    try:
        hatarido_dt = datetime.strptime(fizetesi_hatarido, "%Y-%m-%d")
    except ValueError:
        hibak.append("Hibás fizetési hataridő formátum")

    
    if not hibak:
        if teljesites_dt < kelt_dt:
            hibak.append("Teljesítés nem lehet korábbi mint a kelt")
        if hatarido_dt < kelt_dt:
            hibak.append("A fizetési határidő nem lehet korábbi mint a kelt")
    
    return {"valid": len(hibak) == 0, "hibak": hibak}


# def test_valid_szamla_datum_minden_ok():
#     assert validald_szamla_datum("2026-02-03", "2026-03-04", "2026-03-30") == {"valid": True, "hibak": []}

# def test_valid_szamla_datum_hibas_kelt():
#     assert validald_szamla_datum("20026-02-03", "2026-03-04", "2026-03-30") == {"valid": False, "hibak": ["Hibás kelt formátum"]}

# def test_valid_szamla_datum_hibas_teljesites():
#     assert validald_szamla_datum("2026-02-03", "2026-033-04", "2026-03-30") == {"valid": False, "hibak": ["Hibás teljesítés formátum"]}

# def test_valid_szamla_datum_hibas_fizetesi():
#     assert validald_szamla_datum("2026-02-03", "2026-03-04", "2026-03-3300") == {"valid": False, "hibak": ["Hibás fizetési hataridő formátum"]}

# def test_valid_szamla_datum_korábbi_telj():
#     assert validald_szamla_datum("2026-02-03", "2025-03-04", "2026-03-30") == {"valid": False, "hibak": ["Teljesítés nem lehet korábbi mint a kelt"]}

# def test_valid_szamla_datum_korábbi_fiz():
#     assert validald_szamla_datum("2026-02-03", "2026-03-04", "2024-03-30") == {"valid": False, "hibak": ["A fizetési határidő nem lehet korábbi mint a kelt"]}

# def test_valid_szamla_datum_korábbi_mindketto():
#     assert validald_szamla_datum("2026-02-03", "2025-03-04", "2024-03-30") == {"valid": False, "hibak": ["Teljesítés nem lehet korábbi mint a kelt", "A fizetési határidő nem lehet korábbi mint a kelt"]}

