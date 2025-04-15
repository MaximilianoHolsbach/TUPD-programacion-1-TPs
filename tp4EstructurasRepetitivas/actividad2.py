"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

numero = int(input("Ingrese un numero entero: "))
digitos = 0
if numero != 0:
    while numero != 0:
        decimal = numero // 10 
        digitos += 1
        numero = decimal
    print(f'El numero tiene {digitos} digitos.')
else:
    print('El numero tiene 1 digito.')