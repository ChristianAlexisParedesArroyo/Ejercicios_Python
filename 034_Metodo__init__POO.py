#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el funcionamiento del metodo __init__ para las clases


class Usuario: #se crea la clase
    def __init__(self, nombre, apellidos): #se establecen los valores iniciales a los objetos
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)  #se imprimen los datos

usuario1 = Usuario('Enrique', 'Barros Fernández') #se penon los valores iniciales a el usuario1

usuario2 = Usuario('Javier', 'Gomila Reyes')   #se establecen los valores iniciales a el usuario2

usuario1.imprime_datos()  
usuario2.imprime_datos()
