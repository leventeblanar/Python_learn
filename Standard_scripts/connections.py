from sqlalchemy import create_engine, exc
import psycopg2


def get_engine():

    try:
        engine = create_engine("postgresql+psycopg2://{user}:{pw}@{host}:{port}/{dbname}".format(
            user = "****",
            pw = "****",
            host = "****",
            dbname = "****",
            port = "****"
        ))
        return engine
    except Exception as e:
        print(f"Nem sikerült létrehozni az adatbázis kapcsoaltot. Hiba: {e}")
        return None
    


def get_connection():

    try:
        conn = psycopg2.connect(
                user = "****",
                password = "****",
                host = "****",
                dbname = "****",
                port = "****"
            )
        return conn
    except psycopg2.Error as e:
        print(f"Hiba tortént a kapcsolat létrehozása során: {e}")
        return None