from lector import Lector
import time

RESET: str = "\033[0m"
ROJO: str = "\033[31m"
VERDE: str = "\033[32m"
AMARILLO: str = "\033[33m"
AZUL: str = "\033[34m"
CIAN: str = "\033[36m"

lector = Lector("documento.txt")

print(f"\n{VERDE}------メモリに読み込まれたチャットボット-------{RESET}")

while True:
    print(
        f"\n{AMARILLO}[質問] Introduce tu pregunta (o escribe 'salir' para terminar){RESET}"
    )
    prompt: str = input("~> ")

    if prompt.lower() in ["salir", "exit", "quit"]:
        print(f"{ROJO}Cerrando sistema...{RESET}")
        time.sleep(1)
        break
    respuesta = lector.buscar(prompt)

    print(f"{CIAN}[Respuesta]:{RESET}")
    print(f"{respuesta}")
