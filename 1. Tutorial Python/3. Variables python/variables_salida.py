'''
Variables de salida
La print()función Python se utiliza a menudo para generar variables.
'''

x = 'Luis'
print(x)

'''
En la print()función, se generan múltiples variables, separadas por una coma:
'''
x = 'Python'
y = 'es'
z = 'sorprendente'

print(x,y,z)

'''
También puedes utilizar el +operador para generar múltiples variables:
'''
x = 'Python'
y = 'es'
z = 'sorprendente'
print(x + y + z)


'''
Para los números, el +carácter funciona como un operador matemático:
'''
x = 5
y = 10
print(x + y)

'''
En la print()función, cuando intentas combinar una cadena y un número con el + operador, Python te dará un error:
'''
x = 5
y = "John"
print(x + y)

'''
La mejor manera de generar múltiples variables en la print()función es separarlas con comas, que incluso admiten diferentes tipos de datos:
'''
x = 5
y = "John"
print(x, y)