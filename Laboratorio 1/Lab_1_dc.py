"""
SUE 2024
Laboratorio 1: Fundamentos de Python para usuarios de R.
"""
#%%
# 1 Asignación de variables y objetos mas simples en Python

# En Python el operador de asignación , denotado por el símbolo "=", es el operador que se utiliza 
# para asignar valores a las variables.

# Veamos un ejemplo simple asignemos el valor entero 5 a la variable x
x = 5
# El comportamiento de esta asignación es similar al de R (x <- 5), se toma el valor conocido, 5, 
# y asigna ese valor a la variable con el nombre "x". 

# Después de ejecutar esta línea, este número se almacenará en esta variable. Hasta que se cambie el valor
# o se elimine la variable, el carácter x se comporta como el valor 5. 

# Mas adelante veremos que en realidad la asignacion en Python tiene ciertas diferencias a la de R, 
# pero en este caso simple podria decirse que es similar.

# La funcion print() como en R permite imprimir el valor de una variable en la consola

print(x)

#%%
# Al igual que R los objetos mas simples en Python son los enteros, flotantes, booleanos y caracteres

# Enteros (int)
x = 5

# Flotantes (float)
y = 5.0

# Booleanos (bool)
w = False 

# A diferencia de R en Python los booleanos se escriben solamente con la primera letra en mayuscula True, False

# Caracteres (str)
z = 'hola mundo' # Como en R se pueden definir mediante comillas simples o dobles
 
# Python es un lenguaje de programación orientado a objetos, lo que significa que todo en Python es un objeto,
# funciones, numeros enteros, cadenas, etc.

# Cada objeto en Python tiene un identificador único, un tipo y un valor.

# El identificador de un objeto es un número entero que lo identifica de manera única en la memoria 
# La funcion id() permite obtener este identificador para cada objeto
print('Identificador de x:', id(z))

# El tipo de un objeto indica a que clase pertenece, por ejemplo si es un numero entero, una función, booleano, etc.
# La funcion type() permite obtener el tipo de un objeto

print('Tipo de objeto x:', type(z)) 

# Por otro lado el valor de un objeto son las caracteristicas particulares que posee
# Por ejemplo si es una cadena de caracteres, el valor de la cadena de caracteres es el texto que contiene

print('Valor de z:', z)

#%%
# Una caracteristica de los objetos son los metodos, los metodos son funciones que se pueden 
# aplicar a un objeto, la forma de llamar a un metodo es mediante la siguiente sintaxis

# objeto.metodo(argumentos)

# Por ejemplo para los strings existe el metodo llamado upper() que convierte
# todos los caracteres de la cadena en mayusculas, en este caso no se requiere pasar argumentos al metodo
# con lo cual solamente se escribe de la siguiente manera

print('Cadena en mayusculas:', z.upper())

# Los metodos y objetos son una parte fundamental de Python como lenguaje orientado a objetos 
# que lo diferencian de lenguajes funcionales como R, se vera en este laboratorio y el siguiente 
# muchos ejemplos de metodos y objetos en Python.

# Puede verse mas informacion sobre distintos metodos para objetos de tipo caracter en el siguiente enlace
# https://docs.python.org/3/library/stdtypes.html#string-methods

#%%
# Hasta ahora se han visto los tipos de datos mas simples que permiten asignar un elemento a una variable,
# pero Python al igual que R cuenta con estructuras de datos mas complejas que permiten almacenar multiples 
# elementos

# Listas (list)

# Las listas en Python son estructuras de datos 
# que permiten almacenar multiples objetos de cualquier tipo en su interior (hasta listas dentro de listas)

# La manera mas usual para definirla es mediante los caracteres [] donde se separan los elementos por comas

lista = [5, 5.0, 'hola mundo', 12]

# Al igual que en R es posible acceder a los elementos de la lista mediante su indice aunque presenta
# ciertas diferencias.

# Si se quiere acceder al primer elemento de la lista se utiliza el siguiente indice

print('Primer elemento de la lista:', lista[0]) 
# Observece que los indices en Python comienzan en 0 en lugar de 1 como en R.

#%%
# Adicionalemente en Python es posible acceder a elementos recorriendo la lista de manera inversa.
# Para acceder de manera inversa a los elementos de la lista se utilizan los indices negativos.
# Para acceder al ultimo elemento de la lista se utiliza el indice -1

print('Ultimo elemento de la lista:', lista[-1])

