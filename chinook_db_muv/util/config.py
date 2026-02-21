from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class DBConfig:
    host :str
    port: int
    dbname: str
    user: str
    password: str

    @classmethod
    def from_env(cls, prefix: str = "CHINOOK_DB"):
        return cls(
            host = os.getenv(f"{prefix}_HOST", "localhost"),
            port = int(os.getenv(f"{prefix}_PORT", "5432")),
            dbname = os.getenv(f"{prefix}_DATABASE", "chinook"),
            user = os.getenv(f"{prefix}_USER", "chinook"),
            password = os.getenv(f"{prefix}_PW"),
        )
    
    @classmethod
    def from_connection_string(cls, conn_string: str):
        conn_string = conn_string.replace('postgresql://', '')
        user_pw, host_port_db = conn_string.split('@')
        user, password = user_pw.split(':')
        host_port, dbname = host_port_db.split('/')
        host, port = host_port.split(':')

        return cls(
            host=host,
            port=int(port),
            dbname=dbname,
            user=user,
            password=password
        )
    
    def to_connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"