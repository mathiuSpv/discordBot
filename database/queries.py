from connection import session
from sqlite3 import Cursor

class GameQuery:
    
    @staticmethod
    @session
    def get_user(cursor: Cursor, user_id: int) -> tuple | None:
        """
        Obtiene las estadísticas de un usuario desde una vista.
        """
        cursor.execute(
            """
            SELECT * FROM v_UserStats WHERE user_id = ?
            """,
            (user_id,)
        )
        return cursor.fetchone()

    @staticmethod
    @session
    def upsert_user(cursor: Cursor, user_id: int, user_exp: int) -> tuple:
        """
        Inserta un usuario con experiencia inicial.
        """
        cursor.execute(
            """
            INSERT INTO Users (id, experience)
            VALUES (?, ?)
            ON CONFLICT(id) DO UPDATE SET experience = experience + excluded.experience
            """,
            (user_id, user_exp)
        )
        return (cursor.rowcount == 1)

    @staticmethod
    @session
    def delete_user(cursor: Cursor, user_id: int) -> tuple:
        """
        Elimina un usuario por su ID.
        """
        cursor.execute(
            """
            DELETE FROM Users
            WHERE id = ?
            """,
            (user_id,)
        )
        return (cursor.rowcount == 1)
    