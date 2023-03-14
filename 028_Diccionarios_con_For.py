#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso de los diccionarios en un bucle for

#se creó un primer diccionario
teclado1 = {
	'Categoría': 'Teclados',  #claves con sus respectivos valores
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
#se creó un segundo diccionario
teclado2 = {
	'Categoría': 'Teclados',  #claves con sus respectivos valores
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado1:  #Usamos el bucle for para que recorra todo el diccionario
    print(x, "=", teclado1[x] + ".")  #Imprimimos las claves y valores del diccionario
    
