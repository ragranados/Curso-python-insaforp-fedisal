from figura import Figura
from rectangulo import Rectangulo
from circulo import Circulo

def main():
    r = Rectangulo('Rectangulo', 20, 10)
    f = Figura('Figura')

    f.mostrar_nombre()
    r.mostrar_nombre()
    c.mostrar_nombre()
    c.mostrar_color()

    print(f'el area del {r.nombre} es {r.calcular_area()}')
    print(f'el perimetro del {r.nombre} es {r.calcular_perimetro()}')

if __name__=='__main__':
    main()