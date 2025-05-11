"""
¿Qué pasa si el usuario ingresa la contraseña con mayúsculas? 
- La contraseña no se aceptará como correcta, ya que la comparación es sensible a mayúsculas y minúsculas.

_____________________________________________________

¿Cómo mejorarías el programa para dar más intentos?
- Siguiendo el mismo patrón y los conocimientos adquiridos en esta unidad, agregaria un condicional que valide que el usuario ingrese caracteres en lugar de un string vacío.
- Luego, en el else de ese condicional, le avisaria que tiene otra oportunidad para ingresar la contraseña.
- Si el usuario ingresa la contraseña correcta, se le da la bienvenida.
- Si el usuario ingresa la contraseña incorrecta, se le informa que ha agotado sus intentos.

if contrasena_usuario == "":
    print("No has introducido nada.")   
    contrasena_usuario = input("Introduce la contraseña: ")

if contrasena_usuario == contrasena_correcta:   
    print("Contraseña correcta. Bienvenido.")
else:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contrasena_usuario = input("Introduce la contraseña: ")
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta. Bienvenido.")
    else:
        print("Contraseña incorrecta, agoto sus intentos.")
"""
# Definición de constantes
contrasena_correcta = "programacion1"   

# Ingreso de datos y asignación de variables
contrasena_usuario = input("Introduce la contraseña: ")   

# Comprobación de la contraseña
if contrasena_usuario == contrasena_correcta:   
    print("Contraseña correcta. Bienvenido.")   
else:   
    print("Contraseña incorrecta. Intenta de nuevo.")  

