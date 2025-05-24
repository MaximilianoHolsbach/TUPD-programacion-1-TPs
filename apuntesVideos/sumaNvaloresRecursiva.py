"""
Sumar los n valores ingresados como argumento a la función.
"""

def sumaNValoresRecursiva(n):
    # Caso base: si n es 0, retornamos 0.
    if n == 0:
        return 0
    # Caso recursivo: sumamos n con la suma de los n-1 valores.
    return n + sumaNValoresRecursiva(n - 1)
# Ejemplo de uso
valor = int(input("Ingrese un número: "))
print(f"La suma de los {valor} valores es: {sumaNValoresRecursiva(valor)}")
