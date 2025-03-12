'''
Python - Formato - Cadenas

Formato de cadena
Como aprendimos en el capítulo Variables de Python, no podemos combinar cadenas y números de esta manera:
'''

# age = 36
# txt = "My name is John, I am " + age
# print(txt)

'''
Cuerdas F
F-String se introdujo en Python 3.6 y ahora es la forma preferida de formatear cadenas.

Para especificar una cadena como una f-string, simplemente coloque un fdelante del literal de cadena y agregue llaves {}como marcadores de posición para variables y otras operaciones.

Ejemplo
Crear una cadena f:
'''

age = 36
txt = f"My name is John, I am {age}"
print(txt)

'''
Marcadores de posición y modificadores
Un marcador de posición puede contener variables, operaciones, funciones y modificadores para formatear el valor.

Ejemplo
Añade un marcador de posición para la pricevariable:
'''

price = 59
txt = f"The price is {price} dollars"
print(txt)

'''
Un marcador de posición puede incluir un modificador para formatear el valor.

Se incluye un modificador agregando dos puntos :seguidos de un tipo de formato legal, como .2fque significa un número de punto fijo con 2 decimales:

Ejemplo
Mostrar el precio con 2 decimales:
'''
precio = 59
texto = f'El precio es {precio:.2f} dolares'
print(texto)


'''
Un marcador de posición puede contener código Python, como operaciones matemáticas:
Ejemplo
Realizar una operación matemática en el marcador de posición y devolver el resultado:
'''
texto = f'El precio es {20 * 9} dolares'
print(texto)