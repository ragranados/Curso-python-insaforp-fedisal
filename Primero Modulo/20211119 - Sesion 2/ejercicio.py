nombre = input('Ingrese nombre de la persona: ')
dui = input('Ingrese DUI: ')
horas = int(input('Ingrese horas trabajadas: '))

print(f'\nNombre: {nombre}')
print(f'DUI: {dui}')

if horas <= 40:
    print(f'Sueldo: {40 * 10}')
else:
    print(f'Sueldo: {(40 * 10) + ((horas - 40) * 20)}')