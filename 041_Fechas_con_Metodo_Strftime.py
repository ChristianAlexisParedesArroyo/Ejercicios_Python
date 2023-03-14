#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el metodo strftime() con el que se puede formatear las fechas en strings

import datetime, locale

locale.setlocale(locale.LC_ALL, "es-ES")  #Cambia la fecha a español

ahora = datetime.datetime.now()  

print(ahora.strftime("Día de la semana abreviado: %a "))   #Día de la semana abreviado
print(ahora.strftime("Día de la semana completo: %A "))    #Día de la semana completo
print(ahora.strftime("Mes abreviado: %b "))   #Mes abreviado
print(ahora.strftime("Mes abreviado: %B "))   #Mes completo
print(ahora.strftime("Fecha completa: %c "))  #Fecha completa abreviada
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))  #Número de siglo. Empieza a contar desde 0, por eso cuenta uno menos del esperado
print(ahora.strftime("Día del mes (01 - 31): %d "))        #Día del mes (01 a 31)
print(ahora.strftime("Día/hora/año: %D "))                 #Día/hora/año
print(ahora.strftime("Día del mes (1 - 31): %e "))         #Día del mes (1 a 31)
print(ahora.strftime("Año en dos dígitos: %g "))           #Año en dos dígitos
print(ahora.strftime("Año en cuatro dígitos: %G "))        #Año en cuatro dígitos
print(ahora.strftime("Mes abreviado: %h "))                #Mes abreviado (igual que %b)
print(ahora.strftime("Hora (00 - 23): %H "))               #Hora de 00 a 23
print(ahora.strftime("Hora (01 - 12): %I "))          #Hora de 01 a 12
print(ahora.strftime("Día del año: %j "))             #Día del año del 001 al 366
print(ahora.strftime("Mes del 01 al 12: %m "))        #Mes del 01 al 12
print(ahora.strftime("Minuto: %M "))                  #Minuto
print(ahora.strftime("Salto de línea: %n"))           #Salto de línea
print(ahora.strftime("AM o PM: %p "))                 #AM o PM
print(ahora.strftime("Hora + AM o PM: %r"))           #Hora + AM o PM
print(ahora.strftime("Hora y minutos: %R"))           #Hora + AM o PM
print(ahora.strftime("Segundos: %S"))                 #Segundos
print(ahora.strftime("Tabulación: %t"))               #Tabulación
print(ahora.strftime("Hora, minutos y segundos: %T")) #Hora, minutos y segundos
print(ahora.strftime("Día de la semana (número): %u"))               #Día de la semana (número)
print(ahora.strftime("Semana del año (empieza en domingo): %U"))     #Semana del año (empieza en domingo)
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))  #Semana del año (condiciones especiales)
print(ahora.strftime("Semana del año (empieza en lunes): %W"))       #Semana del año (empieza en lunes)
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))   #Día de la semana(empieza en domingo)
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))              #Día/mes/año de dos dígitos
print(ahora.strftime("Hora/minutos/segundos: %X"))                   #Hora/minutos/segundos
print(ahora.strftime("Año corto: %y"))                #Año corto
print(ahora.strftime("Año largo: %Y"))                #Año largo
