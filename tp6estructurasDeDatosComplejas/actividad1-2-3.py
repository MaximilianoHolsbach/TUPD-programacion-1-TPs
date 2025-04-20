
# 1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

# 1) Añadir las siguientes frutas con sus respectivos precios:

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar los precios de las siguientes frutas:

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) crear una lista que contenga únicamente las frutas sin los precios

frutasNombres = list(precios_frutas.keys())

# Extra: Imprimir el diccionario de frutas y precios actualizado y la lista de frutas

print("Imprimimos el diccionario de frutas y precios actualizado: ")

for fruta, precio in precios_frutas.items():
    print(f"{fruta}: {precio}")

print("Imprimimos la lista de frutas: ")

for fruta in frutasNombres:
    print(fruta)