# Para acceder al penultimo elemento de la lista se utiliza el indice -2 y asi sucesivamente

#%%
# Si se desea acceder a un rango de elementos de la lista se utiliza el slicing :, el mismo es bastante
# similar al lo que tenemos en R

print('Primeros 3 elementos de la lista:', lista[0:3]) 
# Se accede a los elementos desde el indice 0 hasta el indice 3 (sin incluirlo)

#%%
# Es posible omitir el primer caracter para indicar que se desea acceder desde el inicio de la lista

print('Primeros 3 elementos de la lista:', lista[:3])

# A su vez es posible acceder a los elementos de la lista de manera inversa tambien utilizando el slicing

#%%
print('Ultimos 3 elementos de la lista:', lista[-3:])

# En python existen dos tipos de objetos, los objetos MUTABLES y los objetos INMUTABLES, la diferencia
# principal entre ambos es que los objetos inmutables NO pueden ser modificados una vez que han sido creados
# mientras que los objetos mutables si pueden ser modificados.
#%%
# Las listas son objetos MUTABLES, lo que significa que una vez que se ha creado una lista es posible 
# modificar los elementos de la misma, por ejemplo si se desea modificar el primer elemento de la lista

print('Lista original:', lista)
lista[0] = 10
print('Lista modificada:', lista)
#%%
# Al igual que otros objetos, las listas cuentan con una serie de metodos que permiten realizar ciertas operaciones

# Una practica muy comun en Python es añadir elementos a una lista ya creada,
# En este caso se puede utilizar el metodo append() que permite añadir un elemento al final de la lista

# Por ejemplo agregemos una nueva lista con dos enteros al final de la lista, recordando que los metodos
# se llaman mediante la siguiente sintaxis nombre_objeto.metodo(argumentos)

lista.append([5,10]) 

# En este caso el metodo append() requiere como argumento el objeto que se desea agregar a la lista

print('Lista con el nuevo elemento:', lista)

#%%
# TUPLAS (tuple):

# Las tuplas son objetos similares a las listas, pero su mayor diferencia es que son INMUTABLES,
# como se menciono los objetos inmutables NO pueden ser modificados una vez que han sido creados.
# Para definir una tupla se utilizan los caracteres () donde al igual que las listas se separan los elementos por comas

tupla = (5, 5.0, 'hola mundo', False)
print(id(tupla))

# Tambien es posible definir una tupla sin los parentesis, solamente separando los elementos por comas

tupla = 5, 5.0, 'hola mundo', False, "nuevo elemento" # DC
print(id(tupla))

# En este caso no estamos modificando el objeto, sino creando uno nuevo (con distinto id) # DC

# Al igual que las listas es posible acceder a los elementos mediante su indice, siguiendo la misma logica

print('Primer elemento de la tupla:', tupla[0])

print('Ultimos 2 elementos de la tupla:', tupla[-2:])

#%%
# A su vez una practica usual es desempaquetar los elementos de una tupla de la siguiente forma

entero, flotante, caracter, booleano = tupla

print('Entero:', entero)
print('Flotante:', flotante)
# Se debe tener en cuenta que el numero de variables definidas en la izquierda coincida con el numero de
# elementos en la tupla, en caso contrario se generara un error


#%%
# Diccionarios (dict)

# Los diccionarios son estructuras de datos mutables que contienen pares de llave(key)-valor(value), 
# donde cada llave es única y esta asociada a un valor en particular, al igual que las listas o tuplas
# los valores pueden ser de cualquier tipo incluso listas, tuplas, diccionarios, etc.

# Para definir un diccionario se utilizan los caracteres {} y se debe utilizar
# la siguiente sintaxis 'llave': valor separados por comas

diccionario = {'enteros': 5,
                'flotante': 5.0,
                'caracter': 'hola mundo'}

# Al igual que las listas y las tuplas es posible acceder a los valores del diccionario, en este caso
# se le indica al diccionario la llave del valor que se desea obtener

print('Valor de la llave enteros:', diccionario['enteros'])

#%%
# Como objeto mutable que es, es posible modificar los valores del diccionario, por ejemplo el metodo update()
# permite modificar el valor de una llave en particular o agregar una nueva llave-valor al diccionario

diccionario.update({'flotante': 2.4, 'booleano': False, 'lista': [5, 5.0]})

print('Diccionario modificado:', diccionario)

#%%
# Conjuntos (set):

