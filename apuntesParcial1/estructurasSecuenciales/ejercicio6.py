"""
1. Declarar dos variables: x = 10, y = 20.
2. Intercambiar sus valores usando operaciones aritméticas.
3. Mostrar los valores antes y después del intercambio

• ¿Cómo funciona el intercambio sin variable auxiliar?
- El intercambio se realiza mediante operaciones aritméticas, donde se restan los valores y se suman para obtener el nuevo valor de cada variable.
• ¿Qué pasa si los valores iniciales son iguales?
El intercambio no afectará el resultado final, ya que al ser iguales, el resultado será el mismo.
"""

# Definicion de variables
x = 10
y = 20

# Definición de operaciones
y = y - x
x = x + y

# Definición de salida
print(f"Las variables iniciales son x = 10 & y = 20")
print(f"El resultado del interambio es x = {x} & y = {y}")

# Definicion de variables
a = 10
b = 10

# Definición de operaciones
b = b + a
a = b - a
b = b - a

# Definición de salida
print(f"Las variables iniciales son a = 10 & b = 10")
print(f"El resultado del interambio es a = {a} & b = {b}")


