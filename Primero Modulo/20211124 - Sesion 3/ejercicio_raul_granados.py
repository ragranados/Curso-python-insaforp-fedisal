conversion = int(input('1. Dolar a colon.\n2. Colon a dolar.\n3. Dolar a Bitcoin\n4. Bitcoin a dolar\n5. Dolar a Yuan\n6. Yuan a dolar\nIngrese opcion de menu: '))
dinero = float(input('Ingrese cantidad: '))

if conversion == 1:
    print(f'{dinero} dolares son {dinero * 8.75} colones')
elif conversion == 2:
     print(f'{dinero} colones son {(dinero / 8.75):.2f} dolares')
elif conversion == 3:
     print(f'{dinero} dolares son {(dinero / 57057.20):10f} bitcoins')
elif conversion == 4:
     print(f'{dinero} bitcoins son {dinero * 57057.20} dolares')
elif conversion == 5:
     print(f'{dinero} dolares son {(dinero * 6.39)} yuanes')
elif conversion == 6:
     print(f'{dinero} yuanes son {(dinero / 6.39):.5f} dolares')