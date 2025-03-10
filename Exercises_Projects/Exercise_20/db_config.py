from sqlalchemy import create_engine, exc
import psycopg2

DAS_DB_CONFIG = {
    "user": "postgres",
    "password": "Brutal.shred01",
    "host": "localhost",  # Az összes DAS adatbázis ezen a szerveren van
    "port": "5432"
}

def get_engine(database_name):
    # EZT MÉG KORRIGÁLNI KELL - KAPCSOLATI ADATOK NEM PASSZOLNAK
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{DAS_DB_CONFIG['user']}:{DAS_DB_CONFIG['password']}@{DAS_DB_CONFIG['host']}:{DAS_DB_CONFIG['port']}/{database_name}"
        )
        return engine
    except Exception as e:
        print(f"Hiba tortént a kapcsolat létrehozása során: {e}")
        return None
    
def get_hermes_connection():
    try:
        conn = psycopg2.connect(
                user = "postgres",
                password = "Brutal.shred01",
                host = "localhost",
                dbname = "postgres",
                port = "5432"
            )
        return conn
    except psycopg2.Error as e:
        print(f"Hiba tortént a kapcsolat létrehozása során: {e}")
        return None
