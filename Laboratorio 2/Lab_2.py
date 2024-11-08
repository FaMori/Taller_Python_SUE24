"""
0. Introducción

En este proyecto, trabajaremos con un conjunto de datos de la serie *The Office* con el objetivo de predecir la calificación de cada episodio 
en la plataforma IMDB (https://www.imdb.com/). Para ello, utilizaremos una serie de variables o predictores que están incluidos en el conjunto 
de datos y que construiremos progresivamente.

El conjunto de datos se encuentra dividido en tres archivos:

- `episodios.csv`: Incluye el nombre de cada episodio, la temporada a la que pertenece, y su calificación en IMDB.
- `dialogos.csv`: Contiene los diálogos de cada episodio y el personaje que los pronunció, con un diálogo por línea.
- `creadores.csv`: Indica los creadores que participaron en cada episodio. Cada fila representa un episodio, y cada columna 
                   corresponde a un creador; un valor de 1 indica que el creador participó en el episodio.

Los tres conjuntos de datos comparten el campo `episode_name`.
"""

#%% 1. Pandas - Preparacion de datos.

""" 
Pandas es la biblioteca que se usa para trabajar con conjuntos de datos tabulados. Aunque en este curso no profundizaremos 
en el uso de NumPy, es importante saber que Pandas utiliza las estructuras de datos de NumPy para optimizar el almacenamiento 
y manipulación de datos en sus estructuras, como Series y DataFrames. 
Esta dependencia también hace que sea común usar funciones de ambas bibliotecas en proyectos de análisis de datos en Python.

Pandas tiene dos estructuras fundamentales (Serie y Dataframe)

Serie: Informalmente podemos pensarlo como la columna de una tabla. (n, ) donde n es el numero de filas
Dataframe: Es la tabla completa. Un dataframe esta compuesto por la combinacion de Series. 
           Tiene dimensión (n, m) donde m numero de columnas

Ambas estructuras cuentan con indices que nos permiten identificar las filas. Estos indices pueden ser numeros (0,1,2,..)
O pueden ser Texto ("Ana", "Beto", ...) o cualquier otro tipo de identificador unico.
"""""

import pandas as pd #as se usa en Python para definir un alias. En vez de escribir pandas siempre que queramos usar una funcion
                    #poderemos escribir pd (es estandar llamar pandas como pd).

#%% 1.1 Como cargar un conjunto de datos en un dataframe.

## Verificar que en el angulo superior izquierdo tenemos configurado el directorio de trabajo.
episodios = pd.read_csv("episodios.csv")

#%% Vemos las primeras lineas del conjunto de datos para ver la estructura (Podemos usar la funcionalidad de spyder también).
print(episodios.head())

#Podemos visualizar los datos con Spyder tambien!

#%% Checkeamos las clases del dataframe y de su columna
print(type(episodios))
print(type(episodios["season"])) #episodios["season"] es una forma de seleccionar una columna, veremos otras.

#%% Checkeamos las dimensiones
print(episodios.shape)
print(episodios["season"].shape)


#%% 1.2 Seleccionar columnas.

### Hay columnas que no son de nuestro interés, por lo que las eliminaremos.
episodios.drop(
    columns=["total_votes", "air_date"], 
    inplace=True
) #inplace=True es igual a haber hecho episodios = episodios.drop(...)

#%% Si en vez de eliminar columnas queremos seleccionar solo algunas columnas. Podemos hacerlo utilizando loc o iloc. 

#loc: Selecciona columnas por nombre. 
seleccion = episodios.loc[:, ["episode_name", "season", "imdb_rating"]]

#%% iloc: Selecciona columnas por índice.
seleccion = episodios.iloc[:, [0, 1, 2,]]

#%% 1.3 Creacion de atributos.

""" 
Queremos crear las siguientes dos variables objetivo:
    Cantidad de lineas que tiene cada personaje en el episodio.
    Guionistas/Directores (no diferenciaremos el rol) que participan en el episodio.
"""

