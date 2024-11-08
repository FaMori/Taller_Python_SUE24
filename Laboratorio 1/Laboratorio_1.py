"""
SUE 2024
Laboratorio 1: Fundamentos de Python para usuarios de R.
"""

#%%
# 1. Asignación de variables y objetos mas simples 

# En Python el operador de asignación, denotado por 
# el símbolo "=", es el operador que se utiliza 
# para asignar valores a las variables.

# Veamos un ejemplo simple asignemos el valor entero 
# 5 a la variable x

x = 5

# El comportamiento de esta asignación es similar al 
# de R (x <- 5), se toma el valor conocido, 5, 
# y asigna ese valor a la variable con el nombre "x". 

# Después de ejecutar esta línea, este número se 
# almacenará en esta variable. Hasta que se cambie el 
# valor o se elimine la variable, el carácter x se 
# comporta como el valor 5. 

# Mas adelante veremos que en realidad la asignacion 
# en Python tiene ciertas diferencias a la de R, 
# pero en este caso simple podria decirse que es similar.

# La funcion print() como en R permite imprimir el valor 
# de una variable en la consola

print('El valor de x es:', x)

# Al igual que R los objetos mas simples en Python 
# son los enteros, flotantes, booleanos y caracteres.

# Enteros (int)
x = 5

# Flotantes (float)
y = 5.0

# Booleanos (bool)
w = False 

# Observe se escriben solamente con la primer 
# letra en mayuscula True False

# Caracteres (str)
z = 'hola mundo' 
 
# Python es un lenguaje de programación orientado 
# a objetos, lo que significa que todo en Python es 
# un objeto, funciones, numeros enteros, cadenas, etc.

# Cada objeto en Python tiene un identificador único, 
# un tipo y un valor.

# El identificador de un objeto es un número entero que 
# lo identifica de manera única en la memoria 

# La funcion id() permite obtener este identificador 
# para cada objeto

id(z)

# El tipo de un objeto indica a que clase pertenece, 
# por ejemplo si es un numero entero, una función, 
# booleano, etc.

# La funcion type() permite obtener el tipo de un objeto

type(z) 

# Por otro lado el valor de un objeto son las 
# caracteristicas particulares que posee.
# Por ejemplo si es una cadena de caracteres, el valor es
# el texto que contiene

z

# Una caracteristica de los objetos son los metodos, los 
# metodos son funciones que se pueden aplicar a un objeto, 
# la forma de llamar a un metodo es mediante la siguiente sintaxis

# objeto.metodo(argumentos)

# Por ejemplo para los strings existe el metodo llamado 
# upper() que convierte todos los caracteres de la cadena 
# en mayusculas, en este caso no se requiere pasar 
# argumentos al metodo con lo cual solamente se escribe 
# de la siguiente manera

cadena_mayuscula = z.upper()

cadena_mayuscula

# Los metodos y objetos son una parte fundamental de 
# Python como lenguaje orientado a objetos que lo 
# diferencian de lenguajes funcionales como R, se vera 
# en este laboratorio y el siguiente muchos ejemplos
# de metodos y objetos en Python.

# Puede verse mas informacion sobre distintos metodos 
# para objetos de tipo caracter en el siguiente enlace
# https://docs.python.org/3/library/stdtypes.html#string-methods

#%%
# 2. Listas, tuplas, diccionarios y conjuntos

# Hasta ahora se han visto los tipos de datos mas simples
# que permiten asignar un elemento a una variable,
# pero Python al igual que R cuenta con estructuras de 
# datos mas complejas que permiten almacenar multiples 
# elementos

#%%
# Listas (list)

# Las listas en Python son estructuras de datos que 
# permiten almacenar multiples objetos de cualquier tipo 
# en su interior (hasta listas dentro de listas)

# La manera mas usual para definirla es mediante los 
# caracteres [] donde se separan los elementos por comas

lista = [5, 5.0, 'hola mundo', 12]

# Al igual que en R es posible acceder a los elementos de
# la lista mediante su indice aunque presenta
# ciertas diferencias.

# Si se quiere acceder al primer elemento de la lista se
# utiliza el siguiente indice

