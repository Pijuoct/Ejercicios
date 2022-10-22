"""
Este modulo contendra las siguiente funciones:

* instrucciones(): No recibe nada,
                   Retorna un string

* imprimirTablero(): Recibe una lista de listas,
                     Retorna un string

"""


def instrucciones():
    mensaje="""
    =====================================================================
    Bienvenido, esto es Sudoku.

    Para ganar debe completar todas las cuadriculas del Sudoku, en cada cuadricula deben
    estar los numeros del 1 al 9 sin repeticion. ademas cada linea recta (horizontal y 
    vertical) tambien debe poseer los numeros del 1 al 9 sin repeticion.

    Para jugar debe ingresar la posicion de la forma "a-b" donde a,b son numeros entre 0 y 8
    el numero "a" corresponde al cuadro mayor y el numero "b" a la posicion dentro del cuadro
    mayor elegido.
    
    Las posiciones posibles son:

    ===========================================================
    || 0-0 | 0-1 | 0-2 || 1-0 | 1-1 | 1-2 || 2-0 | 2-1 | 2-2 ||
    ||-----------------||-----------------||-----------------||
    || 0-3 | 0-4 | 0-5 || 1-3 | 1-4 | 1-5 || 2-3 | 2-4 | 2-5 ||
    ||-----------------||-----------------||-----------------||
    || 0-6 | 0-7 | 0-8 || 1-6 | 1-7 | 1-8 || 2-6 | 2-7 | 2-8 ||
    ===========================================================
    || 3-0 | 3-1 | 3-2 || 4-0 | 4-1 | 4-2 || 5-0 | 5-1 | 5-2 ||
    ||-----------------||-----------------||-----------------||
    || 3-3 | 3-4 | 3-5 || 4-3 | 4-4 | 4-5 || 5-3 | 5-4 | 5-5 ||
    ||-----------------||-----------------||-----------------||
    || 3-6 | 3-7 | 3-8 || 4-6 | 4-7 | 4-8 || 5-6 | 5-7 | 5-8 ||
    ===========================================================
    || 6-0 | 6-1 | 6-2 || 7-0 | 7-1 | 7-2 || 8-0 | 8-1 | 8-2 ||
    ||-----------------||-----------------||-----------------||
    || 6-3 | 6-4 | 6-5 || 7-3 | 7-4 | 7-5 || 8-3 | 8-4 | 8-5 ||
    ||-----------------||-----------------||-----------------||
    || 6-6 | 6-7 | 6-8 || 7-6 | 7-7 | 7-8 || 8-6 | 8-7 | 8-8 ||
    ===========================================================
    """
    print(mensaje)

def imprimirTablero(tableroLogico:list):

    tableroVisual= """
    =========================================
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    ||-----------||-----------||-----------||
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    ||-----------||-----------||-----------||
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    =========================================
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    ||-----------||-----------||-----------||
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    ||-----------||-----------||-----------||
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    =========================================
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    ||-----------||-----------||-----------||
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    ||-----------||-----------||-----------||
    || {} | {} | {} || {} | {} | {} || {} | {} | {} ||
    =========================================
    """.format(tableroLogico[0][0],tableroLogico[0][1],tableroLogico[0][2],tableroLogico[1][0],tableroLogico[1][1],tableroLogico[1][2],tableroLogico[2][0],tableroLogico[2][1],tableroLogico[2][2],
               tableroLogico[0][3],tableroLogico[0][4],tableroLogico[0][5],tableroLogico[1][3],tableroLogico[1][4],tableroLogico[1][5],tableroLogico[2][3],tableroLogico[2][4],tableroLogico[2][5],
               tableroLogico[0][6],tableroLogico[0][7],tableroLogico[0][8],tableroLogico[1][6],tableroLogico[1][7],tableroLogico[1][8],tableroLogico[2][6],tableroLogico[2][7],tableroLogico[2][8],
               tableroLogico[3][0],tableroLogico[3][1],tableroLogico[3][2],tableroLogico[4][0],tableroLogico[4][1],tableroLogico[4][2],tableroLogico[5][0],tableroLogico[5][1],tableroLogico[5][2],
               tableroLogico[3][3],tableroLogico[3][4],tableroLogico[3][5],tableroLogico[4][3],tableroLogico[4][4],tableroLogico[4][5],tableroLogico[5][3],tableroLogico[5][4],tableroLogico[5][5],
               tableroLogico[3][6],tableroLogico[3][7],tableroLogico[3][8],tableroLogico[4][6],tableroLogico[4][7],tableroLogico[4][8],tableroLogico[5][6],tableroLogico[5][7],tableroLogico[5][8],
               tableroLogico[6][0],tableroLogico[6][1],tableroLogico[6][2],tableroLogico[7][0],tableroLogico[7][1],tableroLogico[7][2],tableroLogico[8][0],tableroLogico[8][1],tableroLogico[8][2],
               tableroLogico[6][3],tableroLogico[6][4],tableroLogico[6][5],tableroLogico[7][3],tableroLogico[7][4],tableroLogico[7][5],tableroLogico[8][3],tableroLogico[8][4],tableroLogico[8][5],
               tableroLogico[6][6],tableroLogico[6][7],tableroLogico[6][8],tableroLogico[7][6],tableroLogico[7][7],tableroLogico[7][8],tableroLogico[8][6],tableroLogico[8][7],tableroLogico[8][8]).replace('None',' ')

    print(tableroVisual)

if __name__=="__main__":
    instrucciones()
    imprimirTablero([[1,None,6,7,None,2,None,None,3],
                     [1,None,6,7,None,9,None,None,3],
                     [1,None,6,7,None,9,None,None,3],
                     [1,None,6,7,None,9,None,None,3],
                     [1,2,6,7,None,9,None,None,3],
                     [1,None,6,7,None,9,None,None,3],
                     [1,None,6,7,None,9,None,None,3],
                     [1,None,6,7,None,9,None,None,3],
                     [1,None,6,7,None,9,None,None,3]])