#%% Cantidad de lineas que tiene cada personaje en el episodio. 

dialogos = pd.read_csv("dialogos.csv")

#Vamos a crear un conjunto de datos con la cantidad de lineas de cada personaje en un episodio
personajes = dialogos.groupby(['episode_name', 'character']) #Agrupamos por episodio y personaje
personajes = personajes.size() #Cuenta la cantidad de filas. Tenemos un objeto Series con indice ['episode_name', 'character']
personajes = personajes.reset_index(name='n') #Cuando aplicamos reset_index a un objeto Series pasamos el indice a columnas.
                                              #Por lo que la Series pasa a ser un Dataframe.
                                              #Con el argumento name, marcamos el valor que va a tener la columna con el valor
                                              #Que tenia la serie. Si no ponemos nada vamos a ver que la columna queda con el
                                              #nombre 0.

"""
Podriamos haber escrito el codigo anterior de la siguiente forma:
personajes = (
    dialogos
        .groupby(['episode_name', 'character']) #Agrupamos por episodio y personaje
        .size() #Cuenta la cantidad de filas
        .reset_index(name='n') #Dejamos con la estructura episode_name, character, n
    )

Esta tecnica de llamar metodos a medida que vamos modificando el objeto se llama 
'Encadamiento de metodos (method chaining)'
"""


#Buscamos a los personajes que hayan tenido mas de 800 lineas a lo largo de toda la serie. 
personajes_frecuentes = (
    personajes
        .groupby('character')['n'] #Agrupamos por personaje y nos quedamos solo con la columna 'n'.
        .sum() #Sumamos las cantidades de lineas de todos los episodios que tuvo el personaje.
        .reset_index(name='n_total') #Misma logica que reset
        .query('n_total >= 800') #Nos quedamos con las filas que cumplan este requisito. Es analogo al filter de dplyr.
)['character']

#Filtramos para tener en cuenta solo estos personajes
personajes = personajes[personajes['character'].isin(personajes_frecuentes)]

#Pasamos los datos a formato wide.
personajes = ( #Los parentesis nos permiten escribir en varias lineas.
    personajes.
        pivot_table(
            index='episode_name', 
            columns='character', #De donde tomar los nombres de las columnas
            values='n', #De donde tomar el valor que le corresponde a cada columna
            fill_value=0 #Para hacerlo completo. En caso de que el personaje no participe en el episodio asignar un 0.
        )
        .reset_index() #Recuperamos episode_name como columna.
    )

# Juntamos el conjunto de datos de episodios con el de personajes
episodios = pd.merge(episodios, personajes, #
                     on = "episode_name", #Que variable usamos para juntar.
                     how="inner") #Que metodo usamos para juntar, mismos que dplyr: inner, left, right. full_join de dplyr equivale a outer.
                                #Siendo inner el por defecto.
#%% 1.4 Tu Turno

#Te animas a cargar el conjunto de datos con los creadores de cada episodio.
creadores = pd.read_csv("creadores.csv")

#Y a mergear el conjunto con el que ya tenemos?
episodios = pd.merge(episodios, creadores)


#%% 1.5 Terminamos con la preparacion

#Dado que no nos interesa usar el episode_name como predictor pero si para identificar la observacion lo vamos a utilizar 
#como indice.

episodios = episodios.set_index("episode_name")

print(episodios.describe())


#%% 2. Matplotlib - Exploracion
import matplotlib.pyplot as plt


"""
Existen varias alternativas como:
    - Plotly (existe en R tambien que nos permite crear graficos interactivos.
    - Altair (https://altair-viz.github.io/) se usa para graficos complejos e interactivos tambien
    - Plotnine (!!) Tiene una sintaxis identica a ggplot y esta construido sobre matplotlib.
"""

