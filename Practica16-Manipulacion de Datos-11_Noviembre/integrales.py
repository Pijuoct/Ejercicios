# 16-11-2022

#----------------- integrales -----------------

#se resuelve utilizando el metodo del trapecio (calculando areas)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
calcular la integral para f(x) = 2x^2 , en los limites x = [0,5]
la integral debe dar (2/3)x^3 [x=0,x=5] = 83.3333333333333333333
"""

limite_inferior=0
limite_superior=5
salto=0.001

x=np.arange(limite_inferior,limite_superior+salto,salto)
y=2*(x**2)

def graficaGenerica(x,y):

    plt.figure()
    plt.plot(x,y,"o")
    plt.show()

integral_numerica=np.trapz(y,x)

#graficaGenerica(x,y)

print("teorico = 83.3333333333")
print("numerico =",integral_numerica)


"""
calcular las integrales de f1,f2,f3 del dataFrame hoja1
"""
x = np.arange(0, 6.28, 0.01)
columna1 = x * np.sin(x) + 0.005 * np.random.rand(628)
columna2 = np.cos(x) + 0.005 * np.random.rand(628)
columna3 = x * 1/2
data = np.column_stack((columna1,columna2,columna3))
hoja1 = pd.DataFrame(data= data,
                     index= x,
                     columns= ["f1", "f2", "f3"])

print(hoja1)

# fig,(ax1,ax2,ax3) = plt.subplots(1,3)
# ax1.plot(x, columna1)
# ax2.plot(x, columna2)
# ax3.plot(x, columna3)
# plt.show()

plt.figure(figsize=(12,4))
for i in range(1,4):
    plt.subplot(1,3,i)
    x = hoja1.index
    y = hoja1.iloc[:,i-1]
    plt.plot(x,y)

plt.savefig("lienzo")
plt.show()


for i in range(0,3):
    x = hoja1.index
    y = hoja1.iloc[:,i]
    integral_numerica = np.trapz(y,x)
    print("integral f{} = ".format(i+1), integral_numerica)

