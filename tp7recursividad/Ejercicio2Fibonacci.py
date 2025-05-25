"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Valores de referencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
valor = int(input("Ingrese un número: "))

for i in range(valor + 1):
    print(f"El número Fibonacci de {i} es: {fibonacci(i)}")