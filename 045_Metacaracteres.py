#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el funcionamiento de algunos metacaracteres


import re  #Importamos el modulo re 

texto1 = "Bienvenidos a mi codigo."  #Declaramos una variable string
buscar1 = re.findall("[c-g]", texto1) #busca si hay datos de la c a la g en el string
print(buscar1) #se imprimen los datos encontrados


texto2 = "El futuro es ahora."  #Declaramos una variable string
buscar2 = re.findall("pasado|futuro", texto2)
if buscar2:   #si buscar es igual a TRUE entra en el if
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")


texto3 = "La programación es fácil."  #Declaramos una variable string
buscar3 = re.findall("progra..ción", texto3)  #el metacaracter de punto es un caracter comodin, reemplaza cualquier caracter
if buscar3:  #si buscar es igual a TRUE entra en el if
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
