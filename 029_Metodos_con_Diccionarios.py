#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra los metodos con diccionarios, como el delete

#se creó un primer diccionario
teclado1 = {
	'Categoría': 'Teclados',   #claves con sus respectivos valores
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
#se creó un segundo diccionario
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1  #borramos el diccionario teclado1 completo
del teclado2['Categoría']  #borramos del diccionario teclado2 la clave y el valor de Categoría
del teclado2['Precio']    #borramos del diccionario teclado2 la clave y el valor de Precio
print(teclado2["Modelo"])  #imprimimos el valor de Modelo del diccionario teclado2

