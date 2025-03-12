'''
Python - Acceso a elementos de la lista

Acceder a elementos
Los elementos de la lista están indexados y puedes acceder a ellos consultando el número de índice:

EjemploObtenga su propio servidor Python
Imprima el segundo elemento de la lista:
'''

lista = ['manzana', 'banana', 'tomate']
print(f'El segundo elemento de la lista es {lista[1]}')

'''
Nota: El primer elemento tiene índice 0.
'''

'''
Indexación negativa
La indexación negativa significa empezar desde el final.

-1se refiere al último elemento, -2se refiere al segundo último elemento, etc.
'''

'''
Ejemplo
Imprima el último elemento de la lista:
'''

print(f'El ultimo elemento de la lista es {lista[-1]}')

'''
Rango de índices
Puede especificar un rango de índices especificando dónde comenzar y dónde finalizar el rango.

Al especificar un rango, el valor de retorno será una nueva lista con los elementos especificados.
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f'El nuevo rando de la lisra es {thislist[2:5]}')

'''
Si omitimos el valor inicial, el rango comenzará en el primer elemento:
'''
print(thislist[:4])

'''
Al omitir el valor final, el rango continuará hasta el final de la lista:
'''
print(thislist[2:])

'''
Rango de índices negativos
Especifique índices negativos si desea iniciar la búsqueda desde el final de la lista:
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

'''
Comprobar si el artículo existe
Para determinar si un elemento específico está presente en una lista, utilice la inpalabra clave:
'''

thislist = ["apple", "banana", "cherry"]

if 'apple' in thislist:
    print(f'El articulo apple existe en la lista')
