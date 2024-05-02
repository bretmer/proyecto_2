# OPERADORES LOGICOS
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son  `and`, `or` y `not`
## OPERADOR AND
 El operador `and` evalúa si el valor a la izquierda y el de la derecha son `True` , y en el caso de ser cierto, devuelve `True` . Si uno de los dos valores es False , el resultado será `False`.
>ejemplo:
```python
nuemro1=10
numero2=15
comparacion=numero1<nuemero2 and numero2>numero1:
print(comparacion)   # True
```
## OPERADOR OR
El operador lógico `or` devuelve el valor booleano true si uno o ambos operandos son `True` y de lo contrario, devuelve `False` .
>ejemplo:
```python
nuemro1=10
numero2=15
comparacion=numero1<nuemero2 or numero2<numero1:
print(comparacion)   # True
```
## OPERADOR NOT
El operador lógico `not` invierte el resultado verdadero o falso de la expresión que sigue inmediatamente.
>ejemplo:
```python
nuemro1=10
numero2=15
comparacion=not numero1<nuemero2 and numero2<numero1:
print(comparacion)   #False
```