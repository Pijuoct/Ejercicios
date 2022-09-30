# ------Listas---------
# operaciones: append(value), insert(index, value), 
#              pop(index), remove(value), --> remover elementos
#              count(value)
# ordenado:    sort(), reverse()
# almacenamiento: clear(), copy()
# Indexado: [indice]
# Slicing:  [indice1:indice2:salto]

"""
crear las siguientes listas:

lista1=[1,2,3,4,5,6,7,8]
lista2=list(range(20))+['a','b','c',100]
lista3=['Cruel','Mundo','Hola',1,100,200,500]


Realice lo siguiente:

*Agregar al final de la lista1, los elementos -> 1,2,3,4
*Agregar al comienzo de la lista1, los elementos -> 0,0,2,4
*Eliminar los 3 ultimos elementos de la lista1
*Eliminar los 2 primeros elementos de la lista1


*Sume todos los elementos de la lista2 que pueden operarse algebraicamente
*Organice la lista2 de forma ascendete
*Elimine todos los elementos de la lista2 original que sean enteros

*Sume todos los elementos de la lista3 que pueden operarse algebraicamente
si alterar o cambiar la lista3 original
*Haga una copia de la lista3 de la siguiente manera:
lista3copia=lista3
y agregue 3 nuevos elementos sobre esta nueva lista, que sucede con la originial?
*Encuentre una manera de alterar la copia sin afectar la original

INDEXADO -> extraer el elemento inicial de lista1 (de dos maneras)
            extraer el elemento final de lista1 (de dos maneras)
            extraer el elemento medio de lista2 (de dos maneras)

SLICING -> extraer los primeros 3 elementos de la lista 1,2,3 y colocarlos en una nueva lista
           extraer cada 2 elementos de la lista 2
           extraer todos los elementos de la lista3 al reves
           extraer los indices impares de la lista 3
"""

lista1=[1,2,3,4,5,6,7,8]
lista2=list(range(20))+['a','b','c',100]
lista3=['Cruel','Mundo','Hola',1,100,200,500]

print(lista1)

lista1.extend([1,2,3,4])
print(lista1)

for index in range(0,4):
    lista1.insert(index,[0,0,2,4][index])
print(lista1)

lista1[-3:]=[]
print(lista1)

for index in range(0,2):
    lista1.pop(0)
print(lista1)

suma=0
for elemento in lista2:
    if type(elemento)==int:
        suma+=elemento
print(suma)

lista=lista2
lista2n=[]
lista2s=[]
for elemento in lista2:
    if type(elemento)==int:
        lista2n.append(elemento)
    else:
        lista2s.append(elemento)

lista2n.sort
lista2s.sort
lista2=lista2n+lista2s
print(lista2)


lista2=lista2=list(range(20))+['a','b','c',100]
lista2s=[]
for elemento in lista2:
    if type(elemento)==str:
        lista2s.append(elemento)
    else:
        pass

lista2=lista2s
print(lista2)


suma=0
for elemento in lista3:
    if type(elemento)==int:
        suma+=elemento
print(suma)
        

# *Haga una copia de la lista3 de la siguiente manera:
# lista3copia=lista3
# y agregue 3 nuevos elementos sobre esta nueva lista, que sucede con la originial?
#
#R= solo es un re nombre, al alterar 1, cambia el otro

lista1=[1,2,3,4,5,6,7,8]
lista2=list(range(20))+['a','b','c',100]
lista3=['Cruel','Mundo','Hola',1,100,200,500]

print(lista1[0],lista1[-len(lista1)])

print(lista1[0:3]+lista2[0:3]+lista3[0:3])

print(lista2[0:len(lista2)-1:2])
print(lista2[::2]) 
#son iguales esos 2 prints, del inicio al fin no hay que poner las especificaciones

print(lista3[::-1])

