'''
Listas de Python
'''

mylist = ["apple", "banana", "cherry"] # esto es una lista

'''
Lista
Las listas se utilizan para almacenar varios elementos en una sola variable.

Las listas son uno de los cuatro tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos; los otros tres son Tuple , Set y Dictionary , todos con diferentes cualidades y usos.

Las listas se crean utilizando corchetes:
'''
lista = ['manzana', 'banana', 'tomate']
print(lista)

'''
Elementos de la lista
Los elementos de la lista están ordenados, son modificables y permiten valores duplicados.

Los elementos de la lista están indexados, el primer elemento tiene índice [0], el segundo elemento tiene índice, [1]etc.

Ordenado
Cuando decimos que las listas están ordenadas, significa que los elementos tienen un orden definido, y ese orden no cambiará.

Si agrega nuevos elementos a una lista, los nuevos elementos se colocarán al final de la lista.

Nota: Hay algunos métodos de lista que cambiarán el orden, pero en general: el orden de los elementos no cambiará.
'''

'''
Cambiable
La lista es modificable, lo que significa que podemos cambiar, agregar y eliminar elementos en una lista después de haberla creado.

Permitir duplicados
Dado que las listas están indexadas, las listas pueden tener elementos con el mismo valor:

Ejemplo
Las listas permiten valores duplicados:
'''
lista = ['manzana', 'banana', 'tomate', 'manzana', 'banana']
print(lista)

'''
Longitud de la lista
Para determinar cuántos elementos tiene una lista, utilice la len()función:
'''

print(f'La longitud de la lista es de {len(lista)}')

'''
Elementos de lista: tipos de datos
Los elementos de la lista pueden ser de cualquier tipo de datos:
'''
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

'''
Una lista puede contener diferentes tipos de datos:
'''
list1 = ["abc", 34, True, 40, "male"]

'''
tipo()
Desde la perspectiva de Python, las listas se definen como objetos con el tipo de datos 'lista':

<class 'list'>
'''

print(f'El tipo de dato de la lisra es {type(lista)}')

'''
El constructor list()
También es posible utilizar el constructor list() al crear una nueva lista.
Ejemplo
Usando el list()constructor para hacer una lista:
'''
lista = list(('manzana', 'banana', 'tomate'))
print(f'Esto es una lista {lista} el tipo de dato es {type(lista)} su longitud es de {len(lista)}')

'''
Colecciones de Python (matrices)
Hay cuatro tipos de datos de colección en el lenguaje de programación Python:

La lista es una colección ordenada y modificable. Permite miembros duplicados.
Tupla es una colección ordenada e inmutable. Permite miembros duplicados.
Un conjunto es una colección desordenada, inmutable* y sin indexar. No contiene miembros duplicados.
El diccionario es una colección ordenada** y modificable. No contiene miembros duplicados.
'''

'''
* Los elementos del conjunto no se pueden modificar, pero puedes eliminarlos y/o agregarlos cuando lo desees.

**A partir de la versión 3.7 de Python, los diccionarios están ordenados . En Python 3.6 y versiones anteriores, los diccionarios están desordenados .

Al elegir un tipo de colección, es útil comprender las propiedades de ese tipo. Elegir el tipo correcto para un conjunto de datos en particular podría significar la retención del significado y un aumento en la eficiencia o la seguridad
'''