lista[0]

# Observe que los indices en Python comienzan en 0 en 
# lugar de 1 como en R.

# Adicionalemente en Python es posible acceder a 
# elementos recorriendo la lista de manera inversa.

# Para acceder de manera inversa a los elementos de la 
# lista se utilizan los indices negativos.
# Para acceder al ultimo elemento de la lista se utiliza 
# el indice -1.

lista[-1]

# Para acceder al penultimo elemento de la lista se 
# utiliza el indice -2 y asi sucesivamente

# Si se desea acceder a un rango de elementos de la lista
# se utiliza el slicing :, el mismo es bastante
# similar a lo que tenemos en R

lista[0:2] 

# Se accede a los elementos desde el indice 0 hasta el 
# indice 2 (sin incluirlo)

# Es posible omitir el primer caracter para indicar que 
# se desea acceder desde el inicio de la lista

lista[:2]

# A su vez es posible acceder a los elementos de la lista
# de manera inversa tambien utilizando el slicing

# Ejercicio: Pruebe acceder a los ultimos 2 elementos
# de la lista completando los ... de la siguiente linea

lista[...]

# En python existen dos tipos de objetos, los objetos 
# MUTABLES y los objetos INMUTABLES, la diferencia
# principal entre ambos es que los objetos inmutables 
# NO pueden ser modificados una vez que han sido creados.

# Las listas son objetos MUTABLES, lo que significa que 
# una vez que se ha creado una lista es posible 
# modificar los elementos de la misma, por ejemplo si 
# se desea modificar el primer elemento de la lista
# el comportamiento es similar a R

print('Lista original:', lista)

lista[0] = 10

print('Lista modificada:', lista)

# Al igual que otros objetos, las listas cuentan con una
# serie de metodos que permiten realizar ciertas 
# operaciones

# Una practica muy comun en Python es añadir elementos a 
# una lista ya creada, utilizando el metodo append()

# Ejercicio: Pruebe añadir al objeto que llamamos lista 
# un nuevo valor que sea un booleano False




# Compruebe el resultado
print('Lista con el nuevo elemento:', lista)

# Puede verse mas informacion sobre los metodos de las 
# listas en el siguiente enlace
# https://docs.python.org/3/tutorial/datastructures.html

#%%
# TUPLAS (tuple):

# Las tuplas son objetos similares a las listas, pero su
# mayor diferencia es que son INMUTABLES, como se menciono
# los objetos inmutables NO pueden ser modificados una 
# vez que han sido creados.

# Para definir una tupla se utilizan los caracteres () 
# donde al igual que las listas se separan los elementos
# por comas

tupla = (5, 5.0, 'hola mundo', False)

id(tupla)

# Tambien es posible definir una tupla sin los parentesis, 
# solamente separando los elementos por comas

tupla = 5, 5.0, 'hola mundo', False, "nuevo elemento" 

id(tupla)

# En este caso no estamos modificando el objeto, sino 
# creando uno nuevo (con distinto id) 

# Al igual que las listas es posible acceder a los 
# elementos mediante su indice, siguiendo la misma logica

# Ejercicio: Pruebe acceder al primer elemento de la 
# tupla



# Ejercicio: Pruebe modificar un elemento de la tupla 
# como hicimos con la lista




# A su vez una practica usual es desempaquetar los 
# elementos de una tupla de la siguiente forma

tupla = (5, 5.0, 'hola mundo', False)

entero, flotante, caracter, booleano = tupla

entero
flotante

# Se debe tener en cuenta que el numero de variables 
# definidas en la izquierda coincida con el numero de
# elementos en la tupla, en caso contrario se generara 
# un error

entero, flotante, caracter = tupla

# En este caso obtendremos un error de tipo ValueError
# ValueError: too many values to unpack (expected 3) 

# Si no se quiere desempaquetar todos los elementos 
# que vienen de la tupla es usual utilizar el caracter _
# para indicar todos los elementos que no se quiera
# utilizar

entero, _, caracter, _ = tupla

#%%
# Diccionarios (dict)

