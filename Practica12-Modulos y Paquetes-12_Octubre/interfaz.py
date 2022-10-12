"""
Este modulo imprime mensajes
NO

"""

def imprimirMensaje(nombre):
    mensaje='hola, soy holaMundo otra vez ' + nombre
    print(mensaje)
    return None

def imprimirSeparador(tipo):
    print('\n'+tipo*50+'\n')

def imprimirVariable(nombre, variable):
    print(nombre+' ==> '+str(variable))
    imprimirSeparador('=')

def imprimirLista(lista):
    for fecha in lista:
        print(fecha)
        imprimirSeparador('=')