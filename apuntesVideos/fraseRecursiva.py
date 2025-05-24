"""
Realizar una función recursiva que reciva un número y una frase y la repita el número de veces indicado por el número.
"""

def repetirFraseRecursiva(frase, num):
    # Caso base: mientras el argumento num sea mayor o igual a 1, se imprime la frase.
    if num >= 1:
        print(frase)
        repetirFraseRecursiva(frase, num - 1)

repetirFraseRecursiva("Hola, soy una frase recursiva", 5)

