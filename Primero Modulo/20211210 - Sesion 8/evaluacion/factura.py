from producto import Producto
from cliente import Cliente

class Factura:

    n_facturas = 0
    
    def __init__(self, idFactura: int, fecha: str, cliente: Cliente) -> None:
        Factura.n_facturas += 1
        self.__idFactura = idFactura
        self.__fecha = fecha
        self.__cliente = cliente
        self.lista_productos = []
    
    def agregar_producto(self, p: Producto) -> None:
        self.lista_productos.append(p)
    
    def __str__(self) -> None:
        total = 0
        print(f'ID: {self.__idFactura}\nfecha: {self.__fecha}')
        print(f'Facturas activas: {self.n_facturas}')
        
        print(f'\n---------------------\n')
        print(f'Informacion cliente:\n')
        self.__cliente.__str__()

        print(f'\n---------------------\n')
        print("Detalle: \n")

        for p in self.lista_productos:
            total += 1
            print(p,'\n')
        
        print(f'Cantidad productos: {total}\n')

        
