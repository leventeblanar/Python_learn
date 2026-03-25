# Problematic parts, moduls, solutions that I have to practice - batch 1

# Context Managers Connection Wrapper
# As we work with code the continues need for DB connection, file handling and things will require an automatic handler that enters and closes
# Resources as we go through our process, otherwise the program will eat up our resources
# Writing a context manager helps with managing the whole process and saves us from creating boilerplate code here and there

# the most simple one
'''
class SimpleManager:
    def __enter__(self):
        print("Belépés")
        return "adat"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Kilépés")

with SimpleManager() as value:
    print(value)
'''

# @contextmanager
'''
from contextlib import contextmanager

@contextmanager
def simple_manager():
    print("Start")
    yield "alma"
    print("End")

with simple_manager() as value:
    print(value)'''


import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from urllib.parse import urlparse

load_dotenv()

CHINOOK_CONN_STRING = os.getenv("CHINOOK_CONN_STRING")
p = urlparse(CHINOOK_CONN_STRING)

pg_connection_dict = {
    'dbname': p.path[1:],
    'user': p.username,
    'password': p.password,
    'port': p.port,
    'host': p.hostname
}

class ChinookDbHandler:
    def __init__(self):
        self.conn_string = pg_connection_dict
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = psycopg2.connect(**pg_connection_dict)

        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    
