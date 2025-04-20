"""
8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
los valores almacenados
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevoNodo = Nodo(dato)
        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end = " -> ")
            actual = actual.siguiente
        print("None")

lista1 = ListaEnlazada()

lista1.agregar(6)
lista1.agregar(5)
lista1.agregar(4)
lista1.agregar(3)
lista1.agregar(2)
lista1.agregar(1)

lista1.mostrar()