#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso del manejo de excepciones


variable = "Correcto."   #declaramos una variable

try:                    #probamos un bloque de código en busca de errores.
	print(variable) #si no hay error se ejecuta el programa
except:                                          #except permite manejar errores en caso de que estos ocurran
	print("La variable no está declarada.")  #se imprime un mensaje de error
