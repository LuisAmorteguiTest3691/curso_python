'''
Variables globales
Las variables que se crean fuera de una función (como en todos los ejemplos de las páginas anteriores) se conocen como variables globales.

Las variables globales pueden ser utilizadas por todos, tanto dentro como fuera de las funciones.
'''

x = 'Asombroso'

def miFuncion():
    print('Python es ' + x)

miFuncion()

'''
Si creas una variable con el mismo nombre dentro de una función, esta variable será local y solo podrá usarse dentro de la función. La variable global con el mismo nombre permanecerá como estaba, global y con el valor original.
'''

x = 'asombroso'

def miFuncion1():
    x = 'Fantastico'
    print('Python es ' + x)

miFuncion1()

'''
La palabra clave global
Normalmente, cuando se crea una variable dentro de una función, esa variable es local y solo se puede utilizar dentro de esa función.

Para crear una variable global dentro de una función, puede utilizar la globalpalabra clave.
'''
def miFuncion2():
    global x
    x = 'fantastico'

miFuncion2()

print('Python es ' + x)

'''
Además, utilice la globalpalabra clave si desea cambiar una variable global dentro de una función.
'''
x = 'sorprendente'

def miFuncion3():
    global x
    x = 'Genial'

miFuncion3()

print('Python es: ' + x)