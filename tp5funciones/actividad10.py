"""
Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
# Definición de la función

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = int(input(f'{mensaje}'))
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def calcularPromedio(a, b, c):
    """
    Función que calcula el promedio de tres números.
    :param a: Primer número.
    :param b: Segundo número.
    :param c: Tercer número.
    :return: Promedio de los tres números.
    """
    return (a + b + c) / 3

#Programa principal

num1 = leerEnteroValido('Ingrese el primer número: ',1)
num2 = leerEnteroValido('Ingrese el segundo número: ',1)
num3 = leerEnteroValido('Ingrese el tercer número: ',1)

print(f'El promedio de los números {num1}, {num2} y {num3} es: {calcularPromedio(num1, num2, num3)}')