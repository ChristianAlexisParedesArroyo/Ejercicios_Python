#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso de los argumentos arbitrarios args*


def colores(*args):  #se crea la funcion con argumentos args*
	pass

colores('rojo', 'azul', 'verde', 'amarillo') #4 argumentos
colores('lila', 'negro', 'rojo')   #3 argumentos
colores('rosa')  #1 argumento
colores('marrón', 'naranja')  #2 argumentos


def colores(*args):  #se crea la funcion con argumentos args*
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.') #se imprime despues de llamar la funcion

colores("verde", "azul")  #se llama a la funcion


def suma(*args):  #se crea la funcion con argumentos args*
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]  #se realaisa la suma de los argumentos segun su posicion
	print('El resultado de la suma es:', resultado)  #se imprime despues de llamar la funcion

suma(8, 573, 2, 152, 37)  #se llama a la funcion
