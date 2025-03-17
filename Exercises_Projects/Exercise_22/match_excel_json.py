from sqlalchemy import create_engine, exc
import pandas as pd
from openpyxl import load_workbook
import sys
import json

sys.stdout.reconfigure(encoding="UTF_8")
sys.stderr.reconfigure(encoding="UTF_8")

def get_engine_p4():

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
    
    
def main():

    bevet_df = pd.read_excel('p36_tpd.xlsx')

    bevet_df['qty'] = pd.to_numeric(bevet_df['qty'], errors='coerce')
    
    json_file = 'itemlist.json'
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if 'dax_szamla_cikkszam' not in bevet_df.columns:
        raise ValueError("A 'dax_tapado_cs' oszlop nem található az Excel fájlban")
    
    excel_items = bevet_df['dax_szamla_cikkszam'].astype(str).tolist()
    print(len(excel_items))

    json_items = [str(item["itemid"]) for item in data["items"]]
    print(len(json_items))

    excel_set = set(excel_items)
    json_set = set(json_items)

    missing_from_excel = json_set - excel_set
    missing_from_json = excel_set - json_set


    if not missing_from_excel and not missing_from_json:
        print("Minden itemid egyezik az Excel ls a JSON között.")
    else:
        print("Eltérések találhatóak")

        if missing_from_excel:
            print(len(missing_from_excel))
            print(f"Excelből hiányzó itemid-k: {missing_from_excel}")
        if missing_from_json:
            print(len(missing_from_json))
            print(f"A JSON-ból hiányzó itemid-k: {missing_from_json}")


    import pandas as pd

    excel_file = "p36_tpd.xlsx"
    df = pd.read_excel(excel_file)

    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    sum_nev = df.loc[df['nev'] == 'Visszaváltási díj DRS 10', 'qty'].sum()
    sum_dax_tapado = df.loc[df['dax_tapado_csz'] == 108155, 'qty'].sum()

    result = pd.DataFrame({
        'Sum_qty_nev': [sum_nev],
        'Sum_qty_dax_tapado': [sum_dax_tapado]
    })

    print(result)

if __name__ == '__main__':
    main()