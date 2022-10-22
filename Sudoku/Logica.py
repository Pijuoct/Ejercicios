"""
Este modulo contiene 3 funciones:

* generarTableroLogico(): No recibe nada,
                          retonra una lista con 9 listas de Nones

* insertarNumeroEntablero(): Recibe (lista de listas,coordenadas,numero)
                               retorna una lista actualizada

* determinarGanador(): Recibe una lista(tablero)
                       retorna una lista (tablero) y retorna ganador

"""

def generarTableroLogico():
    tableroLogico=[[None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None,None]]
    
    return tableroLogico


def insertarNumeroEnTablero(tableroLogico:list,coordenadas:str,numero:str):

    [cuadro_mayor,posicion]=coordenadas.split('-')

    cuadro_mayor=int(cuadro_mayor)
    posicion=int(posicion)

    while tableroLogico[cuadro_mayor][posicion]!=None:
        
        coordenadas=input('Ingrese unas coordenadas DISPONIBLE por favor --> ')
        [cuadro_mayor,posicion]=coordenadas.split('-')

        while (cuadro_mayor not in ('0','1','2','3','4','5','6','7','8')) or (posicion not in ('0','1','2','3','4','5','6','7','8')):
            coordenadas=input('Ingrese una coordenadas VALIDA y DISPONIBLE (0-8) --> ')
            [cuadro_mayor,posicion]=coordenadas.split('-')
        
        cuadro_mayor=int(cuadro_mayor)
        posicion=int(posicion)

    tableroLogico[cuadro_mayor][posicion]=numero

    return tableroLogico



def generarNumerosFijos(tableroLogico_1:list,tableroLogico_2):
    import random

    cuadros=(0,1,2,3,4,5,6,7,8)

    for cuadro in cuadros:

        posicion=[0,1,2,3,4,5,6,7,8]
        numeros=[0,1,2,3,4,5,6,7,8]
        cantidad=(2,3,4)

        cantidad_aleatoria=random.choice(cantidad)

        for i in range(0,cantidad_aleatoria):

            pos=random.choice(posicion)
            posicion.remove(pos)

            num=random.choice(numeros)
            numeros.remove(num)

            tableroLogico_1[cuadro][pos]=num
            tableroLogico_2[cuadro][pos]=num

    return tableroLogico_1,tableroLogico_2

if __name__=="__main__":
    import Interfaz

    tablero=generarTableroLogico()
    tableroFijo=generarTableroLogico()
    #Interfaz.imprimirTablero(tablero)

    [tablero,tableroFijo]=generarNumerosFijos(tablero,tableroFijo)
    

    tablero=insertarNumeroEnTablero(tablero,'0-0','8')
    tablero=insertarNumeroEnTablero(tablero,'1-0','8')


    Interfaz.imprimirTablero(tableroFijo)
    Interfaz.imprimirTablero(tablero)

