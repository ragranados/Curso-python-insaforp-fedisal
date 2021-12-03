from procesos import isr

def main():
    print('''
    Elija una opcion: 
    1. ISSS
    2. AFP
    3. ISR
    4. DESCUENTOS
    5. Sueldo Gravable
    6. Sueldo a pGAR
    #. Salir 
    ''')

    op = int(input('Digite una opcion: '))
    if op >=1 and  op <=6:
        sueldo = float(input('Digite sueldo: '))
        if op==1:
           print(f'el ISSS es: ${isr.isss(sueldo):.2f}')
        elif op==2:
           print(f'el AFP es $ {isr.afp(sueldo):.2f}')
        elif op==3:
            print(f'el ISR es $ {isr.impuesto_isr(sueldo):.2f}')
    
if __name__=='__main__':
    main()