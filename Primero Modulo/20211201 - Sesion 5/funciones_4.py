# argumentos variables con lista

def lista_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

lista_nombres('alicia', 'beto', 'carlos')

#argumentos variables con diccionarios

def listar_diccionarios(**terminos):
    for k, v in terminos.items():
        print(f'la clave es: {k} y el valor es: {v}')

listar_diccionarios(PK='primary key', FK='foreing key', UQ='Unique')
