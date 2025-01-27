def status_message(state: str, message: str) -> None:
    """
    Muestra un mensaje formateado con un color correspondiente al estado dado.

    Parámetros:
        state (str): El estado del mensaje. Puede ser uno de los siguientes valores:
            - 'r': Run (Cian).
            - 'f': Finished (Verde).
            - 'w': Warning (Amarillo).
            - 'e': Error (Rojo).
        message (str): El mensaje a mostrar.
    """
    colors = {
        "r": "\033[36m",  # Cian para "Run"
        "f": "\033[32m",  # Verde para "Finished"
        "w": "\033[33m",  # Amarillo para "Warning"
        "e": "\033[31m",  # Rojo para "Error"
    }
    color = colors.get(state, "\033[0m")
    print(f"    {color}>>\033[0m {message}")
    
def add_color(color: str ,content : str) -> str:
    return ''