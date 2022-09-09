#Ejemplo:
alturas=[10,20,50,80,1,50]
mensaje='holamundo'
pesos=(1,2,3,4,5,6)
secuencia= range(1,10)


print('\nalturas')
for altura in alturas:
    print(altura,end=' ')

print('\nmensanes')
for msg in mensaje:
    print(msg,end='-')

print('\npesos')
for peso in pesos:
    print(peso,end='--')

print('\nsecuencia')
for s in secuencia:
    print(s,end=' ')

"""Utilizar el ciclo for para recorrer iterables sin definirlos"""

print('\nalturas')
for altura in [10,20,50,80,1,50]:
    print(altura,end=' ')

"""
Utilizando el ciclo para generar las siguientes secuencias
"""
print('')
print('')
print('')
print('')
#    * 10, 11, 12, 13, 14, 15, 16, .. 20
for i in range(10, 21, 1):
    print(i, end=' ')

print('')
print('')
#    * 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
for i in range(3, 31, 3):
    print(i, end=' ')

print('')
print('')
#    * 3, 6, 9, 12, 15, 18, 21, 24, 27, 33, 36, 39, 42, 45
for i in range(3, 46, 3):
#    if i!=30:
#        print(i, end=' ')
    if i==30:
        continue
    print(i, end=' ')

print('')
print('')
#    * número pares del 200 al 400
for i in range(200, 401, 2):
    print(i, end=' ')

print('')
print('')
#    * las primeras 20 potencias de 2
for i in range(1,21):
     print(2**i, end = " ")
print()


print('')
print('')
"""determinar si un numero es primo"""

n=7
bandera=True
factores=range(2,n)


for factor in factores:
    if (n%factor)==0:
        print(n,'NO es primo', end='\n\n')
        bandera=False
        break

if bandera==True:
    print(n,'Es primo', end='\n\n')