from figura import Figura
from color import Color

class Circulo(Figura, Color):
    def __init__(self, nombre, color, radio):
        Figura.__init__(self, nombre)
        Color.__init__(self, color)

        self.radio = radio

    def calcular_area(self):
        return 3.1416*self.radio**2
    
    def calcular_perimetro(self):
        return 2*3.1416*self.radio