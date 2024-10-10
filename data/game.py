import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data import session
from sqlite3 import Cursor

class User():
    def __init__(self, response_tuple) -> None:
        len_response = len(response_tuple)
        
        self._id = response_tuple[0] if len_response >  0 else None
        self.experience = response_tuple[1] if len_response >  1 else None
        self.level = response_tuple[2] if len_response >  2 else None
        self.startIn = response_tuple[3] if len_response >  3 else None
        self.endIn = response_tuple[4] if len_response >  4 else None
        
    def getExperience(self) -> tuple:
        
        exp_diff = None; intervals_diff = None
        
        if(isinstance(self.startIn, int)):
            exp_diff = self.experience - self.startIn
        if(isinstance(self.endIn, int)):
            intervals_diff = self.endIn - self.startIn
        return (exp_diff, intervals_diff)

@session
def getUser(cursor: Cursor, userId : int) -> User | None:
    """
    Parameters:
        userId (int): Id del usuario
    Returns:
        tuple: Obtienes True si existe y entidad del usuario
    """
    cursor.execute(
        """
            SELECT * FROM Users WHERE id = ?
        """,
        (userId,))
    response = cursor.fetchone()
    if response:
        return User(response)
    return None

@session
def getUserStats(cursor: Cursor, userId: int) -> User | None:
    cursor.execute(
        """
            SELECT * FROM v_UserStats WHERE user_id = ?
        """,
        (userId,))
    response = cursor.fetchone()
    if (response):
        return User(response)
    return None
    

@session
def insertUser(cursor: Cursor, userId: int, userExp: int) -> tuple:
    """
    Parameters:
        userId (int): Id del usuario.
        userExp (int): Cantidad inicial de experiencia del usuario.
    Returns:
        tuple: True/False y Reason, None si no hubo error.
    """
    cursor.execute(
        """
            INSERT INTO Users (id, experience)
            VALUES (?, ?)
        """,
        (userId, userExp)
    )
    return (cursor.rowcount > 0, None)

@session
def updateExp2User(cursor: Cursor, userId: int, userExp: int) -> tuple:
    """
    Parameters:
        userId (int): Id del usuario.
        userExp (int): Cantidad de experiencia a agregar al usuario.
    Returns:
        tuple: True/False y Reason, None si no hubo error.
    """
    cursor.execute(
    """
        UPDATE Users
        SET experience = experience + ?
        WHERE id = ?
    """,
    (userExp, userId))
    return (cursor.rowcount > 0, None)

@session
def deleteUser(cursor: Cursor, userId: int) -> tuple:
    cursor.execute(
    """
        DELETE FROM Users
        WHERE id = ?
    """,
    (userId,))
    return (cursor.rowcount > 0, None)

if __name__ == "__main__":
    print(getUserStats(userId=395647730112004107))
    # print(updateExp2User(userId=395647730112004107, userExp= 100))
    # print(getUserStats(userId=395647730112004107))