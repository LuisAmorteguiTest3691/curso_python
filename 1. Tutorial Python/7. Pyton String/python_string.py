'''
Python Strings
Instrumentos de cuerda
Las cadenas en Python están rodeadas por comillas simples o comillas dobles.

'hola' es lo mismo que "hola" .

Puede mostrar un literal de cadena con la print()función:
'''

'''
Citas dentro de citas
Puedes utilizar comillas dentro de una cadena, siempre que no coincidan con las comillas que rodean la cadena:
'''
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

'''
Asignar una cadena a una variable
La asignación de una cadena a una variable se realiza con el nombre de la variable seguido de un signo igual y la cadena:
'''
a = "Hello"
print(a)

'''
Cadenas multilineales
Puede asignar una cadena de varias líneas a una variable utilizando tres comillas:
'''

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

'''
O tres comillas simples:
'''
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

'''
Las cadenas son matrices
Al igual que muchos otros lenguajes de programación populares, las cadenas en Python son matrices de bytes que representan caracteres Unicode.

Sin embargo, Python no tiene un tipo de datos de carácter, un solo carácter es simplemente una cadena con una longitud de 1.

Se pueden utilizar corchetes para acceder a elementos de la cadena.

Ejemplo
Obtener el carácter en la posición 1 (recuerde que el primer carácter tiene la posición 0):
'''

a = 'Hola mundo'
print(f'El primer elemento es {a[1]}')

'''
Hacer un bucle a través de una cuerda
Dado que las cadenas son matrices, podemos recorrer los caracteres de una cadena mediante un forbucle.

Ejemplo
Recorre las letras de la palabra "banana":
'''

for x in 'banana':
    print(x)

'''
Longitud de la cuerda
Para obtener la longitud de una cadena, utilice la len()función.
'''
x = 'Hola mundo'
print(f'El largo de la cadena es {len(x )}')

contador = 0
for dato in x:
    contador += 1
    print(contador)

print(f'El valor del contador es de {contador}')


'''
Cadena de verificación
Para comprobar si una determinada frase o carácter está presente en una cadena, podemos utilizar la palabra clave in.

Ejemplo
Comprueba si "free" está presente en el siguiente texto:
'''

texto = "The best things in life are free!"

if 'free' in texto:
    print(f'La palabra free esta dentro del texto')
else:
    print('La palara no esta dentor del texto')

'''
Úselo en una ifdeclaración:
'''
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

'''
Para comprobar si una determinada frase o carácter NO está presente en una cadena, podemos utilizar la palabra clave not in.
Ejemplo
Comprueba si "caro" NO está presente en el siguiente texto:
'''
texto = "The best things in life are free!"
print('esto' not in texto);

'''
Úselo en una ifdeclaración:

Ejemplo
imprimir solo si "caro" NO está presente:
'''

texto = "The best things in life are free!"

if 'esto' not in texto:
    print(f'La palabra esto no esta dentro de la frase')




