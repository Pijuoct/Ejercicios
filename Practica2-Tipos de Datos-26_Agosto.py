# Tipos de datos en python

#Declaramos los siguientes elementos y asignamos
#en variables de su eleccion:

#===================================================================
from xmlrpc.client import boolean


print('')
#Enteros: 10, -100, 500, 200 ==> luego restelos sucesivamente

a=10
b=-100
c=500
d=200

enteros=[b,c,d]
for i in enteros:
    a=a-i
print('La resta sucesiva de los Enteros es: %i'%a)


#===================================================================
print('')
#Flotantes: 100.0, 305.2, 400.3 ==> dividalos de manera sucesiva

a,b,c=100.0,305.2,400.3

flotantes=[b,c]
for i in flotantes:
    a=a/i
print('La division sucesiva de los Flotantes es: %f'%a)


#===================================================================
print('')
#Booleanos: True, False ==> 1ro sumerlos y luego restelos

a=True
b=False

print('La suma de los Booleanos es:',a+b)
print('La resta de los Booleanos es:',a-b)

#son operaciones posibles, se le asigna a True el valor de 1 y False el valor de 0
#pero no son las operaciones para las que fueron diseñadas los booleanos

#===================================================================
print('')
#Strings: 'Cristian', 'Juanita' ==> 1ro sumerlos y luego restelos

a='Cristian'
b='Juanita'
c=a+b
#d=a-b no es posible restar strings

print('La suma de las strings es: %s'%c)
#print('La resta de las strings es: %s'%d)


#===================================================================
print('')
#Strings:"", '',"""","''" ¿que sucede?

a=""
#b="""" genera error, no se cierran las comillas
c="''"

print('Este es el string a: %s'%a)
print('Este es el string c: %s'%c)


#===================================================================
print('')
#Busque una manera de convertir:  (casteo)
#Entero a un flotante
a=22
b=float(a)

print('El entro %d se ve asi como flotante: %.2f'%(a,b))

#Un flotante a entero ----- los fflotantes al pasar a ser enteros, pierden sus decimales NO SE APROXIMA
a=13.78
b=int(a)

print('El flotante %.2f se ve asi como entero: %d'%(a,b))

print('')

#Un flotante y un entero a un string
a=13.78
b=30
c=str(a)
d=str(b)

print('El flotante %.2f se ve asi como string: %s'%(a,c))
print('El entero %d se ve asi como string: %s'%(b,d))

print('')

#Un string a un entero y a un flotante
a='73'
b=int(a)
c=float(b)

print('El string %s se ve asi como entero: %d'%(a,b))
print('El string %s se ve asi como flotante: %.2f'%(b,c))

print('')

#Un booleano a un entero y a un flotante
a=True
b=int(a)
c=float(b)

print('El booleano',a,'se ve asi como entero: %d'%b)
print('El booleano',a,'se ve asi como flotante: %.2f'%c)

print('')

#Un entero y flotante a un booleano
a=1
b=0.0
c=bool(a)
d=bool(b)

print('El entero %d se ve asi como booleano:'%a,c)
print('El flotante %.2f se ve asi como flotante:'%b,d)

print('')