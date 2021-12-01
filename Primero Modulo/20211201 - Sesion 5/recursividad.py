# la recursividad es una funcion que se llama a si misma
# y existe un caso base que termine las llamadas recursivas
#recursividad es una alternativa a las estructuras repetitvas (for, while)

def factorial(n):
    if n==1:
        return 1
    
    return factorial(n-1)*n

#print(factorial(5))

#imprimir los numeros decendentes de n:
# Si n es = 5, se imprimi 5 4 3 2 1

def numeros(n):
    
    print(n)

    if n == 1:
        return 

    numeros(n - 1)

numeros(7)