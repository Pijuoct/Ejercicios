"""
Este modulo contiene 3 funciones:

* generarTableroLogico(): No recibe nada,
                          retonra una lista con 9 listas de Nones

* insertarNumeroEntablero(): Recibe (lista de listas,coordenadas,numero)
                               retorna una lista actualizada

* generarNumerosFijos(): Recibe dos listas (tableroLogico_1,TableroLogico_2)
                         retorna dos lista (tableroLogico,TableroLogicoFijo)

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

    tableroLogico[cuadro_mayor][posicion]=numero

    return tableroLogico



def generarNumerosFijos(tableroLogico_1:list,tableroLogico_2):
    import random

    cuadros=(0,1,2,3,4,5,6,7,8)

    lineasH=[((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)),
             ((0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)),
             ((0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)),
             ((3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)),
             ((3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)),
             ((3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)),
             ((6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)),
             ((6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)),
             ((6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8))]

    lineasV=[((0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)),
             ((1,0),(1,3),(1,6),(4,0),(4,3),(4,6),(7,0),(7,3),(7,6)),
             ((2,0),(2,3),(2,6),(5,0),(5,3),(5,6),(8,0),(8,3),(8,6)),
             ((0,1),(0,4),(0,7),(3,1),(3,4),(3,7),(6,1),(6,4),(6,7)),
             ((1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)),
             ((2,1),(2,4),(2,7),(5,1),(5,4),(5,7),(8,1),(8,4),(8,7)),
             ((0,2),(0,5),(0,8),(3,2),(3,5),(3,8),(6,2),(6,5),(6,8)),
             ((1,2),(1,5),(1,8),(4,2),(4,5),(4,8),(7,2),(7,5),(7,8)),
             ((2,2),(2,5),(2,8),(5,2),(5,5),(5,8),(8,2),(8,5),(8,8))]

    NombresH=['H1','H2','H3','H4','H5','H6','H7','H8','H9']

    NombresV=['V1','V4','V7','V2','V5','V8','V3','V6','V9']

    lineasHDic=dict(zip(NombresH,lineasH))

    lineasVDic=dict(zip(NombresV,lineasV))

    duplas=[]
    lineasInterceptasLista=[]

    for cuadro in cuadros:
        for posicion in range(0,9):
            dupla=(cuadro,posicion)
            duplas.append(str(dupla).replace(' ',''))

            listaIndex=[]
            for index in lineasHDic.keys():
                if dupla in lineasHDic[index]:
                    listaIndex.append(index)

            for index in lineasVDic.keys():
                if dupla in lineasVDic[index]:
                    listaIndex.append(index)

            lineasInterceptasLista.append(listaIndex)

    lineasInterceptasDic=dict(zip(duplas,lineasInterceptasLista))

    for cuadro in cuadros:

        posicion=[0,1,2,3,4,5,6,7,8]
        numeros=[1,2,3,4,5,6,7,8,9]
        cantidad=(2,3,4,5)

        cantidad_aleatoria=random.choice(cantidad)

        for i in range(0,cantidad_aleatoria):

            if numeros!=[]:

                pos=random.choice(posicion)
                posicion.remove(pos)

                [linea1,linea2]=lineasInterceptasDic['('+str(cuadro)+','+str(pos)+')']

                fila1=[]
                fila2=[]

                for cuadro1,posicion1 in lineasHDic[linea1]:
                    numeroExistente=tableroLogico_1[cuadro1][posicion1]
                    fila1.append(numeroExistente)

                for cuadro1,posicion1 in lineasVDic[linea2]:
                    numeroExistente=tableroLogico_1[cuadro1][posicion1]
                    fila2.append(numeroExistente)


                num=random.choice(numeros)
                numeros.remove(num)

                while num in fila1 or num in fila2:
                    numerosFilas=[]

                    if numeros!=[]:
                        num=random.choice(numeros)
                        numerosFilas.append(num)
                        numeros.remove(num)
                    else:
                        num=' '
                        #print('BREAK')
                        break
                    
                    numerosFilas.remove(num)
                    numeros.extend(numerosFilas)

                tableroLogico_1[cuadro][pos]=num
                tableroLogico_2[cuadro][pos]=num
            else:
                #print('BREAK')
                break


    return tableroLogico_1,tableroLogico_2

if __name__=="__main__":
    import Interfaz

    tablero=generarTableroLogico()
    tableroFijo=generarTableroLogico()

    #[tablero,tableroFijo]=generarNumerosFijos(tablero,tableroFijo)
    
    #insertarNumeroEnTablero(tablero,'0-0',1)


    Interfaz.imprimirTablero(tableroFijo)
    Interfaz.imprimirTablero(tablero)

