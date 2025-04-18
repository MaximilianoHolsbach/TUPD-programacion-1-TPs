"""

"""
# Definicion de funciones

def leerEnteroValido(mensaje, min = float('-inf'), max = float('inf')):
    num = input(f'{mensaje}')
    while not num.isdigit() or len(num) == 0:
        num = input(f'Error, {mensaje}')
    num = int(num) # Convertimos a entero el número
    # Validamos que el número esté dentro del rango permitido
    while num < min or num > max:
        num = int(input(f'Error, {mensaje}'))
    return num

def calcularAreaCirculo(radio):
    """
    Función que calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo.
    :return: Área del círculo.
    """
    return 3.14 * (radio ** 2) # Usamos 3.14 como aproximación de pi

def calcularPerimetroCirculo(radio):
    """
    Función que calcula el perímetro de un círculo dado su radio.
    :param radio: Radio del círculo.
    :return: Perímetro del círculo.
    """
    return 2 * 3.14 * radio # Usamos 3.14 como aproximación de pi

# Programa principal

radio = leerEnteroValido('Ingrese el radio del circulo: ', 0)

print(f'El area del circulo es: {calcularAreaCirculo(radio)}, y el perimetro es: {calcularPerimetroCirculo(radio)}')


