#Operador de asignacion: =
print('1. Operador de asignacion:')
print('')
a=1
b=2
c=3
print("- a=1 =>   ",'a =',a)
print("- b=2 =>   ",'b =',b)
print("- c=3 =>   ",'c =',c)

#=========================================================
#Operadores aritmeticos: +,-,*,/,//,%,**
print('')
print('')
print('2. Operadores aritmeticos:')
print('')

print("- 1+2+3 =>             ","suma sencilla:",1+2+3)
print("- 1*2+3 =>             ","multiplicacion con prioridad caso 1:",1*2+3)
print("- 1+2*3 =>             ","multiplicacion con prioridad caso 2:",1+2*3)
print("- 5/3 =>               ","division sencilla:",5/3)
print("- 5//3 =>              ","division entera:",5//3)
print("- 5%3 =>               ","residuo divison:",5%3)
print("- 9**2 =>              ","potenciacion:",9**2)
print("- 9**0.5 =>            ","raices (potencia decimal)",9**0.5)

#P = parentesis
#E = exponentes
#M = multiplicacion
#D = division
#A = adicion
#S = sustraccion

# la multiplicaicon y division estan en iguales niveles de jerarquia
# su prioridad se asigna de izquierda a derecha

print("- 'hola '+'mundo' =>   ",'concatenacion:','hola '+'mundo')
print("- 'a'*8 =>             ",'replicacion:','a'*8)
print("- [1]+[2,3,40] =>      ",'concatenacion listas:', [1]+[2,3,40])
print("- [8]*5 =>             ",'replicacion listas:',[8]*5) 
#replica toda la lista dentro de si misma, no crea mas listas, solo la expande

#=========================================================
#Operadores logicos: not, and, or
print('')
print('')
print('3. Operadores logicos:')
print('')

print("- True and False =>          ",'and:', True and False) #SOLO ES TRUE si ambos son TRUE
print("- False and True =>          ",'and:', False and True)

print("- True or False =>           ",'or:', True or False) #SOLO ES FALSE si ambos son FALSE
print("- False or True =>           ",'or:', False or True)

#usando otros tipos de datos
#todo numero distinto de 0 es True, 0 es False
#toda cadena distian de '' es True, '' es False

print("- 1 and 1 =>                 ",1 and 1) #True and True
print("- 1 and 0 =>                 ",1 and 0) #True and False
print("- 19 and 20 =>               ",19 and 20) #True and True
print("- 0 and 100 =>               ",0 and 100) #False and True
 
print("- 100 or 0 =>                ",100 or 0) #True or False
print("- -2 or 20 =>                ",-2 or 20) #True and True 
#se imprime el -2 ya que al 1ro ser verdadero ya no se evalua el 2do numero

print("- 'cristian' and 'elias' =>  ",'cristian' and 'elias') #True and True
print("- ''and'cristian' =>         ",''and'cristian') #False and True
#se imprime el '' ya que al 1ro ser Falso ya no se evalua el 2do numero

#=========================================================
#Operadores de comparacion: <,>,<=,>=,!=,==
print('')
print('')
print('4. Operadores de comparacion:')
print('')

print("- 1>2 =>                  ",1>2)
print("- 19<0 =>                 ",19<0)
print("- -1001<=-1001 =>         ",-1001<=-1001)
print("- 3==5 =>                 ",3==5)
print("- 19>=20 =>               ",19>=20)
print("- 30!=31 =>               ",30!=31)
print("- 'cristian'>'elias' =>   ",'cristian'>'elias') #los toma letra por letra en codigo ascii
print("- True>False =>           ",True>False) #se toman como 1 y 0 respectivamente
print("- [2,30]>[20,1] =>        ",[2,30]>[20,1]), #compara elementos 1 a 1, todos deben cumplir la relacion para que sea True

#=========================================================
#Operadores de pertenencia: in, not in
print('')
print('')
print('5. Operadores de pertenencia:')
print('')

print("- 'a' in 'holamundo' =>              ",'a' in 'holamundo')
print("- 'A' in 'holamundo' =>              ",'A' in 'holamundo')
print("- 'hola' in 'holamundo' =>           ",'hola' in 'holamundo')
print("- ' ' in 'hola mundo' =>             ",' ' in 'hola mundo')
print("- 1 in [1,2,3] =>                    ",1 in [1,2,3])
print("- 1 in ['1','2','3'] =>              ",1 in ['1','2','3'])
print("- '3' not in '124567890' =>          ",'3' not in '124567890')
print("- '01' in '0 1 2 3 4 5 6 7 8 9' =>   ",'01' in '0 1 2 3 4 5 6 7 8 9')

#=========================================================
#Operadores de conjuntos: |, &, -


