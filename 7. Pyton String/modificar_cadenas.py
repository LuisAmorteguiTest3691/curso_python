'''
Python - Modificar cadenas

Python tiene un conjunto de métodos integrados que puedes usar en cadenas.

Mayúsculas

EjemploObtenga su propio servidor Python
El upper()método devuelve la cadena en mayúsculas:
'''

a = "Hello, World!"
print(a.upper())

'''
Minúscula

Ejemplo
El lower()método devuelve la cadena en minúsculas:
'''
print(a.lower())

'''
Eliminar espacios en blanco
El espacio en blanco es el espacio antes y/o después del texto real, y muy a menudo es conveniente eliminar este espacio.

Ejemplo
El strip()método elimina cualquier espacio en blanco del principio o del final:
'''
a = " Hello, World! "
print(a.strip())

'''
Reemplazar cadena

Ejemplo
El replace()método reemplaza una cadena con otra cadena:
'''
a = "Hello, World!"
print(a.replace('H', 'J'))

'''
Cuerda dividida
El split()método devuelve una lista donde el texto entre el separador especificado se convierte en los elementos de la lista.

Ejemplo
El split()método divide la cadena en subcadenas si encuentra instancias del separador:
'''
print(a.split(','))