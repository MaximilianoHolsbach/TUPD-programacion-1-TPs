"""
Ejercicio 3: Uso de booleanos
 Objetivo: Manipular variables booleanas y aplicar operadores lógicos.
 Instrucciones:
1. Declarar dos variables booleanas: a = True, b = False.
2. Realizar e imprimir los resultados de las operaciones:
o a and b
o a or b
o not a, not b
Preguntas de reflexión:
• ¿Cuál es la utilidad de los operadores lógicos en programas más
complejos?
- Ayudan a evaluar condiciones y determinar el flujo de ejecución de un programa.
• ¿Qué representa cada operación?
- AND: representa una conjunción lógica, es la multiplicación de booleanos.
- OR: representa una disyunción lógica, es la suma de booleanos.
- NOT: representa la negación lógica, invierte el valor de un booleano.
"""
# Definición de variables
a = True
b = False

# Operaciones lógicas
print(f"a = {a}, b = {b}")
print("a and b:", a and b)  # True and False = False
print("a or b:", a or b)    # True or False = True
print(f"not a = {not a}, y not b = {not b}")  # not True = False, not False = True