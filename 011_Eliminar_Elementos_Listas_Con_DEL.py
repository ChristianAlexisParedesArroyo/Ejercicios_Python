#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como borrar elementos de una lista con del()

colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa", "blanco", "naranja"]  #lista de colores

del colores[1]  #borramos de la lista el color azul
print(colores)  #impresion de la lista colores

#colores = ["rojo", "verde", "amarillo", "marrón", "lila", "negro", "rosa", "blanco", "naranja"]  

del colores[3]   #borramos de la lista el color marrón
print(colores)   #impresion de la lista colores

#colores = ["rojo", "verde", "amarillo", "lila", "negro", "rosa", "blanco", "naranja"]

del colores[-4]   #borramos de la lista el color negro
print(colores)    #impresion de la lista colores

#colores = ["rojo", "verde", "amarillo", "lila", "rosa", "blanco", "naranja"]

del colores[-3]   #borramos de la lista el color rosa
print(colores)    #impresion de la lista colores

#colores = ["rojo", "verde", "amarillo", "lila", "blanco", "naranja"]