# Los diccionarios son estructuras de datos MUTABLES 
# que contienen pares de llave(key)-valor(value), 
# donde cada llave es única y esta asociada a un valor 
# en particular, al igual que las listas o tuplas
# los valores pueden ser de cualquier tipo incluso 
# listas, tuplas, diccionarios, etc.

# Para definir un diccionario se utilizan los caracteres 
# {} y se debe utilizar la siguiente sintaxis 
# 'llave': valor separados por comas

diccionario = {'enteros': 5,
               'flotante': 5.0,
               'caracter': 'hola mundo'}

# Al igual que las listas y las tuplas es posible acceder
# a los valores del diccionario, en este caso se le 
# indica al diccionario la llave del valor que se desea 
# obtener

diccionario['enteros']

# Como objeto mutable que es, es posible modificar los 
# valores del diccionario, por ejemplo el metodo update()
# permite modificar el valor de una llave en particular o
# agregar una nueva llave-valor al diccionario

diccionario.update({'flotante': 2.4, 
                    'booleano': False, 
                    'lista': [5, 5.0]})

diccionario

#%%
# Conjuntos (set):

# Los conjuntos son estructuras de datos similares a las
# listas pero con ciertas diferencias, la diferencia 
# principal es que los conjuntos no contienen elementos 
# repetidos y no tienen un orden definido como las 
# listas o tuplas.

# Para definir un conjunto se utilizan los caracteres {}
# y los elementos separados por comas.

# Ejercicio: Defina un conjunto que contenga los 
# siguientes numeros 1, 2, 1, 3.

# Recuerde ingresar el 1 dos veces y observe el resultado
conjunto = 

# Otra diferencia importante de los conjuntos es que 
# solamente se pueden definir elementos inmutables
# como enteros, flotantes, cadenas de caracteres, tuplas

# Si se intenta definir un conjunto con elementos 
# mutables se generara un error de tipo TypeError

conjunto = {5, 5.0, 'hola mundo', False, [5, 5.0]} 

# TypeError: unhashable type: 'list'

# En los conjuntos al no existir un orden definido, 
# NO es posible acceder a los elementos mediante su 
# indice

# Ejercicio: Pruebe acceder al primer elemento del 
# conjunto


#%%
# 3. Diferencias de asignación entre R y Python

# Aunque la asignación de una variable simple como x = 5
# es similar en Python y R, existen ciertas diferencias
# sobre todo cuando se trabaja con objetos mas complejos
# como listas que llevan a errores muy comunes.

# Uno de los errores mas comunes de usuarios de R al 
# comenzar a trabajar con Python es la asignación de 
# objetos y la creación de copias de objetos.

# La asignación en Python NO CREA COPIAS de objetos, 
# solamente crea referencias en memoria a los objetos 
# originales.

# Por lo que si se realiza una asignación de una variable
# a otra, ambas variables apuntaran al mismo objeto.

# El tipico error cometido:

# Supongamos que se tiene una lista y se desea crear una
# copia de la misma, en R es posible realizar la siguiente
# asignación lista_copia <- lista, en este caso si se 
# modificara la lista_copia como funciona internamente R
# no se veria afectada la lista original. En Python esto
# no es asi:

lista = [1,2,3]

lista_copia = lista 

# Si visualizamos el id de ambos objetos se observa que 
# son iguales

print('Id lista original: ', id(lista), 
      'Id lista copia: ', id(lista_copia))

# El operador 'is' permite verificar si dos variables 
# comparten la misma referencia en memoria

lista_copia is lista

# En este caso lista_copia es solamente una referencia 
# a la lista original con lo cual si se modifica la 
# lista_copia tambien se modificara la lista original

# Ejercicio: Pruebe modificar el primer elemento de la 
# lista que definimos como lista_copia por otro numero
# y observe el resultado en la lista original



#%%
# 4. Copias en Python

# Debido a esto en Python es necesario entender como se 
# crean copias de objetos, existiendo dos tipos de copias,
# las copias superficiales y las copias profundas.

# Una copia superficial implica construir un nuevo objeto 
# y luego rellenarlo con referencias a los objetos 
# secundarios que se encuentran en el objeto original. 

# Para entender mejor esto veamos un ejemplo:

