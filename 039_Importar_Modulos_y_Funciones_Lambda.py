#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como importar modulos y a como utilizar las funciones lambda


import math  #importamos un modulo 

#Se realiza una operacion para el area de un circulo con una función
def area(radio):         
	resultado = round(math.pi * radio * radio, 4)
	print(resultado)
area(2)

#Se realiza una operacion para el area de un circulo utilizando lambda
area = lambda radio: round(math.pi * radio * radio, 4)
print (area(2))
