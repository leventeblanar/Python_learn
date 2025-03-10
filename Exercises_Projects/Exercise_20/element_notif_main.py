import pandas as pd
from db_config import get_engine, get_hermes_connection
from nio import AsyncClient
import asyncio
import re
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# ELEMENT login cred
MATRIX_HOMESERVER = "https://matrix.dataedge.io"
USERNAME = "@lblanar:matrix.dataedge.io"
ROOM_ID_20 = "!nMJdpxekfNmGomECrS:matrix.dataedge.io"
ROOM_ID_70 = "!LFWCcYzgkWZQuqwYwc:matrix.dataedge.io"
ACCESS_TOKEN = "syt_bGJsYW5hcg_XefYmeEsMNBrymYGwlID_1NnLTq"

# func for checking if k_naplo_id_tracker table exists, if not create it
def create_knaplo_bejegytracker():
    conn = get_hermes_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_schema = 'test_analytics'
            AND table_name = 'knaplo_bejegytracker')
            """)
        
        table_exists = cur.fetchone()[0]

        if table_exists:
            print("The ""knaplo_bejegytracker"" table already exists.")
        else:
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS test_analytics.knaplo_bejegytracker(
            id BIGINT,
            env_name VARCHAR(50),
            vonalkod BIGINT,
            cikkszam BIGINT,
            date_of_notif TIMESTAMP DEFAULT NOW(),
            PRIMARY KEY (id, env_name, vonalkod)
            );
            """

            cur.execute(create_table_sql)
            print(f"Table for tracking Kassza naplo entries has been created.")

        conn.commit()

    except Exception as e:
        print(f"An error occured during the creation of the Kassza Naplo entries table: {e}")
    finally:
        conn.close()

