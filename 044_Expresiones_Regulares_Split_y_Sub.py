#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el modulo re para la utilizacion de la funciom split() y sub()


import re  #Importamos el modulo re

texto = "tres tristes tigres comen trigo en un trigal"  #Declaramos una variable string
busqueda = re.split(" ", texto)  #se buscan los espacios y los quita 
print(busqueda) #se imprime la variable

busqueda = re.split(" ", texto, 4) #despues de esncontrar 4 espacios deja el texto igual
print(busqueda)  #se imprime la variable

busqueda = re.sub(" ",  "-",  texto)  #se buscan los espacios y los reemplaza por guines
print(busqueda)  #se imprime la variable
