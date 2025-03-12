'''
Nombres de variables
Una variable puede tener un nombre corto (como x e y) o un nombre más descriptivo (edad, nombre del vehículo, volumen total).

Reglas para las variables de Python:

Un nombre de variable debe comenzar con una letra o el carácter de guión bajo.
Un nombre de variable no puede comenzar con un número
Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _)
Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, Edad y EDAD son tres variables diferentes)
Un nombre de variable no puede ser ninguna de las palabras clave de Python .
'''

myvar = 'Luis'
mi_var = 'luis'
_my_var = 'luis'
myVar = 'luis'
MYVAR = 'luis'
myvar2 = 'luis'

'''
De la siguiente forma esta mal
'''

# 2myvar = "John"
# my-var = "John"
# my var = "John"

'''
Nombres de variables de varias palabras
Los nombres de variables con más de una palabra pueden ser difíciles de leer.

Hay varias técnicas que puedes utilizar para hacerlos más legibles:
'''

'''
Camel Case
Cada palabra, excepto la primera, comienza con mayúscula:
'''

myVariableNombre = 'Luis'

'''
Pascal Case
Cada palabra comienza con una letra mayúscula:
'''
MyVariableNombre = 'Luis'

'''
Snake Case
Cada palabra está separada por un guión bajo:
'''
my_variable_nombre = 'Luis'