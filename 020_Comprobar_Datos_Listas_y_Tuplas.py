#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como se puede comprobar datos en listas y tuplas

entrada = input('Introduce un color:\n')   #se pide un color
colores = ('azul', 'rojo', 'morado', 'blanco')  #tupla de colores asignados



if entrada in colores[0]:  #se compara el color pedido con la pisicion 0 de la tupla
	print('El color azul está admitido')
elif entrada in colores[1]:  #se compara el color pedido con la pisicion 1 de la tupla
	print('El color rojo está admitido')
elif entrada in colores[2]:  #se compara el color pedido con la pisicion 2 de la tupla
	print('El color morado está admitido')
elif entrada in colores[3]:  #se compara el color pedido con la pisicion 3 de la tupla
	print('El color blanco está admitido')
else:                    #no se encontro el color en la tupla
	print('Color no admitido')