# Supongamos que tenemos una lista que contiene dos 
# conjuntos:
lista = [{1,3},{2,5}]

# Si se desea realizar una copia superficial de la lista 
# se puede utilizar el metodo copy()

# El metodo copy() retorna una copia superficial de 
# objetos listas, diccionarios, conjuntos, etc.

lista_copia_sup = lista.copy()

# Ejercicio: Comprobar si los id de lista y 
# lista_copia_sup son los mismos


# Que pasa con los objetos internos de la listas?
# Por ejemplo realizemos el is para el primer elemento 
# de las listas

lista_copia_sup[0] is lista[0]

# Se retorna True, lo que implica que los objetos 
# internos de la lista copia superficial son los mismos

# Esto tiene las siguientes implicancias:
    
# Si por ejemplo se agrega un nuevo elemento a la lista 
# copia

lista_copia_sup.append({4,5})

# Se observa que el nuevo elemento se agrega a la 
# lista copia pero NO a la lista original

# Lista original
lista

# Lista copia superficial
lista_copia_sup

# Pero si se modifica un conjunto interno de la lista 
copia superficial

lista_copia_sup[0].add(5)

lista
lista_copia_sup

# Se observa que la modificación realizada en el conjunto
# interno de la copia superficial afecta a la lista 
# original.

# Ahora volvamos a definir la lista y veamos que es una
# copia profunda

lista = [{1,3},{2,5}]

# La copia profunda implica crear un nuevo objeto y 
# rellenarlo con copias de los objetos secundarios

# Para realizar una copia profunda de un objeto en 
# Python se puede utilizar el modulo copy

# Los modulos en Python se pueden considerar como 
# librerias que contienen funciones y objetos
# que se pueden utilizar en un script de Python, en este 
# caso el modulo copy viene incluido 
# en la libreria estandar de Python 
# pero DEBE SER IMPORTADO para poder utilizarlo. 

# El modulo copy contiene la funcion deepcopy() que 
# permite realizar copias profundas
# Para importar un modulo en Python se utiliza la palabra
# reservada import seguida del nombre del modulo

import copy

# Una vez importado un modulo es posible utilizar una 
# funcion del mismo utilizando la siguiente sintaxis

# nombre_modulo.nombre_funcion(argumentos)

# Por ejemplo para utilizar la funcion deepcopy() 

lista_copia_prof = copy.deepcopy(lista)

# A su vez es posible no importar el modulo completo y 
# solamente importar la funcion que se desea utilizar
# En ese caso se utiliza el from seguido del nombre del 
# modulo + import seguido de la funcion

from copy import deepcopy

# En caso de importa solamente la funcion deepcopy() 
# del modulo copy, se debe llamar a la funcion 
# directamente sin especificar el nombre del modulo

lista_copia_prof = deepcopy(lista)

# Ahora que se comprende como importar funciones de 
# modulos veamos que sucede al realizar la copia profunda

# En este caso si realiza el is se observa que los 
# objetos internos de la lista copia profunda son 
# distintos

lista_copia_prof[0] is lista[0]

# Lo que implica que si se modifica un objeto interno de
#  la lista copia profunda no afectara a la lista original

lista_copia_prof[0].add(5)

lista # Lista original

lista_copia_prof # Lista copia profunda

# Mas informacion sobre el modulo copy y la funcion deepcopy() se puede encontrar en el siguiente enlace:
# https://docs.python.org/3/library/copy.html

# En el siguiente enlace puede encontrar todas los modulos disponibles
# en la libreria standard de Python
# https://docs.python.org/3/library/


#%% 5. Estructuras de control y bucles en Python

# Las estructuras de control en Python son similares a 
# las de R, solo se debe tener en cuenta la sintaxis 
# distinta de Python.

# A diferencia de R donde se utilizan llaves {} para 
# definir bloques de codigo,en Python se utiliza la 
# indentación.

# La misma se realiza mediante añadir sangrias usualmente
# 4 espacios o un tabulador

# Por ejemplo si se desea realizar la condicion IF-ELSE 
# de R