# func for loading the already used ids to avoid duplicate messages
def load_sent_entries(database_name):
    conn = get_hermes_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, env_name, vonalkod, cikkszam FROM test_analytics.knaplo_bejegytracker WHERE env_name = %s;
    """, (database_name,))

    sent_entries= {(row[0], row[1], row[2], row[3]) for row in cur.fetchall()}

    cur.close()
    conn.close()

    return sent_entries

# func for saving the ids and the environments linked to them
def save_sent_entries(new_entries, database_name):
    
    if not new_entries:
        return
    
    conn = get_hermes_connection()
    cur = conn.cursor()

    insert_query = """
        INSERT INTO test_analytics.knaplo_bejegytracker (id, env_name, vonalkod, cikkszam, date_of_notif)
        VALUES (%s, %s, %s, %s, NOW())
        ON CONFLICT (id, env_name, vonalkod) DO NOTHING;
    """

    cur.executemany(insert_query, new_entries)
    conn.commit()

    cur.close()
    conn.close()

# func for checking the Kassza naplo and Konstans table - in case of not empy new_rows - send matrix message
async def get_latest_entries(database_name):

    print(f"Lekérdezés indítása: {database_name}")
    
    global already_reported
    already_reported = load_sent_entries(database_name)
    engine = get_engine(database_name)

    while True:
        query = """
        SELECT
        kn."ID",
        kn."K_NAPLO_TIPUS", 
        kn."K_PROGRAM_STATUSZ", 
        kn."K_PROGRAM_ALSTATUSZ",
        kn."MEGJEGYZES",
        kt. "LEIRAS"
        FROM "KASSZA_NAPLO" AS kn
        INNER JOIN "KONSTANS" kt ON kn."K_NAPLO_TIPUS" = kt."ERTEK" AND kt."TIPUS"  = 'KASSZA_NAPLO_TIPUS_CONST'
        WHERE kn."K_NAPLO_TIPUS" = 70 OR  kn. "MEGJEGYZES" ILIKE '%%nincs ára%%'
        ORDER BY kn. "ID" DESC
        LIMIT 5;
        """

        try:
            with engine.connect() as connection:
                df = pd.read_sql(query, connection)
                print(df.head())

            if df.empty:
                print(f"⚠️ Nincs új adat a {database_name} adatbázisban.")
                await asyncio.sleep(60)  # 60 másodperc várakozás, hogy ne legyen infinite loop
                continue

            
            new_entries = []
            for _, row in df.iterrows():
                naplo_id = row["ID"]
                tipus = row["K_NAPLO_TIPUS"]
                statusz = row["K_PROGRAM_STATUSZ"]
                alstatusz = row["K_PROGRAM_ALSTATUSZ"]
                megjegyzes = row["MEGJEGYZES"]
                leiras = row["LEIRAS"]

                vonalkod = None
                cikkszam = None

                if (naplo_id, database_name) in already_reported:
                    continue

                if tipus == 70:
                    vonalkod = megjegyzes.strip()
                    cikkszam = None
                    print(f"📤 Küldés 70-es típus: Vonalkód = {vonalkod}")
                    await send_70_message(database_name, naplo_id, vonalkod, megjegyzes, statusz, alstatusz, leiras)

                elif tipus == 20:
                    match = re.search(r'Cikkszám: (\d+)', megjegyzes)
                    cikkszam = match.group(1) if match else None
                    vonalkod = None
                    
                    if cikkszam is None:
                        print(f"⚠️ Cikkszámot nem sikerült kinyerni! (ID: {naplo_id})")
                        continue

                    print(f"📤 Küldés 20-es típus: Cikkszám = {cikkszam}")
                    await send_20_message(database_name, naplo_id, cikkszam, megjegyzes, statusz, alstatusz, leiras)



                if (naplo_id, vonalkod if vonalkod else cikkszam) in already_reported:
                    continue

                new_entries.append((naplo_id, database_name, vonalkod, cikkszam))
            
            save_sent_entries(new_entries, database_name)
                    

        except Exception as e:
            print(f"Error while pulling query: {e}")

# func for formatting message and send
async def send_20_message(database_name, naplo_id, cikkszam, megjegyzes, statusz, alstatusz, leiras):

    if cikkszam is None:
        print(f"Cikkszám hiányzik, nem küldünk üzenetet. (ID: {naplo_id})")
        return

    client = AsyncClient(MATRIX_HOMESERVER, USERNAME)
    client.access_token = ACCESS_TOKEN
    client.user_id = USERNAME
    
    message = (
        f"** Ár nélküli termék **\n"
        f"-----------------------\n"
        f"Forrás: {database_name}"  
        f"Cikkszám: {cikkszam}"
        f"ID: {naplo_id}"
        f"Hiba üzenet: {megjegyzes}"
        f"Státusz: {statusz}"
        f"Alstátusz: {alstatusz}"
        f"Leírás: {leiras}"
               )
    
    try:
        await client.room_send(
            room_id=ROOM_ID_20,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": message}
        )
        print(f"Üzenet sikeresen elküldve (20-as típus): {naplo_id}") 
    finally:
        await client.close()

async def send_70_message(database_name, naplo_id, vonalkod, megjegyzes, statusz, alstatusz, leiras):

    if vonalkod is None:
        print(f"Vonalkód hiányzik, nem küldünk üzenetet. (ID: {naplo_id})")
        return

    client = AsyncClient(MATRIX_HOMESERVER, USERNAME)
    client.access_token = ACCESS_TOKEN
    client.user_id = USERNAME
    
    message = (
        f"** Ismeretlen vonalkód **\n"
        f"-----------------------\n"
        f"Forrás: {database_name}"  
        f"Vonalkód: {vonalkod}"
        f"ID: {naplo_id}"
        f"Hiba üzenet: {megjegyzes}"
        f"Státusz: {statusz}"
        f"Alstátusz: {alstatusz}"
        f"Leírás: {leiras}"
               )
    
    try:
        await client.room_send(
            room_id=ROOM_ID_70,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": message}
        )
        print(f"Üzenet sikeresen elküldve (70-es típus): {naplo_id}")
    finally:
        await client.close()


async def main():

    databases = [f"T{i}_DAS" for i in range(1, 10)]
    tasks = [get_latest_entries(db) for db in databases]  # Creating coroutines to enable several get_latest functions to run simultaneously
    await asyncio.gather(*tasks)
    

if __name__ == '__main__':
    create_knaplo_bejegytracker()
    try:
        asyncio.run(main()) 
    except RuntimeError: 
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())