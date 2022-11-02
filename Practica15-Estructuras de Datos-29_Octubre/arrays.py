"""
Ejemplos: crear los siguientes vectores, matrices y tensores
vector1 = 1,2,3,4,5
vector2 = 10,20,30,40,50
matriz1 = [1 1 1
           1 1 1
           1 1 1]
matriz2 = [1 2 3
           4 5 6
           7 8 9]
tensor1=[[0 0 0
          0 0 0
          0 0 0]
         [2 2 2
          2 2 2
          2 2 2]] 
tensor2= [[1  2  3
           4  5  6
           7  8  9]
          [10 11 12
           13 14 15
           16 17 18]] 
"""
import numpy as np

#Como crear los vectores numpy
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([10,20,30,40,50])

#como crear matrices numpy
matriz1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

matriz2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

#como crear tensores
tensor1= np.array([ [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],
                 
                    [[2, 2, 2],
                     [2, 2, 2],
                     [2, 2, 2]]
                 ])

tensor2= np.array([ [[1,  2,  3],
                     [4,  5,  6],
                     [7,  8,  9]],
                  
                    [[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]]
                 ])


"""
ejemplos: como crear los anteriores elementos de manera rapida
"""

vector1 = np.arange(1,6,1) #inicio,fin,salto
vector2 = np.arange(10, 51, 10)

matriz1 = np.ones((3,3))   #tamaño (filas,columnas)
matriz2 = np.arange(1, 10).reshape((3,3))  #reshape (filas, columnas)

tensor1 = "pendiente"
tensor2 = np.arange(1,19).reshape((2,3,3))



"""
ejemplos: a) como apilar vector1 y vector2 y formar vector mas grande
          b) como apilar vector1 y vector2 y formar una matriz
          c) como apilar matriz1 y matriz2 y formar matriz mas ancha
          d) como apilar matriz1 y matriz1 y formar matriz más larga
"""

"""
vector1 = 1,2,3,4,5,6,100
vector2 = 10,20,30,40,50
vectorResultante = 1,2,3,4,5,6,100, 10,20,30,40,50 ?????
"""
vectorResultante = np.hstack((vector1, vector2))
print(vectorResultante)

"""
vector1 = 1,2,3,4,5,6,100
vector2 = 10,20,30,40,50
matrizResultante = 1,2,3,4,5,6,100, 
                   10,20,30,40,50
"""

matrizResultante = np.vstack((vector1, vector2))
print(matrizResultante)


"""
matriz1 = [1 1 1
           1 1 1
           1 1 1]
matriz2 = [1 2 3
           4 5 6
           7 8 9]
* Apilarlas horizontalmente
matrizAncha  = [1 1 1 1 2 3
                1 1 1 4 5 6
                1 1 1 7 8 9]
* Apilarlas verticalmente
matrizLarga = [1 1 1 
               1 1 1 
               1 1 1 
               1 2 3
               4 5 6
               7 8 9]
"""

matrizAncha = np.hstack((matriz1, matriz2))
matrizLarga = np.vstack((matriz1, matriz2))
print(matrizAncha)
print(matrizLarga)


"""
como apilar un vector con una matriz de forma 
horizontal y vertical
"""
vectorNuevo = np.array([1,2,3])
matrizNueva = np.arange(1,10).reshape((3,3))
print("=>\n", vectorNuevo)
print("=>\n", matrizNueva)

matrizNueva1 = np.vstack((matrizNueva, vectorNuevo))
print(matrizNueva1)

matrizNueva1 = np.hstack((matrizNueva, vectorNuevo.reshape((3,1))))
print(matrizNueva1)


"""
acceder a 3 columnas distintas del vector 1


"""

print('-----------------------------indexado-----------------------------')
value1=vector1[0]
value2=vector1[2]
value3=vector1[-1]

print(value1,value2,value3)

"Ejemplo: acceder al valor ubicado en la fila 1, columna 3 de matriz1"

value1=matriz2[0,2]
print(matriz2,value1)

value1=matriz2[1,1]
print(matriz2,value1)


"Ejemplo: acceder a filas y columnas"
fila2=matriz2[1,:]
columna3=matriz2[:,2]
print(fila2,columna3)

"Ejemplo: acceder a secciones"
seccion=matriz2[1:,0:2]
print(seccion)


