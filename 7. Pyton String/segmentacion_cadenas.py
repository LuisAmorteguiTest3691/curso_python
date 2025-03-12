'''
Python - Segmentación de cadenas

Rebanar
Puedes devolver un rango de caracteres utilizando la sintaxis de segmentación.

Especifique el índice inicial y el índice final, separados por dos puntos, para devolver una parte de la cadena.

EjemploObtenga su propio servidor Python
Consigue los caracteres de la posición 2 a la posición 5 (no incluidos):
'''

b = "Hello, World!"
print(b[2:5])

'''
Rebanar desde el principio
Si omitimos el índice de inicio, el rango comenzará en el primer carácter:

Ejemplo
Consigue los personajes desde el inicio hasta la posición 5 (no incluidos):
'''

print(b[:5])

'''
Cortar hasta el final
Si omitimos el índice final , el rango irá hasta el final:

Ejemplo
Consigue los personajes desde la posición 2, y hasta el final:
'''

print(b[2:])

'''
Indexación negativa
Utilice índices negativos para iniciar la porción desde el final de la cadena:

Ejemplo
Consigue los personajes:

De: "o" en "¡Mundo!" (posición -5)

A, pero no incluido: "d" en "¡Mundo!" (posición -2):
'''
print(b[-5:-2])