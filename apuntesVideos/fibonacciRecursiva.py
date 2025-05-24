"""
Desarrollar una función recursiva que calcule el n-ésimo número de Fibonacci.
El n-ésimo número de Fibonacci se define como:
la suma de los dos números anteriores en la secuencia, con los dos primeros números siendo 0 y 1.
por ejemplo:
posición 0: 0
posición 1: 1
posición 2: 1 + 0 = 1
posición 3: 1 + 1 = 2
posición 4: 2 + 1 = 3
posición 5: 3 + 2 = 5
Podemos definir la formula de la siguiente manera:
posición n = posición n-1 + posición n-2

"""

def fibonacciRecursiva(posicion):
    # Caso base: si la posición es 0, retornamos 0.
    if posicion == 0:
        return 0
    # Caso base: si la posición es 1, retornamos 1.
    elif posicion == 1:
        return 1
    else:
        return fibonacciRecursiva(posicion - 1) + fibonacciRecursiva(posicion - 2)
    
# Ejemplo de uso

# Guia valores: 0,1,1,2,3,5,8,13,21,34,55
valor = int(input("Ingrese la posición de Fibonacci: "))
print(f"El número de Fibonacci en la posición {valor} es: {fibonacciRecursiva(valor)}")