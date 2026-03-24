import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Any

from chinook_db_muv.util.config import DBConfig

class DBConnector:

    def __init__(self, config: DBConfig):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect(self):

        self.conn = psycopg2.connect(
            host=self.config.host,
            port=self.config.port,
            dbname=self.config.dbname,
            user=self.config.user,
            password=self.config.password
        )

        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        return self
    
    def close(self):

        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self.connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        self.close()


    def get(self, table: str, columns: list[str] = None, where: dict = None) -> list[dict]:

        cols = ", ".join(f'"{c}' for c in columns) if columns else "*"
        sql = f'SELECT {cols} FROM public."{table}"'

        params = []
        if where:
            conditions = []

            for key, value in where.items():
                conditions.append(f'"{key}" = %s')
                params.append(value)
            
            sql += " WHERE " + " AND ".join(conditions)
        
        self.cursor.execute(sql, params)

        return self.cursor.fetchall()

    
    def get_raw(self, sql: str, params: tuple = None) -> list[dict]:

        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    
    def insert(self, table: str, data: dict) -> int | None:
        columns = ", ".join(f'"{k}"' for k in data.keys())
        placeholders = ", ".join(["%s"] * len(data))

        values = list(data.values())

        sql = f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders}) RETURNING id'

        self.cursor.execute(sql, values)

        result = self.cursor.fetchone()

        return result["id"] if result else None

    def insert_batch(self, table: str, rows: list[dict]) ->int:

        if not rows:
            return 0
        
        columns = ", ".join(f'"{k}"' for k in rows[0].keys())
        placeholders = ", ".join(["%s"] * len(rows[0]))

        sql = f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders})'

        values = [tuple(row.values()) for row in rows]

        self.cursor.executemany(sql, values)
        return len(rows)
    
    def update(self, table: str, data: dict, where: dict) -> int:

        set_parts = []
        params = []

        for key, value in data.items():
            set_parts.append(f'"{key}" = %s')
            params.append(value)
        
        where_parts = []
        for key, value in where.items():
            where_parts.append(f'"{key}" = %s')
            params.append(value)

        sql = f'UPDATE "{table}" SET {", ".join(set_parts)} WHERE {" AND ".join(where_parts)}'

        self.cursor.execute(sql, params)

        return self.cursor.rowcount

    def delete(self, table: str, where: dict) -> int:

        where_parts = []
        params = []

        for key, value in where.items():
            where_parts.append(f'"{key}" = %s')
            params.append(value)

        sql = f'DELETE FROM "{table}" WHERE {" AND ".join(where_parts)}'

        self.cursor.execute(sql, params)
        return self.cursor.rowcount