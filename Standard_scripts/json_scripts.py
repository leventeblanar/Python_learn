import json
import pandas as pd

def read_sql_export_json():

 ## This function is for reading a given sql script with the help of pandas and converting it to json
 ## and finally exporting a json file of it

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



def insert_into_sql():

    conn = get_connection()
    cur = conn.cursor()

    try:
        with open('jsonfile.json', 'r') as file:
            json_data = json.load(file)
    except Exception as e:
        print(f"Hiba a json betöltésekor: {e}")
    for record in json_data:
        try:
            cur.execute("""
            INSERT INTO destination.table (
            destination field1, destination field2, destination field3,....
            ) VALUES (
                %(id)s, NULL, NULL, %(d)s, %(version_num)s, to_timestamp(%(created_at)s / 1000.0), 
                %(created_by)s, to_timestamp(%(modified_at)s / 1000.0), %(modified_by)s, 
                %(megjegyzes)s, %(partner_id)s, %(szallito_id)s, %(partner_szallito_kod)s, 
                %(keri_e)s, %(kredit_limit)s
            )
            """, {
                'id': record.get('id'),
                'd': record.get('d'),
                'version_num': record.get('version_num'),
                'created_at': record.get('created_at'),
                'created_by': record.get('created_by'),
                'modified_at': record.get('modified_at'),
                'modified_by': record.get('modified_by'),
                'megjegyzes': record.get('megjegyzes'),
                'partner_id': record.get('partner_id'),
                'szallito_id': record.get('szallito_id'),
                'partner_szallito_kod': record.get('partner_szallito_kod'),
                'keri_e': record.get('keri_e'),
                'kredit_limit': record.get('kredit_limit')
            })
            ## To explain the process here - in the for loop record is one record in the json file
            ## below the VALUES section we have to show the script that in the record, which key stores which data
            ## the new keys are added in the SQL with %()s
        except Exception as e:
            print(f"Sikertelen adatfeltöltés: {e}")
    
    conn.commit()
    print("Adatok sikeresen feltöltve.")


def format_excel():

    df = function_where_we_query_the_df()
    if not os.path.exists('report'):
        os.makedirs('report')

    with pd.ExcelWriter('dest_fold/file.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
        worksheet = writer.sheets['sheet1']

        for i, col in enumerate(df.columns):
            max_length = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(i, i, max_length)