class Cliente:

    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad
    
    def __str__(self) -> str:
        cadena = f'Nombre: {self.__nombre}\nEdad: {self.__edad}'
        print(cadena)
        return cadena