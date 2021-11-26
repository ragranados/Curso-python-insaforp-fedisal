diccionario = {
    'usuario': 'alicia',
    'token': 'sadfsadfasdfa'
}

print(diccionario)
print(diccionario['token'])

for valor in diccionario.values():
    print(valor)

for keys in diccionario.keys():
    print(keys)

for k, v in diccionario.items():
    print(k, v)

print('usuario' in diccionario)

diccionario.clear()
print(diccionario)