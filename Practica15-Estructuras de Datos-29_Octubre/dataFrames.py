"""crear un dataFrame compuesto por la siguiente informacion =>
codigo   tamaño   precio  
  Semestre 1     1       12000   
  Semestre 1         2       15000 
  Semestre 2      3       21000
           2       32000
           1       11000
           2       90000"""

import numpy as np
import pandas as pd

data = np.array([[1, 12000],   
                 [2, 15000], 
                 [3, 21000],
                 [2, 32000],
                 [1, 11000],
                 [2, 90000]])

hoja1 = pd.DataFrame( data = data,
                      columns = ["tamaño", "precio"],
                      index = ["001","001","003","004","005","006"])

print(hoja1.loc['001'])


"""
Crear un dataframe que cumpla con lo siguiente:

cada columna hace referencia a una funcion f1,f2,f3,f4,f5
los indices van a ser referencia al variable independiente [0,0.5,1,1.5,...,200]
semestre =  10
 for i in range (0,len(semestre)):
   Index = str(i)
   Semestre = 'Semestre '+ Index
   Semestre = Semestre 1 , Semestre 2,
   print(DATAFRAME(Semestre))
   print('///////////////////////////////////////////////////)
    

f1(x)= 3x + 5
f2(x)= x + random
f3(x)= sen(x)
f4(x)= e^x
f5(x)= x+sen(x) + random
"""

x=np.arange(0,200.1,0.5)

f1 = 3*x + 5
f2 = x + np.random.rand(401)
f3 = np.sin(x)
f4 = np.exp(x)
f5 = x*np.sin(x) + np.random.rand(401)

# print("f1 =>", f1[0:10])
# print("f2 =>", f2[0:10])
# print("f3 =>", f3[0:10])
# print("f4 =>", f4[0:10])
# print("f5 =>", f5[0:10])

data=np.column_stack((f1,f2,f3,f4,f5))

hoja2=pd.DataFrame(data=data,
                   columns=['f1','f2','f3','f4','f5'],
                   index=x)

print(hoja2)

# mediasC = hoja2.mean(axis=0)
# mediasF = hoja2.mean(axis=1)

# medias = hoja2.mean(axis=0)
# medianas = hoja2.median(axis=0)
# desviaciones = hoja2.std(axis=0)

minimos = hoja2.min(axis=0)
maximos = hoja2.max(axis=0)

print("-----------------------")
print("minimos =>\n", minimos)
print("maximos =>\n", maximos)


#11-11-2022

#-------------Indexado de dataframes --------------------------

#El indexado se trabaja igual que en los arreglos numpy.
#Ademas se puede acceder por clave


arreglo = np.arange(1,25).reshape(3,8)

hoja3 = pd.DataFrame(data= arreglo,
                     columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"],
                     index = ["Alex", "Juan", "Maria"])
print(hoja3)



"""
Ejemplo: Acceder a toda la columna col3
         Acceder a toda la fila Alex"
"""

columna = hoja3["col3"]
fila = hoja3.loc["Alex"]

print("columna =>\n", columna)
print("fila=>\n", fila)


resultado=hoja3.loc['Maria','col2']
print(resultado)
