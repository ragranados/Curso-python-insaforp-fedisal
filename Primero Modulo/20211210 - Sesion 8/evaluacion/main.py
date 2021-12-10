from producto import Producto
from cliente import Cliente
from factura import Factura
from imprimir import ImprimirPDF

def main():
    p1 = Producto('jabon', 10, 2)
    p2 = Producto('Agua', 0.5, 13)
    p3 = Producto('Leche', 1.5, 1)

    c = Cliente('Raul Granados', 23)

    f = Factura(1, '10/12/2021', c)
    f.agregar_producto(p1)
    f.agregar_producto(p2)
    f.agregar_producto(p3)

    p4 = Producto('Compu', 1500, 1)

    f2 = Factura(2, '10/12/2021', c)
    f2.agregar_producto(p2)
    f2.agregar_producto(p4)

    i = ImprimirPDF()

    i.imprimir_factura(f)
    print('---------------------------------------------------------------------')
    i.imprimir_factura(f2)

if __name__=='__main__':
    main()