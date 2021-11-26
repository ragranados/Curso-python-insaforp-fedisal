menu = "1. Agregar\n2. Imprimir lista\n3. Terminar proceso\n"
print(menu)

opcion = int(input('Ingrese una opcion: '))

lista = []

while opcion != 3:

    if opcion == 1:
        nombre = input('Ingrese nombre: ')
        cargo = input('Ingrese cargo: ')
        sueldo = float(input('Ingrese sueldo: '))

        newUser = {
            'nombre': nombre,
            'cargo': cargo,
            'sueldo': sueldo
        }

        lista.append(newUser)
    elif opcion == 2:
        print(lista)
    
    print(menu)
    opcion = int(input('Ingrese una opcion: '))

    


