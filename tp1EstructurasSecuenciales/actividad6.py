"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.

"""
numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")