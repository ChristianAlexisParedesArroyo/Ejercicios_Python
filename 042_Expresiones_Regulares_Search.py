#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el modulo re para la utilizacion de la funciom search()


import re   #Importamos el modulo re

texto = "Bienvenidos a Programación fácil" #Declaramos una variable string
busqueda = re.search("i", texto)  #con la funcio search buscamos una coincidencia en el string, pero solo encuentra la promera que aparezca
print(busqueda) #se imprime si se encontro y la posicion o sino se encontro
