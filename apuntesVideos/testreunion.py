
expresion = input("Ingrese la expresión booleana and, or: ")
A = [0, 0, 1, 1]
B = [0, 1, 0, 1]

print("A\tB\tResultado")
for i in range(4):
    resultado = eval(f"A[i] {expresion} B[i]")
    print(f"{A[i]}\t{B[i]}\t{resultado}")