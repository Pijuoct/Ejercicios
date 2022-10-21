#Obtener tableroLogico() --> lista
#insertarCaracter (tablerologico, posicion, caracter)
#determinarGanador (tableroLogico) --> 'X' 'O' 'NP'

"""
Este modulo contiene 3 funciones:

* generarTableroLogico(): No recibe nada,
                          retonra una lista de Nones

* generarPosiciones(): No recibe nada,
                       returno una lista de Nones

* insertarCaracterEntablero(): Recibe (lista,posicion,caracter)
                               retorna una lista actualizada

* determinarGanador(): Recibe una lista(tablero)
                       retorna una lista (tablero) y retorna ganador

"""

def generarTableroLogico():
    tableroLogico=[None]*9
    
    return tableroLogico


def insertarCaracterEnTablero(tableroLogico:list,posicion:int,caracter:str):

    while tableroLogico[posicion]!=None:
        
        posicion=int(input('Ingrese una posicion DISPONIBLE por favor --> '))
    
    tableroLogico[posicion]=caracter

    return tableroLogico

def determinarGandor(tableroLogico:list):

    posicionesAComparar=[(0,1,2),
                         (3,4,5),
                         (6,7,8),
                         (0,3,6),
                         (1,4,7),
                         (2,5,8),
                         (0,4,8),
                         (2,4,6)]

    Ganador=None

    for pos1,pos2,pos3 in posicionesAComparar:
        if tableroLogico[pos1]==tableroLogico[pos2]==tableroLogico[pos3] and tableroLogico[pos1]!=None:
            Ganador=tableroLogico[pos1]
            break
    return Ganador


if __name__=="__main__":
    tablero=generarTableroLogico()
    print(tablero)

    tablero=insertarCaracterEnTablero(tablero,0,'O')
    tablero=insertarCaracterEnTablero(tablero,4,'O')
    tablero=insertarCaracterEnTablero(tablero,8,'O')

    print(tablero)

    print(determinarGandor(tablero))