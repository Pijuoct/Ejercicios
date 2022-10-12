

import interfaz
import logica
import fechasImportantes


print(interfaz.__doc__)
print(logica.__doc__)

# print(interfaz.__dict__)

# print(dir(interfaz))

interfaz.imprimirSeparador('=')
interfaz.imprimirMensaje('Juan Esteban')
interfaz.imprimirSeparador('=')

a=logica.factorial(9)
b=logica.primo(93)
c=logica.suma(1,8,4,6,7)

interfaz.imprimirVariable('factorial',a)
interfaz.imprimirVariable('primo',b)
interfaz.imprimirVariable('sumatoria',c)

"""
Crear un modulo llamado fechas
en el cual almacene fechas importantes

ejemplo:

fechaImportante1 = '20-07'
fechaImportante2 = '15-05'
fechaImportante3 = '06-03'
... + 3

consuma desde main todas las fechas importantes,
almacenandolas en una lista llamada:
listaFechasImportantes

"""

# lista=[]

# lista=fechasImportantes.fecha(lista,'17','10')
# lista=fechasImportantes.fecha(lista,'01','01')
# lista=fechasImportantes.fecha(lista,'07','07')
# lista=fechasImportantes.fecha(lista,'24','12')
# lista=fechasImportantes.fecha(lista,'31','10')
# lista=fechasImportantes.fecha(lista,'06','09')

# interfaz.imprimirVariable('listado de fechas',lista)

f1=fechasImportantes.fechaimportante1
f2=fechasImportantes.fechaimportante2
f3=fechasImportantes.fechaimportante3
f4=fechasImportantes.fechaimportante4
f5=fechasImportantes.fechaimportante5
f6=fechasImportantes.fechaimportante6

lista=[f1,f2,f3,f4,f5,f6]

interfaz.imprimirLista(lista)

