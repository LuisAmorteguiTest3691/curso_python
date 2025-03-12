'''
Python - Caracteres de escape

Personaje de escape
Para insertar caracteres que no son válidos en una cadena, utilice un carácter de escape.

Un carácter de escape es una barra invertida \seguida del carácter que desea insertar.

Un ejemplo de un carácter ilegal es una comilla doble dentro de una cadena que está rodeada por comillas dobles:

EjemploObtenga su propio servidor Python
Recibirá un error si utiliza comillas dobles dentro de una cadena que está rodeada por comillas dobles:

txt = "We are the so-called "Vikings" from the north."
'''

'''
Para solucionar este problema, utilice el carácter de escape \":

Ejemplo
El carácter de escape le permite utilizar comillas dobles cuando normalmente no estaría permitido:
'''

txt = "We are the so-called \"Vikings\" from the north."

'''
Personajes de escape
Otros caracteres de escape utilizados en Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''

