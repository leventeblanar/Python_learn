

def ellenoriz_valasz(jatekos_v, helyes_v):
    if jatekos_v is None:
        raise ValueError("Hiányzó játékos válasz")

    jatekos_v_generalized = jatekos_v.strip().lower()
    helyes_v_generalized = helyes_v.strip().lower()


    if jatekos_v_generalized == helyes_v_generalized:
        return "Helyes válasz!", True
    else:
        return "Sajnos nem jó...", False

def tovabbjut_e(aktualis_valasz_helyes: bool) -> bool:
    if aktualis_valasz_helyes:
        return True
    elif not aktualis_valasz_helyes:
        return False


if __name__ == "__main__":


    kerdesek = {
    "A katica bogár?": "Igen",
    "A focilabda milyen formájú?": "Gömb",
    "Hány lába van egy póknak?": "8",
    "Milyen színű az ég derült időben?": "Kék",
    "Mi Magyarország fővárosa?": "Budapest",
    "Melyik évszak után jön a nyár?": "Tavasz",
    "A víz nedves?": "Igen",
    "Mennyi 5 meg 5?": "10",
    "Melyik állat mondja azt, hogy vau?": "Kutya",
    "A Nap éjszaka süt?": "Nem"
    }

    pontszam = 0
    korok = 1
    nyeremeny = False
    nyeremeny_osszeg = 0

    for kerdes, valasz in kerdesek.items():
        print(f"Kérdések: {korok}/10")
        jatekos_valasz = input(f"{kerdes}: ")

        eredmeny_str, eredmeny_bool = ellenoriz_valasz(jatekos_valasz, valasz)
        if tovabbjut_e(eredmeny_bool):
            pontszam += 1
            korok += 1
        else:
            break

        if pontszam == 10:
            print("Játék vége.")
        print(eredmeny_str)
        print(pontszam)

    match pontszam:
        case 1 | 2 | 3 | 4 :
            nyeremeny_osszeg = 0
        case 5 | 6 | 7 | 8 | 9:
            nyeremeny_osszeg = 500000
        case 10:
            nyeremeny_osszeg = 1000000

    print(f"Sajnos vesztettél. A nyereményed: {nyeremeny_osszeg}")