# x <- 5
# if (x > 5) {
# 	print('x es mayor a 5')
# } else if (x == 5) {
# 	print('x es igual a 5')
# } else {
# 	print('x es menor a 5')
# }

# En Python se realiza de la siguiente manera

x = 5
if x > 5:
    print('x es mayor a 5')
elif x == 5:
    print('x es igual a 5')
else:
    print('x es menor a 5')

# Se observa que el codigo es bastante similar, solamente 
# se debe tener en cuenta la indentación para definir los 
# bloques de codigo, a su vez se debe tener la precaución 
# de siempre utilizar la misma cantidad de espacios o 
# tabuladores para definir lineas de codigo en un mismo
# bloque.

# Por ejemplo al añadir un espacio adicional el codigo 
# generara un error
if x > 5:
    print('x es mayor a 5')
     y = 10 # Cuidado con la indentación

# En este caso al añadir un espacio adicional obtendremos
# un error de identación
# IndentationError: unexpected indent

# Vea como en este caso Spyder te indica la linea mal 
# indentada

# Si se desea añadir un bloque de codigo dentro de un 
# bloque de codigo se debe añadir una sangria adicional

x = 6
if x >= 5:
    print('x es mayor o igual a 5')
    if x != 5:
        print('x no es 5')


# Vease que las condiciones en Python son muy similares 
# a las de R, se utilizan los mismos operadores
#  == comparacion de igualdad, 
# != comparacion de desigualdad


# Existe otra forma compacta de realizar una condicion 
# IF-ELSE en Python, la misma se conoce como operador 
# ternario

# La estructura del mismo es: 
# <Expresion si es True> if <Condicion> else 
#                                 <Expresion si es False>

x=4
print('x es mayor a 5') if x > 5 else print('x es menor o igual a 5')

# Ejercicio: Cree una variable z que tome valor 10 si x 
# es mayor a 5 y 20 en caso contrario utilizando el 
# operador ternario

z = 10 if x > 5 else 20

# Condicionales con listas, diccionarios

# Si se desea realizar una condicion de pertenencia de 
# un elemento a una lista, tupla o diccionario
# se puede utilizar el operador in que devuelve True 
# si el elemento se encuentra en la lista y False en 
# caso contrario su funcionamiento es similar al %in% de R

lista = [5, 40, 60]

if 5 in lista:
    print('5 se encuentra en la lista')


# A su vez es posible realizar el negado de la condicion 
# con not in que devuelve True si el elemento NO se 
# encuentra en la lista y False en caso contrario

if 10 not in lista:
    print('10 no se encuentra en la lista')

# En caso de los diccionarios se puede verificar si 
# una llave se encuentra en el diccionario

diccionario = {'enteros': 5,
                'flotante': 5.0,
                'caracter': 'hola mundo'}

if 'enteros' in diccionario:
    print('La llave "enteros" se encuentra en el diccionario')

#%%
# El bucle for tiene una estructura similar a R, aunque 
# existen diferentes maneras segun el caso de uso:

# - Iterar sobre una secuencia de numeros 

# Por ejemplo si se desea realizar el siguiente bucle 
# en R

#for (x in 1:3) {
#	print(x)
#}

# En Python se puede realizar de la siguiente manera, 
# donde se usa la funcion range() para generar una 
# secuencia de numeros

for x in range(1, 4): 
    print(x)

# Es importante observar que la funcion range() el 
# argumento de fin es exclusivo, es decir no se incluye
# en la secuencia

# Ejericio: Pruebe hacer el mismo bucle pero sin ingresar 
# el argumento de inicio (range(4))



# - Iterar sobre una lista o tupla

lista = [1, 2, 3, 4]

# Para iterar sobre listas o tuplas simplemente se debe 
# definir la variable que se utilizara para iterar y la 
# lista o tupla

for elemento in lista:
    print(elemento)

# En este caso elemento toma el valor de cada elemento 
# de la lista en cada iteracion

# La compresion de listas es una forma mas compacta de 
# realizar un bucle for y muy utilizada en Python
# para crear listas de manera eficiente la estructura de 
# la compresion de listas es:
    
# [<Expresion> for <Elemento> in <Iterable>]

