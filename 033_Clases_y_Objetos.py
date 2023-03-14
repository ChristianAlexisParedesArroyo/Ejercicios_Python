#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra las clases y objetos


class Usuario:    #se definió una clase llamada Usuario

        #se ponen los atributos
	nombre = ""
	apellidos = ""
	correo = ""
	edad = ""

	def imprime_datos(self):
		print("\nNombre:", self.nombre, "\nApellidos:", self.apellidos, "\nCorreo:", self.correo, "\nEdad:", self.edad) #se imprimen los datos de la clase

usuario1 = Usuario()  #se creó un objeto llamado usuario1

#se guardan los datos de los atributos de la clase
usuario1.nombre = "Enrique"
usuario1.apellidos = "Barros Fernández"
usuario1.correo = "Enrique.Fer678@gmail.com"
usuario1.edad = 35

usuario1.imprime_datos()  #se direcciona a la clase sonde se imprimen los datos


usuario2 = Usuario()  #se creó un objeto llamado usuario2

#se guardan los datos de los atributos de la clase
usuario2.nombre = "Pepe"
usuario2.apellidos = "Gonzales Valles"
usuario2.correo = "VG34@gmail.com"
usuario2.edad = 42

usuario2.imprime_datos()  #se direcciona a la clase sonde se imprimen los datos
