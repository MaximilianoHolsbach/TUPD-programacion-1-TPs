"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
sumatoria = 0
for i in range(valor1+1, valor2):
    sumatoria += i
print(f'La sumatoria de los numeros entre {valor1} y {valor2} es: {sumatoria}')
