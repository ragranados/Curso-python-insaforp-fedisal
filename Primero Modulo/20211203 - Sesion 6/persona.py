class Persona: 

    def __init__(self, nombres, apellidos, edad, dui):
        self.nombres = nombres
        self._apellidos = apellidos # _ para protegidos
        self.__edad = edad # __ para privados
        self.__dui = dui
    
    def mostrar_datos(self): 
        print(
            f'Nombre: {self.nombres}\n'
            f'Apellidos: {self._apellidos}\n'
            f'Edad: {self.__edad}\n'
            f'Dui: {self.__dui}\n'
            f'--------------------------------------'
        )
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_edad(self, edad):
        return self.__edad

    def __str__(self):
        return (
            f'DUI: {self.__dui}'
        )