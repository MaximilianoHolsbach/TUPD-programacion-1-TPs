"""

"""

# Factorial de un número es el producto de todos los números enteros positivos desde 1 hasta n.
def factorial(n):# Esta funcion resuelfe el factorial de un número n de manera iterativa
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact

# Veamos el mismo problema pero de manera recursiva

def factorialRec(num):# Esta funcion resuelve el factorial de un número n de manera recursiva
    return 1 if num == 0 else num * factorialRec(num - 1) # Retorna 1 si el número es 0, de lo contrario multiplica el número por el factorial del número - 1

"""
Existen varios tipos de recursividad:
1. Recursividad simple: La función se llama a sí misma una vez en cada llamada.
2. Recursividad de cola o tail recursion: La función se llama a sí misma al final de su ejecución.
3. Recursividad múltiple: La función se llama a sí misma varias veces en cada llamada.
"""
"""
Los algoritmos recursivos producen un algoritmo mas corto y declarativo, pero son menos eficientes que los algoritmos iterativos.
"""

