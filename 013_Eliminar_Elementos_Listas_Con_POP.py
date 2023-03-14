#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como borrar elementos de una lista con pop() y guardarlo en otra variable o lista para ser utilizado

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
color_azul = colores.pop(1)  #borramos de la lista el color azul con remove()
color_blanco = colores.pop(7)  #borramos de la lista el color blanco con remove()

colores_borrados = [color_azul, color_blanco]  #guardamos los elementos borrados en otra lista

print(colores_borrados)  #mostramos la lista con los elementos borrados