# Los conjuntos son estructuras de datos similares a las listas pero con ciertas diferencias,
# la diferencia principal es que los conjuntos no contienen elementos repetidos y 
# no tienen un orden definido como las listas o tuplas.

# Para definir un conjunto se utilizan los caracteres {} y los elementos separados por comas
# A diferencia de los diccionarios los conjuntos no contienen pares de llave-valor, solamente elementos

# Si se intenta definir un conjunto con elementos repetidos, el conjunto solamente contendra un elemento de cada tipo
conjunto = {5, 10.2, 5, 10.2}

print('Conjunto:', conjunto)

#%%
# En el conjunto solamente se pueden definir elementos inmutables, como enteros, flotantes, cadenas de caracteres, tuplas
# No se pueden definir elementos como listas, diccionarios, conjuntos
# Si se intenta definir un conjunto con elementos mutables se generara un error de tipo TypeError

conjunto = {5, 5.0, 'hola mundo', False, [5, 5.0]} 

# TypeError: unhashable type: 'list'

#%%
# En los conjuntos al no existir un orden definido, NO es posible acceder a los elementos mediante su indice

conjunto[1]
# TypeError: 'set' object is not subscriptable

#%%
# Diferencias de asignación entre R y Python

# Aunque la asignación de una variable simple como x = 5 es similar en Python y R, existen ciertas diferencias
# sobre todo cuando se trabaja con objetos mas complejos como listas que llevan a errores muy comunes.

# Uno de los errores mas comunes de usuarios de R al comenzar a trabajar con Python es la asignación de objetos
# y la creación de copias de objetos.

# La asignación en Python NO CREA COPIAS de objetos, solamente crea referencias en memoria
# a los objetos originales.
# Por lo que si se realiza una asignación de una variable a otra, ambas variables apuntaran al mismo objeto.

# El tipico error cometido:

# Supongamos que se tiene una lista y se desea crear una copia de la misma, en R es posible realizar la siguiente
# asignación lista_copia <- lista, en este caso si se modificara la lista_copia como funciona internamente R
# no se veria afectada la lista original. En Python esto no es asi y si se modifica la lista_copia tambien 
# afectaremos a la lista original.

lista = [1,2,3]

lista_copia = lista 

# Si visualizamos el id de ambos objetos se observa que son iguales
print('Id lista original: ', id(lista), 'Id lista copia: ', id(lista_copia))
#%%
# El operador 'is' permite verificar si dos variables comparten la misma referencia en memoria

print(lista_copia is lista) 
#%%
# En este caso lista_copia es solamente una referencia a la lista original 
# con lo cual como se menciono si se modifica la lista_copia tambien se modificara la lista original

print("Lista Original:", lista)

# Realizemos una modificación en la lista_copia, modificando su primer elemento
lista_copia[0] = 15 

# Ahora volvamos a imprimir la lista original

print("Lista Original Modificando la Copia:", lista)
# Se observa que la modificación realizada en la lista_copia afecta a la lista original y viceversa, con 
# lo que se debe tener mucha precaución al realizar asignaciones a otros objetos en Python.

#%%

# Debido a esto en Python es necesario entender como se crean copias de objetos, existiendo dos tipos de 
# copias, las copias superficiales y las copias profundas.

# Una copia superficial implica construir un nuevo objeto y luego rellenarlo con referencias 
# a los objetos secundarios que se encuentran en el objeto original. Por ejemplo si se crea una 
# copia superficial de una lista, se creara una nueva lista pero que sus elementos internos tendran las mismas
# referencias a los objetos que contiene la lista original.

# Esto se puede ver mas facilmente con un ejemplo:

# Supongamos que se tenemos una lista que contiene dos conjuntos:
lista = [{1,3},{2,5}]

# Si se desea realizar una copia superficial de la lista se puede utilizar el metodo copy()
# El metodo copy() retorna una copia superficial de objetos listas, diccionarios, conjuntos, etc.

lista_copia_sup = lista.copy()

# Si visualizamos ahora mediante el is obtenemos un False 
lista_copia_sup is lista
#%%
# Las listas son distintas, pero que pasa con los objetos internos de la listas?
# Por ejemplo realizemos el is para el primer elemento de las listas

lista_copia_sup[0] is lista[0]
# Se retorna True, lo que implica que los objetos internos de la lista copia superficial son los mismos
#%%
# Esto tiene las siguientes implicancias:
# Si por ejemplo se agrega un nuevo elemento a la lista copia