"""Cree la siguiente matriz y el siguiente vector

matriz=[1  2  3  4  5
        6  7  8  9  10
        11 12 13 14 15]

vector= [1 2 3]

aplique el vector a la matriz y luego extraiga una seccion compuesta 
por la fila 2 (indice 1) y fila 3 (indice 2)

"""

print('')
print('')
print('')
matriz=np.arange(1,16).reshape(3,5)
vector=np.arange(1,4)
print(matriz,vector)
print('')
matrizNueva1 = np.hstack((matriz, vector.reshape((3,1))))

print(matrizNueva1)
print('')
seccion=matrizNueva1[1:3,:]
print(seccion)


#------------------------------- funciones estadisticas mean, std, min, max -------------------------------

"""
calcular la media del vector 1 y vector2
"""
print('')
print('medias:')
print(vector1.mean())
print(vector2.mean())

"""Ejemplo: calcular la media de matriz2
            por fila
            por columna
            total"""

print('') #axis=0 es por columna, axis=1 es por fila
print(matriz2.mean(axis=0))
print(matriz2.mean(axis=1))
print(matriz2.mean())


"""Ejemplo: calcular la desviacion estandar, el max y min de matriz2
            por fila
            por columna
            total"""

print('') 
print(matriz2.std(axis=0))
print(matriz2.std(axis=1))
print(matriz2.std())

print('') 
print(matriz2.max(axis=0))
print(matriz2.max(axis=1))
print(matriz2.max())

print('') 
print(matriz2.min(axis=0))
print(matriz2.min(axis=1))
print(matriz2.min())

"""
ejemplo: 
determine la cantidad media de productos vendidos por trabajador
determine la media por cada producto
determine el producto menos vendido
determine el producto ccon mas ventas

"""

data=[[20    ,    22   ,    30    ,    2     ,    40      ,    20     ,   3 ],
      [31    ,    14   ,    32    ,    15    ,    13      ,    20     ,   11],
      [24    ,    32   ,    40    ,    9     ,    12      ,    50     ,   13],
      [42    ,    12   ,    33    ,    24    ,    22      ,    32     ,   23],
      [51    ,    21   ,    25    ,    10    ,    19      ,    14     ,   2 ],
      [22    ,    31   ,    51    ,    21    ,    35      ,    15     ,   11],
      [21    ,    36   ,    22    ,    32    ,    39      ,    32     ,   15],
      [22    ,    33   ,    41    ,    21    ,    43      ,    31     ,   36],
      [33    ,    31   ,    20    ,    42    ,    33      ,    42     ,   35],
      [22    ,    47   ,    5     ,    28    ,    37      ,    31     ,   32],
      [24    ,    38   ,    33    ,    21    ,    41      ,    31     ,   16],
      [21    ,    18   ,    32    ,    37    ,    39      ,    22     ,   12],
      [33    ,    31   ,    21    ,    21    ,    33      ,    39     ,   25],
      [25    ,    39   ,    20    ,    48    ,    15      ,    30     ,   32],
      [27    ,    32   ,    29    ,    28    ,    37      ,    35     ,   16],
      [24    ,    12   ,    31    ,    21    ,    39      ,    32     ,   13],
      [31    ,    31   ,    50    ,    22    ,    13      ,    30     ,   21],
      [23    ,    35   ,    35    ,    39    ,    31      ,    19     ,   19],
      [26    ,    36   ,    39    ,    27    ,    35      ,    32     ,   16],
      [25    ,    31   ,    21    ,    21    ,    25      ,    37     ,   15],
      [23    ,    34   ,    35    ,    32    ,    37      ,    20     ,   49],
      [31    ,    14   ,    29    ,    39    ,    25      ,    37     ,   16],
      [26    ,    31   ,    31    ,    27    ,    37      ,    32     ,   41],
      [40    ,    42   ,    23    ,    11    ,    21      ,    15     ,   19],
      [27    ,    31   ,    39    ,    21    ,    31      ,    32     ,   25],
      [38    ,    32   ,    19    ,    29    ,    35      ,    50     ,   16]]
 
dataarray=np.array(data)
print(dataarray)

print(dataarray.mean(axis=1))
print(dataarray.mean(axis=0))

filas,columnas=np.where(dataarray==16)
eureka=list(zip(filas,columnas))

"""Ejemplo: como guardar un arrelgo en el disco duro
"""

np.savetxt('ventasTrabajadores.csv',dataarray)