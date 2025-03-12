'''
Valores booleanos de Python

Los valores booleanos representan uno de dos valores: Trueo False.

Valores booleanos
En programación, a menudo es necesario saber si una expresión es Trueo False.

Puede evaluar cualquier expresión en Python y obtener una de dos respuestas, Trueo False.

Cuando comparas dos valores, se evalúa la expresión y Python devuelve la respuesta booleana:
Ejemplo
'''
print(10 > 9)
print(10 == 9)
print(10 < 9)

'''
Cuando se ejecuta una condición en una declaración if, Python devuelve Trueo False:

Ejemplo
Imprima un mensaje en función de si la condición es Trueo False:
'''
a = 200
b = 33

if b > a:
    print('b es mayor que a')
else:
    print('b es menor que a')

'''
Evaluar valores y variables
La bool()función te permite evaluar cualquier valor y darte Trueo False a cambio,
Ejemplo
Evaluar una cadena y un número:
'''

print(bool('Hello'))
print(bool(15))

'''
Ejemplo
Evaluar dos variables:
'''
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

'''
La mayoría de los valores son verdaderos
Casi cualquier valor se evalúa Truesi tiene algún tipo de contenido.

Cualquier cadena es True, excepto las cadenas vacías.

Cualquier número es True, excepto 0.

Cualquier lista, tupla, conjunto y diccionario son True, excepto los vacíos.
'''
a  = bool('abc')
b = bool(123)
c = bool(["apple", "cherry", "banana"])
print(a, b, c)

'''
Algunos valores son falsos
De hecho, no hay muchos valores que evalúen como False, excepto valores vacíos, como (), [], {}, "", el número 0y el valor None. Y, por supuesto, el valor Falsese evalúa como False.

Ejemplo
Lo siguiente devolverá Falso:
'''
a = bool(False)
b = bool(None)
c = bool(0)
d = bool('')
e = bool(())
f = bool([])
g = bool({})
print(a, b, c, d, e, f, g)

'''
Un valor más, u objeto en este caso, se evalúa como False, y eso es si tienes un objeto que está hecho a partir de una clase con una __len__función que devuelve 0o False:


'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

'''
Las funciones pueden devolver un valor booleano
Puede crear funciones que devuelvan un valor booleano:
Ejemplo
Imprima la respuesta de una función:
'''
def miFuncion():
   return True


print(miFuncion())

'''
Puede ejecutar código basado en la respuesta booleana de una función:

Ejemplo
Imprima "¡SÍ!" si la función devuelve Verdadero, de lo contrario imprima "¡NO!":
'''

def miFuncion2():
   return True

if miFuncion:
   print('yes')
else:
   print('no')

'''
Ejemplo
Imprima "¡SÍ!" si la función devuelve Verdadero, de lo contrario imprima "¡NO!":
'''

x = 200
print(isinstance(x, int))
