"""
SUE 2024
Laboratorio 1: Fundamentos de Python para usuarios de R.
"""

# 1. Tipos de estructuras de datos en Python

# 1.1 Asignación de variables, objetos mas comunes

# El operador de asignación en Python es el signo = 
# El mismo tiene un comportamiento distinto al <- R que se vera mas adelante

# Asignación de un entero a una variable
x = 5

# La funcion print() como en R permite imprimir el valor de una variable en la consola

print(x)

# Al igual que en R existen distintos tipos de datos, Enteros, Flotantes, Booleanos, Caracteres, etc.

# Enteros (int)
x = 5

# Flotantes (float)
y = 5.0

# Booleanos (bool)
w = False # A diferencia de R en Python los booleanos se escriben con la primera letra en mayuscula True, False

# Caracteres (str)
z = 'hola mundo' # Como en R se pueden definir mediante comillas simples o dobles
 
# Python es un lenguaje de programación orientado a objetos, lo que significa que todo en Python es un objeto, funciones, enteros, etc.
# Cada objeto en Python tiene un identificador único, un tipo y un valor 

# El identificador de un objeto es un número entero que lo identifica de manera única en la memoria 
# La funcion id() permite obtener este identificador para cada objeto
print('Identificador de x:', id(x))

# El tipo de un objeto indica a que clase pertenece, por ejemplo si es un numero entero, una función, booleano, etc.
# La funcion type() permite obtener el tipo de un objeto

print('Tipo de objeto x:', type(x)) # La funcion type() permite obtener el tipo de un objeto

# Por otro lado el valor de un objeto son las caracteristicas particulares que posee
# Por ejemplo si es un entero, el valor sera el numero entero que representa

print('Valor de x:', x)

# Listas (list)
# Las listas en Python son objetos bastante similares a las listas de R, son estructuras de datos 
# que permiten almacenar multiples objetos de cualquier tipo en su interior
# La manera mas usual para definirla es mediante los caracteres [] donde se separan los elementos por comas

lista = [5, 5.0, 'hola mundo', False]

# Es posible acceder a los elementos de una lista mediante su índice
# Si se quiere acceder al primer elemento de la lista se utiliza el siguiente indice

print('Primer elemento de la lista:', lista[0]) # Observece que los indices en Python comienzan en 0

# Para acceder de manera inversa a los elementos de la lista se utilizan los indices negativos
# Para acceder al ultimo elemento de la lista se utiliza el indice -1

print('Ultimo elemento de la lista:', lista[-1])

# Si se desea acceder a un rango de elementos de la lista se utiliza el operador slicing [:]

print('Primeros 3 elementos de la lista:', lista[0:3]) # Se accede a los elementos desde el indice 0 hasta el indice 3 (sin incluirlo)

# Es posible omitir el primer caracter del rango para indicar que se desea acceder desde el inicio de la lista

print('Primeros 3 elementos de la lista:', lista[:3])

# A su vez es posible acceder a los elementos de la lista de manera inversa

print('Ultimos 3 elementos de la lista:', lista[-3:])

# Las listas son objetos MUTABLES, Este tipo de objeto en python permiten ser modificados una vez que han sido creados
# Por ejemplo si se desea modificar el primer elemento de la lista se puede realizar de la siguiente manera

lista[0] = 10
print('Lista modificada:', lista)

# Si se desea agregar un nuevo elemento al final de la lista se puede utilizar el método append()

# Por ejemplo agregemos una nueva lista con dos enteros al final de la lista
lista.append([5,10]) 
# Como se observa los metodos en python se utilizan mediante la inclusion de un . seguido del nombre del metodo 
# y los argumentos que se desean pasar al metodo.
# En este caso el metodo append() requiere como argumento solamente el objeto que se desea agregar a la lista

print('Lista con el nuevo elemento:', lista)

# TUPLAS (tuple):

# Las tuplas son objetos similares a las listas, pero su mayor diferencia como se menciono es que son inmutables
# los objetos inmutables NO pueden ser modificados una vez que han sido creados.
# Para definir una tupla se utilizan los caracteres () donde al igual que las listas se separan los elementos por comas

tupla = (5, 5.0, 'hola mundo', False)

# Tambien es posible definir una tupla sin los parentesis, solamente separando los elementos por comas

tupla = 5, 5.0, 'hola mundo', False

