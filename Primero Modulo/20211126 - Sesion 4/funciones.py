# programa para uso de funciones
def mi_primera_funcion():
    print('Hola mundo')

mi_primera_funcion()

def suma(a, b):
    return a + b

num = suma (2,3)
print(num)

#paso por valor

a = 6

def modificar_variable(x):
    x+=5
    return x

modificar_variable(a)
print(a)

#por referencia

v = [1,2,3]

def modificar_vector(d):
    d.append(4)
    return d

modificar_vector(v)
print(v)