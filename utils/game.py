from database.queries import GameQuery

class UserGameDTO:
    """
    DTO UserGame
    """
    
    def __init__(self, database_response : tuple = None, **kwargs):
        if database_response: self._serializarResponse_(database_response)
        else:
            self.id = kwargs.get("id", None)
            self.exp = kwargs.get("exp", None)
            self.lvl = kwargs.get("lvl", None)
            self.start = kwargs.get("start", None)
            self.end = kwargs.get("end", None)
        
    def _serializarResponse_(self, response: tuple):
        atributos = ["id", "exp", "lvl", "start", "end"]
        for index, atributo in enumerate(atributos):
            setattr(self, atributo, response[index] if index < len(response) else None)
    
    def __str__(self) -> str:
        return (f"{self.id} {self.exp} {self.lvl} {self.start} {self.end}")

class GameService:
    def __init__(self, gq: GameQuery = None):
        self.gq = gq or GameQuery()

    def get_user(self, user_id: int) -> UserGameDTO | None:
        data = self.gq.get_user(user_id)
        return UserGameDTO(data) if data else None

    def add_experience(self, user_id: int, experience: int) -> bool:
        if experience < 0:
            raise ValueError("La experiencia no puede ser negativa")
        return self.gq.upsert_user(user_id, experience)

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        if not user:
            raise ValueError("El usuario no existe y no se puede eliminar")
        return self.gq.delete_user(user_id)