def status_message(state: str, message: str):
    colors = {
        "ejecucion": "\033[36m",
        "finalizado": "\033[32m",
        "aviso": "\033[33m",
        "error": "\033[31m"
    }
    color = colors.get(state, "\033[0m")
    print(f"    {color}>>\033[0m {message}")