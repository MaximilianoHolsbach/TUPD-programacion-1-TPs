magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud > 0:
    if magnitud < 3:
        print("Muy leve imperceptible")
    elif 3 <= magnitud < 4:
        print("Leve ligeramente perceptible")
    elif 4 <= magnitud < 5:
        print("Moderado sentido por personas, pero generalmente no causa daños")
    elif 5 <= magnitud < 6:
        print("Fuerte puede causar daños en estructuras debiles")
    elif 6 <= magnitud < 7:
        print("Muy fuerte puede causar daños significativos en estructuras")
    else:
        print("Extremo puede causar daños a gran escala")
else:
    print("La magnitud debe ser un número positivo")