'''
Python - Cambiar elementos de la lista

Cambiar el valor del artículo
Para cambiar el valor de un elemento específico, consulte el número de índice:

EjemploObtenga su propio servidor Python
Cambiar el segundo elemento:
'''

thislist = ["apple", "banana", "cherry"]
thislist[1] = 'elemento cambiado'
print(thislist)

'''
Cambiar un rango de valores de elementos
Para cambiar el valor de los elementos dentro de un rango específico, defina una lista con los nuevos valores y haga referencia al rango de números de índice donde desea insertar los nuevos valores:
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
print(f'La longitud de la lista acual es {len(thislist)}')
thislist[1:3] = ['newElement1', 'newElement2']
print(thislist)
print(f'La longitud de la nueva lista es de {len(thislist)}')
'''
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
['apple', 'newElement1', 'newElement2', 'orange', 'kiwi', 'mango']

el segundo rango no se incluye
'''

'''
Si inserta más elementos de los que reemplaza, los nuevos elementos se insertarán donde especificó y los elementos restantes se moverán en consecuencia:

Ejemplo
Cambie el segundo valor reemplazándolo con dos nuevos valores:
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(f'Logitud actual {len(thislist)}')
thislist[1:2] = ['newElement1', 'newElement2']
print(thislist)
print(f'La longitud de la nueva lista es de {len(thislist)}')

'''
Nota: La longitud de la lista cambiará cuando la cantidad de elementos insertados no coincida con la cantidad de elementos reemplazados.
'''

'''
Si inserta menos elementos de los que reemplaza, los nuevos elementos se insertarán donde especificó y los elementos restantes se moverán en consecuencia:
Ejemplo
Cambie el segundo y tercer valor reemplazándolos con un valor:
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(f'La longitud de la lista es de {len(thislist)}')
thislist[1:3] = ['newElement1']
print(thislist)
print(f'La nueva longitud de la lista es de {len(thislist)}')

'''
Insertar elementos
Para insertar un nuevo elemento de la lista, sin reemplazar ninguno de los valores existentes, podemos utilizar el insert()método.

El insert()método inserta un elemento en el índice especificado:
'''

'''
Ejemplo
Insertar "sandía" como tercer elemento:
'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, 'newElement1')
print(thislist)

