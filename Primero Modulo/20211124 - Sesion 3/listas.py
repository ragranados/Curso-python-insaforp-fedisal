nombre = ['x', 'z', 'a', 's', 'xd']

print(len(nombre))
print(nombre[0])
nombre[2] = ':V'
print(nombre)
nombre.append("object")
print(nombre)

for i in nombre:
    print(i)

nombre.remove("xd")
print(nombre)

nombre.insert(0, "anuma")
print(nombre)

nombre.sort()
print(nombre)

print('xd' in nombre)

nombre.clear()
print(nombre)