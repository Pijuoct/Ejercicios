"""

Este modulo sirve para realizar algunas operaciones
y se almacenan variables

contiene 2 funciones

"""


from ast import Break


def factorial(numero):
    resultado=1

    for factor in range(1,numero+1):
        resultado*=factor

    return resultado

def primo(numero):

    esPrimo=True

    for divisor in range(2,numero):
        if numero%divisor==0:
            esPrimo=False
            Break
    
    return esPrimo


def suma(*numeros): #*numeros es un listado de numeros de n longitud
    suma=sum(numeros)
    return suma

if __name__=='__main__':
    a=factorial(5)
    print(a)

    b=primo(13)
    print(b)

    c=suma(1,2,3,4,5,6)
    print(c)