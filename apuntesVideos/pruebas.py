"""
Ejercicio 1: Conversor de bases numéricas"""
numero = input("Ingrese un número: ")   
base_origen = int(input("Ingrese la base de origen (2, 8, 10, 16): "))
base_destino = int(input("Ingrese la base de destino (2, 8, 10, 16): "))
    # Paso 1: convertir a decimal
decimal = int(numero, base_origen)

    # Paso 2: convertir de decimal a la base destino
if numero == "" or numero == "0":
    decimal = 0
if base_destino == 2:
    binario =  bin(decimal)[2:]
    print(f"El número {numero} en base {base_origen} es {binario} en base 2.")
elif base_destino == 10:
    decimal = decimal
    print(f"El número {numero} en base {base_origen} es {decimal} en base 10.")
elif base_destino == 8:
    octal =  oct(decimal)[2:]
    print(f"El número {numero} en base {base_origen} es {octal} en base 8.")
elif base_destino == 16:
    hexadecimal = hex(decimal)[2:].upper()
    print(f"El número {numero} en base {base_origen} es {hexadecimal} en base 16.")
else:
    print("Base de destino no válida. Debe ser 2, 8, 10 o 16.")