# Al igual que las listas es posible acceder a los elementos mediante su indice, siguiendo la misma logica

print('Primer elemento de la tupla:', tupla[0])

print('Ultimos 2 elementos de la tupla:', tupla[-2:])

# Si se intenta modificar un elemento de la tupla 

tupla[0] = 10 # Se genera un error de tipo TypeError
# TypeError: 'tuple' object does not support item assignment
# Una vez asignado un valor a una tupla NO es posible modificar como todo objeto inmutable

# Diccionarios (dict)

# Los diccionarios son estructuras de datos mutables que contienen pares de llave(key)-valor(value), 
# donde cada llave es única y esta asociada a un valor en particular, donde cada valor puede ser de cualquier tipo
# de objeto incluso otro diccionario

# Para definir un diccionario se utilizan los caracteres {} y los pares ('llave': valor) separados por comas

diccionario = {'enteros': 5,
                'flotante': 5.0,
                'caracter': 'hola mundo'}

# Al igual que las listas y las tuplas es posible acceder a los valores del diccionario mediante su llave

print('Valor de la llave enteros:', diccionario['enteros'])

# Tambien es posible acceder a los valores del diccionario mediante el método get()

print('Valor de la llave enteros:', diccionario.get('enteros'))

# Como objeto mutable que es, se puede modificar los valores diccionario y sus valores

diccionario['enteros'] = 10

# A su vez es posible agregar nuevos pares de llave-valor al diccionario

diccionario['booleano'] = False

print('Diccionario modificado:', diccionario)

# Conjuntos (set):

# Los conjuntos son estructuras de datos similares a las listas pero con ciertas diferencias,
# la diferencia principal es que los conjuntos no contienen elementos repetidos, solamente un elemento de cada tipo
# y a su vez no existe un orden definido.
# Para definir un conjunto se utilizan los caracteres {} y los elementos separados por comas
# A diferencia de los diccionarios los conjuntos no contienen pares de llave-valor, solamente elementos

# Si se intenta definir un conjunto con elementos repetidos, el conjunto solamente contendra un elemento de cada tipo
conjunto = {5, 5.0, 'hola mundo', False, 5, 5.0}

print('Conjunto:', conjunto)

# En el conjunto solamente se pueden definir elementos inmutables, como enteros, flotantes, cadenas de caracteres, tuplas
# No se pueden definir elementos mutables como listas, diccionarios, conjuntos
# Si se intenta definir un conjunto con elementos mutables se generara un error de tipo TypeError

conjunto = {5, 5.0, 'hola mundo', False, [5, 5.0]} 

# En los conjuntos al no existir un orden definido, NO es posible acceder a los elementos mediante su indice
# Aunque si es un objeto mutable y se puede agregar o eliminar elementos del conjunto


# Diferencias de asignación entre R y Python

# Adicional a que el simbolo de asignación mas usual de R es el signo <- y en Python es el signo =, existen otras diferencias
# entre la asignación de variables en R y Python


# La asignación en Python NO CREA COPIAS de los objetos, sino que crea referencias a los objetos originales
# Por lo que si se realiza una asignación de una variable a otra, ambas variables apuntaran al mismo objeto

# Con lo cual se debe tener cuidado al realizar copias de objetos:

lista_copia = lista # Asignación de la lista a la variable lista_copia

# Si visualizamos el id de ambos objetos se observa que son iguales
print('Id lista original: ', id(lista), 'Id lista copia: ', id(lista_copia))

# El operador is permite verificar si dos variables apuntan al mismo objeto en la memoria

print(lista_copia is lista) # Se comprueba como lista_copia es igual al objeto original

# En este caso lista_copia es solamente una referencia a la lista original con lo cual si se modifica la lista_copia
# tambien se modificara la lista original

# Ejemplo de error tipico que puede cometer un usuario de R

print("Lista Original:", lista)

# Realizemos una modificación en la lista_copia
lista_copia[0] = 15 # Se modifica el primer elemento de la lista_copia

print("Lista Original:", lista)
# Se observa que la modificación realizada en la lista_copia afecta a la lista original y viceversa

# Ver mas informacion sobre las copias en Python en el siguiente enlace
# https://docs.python.org/3/library/copy.html

# ESTRUCTURAS DE CONTROL 

# Las estructuras de control en Python son similares a las de R, solo se debe tener en cuenta la sintaxis distinta de Python

