#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como eliminar los valores de los objetos o cambiarlos de valor


class Usuario: #se crea la clase
    def __init__(self, nombre, apellidos):  #se establecen los valores iniciales a los objetos
            self.nombre = nombre
            self.apellidos = apellidos

    def imprime_datos(self):
	    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)  #se imprimen los datos


usuario001 = Usuario('Javier', 'Gomila Reyes') #se penon los valores iniciales a el usuario001

usuario001.imprime_datos()  #llama al metodo de impimie_datos

usuario001.nombre = 'Jacinto' #se cambia el valor del atributo nombre 

usuario001.imprime_datos()  #llama al metodo de impimie_datos

del usuario001.nombre  #se borra el atributo nombrte del objeto usuario001


