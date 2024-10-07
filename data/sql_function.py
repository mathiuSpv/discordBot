import sqlite3
from functools import wraps;
from sqlite3 import Cursor;

__DATABASE = 'DISCORD.db'

def _session(func):
    @wraps(func)
    def connection(*args, **kwargs):
        conn = sqlite3.connect(__DATABASE)
        cursor : Cursor = conn.cursor()
        try:
            result = func(cursor, *args, **kwargs)
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            result = (False, e)
        finally:
            cursor.close()
            conn.close()
        return result
    return connection

@_session
def getUser(cursor: Cursor, userId : int) -> tuple:
    """
    Parameters:
        userId (int): Id del usuario
    Returns:
        tuple: Obtienes True si existe y entidad como dict del usuario

    """
    cursor.execute(
        """
            SELECT * FROM Users WHERE id = ?
        """,
        (userId,))
    entity_tuple = cursor.fetchone()
    if entity_tuple:
        entity_map = {
            "id" : entity_tuple[0],
            "experience" : entity_tuple[1]
        }
    else:
        entity_map = {}
    exist = entity_tuple is not None
    return (exist, entity_map)

@_session
def insertUser(cursor: Cursor, userId: int, userExp: int) -> bool | tuple:
    """
    Parameters:
        userId (int): Id del usuario.
        userExp (int): Cantidad inicial de experiencia del usuario.
    Returns:
        bool: True si el usuario fue insertado exitosamente.
        tuple: False y Error, si hubo algun error.
    """
    cursor.execute(
        """
            INSERT INTO Users (id, experience)
            VALUES (?, ?)
        """,
        (userId, userExp)
    )
    return cursor.rowcount > 0

@_session
def updateUserExp(cursor: Cursor, userId: int, userExp: int) -> bool | tuple:
    """
    Parameters:
        userId (int): Id del usuario.
        userExp (int): Cantidad de experiencia a agregar al usuario.
    Returns:
        bool: True si la experiencia del usuario fue actualizada exitosamente, False en caso contrario.
        tuple: False y Error, si hubo algun error.
    """
    cursor.execute(
    """
        UPDATE Users
        SET experience = experience + ?
        WHERE id = ?
    """,
    (userExp, userId))
    return cursor.rowcount > 0
            
if __name__ == "__main__":
    # test
    conn = sqlite3.connect(__DATABASE)
    cursor = conn.cursor()
    print(getUser(userId= 1))
    print(getUser(userId= 2))
    print(insertUser(userId= 3, userExp= 10))
    print(updateUserExp(userId= 2, userExp= 10))
