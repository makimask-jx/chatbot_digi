import os


class Lector:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.contenido = []
        self._cargar_archivo()

    def _cargar_archivo(self):
        if os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, "r", encoding="utf-8") as f:
                self.contenido = f.readlines()
        else:
            print(f"Error: El archivo {self.nombre_archivo} no existe.")

    def buscar(self, prompt: str) -> str:

        palabras_clave = [p.lower() for p in prompt.split() if len(p) > 2]

        if not palabras_clave:
            return "No se detectaron palabras clave para buscar."

        resultados = []
        for linea in self.contenido:
            if any(palabra in linea.lower() for palabra in palabras_clave):
                resultados.append(linea.strip())

        if resultados:
            return "\n".join(resultados)
        return "No se encontró ninguna coincidencia en el documento."
