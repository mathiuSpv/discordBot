from sqlite3 import Cursor
from connection import session

class GameModels:

    @staticmethod
    @session
    def create_users_table(cursor: Cursor) -> bool:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY NOT NULL,
                experience INTEGER NOT NULL
            );
            """
        )
        return True

    @staticmethod
    @session
    def create_levels_table(cursor: Cursor) -> bool:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Levels (
                level INTEGER PRIMARY KEY NOT NULL,
                startIn INTEGER NOT NULL
            );
            """
        )
        return True

    @staticmethod
    @session
    def create_user_stats_view(cursor: Cursor) -> bool:
        cursor.execute(
            """
            CREATE VIEW IF NOT EXISTS v_UserStats AS
            SELECT
                u.id AS user_id,
                u.experience AS experience,
                l.level AS level_id,
                l.startIn AS startIn,
                (SELECT MIN(l2.startIn)
                    FROM Levels AS l2
                    WHERE l2.startIn > l.startIn) AS endIn
            FROM
                Users AS u
            INNER JOIN
                Levels AS l
            ON
                u.experience >= l.startIn
            GROUP BY
                u.id
            HAVING
                l.startIn = MAX(l.startIn);
            """
        )
        return True

    @staticmethod
    @session
    def generate_levels(cursor: Cursor, start_level: int, end_level: int) -> int:
        """
        Genera niveles en la tabla 'Levels' de forma recursiva usando SQL con parámetros.
        """
        cursor.execute(
            """
            WITH RECURSIVE LevelsRecursive(level, startIn) AS (
                -- Caso base
                SELECT 
                    :start_level AS level, 
                    (600 * (:start_level * :start_level) - 600 * :start_level) AS startIn
                UNION ALL
                -- Paso recursivo
                SELECT 
                    level + 1, 
                    (600 * ((level + 1) * (level + 1)) - 600 * (level + 1))
                FROM LevelsRecursive
                WHERE level < :end_level
            )
            INSERT INTO Levels (level, startIn)
            SELECT level, startIn FROM LevelsRecursive;
            """,
            {"start_level": start_level, "end_level": end_level}
        )
        return cursor.rowcount
        
if __name__ == "__main__":
    pass