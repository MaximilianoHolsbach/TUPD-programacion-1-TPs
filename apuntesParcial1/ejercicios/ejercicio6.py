N = 5
A = [0] * N
B = [0] * N

for i in range(N):
    A[i] = i+i+i

for i in range(N):
    B[i] = i * 2

contador = 0

for i in range(N):
    if A[0] < A[i] and A[0] < B[i]:
        contador += 1
        N = N - contador
resultado = str(contador)

if A[0] < 1:
    resultado = "verdadero"
elif A[0] == 2:
    resultado = "2"
elif A[0] == 3:
    resultado = "falso"

print(resultado)