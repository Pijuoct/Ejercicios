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

        while (cuadro_mayor and posicion) not in ('0','1','2','3','4','5','6','7','8'):
            coordenadas=input('Ingrese una coordenadas VALIDA y DISPONIBLE (0-8) --> ')
            [cuadro_mayor,posicion]=coordenadas.split('-')
        
        cuadro_mayor=int(cuadro_mayor)
        posicion=int(posicion)

    tableroLogico[cuadro_mayor][posicion]=numero

    return tableroLogico


if __name__=="__main__":
    import Interfaz

    tablero=generarTableroLogico()
    Interfaz.imprimirTablero(tablero)


    tablero=insertarNumeroEnTablero(tablero,'4-8','8')
    tablero=insertarNumeroEnTablero(tablero,'2-6','9')
    tablero=insertarNumeroEnTablero(tablero,'5-1','2')
    tablero=insertarNumeroEnTablero(tablero,'0-3','9')
    tablero=insertarNumeroEnTablero(tablero,'7-8','1')

    Interfaz.imprimirTablero(tablero)

