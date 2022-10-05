# -----diccionarios--------
# Extraccion: items(), keys(), values(), get(key)
# Eliminar: pop(key)
# Almacenamiento: clear(), copy()
# Indexado: [key]

print('')

'''
Los diccionarios son una estructura que contiene un par
clave: valor y nos permite acceder a la informacion de manera
mas personalizada y eficiente
'''

diccionarioEstudiantes={
    "Cristian Pachon":   2.0,
    'Maria Bermudez':    3.0,
    'Camilo Ibarra':     4.0,
    'Fernado Gutierrez': 5.0
}

diccionarioPaises={
    'Colombia': ['Cali','Manizales','Cartagena'],
    'Argentina':['Buenos Aires','La Plata','Cordoba'],
    'Brasil':   ['Sao Paulo','Brasilia','Minas Gerais'],
}

diccionarioNumeros={
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro'
}



#¿Como extraer un valor dada una clave?

valor=diccionarioEstudiantes["Cristian Pachon"]
print(valor)

for clave in ["Cristian Pachon",'Maria Bermudez','Camilo Ibarra','Fernado Gutierrez']:
    print(diccionarioEstudiantes[clave])

print('')
print('')

#¿Como eliminar un par clave-valor?
"""eliminar los elementos cuya clave empiece por c"""

for clave in ["Cristian Pachon",'Maria Bermudez','Camilo Ibarra','Fernado Gutierrez']:
    if clave[0]=='C':
        diccionarioEstudiantes.pop(clave)
print(diccionarioEstudiantes)

print('')
print('')

#¿Como agrego elementos?
"""
agregue:
- Juan Loaiza (3.2)
- Sofia Ospina (5.0)
- Miguel Pineda (3.1)
"""

diccionarioEstudiantes["Juan Loaiza"]=3.2
diccionarioEstudiantes["Sofia Ospina"]=5.0
diccionarioEstudiantes["Miguel Pineda"]=3.1

print(diccionarioEstudiantes)

print('')
print('')

#¿Como cambio un valor?

for clave in diccionarioEstudiantes:
    if clave.split()[0][-1]=='a':
        diccionarioEstudiantes[clave]=5.0
    else:
        diccionarioEstudiantes[clave]=0.0

print(diccionarioEstudiantes)

print('')
print('')

#¿Como extraer las claves de un diccionario?

claves=diccionarioEstudiantes.keys()
print(claves)

print('')
print('')

#¿Como extraer los valores de un diccionario?

valores=diccionarioEstudiantes.values()
print(valores)

print('')
print('')

#¿Como extraer las parejas clave-valor de un diccionario?

items=diccionarioEstudiantes.items()
print(items)

print('')
print('')

for par in items:
    print(str(par[0])+'-'+str(par[1]))

print('')

for clave in claves:
    print(str(clave)+'-'+str(diccionarioEstudiantes[clave]))


"""
EJERCICIOS CLASE

1) Crear la siguiente base de datos utilizando diccionarios
Costo de entrada al cine 
                   Niños       Adultos
Entre semana        5000         7000
Fin de semana       8000         1000
* ¿Cómo acceder al precio de la entrada utilizando como claves
si es niño-adulto y si es Entre Semana-Fin de semana
"""
print('')


precioS={
    'Adulto':7000,
    'Niño':5000
}

precioF={
    'Adulto':10000,
    'Niño':8000
}

fecha={
    'Semana':precioS,
    'Fin':precioF
}

print(fecha['Semana']['Adulto'])

# tiempo=input('Ira al cine entre Semana o un Fin de semana (ingrese "Semana" o "Fin")--> ')
# opcion=input('Comprara una boleta de adulto o de niño (ingrese "Adulto" o "Niño")--> ')

# momento_semana=fecha[tiempo]

# print('')

# if momento_semana=='S':
#     valor_pagar=precioS[opcion]
#     print('El valor de una boleta para un %s entre %s es de %d'%(opcion,tiempo,valor_pagar))
# else:
#     valor_pagar=precioF[opcion]
#     print('El valor de una boleta para un %s un %s de semana es de %d'%(opcion,tiempo,valor_pagar))



