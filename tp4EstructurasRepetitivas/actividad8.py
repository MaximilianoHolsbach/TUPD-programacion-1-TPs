"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

CORTE = 100 # Definimos la constante CORTE para el número de entradas
# Inicializamos los contadores
contadorPares = 0
contadorImpares = 0
contadorNegativos = 0
contadorPositivos = 0
ciclos = 0

while ciclos < CORTE:
    numero = int(input("Ingrese un número: "))
    ciclos += 1

    if numero > 0:
        if numero % 2 == 0:
            contadorPares += 1
            contadorPositivos += 1
        else:
            contadorImpares += 1
            contadorPositivos += 1
    elif numero < 0:
        if numero % 2 == 0:
            contadorPares += 1
            contadorNegativos += 1
        else:
            contadorImpares += 1
            contadorNegativos += 1
    else:
        print("Ingreso inválido, el número no puede ser cero")

print(f"Cantidad de números pares: {contadorPares}")
print(f"Cantidad de números impares: {contadorImpares}")
print(f"Cantidad de números negativos: {contadorNegativos}")
print(f"Cantidad de números positivos: {contadorPositivos}")