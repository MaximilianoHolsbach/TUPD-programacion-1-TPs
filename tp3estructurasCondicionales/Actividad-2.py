"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.

"""

NOTA_MINIMA = 6
nota = float(input("Ingrese su nota: "))
if nota >= NOTA_MINIMA:
    print("Aprobado")
else:
    print("Desaprobado")

