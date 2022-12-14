"""
En este archivo encontramos ejercicios para introducirnos en el lenguaje, 
ejercicios introductorios para uso de variables y ejercicios con operadores.
"""

import numpy as np
ejercicio=int(input('Que ejercicio desea ejecutar (1 a 22)--> '))


if ejercicio==1:
    #====================== EJERCICIOS INTRODUCTORIOS ====================
    #==>  EJERCICIO 1 
    """ Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
    mostrando en pantalla en formato "horas:minutos"  """
    print('EJERCICO 1')
    print('')

    seg=int(input('Ingrese una cantidad de segundos --> '))
    if seg>=60:
        min=seg//60
    if min>=60:
        hor=min//60

    min=min-(hor*60)

    min=str(min)
    hor=str(hor)

    lmin=len(str(min))
    lhor=len(str(hor))

    if lmin==1:
        min='0'+min
    if lhor==1:
        hor='0'+hor

    print('formato --> hora:minutos')
    print(hor+':'+min)


elif ejercicio==2:
    #==>  EJERCICIO 2 
    """ ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm? """
    print('')
    print('EJERCICO 2')
    print('')

    vcubo=5**3
    #v_esfera=(4/3)*np.pi*(r**3)

    r=(((5**3)*(3/4))/(np.pi))**(1/3)
    print('el radio que debe tener una esfera para que su volumen sea de 125 unidades cubicas es:',r)


elif ejercicio==3:
    #==>  EJERCICIO 3 
    """ ¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del
    cubo es 10 cm. Y el radio de la esfera 2 cm ? """
    print('')
    print('EJERCICO 3')
    print('')

    lado_cubo=10
    area_cubo=8*(10**2)

    radio_esfera=2
    area_esfera=4*np.pi*(radio_esfera**2)

    diferencia=area_cubo-area_esfera

    print('el area del cubo supera al dDDe la esfera en %d centimetros cubicos'%diferencia)


elif ejercicio==4:
    #==>  EJERCICIO 4 
    """ Realice un código, que permita la conversión de millas a km y km a millas """
    print('')
    print('EJERCICO 4')
    print('')
    

    print('Bienvenido a nuestro conversor\n\nIngrese "millas" para convertir millas a kilometros\nIngrese "kilometros" para convertir kilometros a millas')
    opciones=input('--> ')

    if opciones=='millas':
        numero=float(input('Ingrese las millas --> '))
        kilometros=numero*1.609
        print('%.4f millas corresponden a %.4f kilometros'%(numero,kilometros))
    elif opciones=='kilometros':
        numero=float(input('Ingrese los kilometros --> '))
        millas=numero/1.609
        print('%.4f millas corresponden a %.4f kilometros'%(numero,millas))
    else:
        print('El usuario no ingreso unidades validas')



elif ejercicio==5:
    #==>  EJERCICIO 5 
    """ Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
    Realice un codigo que determine la distancia entre ambos puntos """

    print('')
    print('EJERCICO 5')
    print('')

    distancia_x=(5-0)**2
    distancia_y=(4-10)**2
    distancia_z=(5-9)**2

    sumatoria=distancia_x+distancia_y+distancia_z
    distancia_total=(sumatoria)**(1/2)

    print('la distancia total entre los puntos (5,4,5) y (0,10,9) es %.4f unidades'%distancia_total)


