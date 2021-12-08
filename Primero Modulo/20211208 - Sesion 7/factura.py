class Factura:

    #variable de clase
    cantidad_facturas = 0

    def __init__(self, cliente, total, idfactura):
        self.cliente = cliente
        self.total = total
        self.idfactura = idfactura
        Factura.cantidad_facturas +=1

    @classmethod
    def mostrar_cantidad_facturas(cls):
        print(f'la cantidad de facturas es: {cls.cantidad_facturas}')
    
    @staticmethod
    def sumar_facturas(lista_facturas):
        total_facturas = 0
        for f in lista_facturas:
            total_facturas += f.total
        return total_facturas

    