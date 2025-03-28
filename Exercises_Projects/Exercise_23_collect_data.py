import pandas as pd
from db_config import get_engine
import datetime
import sys

today = pd.Timestamp('today')
kerekes_cikktorzs = pd.read_excel(f'*********')

sys.stdout.reconfigure(encoding="UTF-8")
sys.stdout.reconfigure(encoding="UTF-8")

def csekk_cikk_adatok():

    engine = get_engine()

    ### Adatbázisból DF lekérdezés
    query = """
    *****
    """

    try:
        with engine.connect() as connection:
            atlas_df = pd.read_sql(query, connection) # adatbázisból df cikk adatok lehúzására
            atlas_df = atlas_df.rename(columns={'kod': 'vonalkod'})
            atlas_df['vonalkod'] =atlas_df['vonalkod'].astype(str).str.strip()
            print("Atlas Dataframe sikeresen lekérve.")
    except Exception as e:
        print(f"Hiba történt a report lehúzásakor: {e}")
        return
    
    ### Vágólapon levő szállító_cikkszámok DF-be
    
    napi_df = pd.read_clipboard(header=None, dtype=str)  # vágólapról df létrehozás
    if napi_df.empty:
        print("Üres a vágólap.")
        return
    else:
        napi_df.columns = ['szallito_cikkszam']
        print("A vágólapon levő cikkszámok belekerültek egy Dataframe-be.")

    ### Kerekes_cikktörzs vonalkódjainak szétbontása, cikkszám átnevezés, typecastolás
    ker_df = kerekes_cikktorzs.rename(columns={'cikkszám': 'szallito_cikkszam', 'Vonalkódok': 'vonalkod' })
    ker_df[['szallito_cikkszam']] = ker_df[['szallito_cikkszam']].astype(str)

    ###Vonalkód listává alakítása
    ker_df['vonalkod'] = ker_df['vonalkod'].fillna('').astype(str).str.split(',')
    ker_df['vonalkod'] = ker_df['vonalkod'].apply(lambda lst: sorted(set(v.strip() for v in lst if v.strip())))

    napi_ker_df = napi_df.merge(ker_df, on='szallito_cikkszam', how='inner')
    print("Joint Dataframe létrehozva.")

    vonalkod_set = set(atlas_df['vonalkod'])

    def ellenorzes(vonalkod_lista):
        megtalalt = [kod for kod in vonalkod_lista if kod in vonalkod_set]
        nem_talalt = [kod for kod in vonalkod_lista if kod not in vonalkod_set]
        return pd.Series([megtalalt, nem_talalt])

    napi_ker_df[['egyező_vonalkódok', 'hiányzó_vonalkódok']] = napi_ker_df['vonalkod'].apply(ellenorzes)

    # Listából vesszővel elválasztott stringgé alakítás
    napi_ker_df = napi_ker_df.explode('egyező_vonalkódok')
    napi_ker_df['vonalkod'] = napi_ker_df['vonalkod'].apply(lambda lst: ', '.join(lst) if isinstance(lst, list) else lst)
    napi_ker_df['egyező_vonalkódok'] = napi_ker_df['egyező_vonalkódok'].apply(lambda lst: ', '.join(lst) if isinstance(lst, list) else lst)
    napi_ker_df['hiányzó_vonalkódok'] = napi_ker_df['hiányzó_vonalkódok'].apply(lambda lst: ', '.join(lst) if isinstance(lst, list) else lst)
    
    ### Utolsó lépésként rácsatolom left joinal az atlas Dataframet ugy, hogy ahol van egyező vonalkód, ott legyen atlas_nev, cikk_id, meg taltos_cikkszam
    final_cikkek_df = napi_ker_df.merge(atlas_df, left_on='egyező_vonalkódok', right_on='atlas_vonalkod', how='left')
    final_cikkek_df = final_cikkek_df.rename(columns={'id': 'Cikk_ID', 'nev': 'atlas_nev'})
    final_cikkek_df = final_cikkek_df.drop(columns=['vonalkod', 'atlas_vonalkod'])
    final_cikkek_df = final_cikkek_df.drop_duplicates(['szallito_cikkszam', 'egyező_vonalkódok'])

    output_path = f"Napi_hiányzo_cikkek_adatok_report/cikk_ellenorzes_eredmeny_{today:%m%d%Y}.xlsx"
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        final_cikkek_df.to_excel(writer, sheet_name="hiányzó_cikkek", index=False)
        workbook = writer.book
        sheet = writer.sheets["hiányzó_cikkek"]
        for idx, col in enumerate(final_cikkek_df.columns):
            max_len = max(final_cikkek_df[col].astype(str).map(len).max(), len(str(col))) + 1
            sheet.set_column(idx, idx, max_len)

    # napi_kerekes_df.to_excel(f"cikk_ellenorzes_eredmeny_{today:%m%d%Y}.xlsx", index=False)
    print(f"A lekérdezés sikeresen lefutott. Az eredmény a cikk_ellenorzes_eredmeny_{today:%m%d%Y}.xlsx fájlban található.")

    return final_cikkek_df

if __name__ == '__main__':
    csekk_cikk_adatok()