# Por ejemplo creemos una lista con las valores 2^0 
# hasta 2^5 

potencias = [2**x for x in range(6)]

potencias

# Tambien es posible añadir una condicion, probemos 
# crear una lista con los numeros pares de 1 a 10
# En este caso la linea se compone de un bucle for que 
# recorre todo los valores de 1 a 10 y una condicion 
# que decide si el elemento se añade a la lista creada o 
# no

pares = [x for x in range(1,11) if x % 2 == 0] 

pares

# - Iterar sobre un diccionario

diccionario = {'lista': [1,2],
                'flotante': 5.0,
                'caracter': 'z'}

# Para iterar sobre un diccionario se puede utilizar 
# el metodo items() que retorna una lista con los pares 
# llave-valor

diccionario.items()

for llave, valor in diccionario.items():
    print('Llave:', llave, '; Valor:', valor)

# - Iterar listas con enumerate() 

# En caso de que se desee iterar sobre una lista y a su 
# vez se desee obtener el indice del objeto a iterar
# la funcion enumerate() es de bastante utilidad, la misma
# retorna una tupla con el indice y el elemento de la 
# lista

for indice, elemento in enumerate(lista):
    print('Indice:', indice, 'Elemento:', elemento)

#%%
# El bucle while en Python es similar al de R, siguiendo 
# la misma estructura de identación que vimos en el bucle
# for

x = 0
while x < 5:
    print(x)
    x += 1 

# En este caso podemos destacar el uso del operador += el 
# mismo es equivalente a escribir x = x + 1

# Python cuenta con una serie de operadores que permiten
# realizar operaciones de asignación de manera mas 
# sencilla

#%%
# 6. Funciones

# Aunque Python es un lenguaje de programación orientado 
# a objetos, es posible trabajar simplemente con funciones
# como en R.

# Las funciones en Python se definen mediante la palabra 
# reservada def seguida del nombre de la funcion y los 
# argumentos que se desean pasar a la funcion entre 
# parentesis.

# En este caso se cumple las mismas reglas que en R las 
# variables definidas dentro de la funcion
# son locales a la funcion y no pueden ser accedidas 
# desde fuera de la funcion. 

# Se debe respetar nuevamente la identación para definir 
# los bloques de codigo de la funcion.

# Por ejemplo definamos una funcion que compare si dos 
# numeros son iguales

def comparar_numeros(x, y):
    if x == y:
        return print('x es igual a y')
    else:
        return print('x es distinto de y')

# Para llamar a la funcion simplemente se debe escribir 
# el nombre de la funcion seguido de los argumentos que 
# se desean pasarle similar a R

comparar_numeros(x=5, y=5)

comparar_numeros(x=5, y=10)

# Al igual que en R es posible definir argumentos por 
# defecto en las funciones 

def comparar_numeros(x, y=5):
    if x == y:
        return print('x es igual a y')
    else:
        return print('x es distinto de y')

comparar_numeros(5) 

# En R cuando no se especifica el retorno de una funcion
# se retorna el ultimo valor evaluado, probemos que 
# sucede en Python 

# Ejercicio: Cree una funcion llamada multiplicacion 
# que tome x e y como argumentos y calcule la 
# multiplicacion de ambos pero no utilice return


# Verifique que pasa al evaluar la funcion en este caso
print('Resultado de la multiplicacion:', 
      multiplicacion(x=10, y=5))


# En el ejemplo anterior puede parecer que definir una 
# funcion para una operacion tan simple como una 
# multiplicacion parece excesivo, para esto en Python 
# cuando la funcion es una expresion 
# simple es posible definir funciones de manera mas 
# compacta utilizando las llamadas funciones lambda

# La estructura de una funcion lambda es:
# lambda argumentos: expresion

# Por ejemplo realicemos la misma funcion multiplicacion 
# pero utilizando una funcion lambda

multiplicacion = lambda x, y: x * y

print('Resultado de la multiplicacion:',
      multiplicacion(10, 5))

#%%
# 7. Programacion Orientada a Objetos (POO)

# Uno de los cambios mas importantes y que cuesta mas 
# acostumbrarse por un usuario normal de R
# es el enfoque orientado a objetos de Python. 

