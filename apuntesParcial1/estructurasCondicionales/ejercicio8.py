"""
¿Cómo añadirías la regla de usar un carácter especial? 
- Se podría añadir una condición adicional que verifique si la contraseña contiene al menos un carácter especial, como @, #, $, %, etc. Esto se puede hacer utilizando una lista de caracteres especiales y verificando si alguno de ellos está presente en la contraseña.

¿Por qué es importante limitar la longitud máxima? 
- Limitar la longitud máxima de una contraseña es importante para evitar contraseñas excesivamente largas que podrían ser difíciles de recordar y manejar. Además, algunas aplicaciones o sistemas pueden tener restricciones en la longitud de las contraseñas por razones de seguridad o compatibilidad.
"""

# Ingreso de datos y asignación de variables

contraseña = input("Crea una contraseña: ")

longitud_valida = 8 <= len(contraseña) <= 20
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)

if longitud_valida and tiene_mayuscula and tiene_numero:
    print("Contraseña válida.")
else:
    print("La contraseña no cumple con los requisitos.")

