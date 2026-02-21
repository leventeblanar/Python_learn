from chinook_db_muv.util.db import DBConnector
from chinook_db_muv.util.config import DBConfig

config = DBConfig.from_env("CHINOOK_DB")

def gyak_service():
    with DBConnector(config) as db:
        artists = db.get("artist")
        print(artists[:3])