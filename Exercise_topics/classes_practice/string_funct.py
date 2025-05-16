from sqlalchemy import create_engine, exc, text

def get_local_db():
    
    try:
        return create_engine("postgresql+psycopg2://{user}:{pw}@{host}:{port}/{dbname}".format(
            user = "postgres",
            pw = "Brutal.shred01",
            host = "localhost",
            port = "5432",
            dbname = "practice"
        ))
    except Exception as e:
        print(f"Hiba a kapcsolat létrehozása során: {e}")
        
        
def create_table(table_name):
    
    engine = get_local_db()
    try:
        with engine.connect() as connection:
            connection.execute(
                text(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT,
                    phone TEXT,
                    age INT
                )
                """)
            )
            print(f"A tábla sikeresen létrehozva: {table_name}")
    except Exception as e:
        print(f"Hiba a tábla létrehozása során: {e}")
        
        
if __name__ == '__main__':
    create_table("users")
            