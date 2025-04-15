emisferio = input("¿En qué hemisferio se encuentra el país? (N/S): ").lower()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

if emisferio == "n":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or (mes == 3 and dia < 21):
        estacion = "Invierno"
        print("La estación del año es:", estacion)
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or (mes == 6 and dia < 21):
        estacion = "Primavera"
        print("La estación del año es:", estacion)
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or (mes == 9 and dia < 21):
        estacion = "Verano"
        print("La estación del año es:", estacion)
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
        estacion = "Otoño" 
        print("La estación del año es:", estacion) 
elif emisferio == "s":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or (mes == 3 and dia < 21):
        estacion = "Verano"
        print("La estación del año es:", estacion)
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or (mes == 6 and dia < 21):
        estacion = "Otoño"
        print("La estación del año es:", estacion)
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or (mes == 9 and dia < 21):
        estacion = "Invierno"
        print("La estación del año es:", estacion)
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
        estacion = "Primavera"
        print("La estación del año es:", estacion)     
else:
    print("Error: El hemisferio debe ser 'N' o 'S'.")

   