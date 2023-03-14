#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso de **kwargs en diccionarios


def numeros (**kwargs):  #se crea la funcion con **kwargs
	print("Este es el numero " + kwargs['num1'] + '.') #se imprime despues de llamar la funcion

numeros(num1="1500", num2="3234") #se llama a la funcion con un diccionario
