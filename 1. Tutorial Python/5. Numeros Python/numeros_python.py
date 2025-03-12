'''
Números de Python
Hay tres tipos numéricos en Python:

int
float
complex
Las variables de tipo numérico se crean cuando se les asigna un valor:
'''

x = 8 # enteros
y = 2.8 # flotantes
z = 1j # complejos

'''
Para verificar el tipo de cualquier objeto en Python, utilice la type()función:
'''

print(type(x))
print(type(y))
print(type(z))

'''
Int
Int, o entero, es un número entero, positivo o negativo, sin decimales, de longitud ilimitada.
'''

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

'''
Flotar
Un número flotante o "número de punto flotante" es un número, positivo o negativo, que contiene uno o más decimales.
'''
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

'''
Los flotantes también pueden ser números científicos con una "e" para indicar la potencia de 10.
'''
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

'''
Complejo
Los números complejos se escriben con una "j" como parte imaginaria:
'''
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

'''
Conversión de tipos
Puede convertir de un tipo a otro con los métodos int(), float()y complex():
'''
x = 1 # numero entero
y = 2.8 # numero flotante
z = 1j # numero complejo

# convertir de entero a flotante 
a = float(x)
print(f'El numero es de tipo {type(a)} el numero es {a}')

# convertir de flotante a entero
b = int(y)
print(f'El numero es de tipo {type(b)} el numero es {b}')

# converit de entero a complejo
c = complex(x)
print(f'El numero es de tipo {type(c)} el numero es {c}')

'''
Número aleatorio
Python no tiene una random()función para crear un número aleatorio, pero Python tiene un módulo incorporado llamado randomque se puede usar para crear números aleatorios:

Ejemplo
Importa el módulo aleatorio y muestra un número aleatorio del 1 al 9:
'''

import random

print(f'El numero aleatorio es: {random.randrange(1, 10)}')