import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data import session
from sqlite3 import Cursor

@session
def isDeveloper(cursor: Cursor, userId: int) -> bool:
    cursor.execute(
        """
            SELECT 1 FROM Developers WHERE id = ?
        """,
        (userId,))
    response = cursor.fetchone()
    return response is not None

if __name__ == "__main__":
    print(isDeveloper(userId=395647730112004107))
    
    