elif ejercicio==6:
    #==>  EJERCICIO 6 
    """ La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
    con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
    Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

    print('')
    print('EJERCICO 6')
    print('')

    nota_1=float(input('Ingrese su 1ra nota --> '))*0.15
    nota_2=float(input('Ingrese su 2da nota --> '))*0.25
    nota_3=float(input('Ingrese su 3ra nota --> '))*0.2

    #nota_final=(nota_1*0.15)+(nota_2*0.25)+(nota_3*0.2)+(nota_4*0.4)
    nota_4=(3-nota_1-nota_2-nota_3)/0.4

    print('Necesitas un %.2f para pasar tu materia ¡Animoo!'%nota_4)


elif ejercicio==7:
    #==>  EJERCICIO 7 
    """ La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
     con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
    Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia. """

    print('')
    print('EJERCICO 7')
    print('')

    nota_1=float(input('Ingrese su 1ra nota --> '))*0.15
    nota_2=float(input('Ingrese su 2da nota --> '))*0.25

    nota_3=float(input('Ingrese la 3ra nota que desearia sacar, asi en base calcular la 4ta necesaria --> '))*0.2    

    nota_4=(3-nota_1-nota_2-nota_3)/0.4

    print('Necesitas un %.2f para pasar tu materia ¡Animoo!'%nota_4)

elif ejercicio==8:
    #==>  EJERCICIO 8 
    """ Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
    El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
    prestará solo de ida.

    Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
    debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
    utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
    A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:

                LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
    JUAN          Si        Si        No        Si    No
    CAMILA        Si        Si        No        No    No
    JOSE          Si        No        Si        No    No
    MARIA         Si        Si        Si        No    No      

    ¿Cuanto debe pagar cada estudiante? """

    pago_lunes=15000/4
    pago_martes=15000/3
    pago_miercoles=15000/2
    pago_jueves=15000/1
    pago_viernes=10000/4

    pago_juan=pago_lunes+pago_martes+pago_jueves+pago_viernes
    pago_camila=pago_lunes+pago_martes+pago_viernes
    pago_jose=pago_lunes+pago_miercoles+pago_viernes
    pago_maria=pago_lunes+pago_martes+pago_miercoles+pago_viernes

    print('El pago que debe hacer cada estudiante es:\nJuan=%.2f\nCamila=%.2f\nJose=%.2f\nMaria=%.2f'%(pago_juan,pago_camila,pago_jose,pago_maria))



elif ejercicio==9:
    #==>  EJERCICIO 9 
    """ El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
        en donde el precio de cada seguro es de $120000. 
        Para los primeros 20 seguros, la comisión es del 20%.
        Para los siguientes 100 seguros las comisión es del 30%.
        Para los siguientes seguros vendidos. La comisión es de 10%.

        a) Si un empleado vende 435 seguros, ¿cual será su salario?
        b) Para un salario de $10'000.000. ¿Cuántos seguros debe vender?
        c) Si un empleado devenga $15'000.000. ¿Cuantos salarios vendió en promedio al dia? 
           Teniendo en cuenta que solo trabajaba de lunes a jueves """

    #a
    


elif ejercicio==10:
    #==>  EJERCICIO 10 
    """ El salario de un empleado de una empresa se calcula, utilizando como base el 
    salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
    Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:

                precio_unidad  comisión
    * Zapatos:    $ 50 000        5%
    * Tenis:      $ 70 000        4%  
    * Camizas:    $ 40 000        6%
    * Corbatas:   $ 25 000        7%
    * Pantalon:   $ 35 000        5%
    * Blusas:     $ 80 000        3%
    * Vestidos:   $ 95 000        2%
    * Medias:     $ 10 000        8%

    a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
    b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
       ¿Qué productos deben cambiar en su porcentaje de comision?
    c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
       ¿en cuanto se deben fijar las comisiones de los productos"""


elif ejercicio==11:
    #==>  EJERCICIO 11 
    """ Un auto acelera de manera uniforme 0.5 km/s², 
    a) ¿cuantas horas deben pasar para alcanzar la velocidad de la luz?
    b) ¿qué distancia se habrá recorrido? (suponga que es posible alcanzar la velocidad de la luz) """


elif ejercicio==12:
    #==>  EJERCICIO 12 
    """ Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
    alcanzar una altura dada. """


elif ejercicio==13:
    #==>  EJERCICIO 13 
    """ Un proyectil es lanzado siguiendo una trayectoria parabólica, calcule el ángulo y la velocidad inicial
    que debe tener para alcanzar una distancia horizontal y vertical dada. """


elif ejercicio==14:
    #==>  EJERCICIO 14 
    """ Un atleta inicia su entrenamiento, desde el punto de partida de una pista, a una velocidad constante de 3m/s. 
    Diez segundos después otro atleta empieza su recorrido a una velocidad constante de 5m/s. ¿Cuánto tiempo 
    habrá pasado para que el segundo atleta alcance al primero? """


elif ejercicio==15:
    #==>  EJERCICIO 15 
    """ Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
    a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
    ¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """



    #====================== EJERCICIOS OPERADORES ====================
elif ejercicio==16:
    #==> Ejercicio 16
    """ Realice las siguientes operaciones mentalmente. Intente determinar la respuesta, luego verifique en python

       1 + 3 - 5      "cristian" + "Unal"     [1,2,3] + [4,5,6]    True and False          5 > 3          1 in [1,2,3]
       13 / 2         "Unal" * 5              [1,2] * 4            1 and 2                 2 != 2            "A" in ("A", "B", "C")   
       19 // 6                                (1,2,3) + (4,5,6)    5 and True              3 == "3"          1 not in ["A", "B", "C"]    
       31 % 3                                 (1,2) * 4            False and 5             5 > True          "A" in {"A", "B", "C"} 
       2 ** 5                                                      [] and "resultado"      True < 0
       16 ** 0.5                                                   True and (2,3,4)        True != False
                                                                   False or True           "abc" < "bcd"
                                                                   0 or 5
                                                                   True or 5
                                                                   "resultado" or False
       """

elif ejercicio==17:
    #==> EJERCICIO 17
    """ ¿Qué operaciones puede realizar con los anteriores operadores?
    ¿Qué tipos de datos se pueden utilizar con cada uno de los operadores? """


elif ejercicio==18:
    #==> EJERCICIO 18
    """ De los operadores *, /, +. ¿Cual tiene mayor prioridad?
    => 3 / 2 * 5  compare con 3 * 2 / 5
    => 3 / 2 + 5  compare con 3 + 2 / 5
    => 3 * 2 + 5  compare con 3 + 2 * 5  """


elif ejercicio==19:
    #==> EJERCICIO 19
    """ De los operadores *, **. ¿Cual tiene mayor prioridad?
    => 3 * 2 ** 5  compare con 3 ** 2 * 5
    => 2 * 2 ** 3  compare con 2 ** 2 * 3
    => 2 ** 2 ** 3 ¿Qué sucede en este caso? """


elif ejercicio==20:
    #==> EJERCICIO 20
    """ De los operadores *, /, //, % ¿cual tiene mayor prioridad?:
    => 13 // 6 * 2 compare con 27 // 6 * 2
    => 13 / 6 // 2 compare con 13 // 6 / 2
    => 13 * 6 % 2 compare con 13 % 6 * 2 """


elif ejercicio==21:
    #==> EJERCICIO 21
    """ Realice las siguientes operaciones, y determine:
    ¿Cuál es el orden de prioridades de los operadores not, and, or?
    => not True and False
    => True and not False
    => True and False or False
    => True or False and False """


elif ejercicio==22:
    #==> EJERCICIO 22
    """ Intente determinar mentalmente la salida de las siguientes operaciones
     1 and 2 and 3     1 or 2 or 3
     1 and 0 and 3     1 or 0 or 3
     0 and 2 and 3     0 or 1 or 2
     """