"""
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
"""

def piramide(n):
    if n == 0:
        return ""
    else:
        piramide(n - 1)
        print("#" * n)
    
# Ejemplo de uso

base = int(input("Ingrese la base de la pirámide: "))

piramide(base)
