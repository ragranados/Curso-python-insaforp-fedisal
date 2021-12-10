class Empleado:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def calcular_sueldo(self):
        return 1000
    
class EmpleadoPorComision(Empleado):

    def __init__(self, nombre, ventas, comision) -> None:
        super().__init__(nombre)
        self.ventas = ventas
        self.comision = comision

    def calcular_sueldo(self):
        return self.ventas*self.comision
    
e1 = Empleado('Alicia')
e2 = EmpleadoPorComision('eva', 10000, 0.05)

print(e1.nombre, e1.calcular_sueldo())
print(e2.nombre, e2.calcular_sueldo())