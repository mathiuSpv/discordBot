import sqlite3
from functools import wraps;
from sqlite3 import Cursor;

__DATABASE = "DISCORD.db"

def session(func):
    @wraps(func)
    def connection(*args, **kwargs):
        conn = sqlite3.connect(__DATABASE)
        cursor : Cursor = conn.cursor()
        try:
            result = func(cursor, *args, **kwargs)
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            result = e
        finally:
            cursor.close()
            conn.close()
        return result
    return connection