lista_copia_sup.append({4,5})

# Se observa que el nuevo elemento se agrega a la lista copia pero NO a la lista original

print('Lista Original:', lista)
print('Lista Copia Superficial:', lista_copia_sup)
#%%
# Pero que pasa si se modifica un conjunto interno de la lista copia superficial

lista_copia_sup[0].add(5)

print('Lista Original:', lista)
print('Lista Copia Superficial:', lista_copia_sup)
#%%
# Se observa que la modificación realizada en el conjunto interno de la copia superficial
# afecta a la lista original

# Ahora volvamos a definir la lista y veamos que sucede si se realiza una copia profunda

lista = [{1,3},{2,5}]

# La copia profunda implica crear un nuevo objeto y rellenarlo con copias de los objetos secundarios
# Para realizar una copia profunda de un objeto en Python se puede utilizar el modulo copy y 
# la funcion deepcopy(),
# Los modulos en Python se pueden considerar como librerias que contienen funciones y objetos
# que se pueden utilizar
# en un script de Python, en este caso el modulo copy viene incluido en la libreria estandar de 
# Python pero debe ser importado para poder utilizarlo. 
# En este caso el modulo copy contiene la funcion deepcopy() que permite realizar copias profundas

# Para importar un modulo en Python se utiliza la palabra reservada import seguida del nombre del modulo

import copy

# Una vez importado un modulo es posible utilizar una funcion  del mismo utilizando la siguiente sintaxis

# nombre_modulo.nombre_funcion(argumentos)

# Por ejemplo para utilizar la funcion deepcopy() 

lista_copia_prof = copy.deepcopy(lista)
#%%
# A su vez es posible no importar el modulo completo y solamente importar la funcion que se desea utilizar
# En ese caso se utiliza el from seguido del nombre del modulo + import seguido de la funcion

from copy import deepcopy

# En caso de importa solamente la funcion deepcopy() del modulo copy, se debe llamar a la funcion directamente
# sin especificar el nombre del modulo

lista_copia_prof = deepcopy(lista)
#%%
# Ahora que se comprende como importar funciones de modulos veamos que sucede al realizar la copia profunda

# En este caso si realiza el is se observa que los objetos internos de la lista copia profunda son distintos

lista_copia_prof[0] is lista[0]

#%%
# Lo que implica que si se modifica un objeto interno de la lista copia profunda no afectara a la lista original

lista_copia_prof[0].add(5)

print('Lista Original:', lista)
print('Lista Copia Profunda:', lista_copia_prof)

# Mas informacion sobre el modulo copy y la funcion deepcopy() se puede encontrar en el siguiente enlace:
# https://docs.python.org/3/library/copy.html

#%%

# Las estructuras de control en Python son similares a las de R,
# solo se debe tener en cuenta la sintaxis distinta de Python
# A diferencia de R donde se utilizan llaves {} para definir bloques de codigo,
# en Python se utiliza la indentación
# para definir los bloques de codigo, la misma se realiza mediante añadir 
# sangrias usualmente 4 espacios o un tabulador

# Por ejemplo si se desea realizar la condicion IF-ELSE de R
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

# Se observa que el codigo es bastante similar, solamente se debe tener en cuenta la indentación
# para definir los bloques de codigo, a su vez se debe tener la precaución de siempre utilizar 
# la misma cantidad de espacios o tabuladores para definir lineas de codigo en un mismo bloque.
#%%
# Por ejemplo si se observa el siguiente codigo al añadir un espacio adicional el codigo generara un error
if x > 5:
    print('x es mayor a 5')
     y = 10 # Cuidado con la indentación

# En este caso al añadir un espacio adicional obtendremos un error de identación
# IndentationError: unexpected indent

#%%
# Si se desea añadir un bloque de codigo dentro de un bloque de codigo se debe añadir una sangria adicional

x = 6
if x >= 5:
    print('x es mayor o igual a 5')
    if x != 5:
        print('x no es 5')


# Vease que las condiciones en Python son muy similares a las de R, se utilizan los mismos operadores
#  == comparacion de igualdad, != comparacion de desigualdad...
#%%
# Condicionales con listas, diccionarios

# Si se desea realizar una condicion de pertenencia de un elemento a una lista, tupla o diccionario
# se puede utilizar el "in" que devuelve True si el elemento se encuentra en la lista y False en caso contrario
# Su funcionamiento es similar al %in% de R

lista = [5, 40, 60]