"""
2) Crear la siguiente base de datos utilizando diccionarios
CodEstudiante   Ingles Deportes Idiomas Cuantica Español
    01           2.0     2.2     4.2       4.0    0.5
    02           2.2     1.0     4.0       3.1    4.0
    03           2.9     4.2     3.1       0.0    3.1
    04           2.0     4.0     4.0       0.2    0.0
    05           2.2     0.2     0.2       1.0    0.2
    06           2.0     5.0     1.0       1.3    1.0
    07           5.0     1.2     1.2       1.9    1.3
    08           0.2     2.9     1.0       4.2    1.9
    09           5.0     2.3     2.9       2.9    0.2
    10           4.2     5.0     4.2       4.2    3.9
    11           4.5     4.2     4.0       0.5    4.2
    12           4.2     4.5     4.2       0.0    0.5
    13           0.5     0.5     2.3       4.2    0.0
    14           4.1     3.1     2.5       4.3    3.2
    15           4.2     4.2     4.2       2.5    4.3
    16           4.1     0.0     4.5       4.2    2.5
    17           1.2     3.1     0.5       4.5    3.2
    18           0.5     0.2     4.1       4.1    4.5
    19           2.2     0.5     0.2       0.2    4.1
*Cómo acceder a la base de datos utilizando como clave
 el codigo y la materia
*Determine el promedio de cada estudiante             
*Determine el promedio de cada una de las materias
*Determine los 3 estudiantes con peor promedio
0.5
4.0
3.1
0.0
0.2
1.0
1.3
1.9
0.2
3.9
4.2
0.5
0.0
3.2
4.3
2.5
3.2
4.5
4.1
3.2
"""
print('')

materias=['Ingles','Deportes','Idiomas','Cuantica','Español']
notas=[
            [2.0,      2.2,      4.2,       4.0,      0.5],
            [2.2,      1.0,      4.0,       3.1,      4.0],
            [2.9,      4.2,      3.1,       0.0,      3.1],
            [2.0,      4.0,      4.0,       0.2,      0.0],
            [2.2,      0.2,      0.2,       1.0,      0.2],
            [2.0,      5.0,      1.0,       1.3,      1.0],
            [5.0,      1.2,      1.2,       1.9,      1.3],
            [0.2,      2.9,      1.0,       4.2,      1.9],
            [5.0,      2.3,      2.9,       2.9,      0.2],
            [4.2,      5.0,      4.2,       4.2,      3.9],
            [4.5,      4.2,      4.0,       0.5,      4.2],
            [4.2,      4.5,      4.2,       0.0,      0.5],
            [0.5,      0.5,      2.3,       4.2,      0.0],
            [4.1,      3.1,      2.5,       4.3,      3.2],
            [4.2,      4.2,      4.2,       2.5,      4.3],
            [4.1,      0.0,      4.5,       4.2,      2.5],
            [1.2,      3.1,      0.5,       4.5,      3.2],
            [0.5,      0.2,      4.1,       4.1,      4.5],
            [2.2,      0.5,      0.2,       0.2,      4.1]
]


#=============================================
clase={}

for codigo in range(1,20):
    if len(str(codigo))==1:
        clase['0'+str(codigo)]=dict(zip(materias,notas[codigo-1]))
    else:
        clase[str(codigo)]=dict(zip(materias,notas[codigo-1]))

print(clase['13']['Cuantica'])


#=============================================
promedioEst={}

for code in range(1,20):

    if len(str(code))==1:
        codigo='0'+str(code)
    else:
        codigo=str(code)

    notas=clase[codigo].values()
    
    suma=0
    total=len(clase[codigo])

    for nota in notas:
        suma+=nota

    prom=suma/total

    promedioEst[codigo]=prom

print(promedioEst)

#=============================================
promedioCla={}

for code in range(1,20):

    if len(str(code))==1:
        codigo='0'+str(code)
    else:
        codigo=str(code)

    #hacer un if para ver si si es la clase deseada
    #coger la ntoa de esa clase por cd/est
    #sumar la nota a la suma total
    #dividir en los 19 est
    #repetir para cada clase

    notas=clase[codigo].values()
    
    suma=0
    total=len(clase[codigo])

    for nota in notas:
        suma+=nota

    prom=suma/total

    promedioCla[codigo]=prom

print(promedioCla)

print('')