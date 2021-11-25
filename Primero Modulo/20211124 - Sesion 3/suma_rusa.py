multiplicando = int(input('multiplicando: '))
multiplicador = int(input('multiplicador: '))

res = 0

while multiplicando > 0:
    if multiplicando % 2 != 0:
        res += multiplicador
    
    multiplicando //= 2
    multiplicador *= 2

print(res)