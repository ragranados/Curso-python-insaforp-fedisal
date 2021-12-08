#Abstract Base Class

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def mostrar_datos(self):
        pass

# no es posible instanciar la clase abstracta
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_datos(self):
        print(f'nombre: {self.nombre}\nedad: {self.edad}\nsueldo: {self.sueldo}')

e = Empleado('alicia', 20, 1000)
e.mostrar_datos()