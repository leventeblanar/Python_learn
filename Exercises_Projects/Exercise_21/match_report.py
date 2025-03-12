from db_config import get_engine_taltos
import pandas as pd
import sys

# This is a report match to a database, filtering the same and the different records 

sys.stdout.reconfigure(encoding = 'UTF-8')
sys.stderr.reconfigure(encoding = 'UTF-8')


def pull_query():

    engine = get_engine_taltos()

    query = """
        SELECT vk.kod, c.taltos_cikkszam
        FROM taltos.vonalkod AS vk
        INNER JOIN taltos.cikk c ON vk.cikk_id  = c.id;
    """

    try:
        with engine.connect() as connection:
                print("Taltos vonalkodok lekérdezése.")
                df_taltos = pd.read_sql(query, connection)
                df_taltos = df_taltos.fillna("-")
                return df_taltos
                
    except Exception as e:
            print(f"An error occured during query: Cikk. Details: {e}")
    finally:
             engine.dispose()
def match():

        excel_path = "C:/Work/Meló/p72_cikk_csekk/cikkek.xlsx"  

        # Adatbázis DF
        df_taltos = pull_query()
        df_cikkek = pd.read_excel(excel_path, sheet_name="cikkek")
        df_vonal = pd.read_excel(excel_path, sheet_name="vonal")
        df_cikkek_full = df_cikkek.merge(df_vonal, on="CIKK_SZAM", how="left")

        print(len(df_cikkek_full))
        print(len(df_cikkek))
        print(len(df_vonal))

        # itt merge-ölöm a teljes cikkek.xlsx-et a taltos Dataframe-hez
        df_merge = df_cikkek_full.merge(df_taltos, left_on="vonalkod", right_on="kod", how="left")

        # Egyező vonalkódok
        df_merge["egyezo_vonalkodok"] = df_merge.apply(lambda x: x["vonalkod"] if pd.notna(x["taltos_cikkszam"]) else None, axis=1)

        # Nem egyező vonalkódok
        df_merge["nem_egyezo_vonalkodok"] = df_merge.apply(lambda x: x["vonalkod"] if pd.isna(x["taltos_cikkszam"]) else None, axis=1)

        # groupolok cikkszám alapján (cikkek.xlsx) - egyező és nem egyező vonalkodók egy oszlopba + taltos cikkszám ahol van
        df_final = df_merge.groupby("CIKK_SZAM").agg({
                "CIKK_NEV": "first", 
                "afa_kulcs": "first",
                "MENNY_EGYS": "first",
                "BRUTTO_AR": "first",
                "egyezo_vonalkodok": lambda x: ", ".join(x.dropna().astype(str)),
                "nem_egyezo_vonalkodok": lambda x: ", ".join(x.dropna().astype(str)),
                "taltos_cikkszam": lambda x: ", ".join(x.dropna().astype(str))
        }).reset_index()

        # nincs táltosban dataframe azoknak ahol nincs egyező vonalkód = nincs atlasban
        nincs_taltosban = df_final[df_final["egyezo_vonalkodok"] == ""]
        nincs_taltosban = nincs_taltosban.drop(columns=["egyezo_vonalkodok", "taltos_cikkszam"])

        print(f"{len(nincs_taltosban)} cikk vonalkódja nem található meg a Atlasban.")


        with pd.ExcelWriter("cikkek_osszehasonlitas.xlsx", engine="xlsxwriter") as writer:
                df_final.to_excel(writer, sheet_name="meglevok", index=False)
                nincs_taltosban.to_excel(writer, sheet_name="nincs_taltosban", index=False)

                workbook = writer.book
                sheet_meglevok = writer.sheets["meglevok"]
                sheet_nincs_taltosban = writer.sheets["nincs_taltosban"]

                for sheet, df in zip([sheet_meglevok, sheet_nincs_taltosban], [df_final, nincs_taltosban]):
                        for idx, col in enumerate(df.columns):
                                max_len = max(
                                        df[col].astype(str).map(len).max(),
                                        len(str(col))
                                ) + 1  
                                sheet.set_column(idx, idx, max_len)

                        print("Csekkold az exceled bro.")


if __name__ == '__main__':
       match()


