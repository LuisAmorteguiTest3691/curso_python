'''
Operadores de Python

Operadores de Python
Los operadores se utilizan para realizar operaciones sobre variables y valores.

En el siguiente ejemplo, utilizamos el +operador para sumar dos valores:

Ejemplo
'''
print(10 + 5)

'''
Python divide los operadores en los siguientes grupos:

Operadores aritméticos
Operadores de asignación
Operadores de comparación
Operadores lógicos
Operadores de identidad
Operadores de membresía
Operadores bit a bit
'''

'''
Operadores aritméticos de Python
Los operadores aritméticos se utilizan con valores numéricos para realizar operaciones matemáticas comunes:

Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''

'''
Operadores de asignación de Python
Los operadores de asignación se utilizan para asignar valores a las variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)	

'''

'''
Precedencia del operador
La precedencia del operador describe el orden en que se realizan las operaciones.

Ejemplo
Los paréntesis tienen la mayor precedencia, lo que significa que las expresiones dentro de paréntesis deben evaluarse primero:
'''

print((6 + 3) - (6 + 3))

'''
Ejemplo
La multiplicación *tiene mayor precedencia que la suma +y, por lo tanto, las multiplicaciones se evalúan antes que las sumas:
'''
print(100 + 5 * 3)

'''
El orden de precedencia se describe en la siguiente tabla, comenzando con la precedencia más alta en la parte superior:

https://onedrive.live.com/edit.aspx?resid=AC0DAB73E34F4AA1!104&migratedtospo=true&wd=target%2812.%20Curso%20de%20python.one%7Cac1697cd-1fba-4666-af83-2708981ab07d%2FP%C3%A1gina%20sin%20t%C3%ADtulo%7C08a9435d-1dec-47a0-b118-0d795c57e68e%2F%29&wdorigin=NavigationUrl
'''


'''
Ejemplo
La suma +y la resta -tienen la misma precedencia, por lo tanto evaluamos la expresión de izquierda a derecha:
'''
print(5 + 4 - 7 + 3)
