from sqlalchemy import create_engine, exc

def get_engine_taltos():

    try:
        engine = create_engine("postgresql+psycopg2://{user}:{pw}@{host}:{port}/{dbname}".format(
            user = "lblanar",
            pw = "****",
            host = "****",
            dbname = "****",
            port = "****"
        ))
        return engine
    except Exception as e:
        print(f"Nem sikerült létrehozni az adatbázis kapcsoaltot. Hiba: {e}")
        return None