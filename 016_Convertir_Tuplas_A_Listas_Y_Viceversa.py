#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el fucionamiento de una tupla y como se puede convertir una lista en tupla

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #creamos una lista

tuple_col = tuple(colores) #convertimos la lista en una tupla
print(type(tuple_col))   #confirmamos que se convirtio en una tupla
print(tuple_col[1])   #imprimimos la segunda posicion de la tupla
  

numeros = (10, 1, 5, 11)   #creamos otra tupla
print(numeros[0] - numeros[1] + numeros[2] + numeros[3])  #hacemos operaciones con los elementos de la tupla para que nos de 25


