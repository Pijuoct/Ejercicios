# Entrada y Salida


#Solicitar una clave y luego responder si es correcta o no. 
#                    Clave="Unal2022"

print(18<18)

clave=str(input('Ingrese su clave --> '))
clave_real='Unal2022'

print((clave==clave_real and 'La clave es correcta') or 'La clave es incorrecta')
#optimizacion de codigo con un print

#-----------------------------------------------------------------------
#Solicitar un numero y responder en pantalla si es mayor a 18

numero=int(input('Ingrese un numero --> '))

print((numero>18 and 'El numero es MAYOR que 18') or 'El numero NO es MAYOR que 18')

#-----------------------------------------------------------------------
#Formateo de valores numeros --> format(valor,tipo)

numero=0.000000029213

#formato_cientifico = format(numero,'e')
formato_cientifico = format(numero,'.3e')

print(formato_cientifico)

#-----------------------------------------------------------------------
#Formateo de valores numeros --> format(valor,tipo)
numero=12.1392
print(format(numero,'.2f'))

numero1=0.045
numero2=12.531
print(format(numero1,'.1f'))
print(int(numero2))





#=========================================================
# Ayuda

#Determine el tipo de dato para cada linea de codigo

# {"1","2"}
# {1:2}
# range(10)
print(type({1:2}))

#Que funcionalidades tienen lso tipos de datos: int, float, str, set

entero=1
flotante=2.35
string='holamundo'
conjunto={1,2,3,4,5}

print('-----Funcionalidades enteros-----')
for funcion in dir(entero):
   print(funcion)



#=========================================================
# Conversiones

#pasar binario, octal, hexadecimal los numeros: 1,3,513
a,b,c=1,8,513
print(a,bin(a),oct(a),hex(a))
print(a,bin(b),oct(b),hex(b))
print(a,bin(c),oct(c),hex(c))

#convertir a decimales
print(c,int(bin(c),2),int(oct(c),8),int(hex(c),16))



#=========================================================
# Secuencias

#crear una secuencia con numero del 1 al 10
a=range(1,11,1)
print(list(a))


#cree ñas siguientes secuencias

a=range(2,51,2)
print(list(a))

b=range(0,200,3)
print(list(b))

c=range(10,-1,-1)
print(list(c))

d=range(96,5,-6)
print(list(d))

# len(), min(), max(), sum()
# de la ultima secuencia creada

print(len(d),min(d),max(d),sum(d))

#------------ mapeo y filtrado

secuencia= range(900,-1,-15)

#multiplicar cada elemento por 3.1
#convertir los numeros strings
#transformar los numeros al residuo entre 5

#retener solo los pares
#retener solo los numeros que al sumarle 5 sean pares
#retener solo los numeros cuyo 2do digito sea

def multiplicacion(elemento):
   return elemento*3.1

print(list(map(multiplicacion,secuencia)))



def par(elemento):
   return elemento%2==0

print(list(filter(par,secuencia)))

