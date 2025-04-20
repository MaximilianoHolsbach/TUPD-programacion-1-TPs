lista = []

def estaVacia(lista):
    return len(lista) == 0

def apilar(lista, elemento):
    lista.append(elemento) # Agrega un elemento a la lista (pila)

def desapilar(lista):
    return lista.pop() if not estaVacia(lista) else "No hay elementos en la lista"

apilar(lista, 1) # Agrega el elemento 1 a la lista (pila)
apilar(lista, 2) # Agrega el elemento 2 a la lista (pila)
print(lista) # Imprime la lista (pila) con los elementos 1 y 2
desapilar(lista) # Elimina el último elemento agregado (2) de la lista (pila)
print(lista) # Imprime la lista (pila) con el elemento 1 restante
#terna = lista.pop(0) if not estaVacia(lista) else "No hay elementos en la lista"
#print(terna) # Imprime el primer elemento de la lista o un mensaje si la lista está vacía

