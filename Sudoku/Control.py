import Interfaz

Interfaz.instrucciones()
print('')

print('¡Empezamos el juego!')
print('')

import Logica

tableroLogico=Logica.generarTableroLogico()
tableroLogicoFijo=Logica.generarTableroLogico()

[tableroLogico,tableroLogicoFijo]=Logica.generarNumerosFijos(tableroLogico,tableroLogicoFijo)

vacio=True

while vacio==True:
    Interfaz.imprimirTablero(tableroLogico)

    coordenadas=input('Ingrese las coordenadas donde ingresará el número (a-b) --> ')

    [cuadro_mayor,posicion]=coordenadas.split('-')

    while (cuadro_mayor not in ('0','1','2','3','4','5','6','7','8')) or (posicion not in ('0','1','2','3','4','5','6','7','8')):
            coordenadas=input('Ingrese unas coordenadas VALIDAS  (0-8) --> ')
            [cuadro_mayor,posicion]=coordenadas.split('-')


    print('')
    numero=input('Ingrese el numero que desea poner --> ')

    while numero not in ('1','2','3','4','5','6','7','8','9'):
        numero=input('Ingrese un numero VALIDO (1-9) --> ')


    if tableroLogicoFijo[int(cuadro_mayor)][int(posicion)]==None:

        tableroLogico=Logica.insertarNumeroEnTablero(tableroLogico,coordenadas,numero)
    else:
        print('El numero en esta posicion (%s-%s) es FIJO y por ende no puede ser reemplazado'%(cuadro_mayor,posicion))


    for cuadricula in tableroLogico:
        if None not in cuadricula:
            vacio=False
            break
    

