"""
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula:
"""

# Resolver la siguiente fórmula recursivamente: n^m = n * n^(m-1)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1) 
    
# Solicitar al usuario la base y el exponente
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
# Calcular la potencia utilizando la función recursiva
print(f"{base}^{exponente} = {potencia(base, exponente)}")

