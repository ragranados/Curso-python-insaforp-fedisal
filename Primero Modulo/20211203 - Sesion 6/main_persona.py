from persona import Persona

def main():
    alicia = Persona('Alicia Maria', 'Diaz', 25, '12345678-9')

    print(alicia.nombres)
    print(alicia._apellidos)
    #print(alicia.__edad)
    alicia.mostrar_datos()
    print(alicia)

if __name__=='__main__':
    main()