if 5 in lista:
    print('5 se encuentra en la lista')

#%%
# A su vez es posible realizar el negado de la condicion con not in que devuelve True si el elemento NO se encuentra
# en la lista y False en caso contrario

if 10 not in lista:
    print('10 no se encuentra en la lista')

#%%
# En caso de los diccionarios se puede verificar si una llave se encuentra en el diccionario

diccionario = {'enteros': 5,
                'flotante': 5.0,
                'caracter': 'hola mundo'}

if 'enteros' in diccionario:
    print('La llave "enteros" se encuentra en el diccionario')
#%%

# FOR

# El bucle for tiene una estructura similar, aunque existen diferentes maneras segun el caso de uso:

# 1. Iterar sobre una secuencia de numeros 
# Por ejemplo si se desea realizar el siguiente bucle en R
#for (x in 1:10) {
#	print(x)
#}

# En Python se puede realizar de la siguiente manera, donde se usa la funcion range() para generar 
# una secuencia de numeros
for x in range(1, 11): 
    print(x)

# Es importante observar que la funcion range() el argumento de fin es exclusivo, 
# es decir no se incluye en la secuencia
# Si no se ingresa un argumento de inicio como por ejemplo range(11) el for comenzara en 0 y terminara en 10

#%%
# 2. Iterar sobre una lista o tupla

lista = [1, 2, 3, 4]

# Para iterar sobre listas o tuplas simplemente se debe definir la variable que se utilizara para iterar y la lista o tupla
for elemento in lista:
    print(elemento)

#%%
# 3. Iterar sobre un diccionario

diccionario = {'lista': [1,2],
                'flotante': 5.0,
                'caracter': 'z'}

# Para iterar sobre un diccionario se puede utilizar el metodo items() 
# que retorna una lista de tuplas con los pares llave-valor

print(diccionario.items())

for llave, valor in diccionario.items():
    print('Llave:', llave, '; Valor:', valor)

# Observese que en este caso el metodo items() retorna una lista de tuplas con los pares llave-valor
#%%

# 4. Iterar listas con enumerate() 

# En caso de que se desee iterar sobre una lista y a su vez se desee obtener el indice de la lista la funcion enumerate() es util
# La funcion enumerate() retorna una tupla con el indice y el elemento de la lista
for indice, elemento in enumerate(lista):
    print('Indice:', indice, 'Elemento:', elemento)

#%%

# WHILE

# El bucle while en Python es similar al de R, siguiendo la misma estructura de identación que vimos 
# en el bucle for

x = 0
while x < 5:
    print(x)
    x += 1 

# En este caso podemos destacar el uso del operador += el mismo es equivalente a escribir x = x + 1
# Python cuenta con una serie de operadores que permiten realizar operaciones de asignación de manera mas sencilla
# Entre los se encuentran los operadores -=, *=, /=, etc. que ahorran escribir toda la expresion.
#%%
# FUNCIONES

# Aunque Python es un lenguaje de programación orientado a objetos,
# es posible trabajar simplemente con funciones como en R
# Las funciones en Python se definen mediante la palabra reservada def seguida
# del nombre de la funcion y los argumentos que se desean pasar a la funcion.
# En este caso se cumple las mismas reglas que en R las variables definidas dentro de la funcion
# son locales a la funcion y no pueden ser accedidas desde fuera de la funcion. Se debe 
# respetar nuevamente la identación para definir los bloques de codigo de la funcion.

# Por ejemplo definamos una funcion que compare si dos numeros son iguales
def comparar_numeros(x, y):
    if x == y:
        return 'x es igual a y'
    else:
        return 'x es distinto de y'

# Para llamar a la funcion simplemente se debe escribir el nombre de la funcion
# seguido de los argumentos que se desean pasar

print(comparar_numeros(x=5, y=5))

print(comparar_numeros(x=5, y=10))

#%%
# Al igual que en R es posible definir argumentos por defecto en las funciones 

def comparar_numeros(x, y=5):
    if x == y:
        return 'x es igual a y'
    else:
        return 'x es distinto de y'

print(comparar_numeros(5)) # Se pasa un solo argumento, el segundo argumento toma el valor por defecto

#%%
# Una diferencia destacable entre las funciones de R y Python es el retorno de las funciones.
# En R si no se especifica un valor de retorno la funcion retornara el ultimo valor calculado, 
# en Python si no se especifica un valor de retorno la funcion 
# retornara None que es un objeto especial que representa la ausencia de un valor,
# Con lo cual es importante tener en cuenta retornar un valor en todas las funciones.

