#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como agragar uno o varios elementos a una lista con el metodo append() para a{}ñadirlos al final y con insert() en una posicion especifica


colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.append("fuxia")       #añadimos a la lista el color fuxia con append() al final de la lista
colores.append("celeste")     #añadimos a la lista el color celeste con append() al final de la lista  
print(colores)  #mostramos la lista con los elementos agregados
print("\n\n")

colores.insert(6, "magenta")    #agegamos a la lista el color magenta con insert() en la posicion 6
colores.insert(12, "turquesa")  #agregamos a la lista el color turquesa con insert() en la posicion 12
print(colores)  #mostramos la lista con los elementos agregados
