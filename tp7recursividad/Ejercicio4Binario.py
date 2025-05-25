"""
Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto
"""

def deccimalBinario(n):
    """
    Convierte un número decimal a binario.
    :param n: Número decimal a convertir.
    :return: Cadena que representa el número en binario.
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Casteamos el modulo a string para que no se imprima como un número
        # y lo concatenamos a la llamada recursiva
        return deccimalBinario(n // 2) + str(n % 2)
    
# Solicitar al usuario un número decimal
n = int(input("Introduce un número decimal: "))
# Convertir el número decimal a binario utilizando la función recursiva
print(f"El número {n} en binario es: {deccimalBinario(n)}")