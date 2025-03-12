'''
Python no tiene ningún comando para declarar una variable
Una variable se crea en el momento en que se le asigna un valor por primera vez
'''

x = 5 
y = 'Jhon'
print(x)
print(y)

'''
Las variables no necesitan declararse con ningún tipo particular, e incluso pueden cambiar de tipo despúes de haber sido
configuradas
'''

x = 4 # x es de tipo int
x = 'Sally' # ahora es de tipo string
print(x)

'''
Casting

En el caso donde se desee especificar el tipo de dato para una variable, esot se puede realizar mediante conversión
'''

x = str(3) #tipo cadena
y = int(3) # tipo entero
z = float(3) # tipo florante decimal

'''
Obtener el tipo

Se puede obtener el tipo de dato de un variable de la siguiente forma 
'''

x = 5
y = 'Jhon'
print(type(x))
print(type(y))

'''
¿Comillas dobles o simples?

Las variables de cadena se pueden declara utilizando comillas dobles o simples
'''

x = "Jhon"
x = 'Jhon'

'''
Los nombres de las variables entre mayúsculas y minúsculas
'''
a = 4
A = 'Sally'
print(a)