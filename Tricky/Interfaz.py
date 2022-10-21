"""
Aqui se contiene la parte visual del tricky. 

Este modulo contiene 2 funciones:

* explicarJuego(): Retorna un mensaje explicativo
* imprimirTablero(): Retornar un string con el tablero

"""


def explicarJuego():
    explicacion="""
    ==================================================================
    Bienvenido, esto es triky.

    Para ganar debe completar una linea recta, compuesta por un mismo
    caracter ya sea "X" o "O"

    linea recta => horizontal, vertial o diagonal

    Debe ingresar la posicion 0-8, para ingresar la opcion durante
    su turno

      0  |  1  |  2  
    -----------------
      3  |  4  |  5  
    -----------------
      6  |  7  |  8   

    ==================================================================
    """

    print(explicacion)

def imprimirTablero(tableroLogico:list):

    tableroVisual= """      
      {}  |  {}  |  {}  
    -----------------
      {}  |  {}  |  {}  
    -----------------
      {}  |  {}  |  {}   
    """.format(tableroLogico[0],
               tableroLogico[1],
               tableroLogico[2],
               tableroLogico[3],
               tableroLogico[4],
               tableroLogico[5],
               tableroLogico[6],
               tableroLogico[7],
               tableroLogico[8]).replace('None',' ')

    print(tableroVisual)

if __name__=="__main__":
    explicarJuego()
    imprimirTablero(['X',None,None,None,None,'X',None,None,'O'])

