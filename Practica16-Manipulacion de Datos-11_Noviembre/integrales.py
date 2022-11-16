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

x=np.arange(0,5,0.001)
y=2*(x**2)

def graficaGenerica(x,y):

    plt.figure()
    plt.plot(x,y,"o")
    plt.show()

integral_numerica=np.trapz(y,x)

#graficaGenerica(x,y)

print("teorico = 83.3333333333")
print("numerico =",integral_numerica)