def multiplicacion(x, y):
    x * y

print(multiplicacion(5, 5)) # Se retorna None

#%%
def multiplicacion(x, y):
    return x * y

print(multiplicacion(5, 5)) # Se retorna el valor de la multiplicacion

#%%

# Uno de los cambios mas importantes y que cuesta mas acostumbrarse por un usuario normal de R
# es el enfoque orientado a objetos de Python. La implementaciones medianamente complejas de la 
# ciencia de datos como pueden ser algoritmos de machine learning o redes neuronales muchas veces 
# se ven beneficiados de seguir una estructura orientada a objetos. 
# Por lo que en la gran mayoria implementaciones que se encuentran van a tener dentro
# conceptos como clases, objetos, atributos, metodos, etc.

# CLASES

# Una clase define atributos y métodos que un objeto puede tener. 
# Las clases de Python actúan como plantillas para crear objetos concretos llamados instancias de esa clase.

# Una analogia muy utilizada es pensar en autos, las clases serian los autos en general, 
# cuando definimos un auto apartir de una clase estamos creando una INSTANCIA de la clase,
# pero a su vez cada auto que definimos puede tener ciertas caracteristicas que pueden diferir 
# o no de otros autos, como por ejemplo la marca, modelo, color, etc. estas caracteristicas
# se denominan ATRIBUTOS de la clase, donde cada instancia de la clase puede
# tener distintos valores para los atributos.
# A su vez los autos tienen distintas funcionalidades como encender el motor, acelerar, frenar, etc.
# estas funcionalidades se denominan METODOS de la clase.

# Para definir una clase en Python se utiliza la palabra reservada class seguida del
# nombre de la clase, por convención los nombres de las clases comienzan con mayusculas 
# y se utiliza la llamada notacion CamelCase

# Empezemos con un ejemplo simple, supongamos que se desea definir una clase llamada Auto

class Auto:
    pass

# En este caso se define una clase que no tiene ninguna funcionalidad, la palabra reservada 
# pass se utiliza en Python para indicar que no se desea realizar ninguna accion en ese bloque de codigo.

# Para crear una instancia de la clase simplemente se debe llamar a la clase

auto = Auto()

# Ahora me interesaria no solo crear una clase vacia sino que me gustaria añadirle ciertos atributos, 
# por ejemplo que cada auto generado tenga un color y un numero de puertas determinado.

# Para añadir atributos a una instancia se puede utilizar el metodo __init__, en Python existe una clase
# de metodos llamados especiales que se utilizan para realizar operaciones especiales en las clases,
# en este caso __init__ se ejecuta cada vez que se crea una instancia de la clase.
# Observese los __ al inicio y al final del nombre del metodo, indican que es un metodo especial, existen
# una gran cantidad de metodos especiales en Python que se pueden utilizar para realizar operaciones
# especiales en las clases.

class Auto:
    # Metodo __init__ que se ejecuta cada vez que se crea una instancia de la clase
    def __init__(self, color, num_puertas):
        self.color = color
        self.num_puertas = num_puertas

# Observe que los metodos no son mas que funciones que se definen dentro de una clase, que tienen ciertas
# particularidades como el argumento self.
# Las clases de Python necesitan una forma de referirse a sí mismas,
# como forma de distinguir una instancia de otra. 
# Por ejemplo si defino una instancia de auto con color rojo y otra con color azul,
# necesito una forma de distinguir entre ambas instancias ahi es donde entra en juego el argumento self.
# Como convencion se utiliza self como el primer argumento de los metodos de la clase, 
# todos los metodos de la clase que tengan self como argumento podran acceder a los 
# atributos y metodos de la clase.

# Ahora añadamos un metodo que describa las caracteristicas del auto, reutilizemos el metodo __init__
# anteriormente definido
#%%
class Auto:
    def __init__(self, color, num_puertas):
        self.color = color
        self.num_puertas = num_puertas

    # Metodo que describe las caracteristicas del auto
    def descripcion(self):
        return f'El Auto es de color {self.color} y tiene {self.num_puertas} puertas'

# Observe que el metodo descripcion no requiere los argumentos de color y num_puertas, ya que estos atributos
# son accesibles mediante self.

# Para crear una instancia de la clase simplemente se debe llamar a la clase, pasando los argumentos
# que requiere el metodo __init__

