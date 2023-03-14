#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el modulo re para la utilizacion de la funciom findall()


import re   #Importamos el modulo re


texto = "tres tristes tigres comen trigo en un trigal"  #Declaramos una variable string
busqueda = re.findall("es", texto)  #con la funcion search buscamos una coincidencia en el string, y ecuentra todos los caracteres que pongas en el argumento
print(busqueda) #se imprime todos los caracteres que se encuentren
