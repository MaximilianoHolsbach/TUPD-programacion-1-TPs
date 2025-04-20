"""
7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila.
"""

from collections import deque

class Clientes:
    def __init__(self):
        self.clientes = deque()
    
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    
    def hayClientes(self):
        return len(self.clientes) > 0
    
    def atenderCliente(self):
        return self.clientes.popleft() if self.hayClientes() else "No hay clientes en la fila"
    
    def VerSiguienteCliente(self):
        return self.clientes[0] if self.hayClientes() else "No hay clientes en la fila"
    

fila1 = Clientes()

fila1.agregarCliente("Cliente 1, Juan Perez")
fila1.agregarCliente("Cliente 2, Maria Lopez")
fila1.agregarCliente("Cliente 3, Pedro Gonzalez")
fila1.agregarCliente("Cliente 4, Ana Torres")
fila1.agregarCliente("Cliente 5, Luis Ramirez")

print(f'La fila tiene {len(fila1.clientes)} clientes')
print(fila1.VerSiguienteCliente())

fila1.atenderCliente()

print(f'La fila tiene {len(fila1.clientes)} clientes')
print(fila1.VerSiguienteCliente())