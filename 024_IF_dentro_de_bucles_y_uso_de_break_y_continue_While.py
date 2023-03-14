#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra como anidar if dentro de bucles, tambien el uso de break y continue en bucles while

x = 0  # Valor inicial de x

while x <= 30:  #while se ejecuta hasta menor o igual que 30
    x += 1  #incrementos de 1
        
    if x == 4 or x == 6 or x == 10:  #if para saltar ejecuciones del bucle
        print("Se saltó el valor", x, "de x")
        continue
	    
    if x == 15:  #if para romper la ejecución del bucle
        print("Se rompió la ejecucion del bucle cuando x valia ", x)
        break
    print(x) #imprime los resultados que no se corresponden a ninguno de los if

	
	
