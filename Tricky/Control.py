import Interfaz

Interfaz.explicarJuego()


jugador1=input('Ingrese que simbolo sera el 1er jugador ("X" o "O") --> ')

while jugador1!='X' and jugador1!='O':
    jugador1=input('Ingrese un simbolo VALIDO ("X" o "O") --> ')

if jugador1=='X':
    jugador2='O'
else:
    jugador2='X'

import Logica

tableroLogico=Logica.generarTableroLogico()

Interfaz.imprimirTablero(tableroLogico)
print('¡EMPEZAMOS!')

hayganador=Logica.determinarGandor(tableroLogico)
turno=1
while hayganador==None and None in tableroLogico:
    
    if (turno%2)!=0:
        print('Jugador 1 (%s) ingrese la posicion de su jugada:'%jugador1)
        caracter=jugador1
    else:
        print('Jugador 2 (%s) ingrese la posicion de su jugada:'%jugador2)
        caracter=jugador2

    pos=input('--> ')

    while pos not in ('0','1','2','3','4','5','6','7','8'):
        pos=input('Ingrese una posicion valida (0-8) --> ')
    
    pos=int(pos)

    tableroLogico=Logica.insertarCaracterEnTablero(tableroLogico,pos,caracter)

    hayganador=Logica.determinarGandor(tableroLogico)

    Interfaz.imprimirTablero(tableroLogico)

    turno+=1

turno=turno-1

if None not in tableroLogico:
    print('Empate, No hay ganador')
else:
    if turno%2!=0:
        ganador=1
    else:
        ganador=2

    print('El ganador es el jugador %i con las %s'%(ganador,caracter))
