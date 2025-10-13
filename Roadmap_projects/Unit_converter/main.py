from units import normalize_unit
from engine import convert

MENU = {
    "1": ("length",  ["mm","cm","m","km","inch","foot","yard","mile"]),
    "2": ("weight",  ["mg","g","kg","oz","lb"]),
    "3": ("temperature", ["celsius","fahrenheit","kelvin"]),
}

def print_menu():
    print("****** UNIT CONVERTER ******")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")


def pick(options, prompt):

    for i, o in enumerate(options, 1):
        print(f" {i}. {o}")
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if 1 <= n <= len(options):
                return options[n-1]
        except ValueError:
            pass
        print(f"Adj meg 1..{len(options)} közötti számot.")


def main():
    print_menu()
    kind_key = input("Válassz (1,2,3)...").strip()
    if kind_key not in MENU:
        print(f"Válassz egyet a rendelkezésre álló opciókból..."); return
    kind, unit_opts = MENU[kind_key]
    
    from_unit = pick(unit_opts, "Válassz kiindulási mértékegységet... ")
    to_unit = pick(unit_opts, "Válassz cél mértékegységet... ")

    while True:
        raw = input("Érték (q = kilépés): ").strip().lower()
        if raw == "q":
            break

        try:
            val = float(raw.replace(",", "."))
        except ValueError:
            print("adj meg egy számot, pl. 12.5"); continue
        
        try:
            res = convert(kind, val, from_unit, to_unit)
            print(f"{val} {normalize_unit(from_unit)} -> {res} {normalize_unit(to_unit)}")
            return
        except Exception as e:
            print(f"Hiba az átváltás során: {e}")

if __name__ == "__main__":
    main()

