import Interfaz

Interfaz.instrucciones()
print('')

print('¡Empezamos el juego!')
print('')

import Logica

tablero=Logica.generarTableroLogico()
tableroFijo=Logica.generarTableroLogico()

[tablero,tableroFijo]=Logica.generarNumerosFijos(tablero,tableroFijo)

vacio=True

while vacio==True:
    Interfaz.imprimirTablero(tablero)

    coordenadas=input('Ingrese las coordenadas donde ingresará el número (a-b) --> ')

    [cuadro_mayor,posicion]=coordenadas.split('-')

    while (cuadro_mayor not in ('0','1','2','3','4','5','6','7','8')) or (posicion not in ('0','1','2','3','4','5','6','7','8')):
            coordenadas=input('Ingrese una coordenadas VALIDA  (0-8) --> ')
            [cuadro_mayor,posicion]=coordenadas.split('-')


    print('')
    numero=input('Ingrese el numero que desea poner --> ')

    while numero not in ('1','2','3','4','5','6','7','8','9'):
        numero=input('Ingrese un numero VALIDO (1-9) --> ')


    tablero=Logica.insertarNumeroEnTablero(tablero,coordenadas,numero)

    for cuadricula in tablero:
        if None not in cuadricula:
            vacio=False
            break
    