# Aunque en R existe una forma de trabajar en base 
# POO mediante S3 o S4, se puede convivir sin la  
# necesidad de trabajar o conocer ese paradigma. 

# En Python la gran mayoria de las librerias estan 
# desarrolladas bajo este enfoque. 

# A su vez las implementaciones medianamente complejas de 
# la ciencia de datos como pueden ser algoritmos de 
# machine learning o redes neuronales muchas veces 
# se ven beneficiados de seguir una estructura orientada 
# a objetos al desarrollarlas.

# Es por eso que al trabajar en Python se debe tener claro
# conceptos como clase, instancias, atributos y metodos.

# Conceptos basicos:

# Una clase define atributos y métodos que un objeto 
# puede tener. 
# Las clases de Python actúan como plantillas para crear 
# objetos concretos llamados INSTANCIAS de esa clase.

# Una analogia muy utilizada es pensar en autos, las 
# clases serian los autos en general, 
# cuando definimos un auto a partir de una clase estamos 
# creando una INSTANCIA de la clase,
# pero a su vez cada auto que definimos puede tener 
# ciertas caracteristicas que pueden diferir 
# o no de otros autos, como por ejemplo la marca, modelo,
# color, etc. estas caracteristicas
# se denominan ATRIBUTOS de la clase, donde cada instancia
# de la clase puede tener distintos valores para los 
# atributos.
# A su vez los autos tienen distintas funcionalidades 
# como encender el motor, acelerar, frenar, etc.
# estas funcionalidades se denominan METODOS de la clase.

# Para definir una clase en Python se utiliza la palabra
# reservada class seguida del nombre de la clase, 
# por convención los nombres de las clases comienzan con
#  mayusculas y se utiliza la llamada notacion CamelCase

# Empezemos con un ejemplo simple, supongamos que se 
# desea definir una clase llamada Auto

class Auto:
    pass

# En este caso se define una clase que no tiene ninguna 
# funcionalidad, la palabra reservada 
# pass se utiliza en Python para indicar que no se desea 
# realizar ninguna accion en ese bloque de codigo.

# Para crear una instancia de la clase simplemente se 
# debe llamar a la clase, en este caso creemos
# una instancia de la clase Auto

auto = Auto()

# Ahora me interesaria no solo crear una clase vacia sino
# que me gustaria añadirle ciertos atributos, 
# por ejemplo que cada auto generado tenga un color y 
# un numero de puertas determinado.

# Para añadir atributos a una instancia se puede utilizar 
# el metodo __init__, en Python existe una clase
# de metodos llamados especiales que se utilizan para 
# realizar operaciones especiales en las clases,
# en este caso __init__ tambien conocido como constructor
# se ejecuta cada vez que se crea una instancia de la 
# clase.

# Observese los __ al inicio y al final del nombre del 
# metodo, indican que es un metodo especial, existen
# una gran cantidad de metodos especiales en Python que 
# se pueden utilizar para realizar operaciones
# especiales en las clases.

class Auto:
    def __init__(self, color, num_puertas):
        self.color = color
        self.num_puertas = num_puertas

# Observe aunque es un metodo especial, los metodos no 
# son mas que funciones que se definen dentro de una 
# clase, que tienen ciertas particularidades como el 
# argumento self.

# Las clases de Python necesitan una forma de referirse 
# a sí mismas, como forma de distinguir una instancia de 
# otra. 

# Como convencion se utiliza self como el primer argumento
# de los metodos de la clase, todos los metodos de la 
# clase que tengan self como argumento podran acceder
# a los atributos y metodos de la clase.

# Ahora añadamos un metodo que describa las 
# caracteristicas del auto, reutilizemos el metodo 
# __init__ anteriormente definido

class Auto:
    def __init__(self, color, num_puertas):
        print ("Se ha creado una instancia de la clase Auto")
        self.color = color
        self.num_puertas = num_puertas

    def descripcion(self):
        return print(f'El Auto es de color {self.color} y tiene {self.num_puertas} puertas')

