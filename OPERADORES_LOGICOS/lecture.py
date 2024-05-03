## EJERCICIOS

# Ejercicio 1:   
# operador and

# ejemplo 1
# crear un programa que compare dos numeros
numero1:int=13
numero2:int=16
comparacion=numero1 < numero2 and numero2 > numero1
print(comparacion)

# ejemplo 2
numero1:int=13
numero2:int=16
comparacion:bool=numero1 > numero2 and numero2 > numero1
print(comparacion)

print("----------------------------")
# Ejercicio 2:   
# operador or

# ejemplo 1
# crear un programa que compare dos edades
edad1:int=14
edad2:int=18
comparar= edad1 <= edad2 or edad2 < edad1
print(comparar)

# ejemplo 2
edad1:int=14
edad2:int=18
comparar= edad1 >= edad2 or edad2 <= edad1
print(comparar)

print("----------------------------")
# Ejercicio 3:
# operador not

# ejemplo 1
# crear un programa de negacion con los dias de la semana
dia_semana:str="martes"
dia_semana=False
negacion=not dia_semana
print(negacion)

# ejemplo 2
dia_semana:str="martes"
dia_semana=True
negacion=not dia_semana
print(negacion)