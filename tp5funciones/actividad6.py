"""
Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función
"""
# Definición de la función

def tablaMultiplicar(numero):
    """
    Función que imprime la tabla de multiplicar de un número dado.
    :param numero: Número del cual se quiere imprimir la tabla de multiplicar.
    """
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}') # Imprimimos la tabla de multiplicar del número

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = input(f'{mensaje}')
    while not num.isdigit() or len(num) == 0:
        num = input(f'Error, {mensaje}')
    num = int(num) # Convertimos a entero el número
    # Validamos que el número esté dentro del rango permitido
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

# Programa principal

numero = leerEnteroValido('Ingrese un número entero positivo: ')
tablaMultiplicar(numero) # Llamamos a la función para imprimir la tabla de multiplicar del número ingresado