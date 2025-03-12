'''
Conversión de Python

Puede haber ocasiones en las que desees especificar un tipo en una variable. Esto se puede hacer mediante conversión. Python es un lenguaje orientado a objetos y, como tal, utiliza clases para definir tipos de datos, incluidos sus tipos primitivos.

Por lo tanto, la conversión en Python se realiza mediante funciones constructoras:

int() - construye un número entero a partir de un literal entero, un literal flotante (eliminando todos los decimales) o un literal de cadena (siempre que la cadena represente un número entero)
float() - construye un número flotante a partir de un literal entero, un literal flotante o un literal de cadena (siempre que la cadena represente un flotante o un entero)
str() - construye una cadena a partir de una amplia variedad de tipos de datos, incluidas cadenas, literales enteros y literales flotantes

EjemploObtenga su propio servidor Python
Números enteros:
'''

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

'''
Ejemplo
Flotadores:
'''
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

'''
Ejemplo
Instrumentos de cuerda:
'''
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'