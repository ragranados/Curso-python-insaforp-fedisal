from factura import Factura

class ImprimirPDF:

    def imprimir_factura(self, factura: Factura) -> None:
        total = 0
        print('Informacion factura: \n')
        factura.__str__()