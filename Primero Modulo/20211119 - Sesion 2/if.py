# programa para estructuras de decision if

edad = int(input('Digite su edad: '))

if edad >= 18:
    print('Es mayor de edad')

    if edad > 60:
        print('Y es de la tercera edad')
else:
    print('Es menor de edad')