auto_1 = Auto(color='rojo', num_puertas=4)

# En esta caso al pasarle los argumentos color='rojo' y num_puertas=4 se crea una instancia de la clase Auto
# la misma se almacena en la variable auto_1 y el metodo __init__ le asigna 
# los atributos color y num_puertas a la instancia.

# Podemos verificar que los atributos se han asignado correctamente
print(auto_1.color)

# En este caso el self hace referencia a la instancia auto_1, 
# con lo cual se accede al atributo color del auto_1

#%%
# De igual forma podemos definir otra instancia de la clase Auto
auto_2 = Auto(color='azul', num_puertas=2)

# Ahora que se han creado las instancias de la clase apliquemos el metodo descripcion

print(auto_1.descripcion())
print(auto_2.descripcion())


#%%
# Ejercicio:
# Crear una clase que tome como argumento una lista de numeros y
# calcule la media y la desviacion estandar

# Completar la clase MedidasResumen en los lugares indicados

class MedidasResumen:
    def __init__(self, lista):
        # Guardemos la lista de numeros en un atributo
        self.lista = lista
        # Puede ser de utilidad guardarnos tambien la longitud de la lista
        # Para ello puede usar la funcion len() que retorna la longitud de una lista
        self.n = # COMPLETAR

        # Adicionalemnete creemos un placeholder para la media y la desviacion estandar
        # Estos valores seran None hasta que se llame a los metodos que la calculan
        self.media = None
        self.sd = None

    # Crear el metodo que calcule la media
    # Para calcular la media puede utilizar la funcion sum() que suma los elementos de una lista
    def calcular_media(self):
        
        self.media = # COMPLETAR
        
    def calcular_sd(self):
        
        # Agregemos un condicional para calcular la media si no se ha llamado al metodo calcular_media
        # Vea que en este caso llamamos a un metodo de la clase dentro de otro metodo siempre utilizando self
        if self.media is None:
            self.calcular_media()
        
        # Calculemos la desviacion estandar
        # La sigiente linea calcula la suma de los cuadrados de la diferencia entre cada elemento de la lista y la media
        suma = sum([(x - self.media)**2 for x in self.lista])

        .... = (suma / (....-1))**0.5 # COMPLETAR LOS ....


#%%
# Una vez completada probemos la clase MedidasResumen
medidas = MedidasResumen([1,2,3,4,5])

# Observe que pasa si se intenta imprimir la media y la desviacion estandar antes de llamar a los metodos que las calculan
print(medidas.media)
print(medidas.sd)

#%%
# Ahora calculemos la media y la desviacion estandar
medidas.calcular_media()
print(medidas.media)

medidas.calcular_sd()
print(medidas.sd)


#%%
# SOLUCION

# Ejercicio Crearemos una clase que tome como argumento una lista de numeros y
# calcule la media y la desviacion estandar

class MedidasResumen:
    def __init__(self, lista):
        # Guardemos la lista de numeros en un atributo
        self.lista = lista
        # Puede ser de utilidad guardarnos la longitud de la lista
        # Para ello puede usar la funcion len(lista) que retorna la longitud de una lista
        self.n = len(lista)

        # Creemos un placeholder para la media y la desviacion estandar
        # Estos valores seran None hasta que se llame a los metodos que la calculan
        self.media = None
        self.sd = None

    # Crear el metodo que calcule la media
    # Para calcular la media puede utilizar la funcion sum() que suma los elementos de una lista
    def calcular_media(self):
        
        self.media = sum(self.lista) / self.n
        
    def calcular_sd(self):
        
        # Agregemos un condicional para calcular la media si no se ha llamado al metodo calcular_media
        # Vea que en este caso llamamos a un metodo de la clase dentro de otro metodo siempre utilizando self
        if self.media is None:
            self.calcular_media()
        
        media = self.media

        # Calculemos la desviacion estandar
        suma = sum([(x - media)**2 for x in self.lista])

        self.sd = (suma / (self.n-1))**0.5 


#%%
# Probemos la clase MedidasResumen
medidas = MedidasResumen([1,2,3,4,5])

# Observe que pasa si se intenta imprimir la media y la desviacion estandar antes de calcularlas
print(medidas.media)
print(medidas.sd)

#%%
# Ahora calculemos la media y la desviacion estandar
medidas.calcular_media()
print(medidas.media)

medidas.calcular_sd()
print(medidas.sd)