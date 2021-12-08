from factura import Factura

def main():
    f1 = Factura('alicia', 100, 1)
    f2 = Factura('alicia 2', 30, 2)
    f3 = Factura('alicia 3', 1500,31)

    print(f'Cantidad: {Factura.cantidad_facturas}')
    Factura.mostrar_cantidad_facturas()

    suma = Factura.sumar_facturas([f1,f2,f3])
    print(suma)

if __name__ == '__main__':
    main()