#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso de las funciones anidadas y las variables globales


def funcion1():  #se crea una funcion 
    variable1 = "Variable dentro de la funcion."  #se crea una variable
    print(variable1) #se imprime la variable
    
    def funcion2():  #se crea una funcion dentro de la primera funcion 
        variable1 = "He cambiado el valor de la funcion."  
        print(variable1)  #se imprime la variable

    funcion2()
        
funcion1() #se imprime primero esta funcion porque es la principal



num = 100  #Variable global fuera de la funcion

def funcion3():
	global num1  #se declara la variable global
	num1 = 10    #se inicializa la variable global

funcion3()

print(num1) #se imprime la variable global
