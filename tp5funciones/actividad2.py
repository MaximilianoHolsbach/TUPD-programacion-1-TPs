"""
Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
# Definición de funciones

def saludar_usuario(nombre):
    """
    Esta función saluda al usuario con un mensaje personalizado.
    :param nombre: El nombre del usuario a saludar.
    :param mensaje: El mensaje de saludo. Por defecto es "Hola".
    """
    while nombre == "":
        nombre = input("Por favor, ingresa tu nombre: ")
    print(f"Buenos días estimado {nombre}! \nEs un placer saludarte!")

# Programa principal

nombre = input(f'Ingresá el nombre del usurio: ')
saludar_usuario(nombre)

