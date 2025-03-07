import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
                dbname = "chinook",
                user = "postgres",
                password = "****",
                host = "localhost",
                port = "****"
            )
        return conn
    except psycopg2.Error as e:
        print(f"Hiba tortént a kapcsolat létrehozása során: {e}")
        return None

if get_connection():
    print("Successful database connection")
else:
    print("Error during database connection")