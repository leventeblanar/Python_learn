import pandas as pd
from sqlalchemy import create_engine, exc

query = """SELECT * FROM album"""

def get_engine():    

    try:
        engine = create_engine("postgresql+psycopg2://postgres:Brutal.shred01@localhost:5432/chinook")
        print("Sikeres kapcsolat")
        return engine
    except Exception as e:
        print(f"Nem sikerült adatbázis kapcsolatot létesíteni a localhost adatbázissal. Hiba: {e}")
        return None

def run_query():

    try:
        engine = get_engine()

        with engine.connect() as connection:
            print("Sikeres csatlakozás az adatbázishoz")
            df = pd.read_sql(query, connection)
            if df.empty:
                print("A DataFrame üres.")
            else: 
                df.to_csv('test.csv', index=False)
            return df
    except Exception as e:
        print(f"Nem sikerült az adat kinyerése. Hiba: {e}")
        return None

def tasks():

    df1_query = """SELECT * FROM employee"""

    df2_query = """SELECT * FROM customer"""


    try:
        engine = get_engine()

        with engine.connect() as connection:
            df1 = pd.read_sql(df1_query, connection)
            df2 = pd.read_sql(df2_query, connection)

            num_customers = df2.groupby('support_rep_id', as_index=False)['customer_id'].count()

            merged_df = num_customers.merge(df1, left_on='support_rep_id', right_on='employee_id', how='inner')

            most_clients_id = merged_df['customer_id'].idxmax()
            most_clients = merged_df.loc[most_clients_id]

            full_name = f"{most_clients['first_name']} {most_clients['last_name']}"
            total_spent = most_clients 

            print(f"A legtöbbet dolgozó alkalmazott: {full_name} ({most_clients['customer_id']} ügyfél)")



    except Exception as e:
        print(f"Hiba történt: {e}")
        return None

def main():
    tasks()

if __name__ == '__main__':
    main()




            # LEGTÖBBET KÖLTŐ ÜGYFÉL *************************************************
            # total_spent = df1.groupby('customer_id', as_index=False)['total'].sum()

            # merge_df = total_spent.merge(df2, on='customer_id', how='inner')

            # top_spender_id = merge_df['total'].idxmax()
            # top_spender = merge_df.loc(top_spender_id)

            # full_name = f"{top_spender['first_name']} {top_spender['last_name']}"
            # total_spent_amount = top_spender['total']

            # print(f"A legtöbbet költő ügyfél: {full_name} ({total_spent_amount} USD)")
            #***************************************************************************



            # Összes vásárlás országonként ************************************
            # df = df.groupby('billing_country', as_index=False)['total'].sum()
            # df = df.sort_values(by='total', ascending=False)

            # print('Összes vásárlás országonként:')
            # print(df)
            #******************************************************************