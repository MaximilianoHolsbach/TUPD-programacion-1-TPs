"""
Realizar una función recursiva que permita sumar los n valores primos. 

Propiedad matemática:
Un número NO es primo si tiene al menos un divisor diferente de 1 y de sí mismo.
Si un número n tiene un divisor d, tal que d <= sqrt(n), entonces n puede ser expresado como n = d * k,
donde k >=dsqrt(n).
Por ejemplo:
Para n = 36, los divisores son 1, 2, 3, 4, 6, 9, 12, 18, 36.
y basta con comprobar 36 = 6 * 6, donde 6 <= sqrt(36).
Esto significa que si no encontramos divisores de n menores o iguales a sqrt(n), entonces n es primo.
"""
def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumaNvaloresPrimos(n):
    if n == 1:
        return 0
    elif esPrimo(n):
        return n + sumaNvaloresPrimos(n - 1)
    else:
        return sumaNvaloresPrimos(n - 1)
    
print(f"La suma de los {5} valores primos es: {sumaNvaloresPrimos(10)}")

