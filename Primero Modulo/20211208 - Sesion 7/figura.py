class Figura:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(f'La figura es: {self.nombre}')