# Observe que el metodo descripcion no requiere los 
# argumentos de color y num_puertas, ya que estos 
# atributos son accesibles mediante self.

# Para crear una instancia de la clase es igual que en el
# caso de la clase vacia solamente que ahora le debemos
# pasar los argumentos que requiere para contruir la 
# intancia, es decir los argumentos que requiere el 
# metodo __init__

auto_1 = Auto(color='rojo', num_puertas=4)

# En esta caso al pasarle los argumentos color='rojo' y
# num_puertas=4 se crea una instancia de la clase Auto
# la misma se almacena en la variable auto_1 y el metodo 
# __init__ le asigna los valores a los atributos 
# color y num_puertas.

# Ejercicio: Vea que muestra spyder al poner auto_1.


# Podemos verificar que los atributos se han asignado 
# correctamente

auto_1.color

auto_1.num_puertas

# En este caso el self hace referencia a la instancia 
# auto_1, con lo cual se accede al atributo color y
# numero de puertas del auto 1

# De igual forma podemos definir otra instancia de la 
# clase Auto
auto_2 = Auto(color='azul', num_puertas=2)

# Ahora que se han creado las instancias de la clase 
# apliquemos el metodo descripcion

# Para la instancia auto_1
auto_1.descripcion()

# Para la instancia auto_2
auto_2.descripcion()

#%%
# Ejercicio:
    
# Vamos a crear una clase que tome como argumento una 
# lista de numeros y calcule la media 
# y la desviacion estandar

# Completar la clase MedidasResumen en los lugares 
# indicados

class MedidasResumen:
    # Ingresa la lista como argumento del constructor
    def __init__(self, lista):
        
        # Guardemos la lista de numeros en un atributo
        self.lista = lista
        
        # Puede ser de utilidad definir un 
        # atributo que sea el largo de la lista.
        # Para ello puede usar la funcion len() que 
        # retorna la longitud de una lista
        
        self.n = # COMPLETAR

        # Adicionalemnete creemos un placeholder para la 
        # media y la desviacion estandar
        # Estos valores seran None hasta que se llame a 
        # los metodos que la calculan
        
        self.media = None
        self.sd = None

    # Crear el metodo que calcule la media
    # Para calcular la media puede utilizar la 
    # funcion sum() que suma los elementos de una lista.
    # Recuerde que los atributos pueden ser accedidos
    # desde cualquier metodo 
    
    def calcular_media(self):
        
        self.media = # COMPLETAR
        
    def calcular_sd(self):
        
        # Agregemos una condicion para calcular la media
        # si no se ha llamado al metodo calcular_media.
        # Vea que en este caso llamamos a un metodo de la
        # clase dentro de otro metodo siempre utilizando 
        # self
        if self.media is None:
            self.calcular_media()
        
        # Calculemos la desviacion estandar
        # La sigiente linea calcula la suma de los cuadrados de 
        # la diferencia entre cada elemento de la lista y la media
        suma = sum([(x - self.media)**2 for x in self.lista])
        
        # COMPLETAR LOS ... siguientes
        ... = (suma / (...-1))**0.5 


#%%
# Una vez completada probar la clase MedidasResumen
lista = [1,2,3,4,5]
medidas = MedidasResumen(lista)

# Observe que pasa si se intenta imprimir la media y 
# la desviacion estandar antes de llamar a los metodos que 
# las calculan
print(medidas.media)
print(medidas.sd)

# Ahora calculemos la media y la desviacion estandar
medidas.calcular_media()
print(medidas.media)

medidas.calcular_sd()
print(medidas.sd)





#%%
# SOLUCION

class MedidasResumen:
    def __init__(self, lista):

        self.lista = lista
        # Utilizamo len(lista) para calcular el largo
        self.n = len(lista)
        self.media = None
        self.sd = None

    def calcular_media(self):
        # Calculamos la media simplemente sumamos y dividimos por n
        self.media = sum(self.lista) / self.n
        
    def calcular_sd(self):
        
        if self.media is None:
            self.calcular_media()
        
        suma = sum([(x - self.media)**2 for x in self.lista])
        
        # Completamos 
        self.sd = (suma / (self.n-1))**0.5 

