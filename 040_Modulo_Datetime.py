#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso del datetime para poner el tiempo


import datetime  #se importa el modulo datetime

fecha = datetime.datetime(2022, 9, 3, 10, 43)   #se declara la fecha o se puede poner la actual con now
print(fecha)  #se imprime la fecha decrarada


print("El dia es:", fecha.day)    #se imprime por separado el dia
print("El mes es:", fecha.month)  #se imprime por separado el mes
print("El dia es:", fecha.year)  #se imprime por separado el año
