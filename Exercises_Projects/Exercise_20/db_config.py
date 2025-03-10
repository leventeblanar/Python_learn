from sqlalchemy import create_engine, exc
import psycopg2

DAS_DB_CONFIG = {
    "user": "lblanar",
    "password": "*",
    "host": "*",  # Az összes DAS adatbázis ezen a szerveren van
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
                user = "lblanar",
                password = "*",
                host = "*",
                dbname = "hermes",
                port = "5434"
            )
        return conn
    except psycopg2.Error as e:
        print(f"Hiba tortént a kapcsolat létrehozása során: {e}")
        return None