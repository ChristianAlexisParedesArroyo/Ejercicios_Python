#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso del condicional if elif else, asi como el imput para la entrada de datos


edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:   #si es verdadesra la condicion, entra en el if
	print('Nadie puede tener esa edad.') #imprime la primera condicion
elif edad >= 1 and edad < 18:   #si no es verdadera la condicion del if, entra en el primer elif
	print('Eres menor de edad.')   #imprime la segunda condicion
elif edad >= 18 and  edad <= 45:   #si no es verdadero el primer elif, entra en el segundo elif
	print('Eres mayor de edad.')  #imprime la tercera condicion
elif edad < 100:      #si no es verdadero el segundo elif, entra en el tercer elif
	print('Eres mas mayor de edad.')  #imprime la cuarta condicion
elif edad >= 100 and  edad <= 120:     #si no es verdadero el tercer elif, entra en el cuarto elif
	print('Eres muy mayor de edad.') #imprime la quinta condicion
else:             #si no es verdadera ninguna condicion, entonces entra en el else
	print('Edad no válida.') 
