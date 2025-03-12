'''
Muchos valores para múltiples variables
Python le permite asignar valores a múltiples variables en una línea:
'''

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''
Un valor para múltiples variables
Y puedes asignar el mismo valor a múltiples variables en una línea:
'''

x = y = z = 'Luis'
print(x)
print(y)
print(z)

'''
Desempaquetar una colección
Si tienes una colección de valores en una lista, tupla, etc., Python te permite extraer los valores en variables. Esto se llama desempaquetar 

Descomprimir una lista:
'''
frutas = ['manzana','banana', 'tomate']
x, y, z = frutas
print(x)
print(y)
print(z)
