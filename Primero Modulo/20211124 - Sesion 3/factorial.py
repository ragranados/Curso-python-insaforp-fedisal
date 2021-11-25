n = int(input('Digite un numero: '))

f = n

for i in range(1, n):
    f = f * i

print(f'el factorial es: {f}')