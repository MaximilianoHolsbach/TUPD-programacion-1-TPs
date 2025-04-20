"""
def __init__() se utiliza para inicializar objetos dentro una clase, se escribe dos guiones bajos init dos guiones bajos seguido de parentesis (self).
self es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la clase. 

Por que usar el Constructor?
✓ Modularidad: Permite crear objetos con diferentes atributos sin tener que configurar cada uno de ellos manualmente.
✓ Claridad: el constructor proporciona una forma clara de cómo deben ser inicializados los objetos de la clase.
✓ Facilidad de uso: simplifica la creación de objetos, ya que los valores de los atributos se pasan directamente al constructor al crear el objeto.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo 'nombre' inicializado con el valor pasado al constructor
        self.edad = edad

    def presentarse(self):
        print(f'Buenos días soy {self.nombre} y tengo {self.edad} años.')

persona1 = Persona('Juan', 25) # Creamos un objeto de la clase Persona, pasamos los valores 'Juan' y 25 al constructor
persona1.presentarse() # Llamamos al método presentarse del objeto persona1, que imprime su presentación

class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Año:{self.año}')

coche1 = Coche('Toyota', 'Corolla', 2020) # Creamos un objeto de la clase Coche, pasamos los valores 'Toyota', 'Corolla' y 2020 al constructor
coche1.mostrar_info() # Llamamos al método mostrar_info del objeto coche1, que imprime la información del coche

print(coche1.marca) # Imprimimos el atributo 'marca' del objeto coche1, que es 'Toyota'

"""
Pilas y Colas

Pilas (Stacks)
✓ Estructura de datos LIFO (Last In First Out), el último elemento agregado es el primero en salir.
✓ Se utiliza para almacenar datos temporalmente, como en la ejecución de funciones o el deshacer acciones en aplicaciones.
"""

class Pila:
    def __init__(self):
        self.elementos = [] # Inicializamos una lista vacía para almacenar los elementos de la pila

    def apilar(self, elementos):
        self.elementos.append(elementos) # Agregamos un elemento a la pila utilizando el método append de la lista


    def estaVacia(self):
        return len(self.elementos) == 0

    def desapilar(self):
        return self.elementos.pop() if not self.estaVacia() else "No hay elementos en la pila"
    
    def verTop(self):
        return self.elementos[-1] if not self.estaVacia() else "No hay elementos en la pila"
    
pila = Pila() # Creamos un objeto de la clase Pila

pila.apilar("🍎 Manzana")
pila.apilar("🍌 Banana") # Agregamos elementos a la pila utilizando el método apilar
pila.apilar("🍊 Naranja")
pila.apilar("🍇 Uva") # Agregamos elementos a la pila utilizando el método apilar


print(pila.verTop()) # Imprimimos el elemento en la parte superior de la pila utilizando el método verTop

print(pila.desapilar()) # Desapilamos el último elemento agregado a la pila utilizando el método desapilar

"""
Colas (Queues)

✓ Estructura de datos FIFO (First In First Out), el primer elemento agregado es el primero en salir.
✓ Se utiliza para almacenar datos en orden, como en la impresión de documentos o la gestión de tareas en un sistema operativo.
✓ Debemos importar la librería collections para usar deque, que es una cola doblemente enlazada.
✓ La función deque() crea una cola vacía, y podemos agregar elementos a la cola utilizando el método append() y eliminar elementos utilizando el método popleft().

"""

from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque() # Inicializamos una cola vacía utilizando deque

    def enFilar(self, elemento):
        self.elementos.append(elemento)

    def estaVacia(self):
        return len(self.elementos) == 0

    def desEnFilar(self):
        return self.elementos.popleft() if not self.estaVacia() else "No hay elementos en la cola"
    
    def verFrente(self):
        return self.elementos[0] if not self.estaVacia() else "No hay elementos en la cola"
    
cola1 = Cola() # Creamos un objeto de la clase Cola

cola1.enFilar("Juan")# Agregamos elementos a la cola utilizando el método enFilar
cola1.enFilar("Maria") 
cola1.enFilar("Ana")
cola1.enFilar("Laura") 
cola1.enFilar("Platon")

print(cola1.verFrente()) # Imprimimos el elemento en la parte frontal de la cola utilizando el método verFrente

cola1.desEnFilar() # Desenfilamos el primer elemento agregado a la cola utilizando el método desEnFilar

print(cola1.verFrente())