#%%2.1 Histograma de puntajes
plt.figure(figsize=(8, 6))
plt.hist(data = episodios, #Marcamos el conjunto de datos que queremos usar.
         x = "imdb_rating", #Marcamos la variable que queremos graficar.
         density=1, #Area = 1.
         bins=20 #Cantidad de bins (todos del mismo tamaño).
        )
plt.xlabel("Puntaje IMDB") #Agregamos etiqueta al eje x.
plt.ylabel("Densidad") #Agregamos etiqueta al eje y.
plt.title("Distribución de puntajes") #Agregamos titulo al gráfico.
plt.show() #Mostramos el gráfico.

#%%2.2 Boxplot por temporada

# Vamos a usar Seaborn, que nos permite la construcción de gráficos más complejos.
# Seaborn está construido sobre Matplotlib, lo que nos permite combinarlos de manera natural.
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(data = episodios, x = "season", y = "imdb_rating") #Aqui es que usamos seaborn, como vemos es muy similar a Matplotlib.
plt.xlabel("Temporada")
plt.ylabel("Puntaje IMDB")
plt.title("Distribución de puntajes por temporada")
plt.savefig("boxplot.png") #Exportamos el gráfico como un png.

#%% 3. Scikit Learn - Modelos lineales
from sklearn import model_selection, linear_model

"""
Scikit-Learn es una biblioteca de Python que permite entrenar modelos de aprendizaje supervisado y no supervisado.
Además, ofrece un conjunto de herramientas para preprocesar datos, ajustar hiperparámetros y evaluar el rendimiento de los modelos.

A diferencia de R, Scikit-Learn reúne una gran variedad de modelos y funcionalidades 
relacionadas con el modelado en una única biblioteca!

Scikit-Learn es un excelente ejemplo de una buena aplicación de la Programación Orientada a Objetos. 
Dado el amplio número de modelos y herramientas, así como la colaboración de múltiples desarrolladores, 
fue esencial seguir un diseño uniforme. 
Por eso, todas las clases de modelos en Scikit-Learn implementan métodos estándar como fit para entrenar 
modelos y predict para realizar predicciones, garantizando una experiencia de usuario consistente. [https://arxiv.org/abs/1309.0238]

Cuenta con documentacion oficial muy completa: https://scikit-learn.org/stable/user_guide.html
"""

#%% 3.1 Separamos los predictores y la variable a predecir
X = episodios.drop(columns = ["imdb_rating"])
y = episodios.imdb_rating #Otra forma de seleccionar columnas

#%% 3.2 Dividimos los datos en entrenamiento/test
X_train, X_test, y_train, y_test  = model_selection.train_test_split(X, y, 
                     test_size=0.2, #80% entrenamiento, 20% test.
                     random_state = 1234 #Fijamos la semilla.
                     )     


#%% 3.3 Ajustamos el modelo con los datos de entrenamiento.
lm = linear_model.LinearRegression()
lm.fit(X_train,y_train)

#%% 3.4 Realizamos la prediccion con el conjunto de test.
y_pred = lm.predict(X_test)

#Queremos crear un dataframe con los resultados de la prediccion.
resultados = pd.DataFrame({ 
    "Observado": y_test,
    "Predicho": y_pred
})

#%% 3.5 Evaluamos resultados.
from sklearn import metrics

print(metrics.mean_absolute_error(resultados["Observado"], resultados["Predicho"]))

#%% 3.6 Tu turno!

## Te animas a reportar el RMSE? https://scikit-learn.org/1.5/api/sklearn.metrics.html
print(metrics.root_mean_squared_error(resultados["Observado"], resultados["Predicho"]))

## Te animas a crear un grafico de observado vs predicho?
plt.scatter(data=resultados, x="Observado", y="Predicho")
plt.xlabel("Observado")
plt.ylabel("Predicho")
plt.title("Observado vs Predicho")
plt.plot([6.5,10],[6.5,10], color="black", linestyle="--")
plt.show()
# %%
