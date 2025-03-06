from sqlalchemy import create_engine
import pandas as pd

def pull_report():
    query = """
    SELECT * FROM track;
    """

    try:
        engine = create_engine("postgresql+psycopg2://{user}:{pw}@{host}:{port}/{dbname}".format(
                user = "postgres",
                pw = "Brutal.shred01",
                host = "localhost",
                dbname = "chinook",
                port = "5432"
            ))
    except Exception as e:
        print(f"An error occured during establishing connection: {e}")

    df = pd.read_sql(query, engine)
    df.to_csv('invoice.csv', index=False)


pull_report()