# IF-ELSE
# Para escribir cualquier secuencia de control en Python se debe tener en cuenta la indentación
# En lugar de utilizar llaves {} como en R, Python utiliza la indentación para definir los bloques de código
# La misma se realiza mediante 4 espacios o un tabulador

x = 5

if x > 5:
    print('x es mayor a 5')
elif x == 5:
    print('x es igual a 5')
else:
    print('x es menor a 5')

# FOR

# El bucle for tiene una estructura similar, aunque existen diferentes maneras segun el caso de uso:

# 1. Iterar sobre una secuencia de numeros 
# Por ejemplo si se desea realizar el siguiente bucle en R
#for (x in 1:10) {
#	print(x)
#}

# En Python se puede realizar de la siguiente manera, donde se usa la funcion range() para generar una secuencia de numeros
for x in range(1, 11): 
    print(x)

# Es importante observar que la funcion range() el argumento de fin es exclusivo, es decir no se incluye en la secuencia
# Si no se ingresa un argumento de inicio, por defecto se inicia en 0

# 2. Iterar sobre una lista o tupla
#  
lista = [5, 5.0, 'hola mundo', False]

# Para iterar sobre listas o tuplas simplemente se debe definir la variable que se utilizara para iterar y la lista o tupla
for elemento in lista:
    print('Tipo de elemento:', type(elemento))


# 3. Iterar sobre un diccionario

diccionario = {'enteros': 5,
                'flotante': 5.0,
                'caracter': 'hola mundo'}

# Para iterar sobre un diccionario se puede utilizar el metodo items() que retorna una lista de tuplas con los pares llave-valor

for llave, valor in diccionario.items():
    print('Llave:', llave, 'Valor:', valor)

# Observese que en este caso el metodo items() retorna una lista de tuplas con los pares llave-valor

# 4. Iterar listas con enumerate() o zip()

# En caso de que se desee iterar sobre una lista y a su vez se desee obtener el indice de la lista la funcion enumerate() es util
# La funcion enumerate() retorna una tupla con el indice y el elemento de la lista
for indice, elemento in enumerate(lista):
    print('Indice:', indice, 'Elemento:', elemento)

# Otro caso usual de uso de for es cuando se quiere iterar sobre dos listas de igual longitud y se desea obtener 
# los elementos de ambas listas en lugar de realizar dos bucles for es posible utilizar la funcion zip()
# La misma retorna una tupla con los elementos de las listas en la misma posicion

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [5, 4, 3, 2, 1]

for elemento_1, elemento_2 in zip(lista_1, lista_2):
    print('Elemento lista 1:', elemento_1, 'Elemento lista 2:', elemento_2)

# WHILE

# El bucle while no tiene ninguna dificultad y su estructura es similar a la de un bucle for,
# y mas halla de la sintaxis la logica es la misma que en R

x = 0
while x < 5:
    print(x)
    x += 1 

# En este caso podemos destacar el uso del operador += que es equivalente a escribir x = x + 1
# Python cuenta con una serie de operadores que permiten realizar operaciones de asignación de manera mas sencilla
# Entre los se encuentran los operadores -=, *=, /=, etc. que ahorran escribir toda la expresion.

# FUNCIONES

# Aunque Python es un lenguaje de programación orientado a objetos, es posible trabajar simplemente con funciones como en R
# Las funciones en Python se definen mediante la palabra reservada def seguida del nombre de la funcion y los argumentos
# que se desean pasar a la funcion

def suma(x, y):
    return x + y

# Para llamar a la funcion simplemente se debe escribir el nombre de la funcion seguido de los argumentos que se desean pasar

print('Suma:', suma(5, 5))

# Al igual que en R es posible definir argumentos por defecto en las funciones 

def resta(x, y=5):
    return x - y

print('Resta:', resta(5)) # Se pasa un solo argumento, el segundo argumento toma el valor por defecto

# Existe ciertas diferencias en el retorno de una funcion comparado con R, en R si no se especifica un valor de retorno
# la funcion retornara el ultimo valor calculado, en Python si no se especifica un valor de retorno la funcion 
# retornara None que es un objeto especial que representa la ausencia de un valor

def multiplicacion(x, y):
    x * y

print('Multiplicacion:', multiplicacion(5, 5)) # Se retorna None

def division(x, y):
    return x / y

print('Division:', division(5, 5)) # Se retorna el valor de la division

# Parte de clases y objetos en Python




