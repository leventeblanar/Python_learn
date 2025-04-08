import json
import pandas as pd

def get_engine():

    engine = get_engine()

    if engine is None:
        print("Nem sikerült létrehozni az adatbázis kapcsolatot.")
        return None

    try:
        with engine.connect() as connection:
            query = """
            ********
            """
            json_data = pd.read_sql(query, connection).to_json(orient='records')
            print(json_data)
    except Exception as e:
        print(f"Hiba történt az adatlekérdezés során: {e}")
        return None
    
    with open('data.json', 'w') as file:
        file.write(json_data)
