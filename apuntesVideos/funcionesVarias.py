#Definición de funciones del video https://www.youtube.com/watch?v=coeuXXCoVl4&t=614s perteneciente a la ACTIVIDAD II

def obtenerResto(dividendo, divisor):
    """
    Función que obtiene el resto de una división entera.
    :param dividendo: Número entero que se va a dividir.
    :param divisor: Número entero por el cual se va a dividir.
    :return: Resto de la división entera.
    """
    return dividendo % divisor


def suma(num1, num2):
    """
    Función que suma dos números.
    :param num1: Primer número a sumar.
    :param num2: Segundo número a sumar.
    :return: Suma de los dos números.
    """
    return num1 + num2

def esMultipo(num1, num2): # En este caso utilizamos el uso de composición de funciones
   """
    Función que determina si un número es múltiplo de otro.
    param num1: Número que se va a comprobar si es múltiplo.
    param num2: Número por el cual se va a comprobar si es múltiplo.
    return: True si num1 es múltiplo de num2, False en caso contrario.
    """
   return obtenerResto(num1, num2) == 0

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = int(input(f'{mensaje}'))
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def esPrimo(numero1):
    cont = 2
    numero1 = numero1 // 2 # Dividimos entre 2 el número para optimizar el proceso
    while cont <= numero1 and not(esMultipo(numero1, cont)):
        cont += 1
    return cont > numero1 # Si el contador es igual al número, es primo

def informarSiEsPrimo(num1):
    if esPrimo(num1):
        print(f'El número {num1} es primo')
    else:
        print(f'El número {num1} no es primo')

def sumaDivisoresPropios(num1):
    suma = 0
    for i in range(1, (num1 // 2) + 1):
        if esMultipo(num1, i):
            suma = suma + i
    return suma

def esPerfecto(num1):
    return sumaDivisoresPropios(num1) == num1

def informarSiEsPerfecto(num1):
    if esPerfecto(num1):
        print(f'El número {num1} es perfecto')
    else:
        print(f'El número {num1} no es perfecto')

def sucesionSimbolos(simbolo, cantidad):
    sucecion = ''
    for i in range(cantidad):
        sucecion += simbolo
    return sucecion

def imprimirSimbolo(simbolo, cantidad):
    print(sucesionSimbolos(simbolo, cantidad))

def imprimirMatrizSimbolos(columnas, filas, simbolo = 'X'):
    for i in range(filas):
        imprimirSimbolo(simbolo, columnas)