'''
Python - Agregar elementos a una lista

Añadir elementos
Para agregar un elemento al final de la lista, utilice el método append() :

EjemploObtenga su propio servidor Python
Usando el append()método para agregar un elemento:
'''

thislist = ["apple", "banana", "cherry"]
thislist.append('newElement1')
print(thislist)

'''
Insertar elementos
Para insertar un elemento de lista en un índice especificado, utilice el insert()método.

El insert()método inserta un elemento en el índice especificado:
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(2, 'newElement1')
print(thislist)

'''
Ampliar lista
Para agregar elementos de otra lista a la lista actual, utilice el extend()método.
Ejemplo
Añade los elementos de tropicala thislist:
'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Los elementos se agregarán al final de la lista.

'''
Agregar cualquier iterable
El extend()método no tiene que agregar listas , puede agregar cualquier objeto iterable (tuplas, conjuntos, diccionarios, etc.).

Ejemplo
Agregar elementos de una tupla a una lista:
'''

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)





