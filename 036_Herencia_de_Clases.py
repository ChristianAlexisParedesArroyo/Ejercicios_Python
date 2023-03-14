#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el funcionamiento de la herencia de clases


# Esta es la superclase
class Usuarios:
    def __init__(self, nombre, apellidos):  #se establecen los valores iniciales a los objetos
            self.nombre = nombre
            self.apellidos = apellidos

    def imprime_datos(self):
            print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)  #se imprimen los datos
usuario1 = Usuarios('Enrique', 'Barros Fernández') #se penon los valores iniciales a el usuario1

usuario1.imprime_datos()   #llama al metodo de impimie_datos


# Esta es la subclase
class UsuariosPremium(Usuarios):
	pass

usuario2 = UsuariosPremium('Javier', 'Gomila Reyes')   #se establecen los valores iniciales a el usuario2
  
usuario2.imprime_datos() #llama al metodo de impimie_datos
