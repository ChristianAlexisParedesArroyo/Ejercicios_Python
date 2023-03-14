#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra a como heredar propiedades __init__ entre clases


# Esta es la superclase
class Usuarios:
    def __init__(self, nombre, apellidos):  #se establecen los valores iniciales a los objetos de la superclase
            self.nombre = nombre
            self.apellidos = apellidos

    def imprime_datos(self):
	    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)  #se imprimen los datos

usuario1 = Usuarios('Enrique', 'Barros Fernández') #se penon los valores iniciales a el usuario1

usuario1.imprime_datos()   #llama al metodo de impimie_datos


# Esta es la subclase
class UsuariosPremium(Usuarios):
    def __init__(self, nombre, apellidos, instagram):  #se establecen los valores iniciales a los objetos de la subclase
            Usuarios.__init__(self, nombre, apellidos)
            self.instagram = instagram

    def imprime_datos_premium(self):
	    print('\nNombre:', self.nombre, '\nApellidos:', self.apellidos, '\nInstragram:', self.instagram)  #se imprimen los datos
	    

usuario2 = UsuariosPremium('Javier', 'Gomila Reyes', 'Javi.463')   #se establecen los valores iniciales a el usuario2
  
usuario2.imprime_datos_premium() #llama al metodo de impimie_datos
