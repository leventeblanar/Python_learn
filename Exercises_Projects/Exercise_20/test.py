from element_notif_main import create_knaplo_bejegytracker
from db_config import get_hermes_connection

def check_table_exists():
    """Lekérdezi, hogy a knaplo_bejegytracker tábla létezik-e a Hermes adatbázisban."""
    conn = get_hermes_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT EXISTS (
        SELECT FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'knaplo_bejegytracker')
    """)
    
    exists = cur.fetchone()[0]
    conn.close()
    
    return exists

def insert_test_entry():
    """Beilleszt egy teszt bejegyzést a knaplo_bejegytracker táblába."""
    conn = get_hermes_connection()
    cur = conn.cursor()

    test_entry = (1, 'T1_DAS', 5901234567890, None)  # Vonalkód bejegyzés, cikkszám üres
    try:
        cur.execute("""
            INSERT INTO public.knaplo_bejegytracker (id, env_name, vonalkod, cikkszam, date_of_notif)
            VALUES (%s, %s, %s, %s, NOW())
            ON CONFLICT (id, env_name, vonalkod) DO NOTHING;
        """, test_entry)
        conn.commit()
        print("✅ Teszt bejegyzés sikeresen beszúrva!")
    except Exception as e:
        print(f"❌ Hiba történt a tesztadat beszúrásakor: {e}")
    finally:
        conn.close()

def fetch_test_entry():
    """Lekérdezi a teszt bejegyzést a táblából."""
    conn = get_hermes_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM public.knaplo_bejegytracker LIMIT 1;")
    row = cur.fetchone()
    conn.close()

    if row:
        print(f"✅ Tesztadat megtalálva: {row}")
    else:
        print("❌ Nem található teszt bejegyzés!")

if __name__ == "__main__":
    print("\n=== Táblalétrehozás Teszt ===")
    create_knaplo_bejegytracker()

    print("\n=== Ellenőrizzük, hogy létezik-e a tábla ===")
    if check_table_exists():
        print("✅ A tábla létezik!")
    else:
        print("❌ A tábla NEM jött létre!")

    print("\n=== Teszt bejegyzés beszúrása ===")
    insert_test_entry()

    print("\n=== Ellenőrizzük a beillesztett adatot ===")
    fetch_test_entry()
