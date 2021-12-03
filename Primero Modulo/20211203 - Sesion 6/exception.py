import sys

def main():
    input('digite una palabra')

if __name__=='__main__':
    try:
        v = [7,10]
        main()

        #4/0
        print('hola')
    except TypeError as e:
        print(f'operacion no valida')
    except ZeroDivisionError as e:
        print(f'divison no permitida')
    except KeyboardInterrupt as e:
        print(f'adios...')
    else:
        print('sin errores')
    finally:
        print('finalmente')