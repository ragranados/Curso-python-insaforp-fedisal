from factura import Factura

class ImprimirPDF:

    def imprimir_factura(self, factura: Factura) -> None:
        print('Informacion factura: \n')
        factura.__str__()