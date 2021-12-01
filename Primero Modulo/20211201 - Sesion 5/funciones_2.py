def dia_mes(mes):
    if mes == 12 or mes == 7 or mes==8:
        return 31
    elif mes == 4 or mes == 6:
        return 30
    elif mes == 2:
        return 28
    else:
        return 0

print(dia_mes(12))

def aritme(a, b):
    return a+b, a-b, a/b, a*b, 'hola'

print(aritme(4, 2))