"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

digito = 0
invertir = 0
numero = int(input("Ingrese un número entero positivo: "))

if numero != 0:
    while numero > 0:
        digito = numero % 10
        invertir = (invertir * 10) + digito
        numero = numero // 10
    print("El número invertido es:", invertir)
else:
    print("El número es cero, no se puede invertir.")