"""
0. Introducción

En este proyecto, trabajaremos con un conjunto de datos de la serie *The Office*
con el objetivo de predecir la calificación de cada episodio 
en la plataforma IMDB (https://www.imdb.com/). Para ello, utilizaremos una 
serie de variables o predictores que están incluidos en el conjunto 
de datos y que construiremos progresivamente.

El conjunto de datos se encuentra dividido en tres archivos:

- `episodios.csv`: Incluye el nombre de cada episodio, la temporada a la que
   pertenece, y su calificación en IMDB.
- `dialogos.csv`: Contiene los diálogos de cada episodio y el personaje que 
   los pronunció, con un diálogo por línea.
- `creadores.csv`: Indica los creadores que participaron en cada episodio.
   Cada fila representa un episodio, y cada columna corresponde a un creador;
   un valor de 1 indica que el creador participó en el episodio.

Los tres conjuntos de datos comparten el campo `episode_name`.
"""

#%% 1. Pandas - Preparacion de datos.
import pandas as pd

# AGREGARÍA UNA DESCRIPCIÓN BREVE DE PANDAS Y LOS DATA FRAMES
# QUIZA EXPLICAR QUE SE APLICAN METODOS A LOS DF COMO VIMOS ANTES

# AGREGARÍA UNA INSTRUCCIÓN PARA SETTEAR EL WORKING DIR DESDE LA BARRA EN ANGULO SUP DERECHO 

#%% 1.1 Como cargar un conjunto de datos EN UN DATA FRAME. 
episodios = pd.read_csv("episodios.csv")

#%% Vemos las primeras lineas del conjunto de datos para ver la estructura 
#(Podemos usar la funcionalidad de spyder también).
print(episodios.head())

#%% 1.2 Seleccionar columnas.

### Hay columnas que no son de nuestro interés, por lo que las eliminaremos.
episodios.drop(
    columns=["total_votes", "air_date"], 
    inplace=True
) #inplace=True es igual a haber hecho episodios = episodios.drop(...)

#%% Si en vez de eliminar columnas queremos seleccionar solo algunas columnas.
# Podemos hacerlo utilizando loc o iloc. 

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
personajes = (
    dialogos
        .groupby(['episode_name', 'character']) #Agrupamos por episodio y personaje
        .size() #Cuenta la cantidad de filas
        .reset_index(name='n') #Dejamos con la estructura episode_name, character, n
)

# CREO QUE NO QUEDA CLARO LO QUE HACE EL RESET INDEX
# QUIZÁ ACA SE PUEDE EXPLICAR EL METHOD CHAINING Y COMO ES SIMILAR A HACER:

# grouped = dialogos.groupby(['episode_name', 'character']) 
# counts = grouped.size()
# personajes = counts.reset_index(name='n')

# PORQUE PUEDE CONFUNDIR UN POCO AL VERLO POR PRIMERA VEZ

#Buscamos a los personajes que hayan tenido mas de 800 lineas a lo largo de toda la serie. 
personajes_frecuentes = (
    personajes
        .groupby('character')['n']
        .sum()
        .reset_index(name='n_total')
        .query('n_total >= 800')
)['character']

#Filtramos para tener en cuenta solo estos personajes
personajes = personajes[personajes['character'].isin(personajes_frecuentes)]

#Pasamos los datos a formato wide.
personajes = (
    personajes.
        pivot_table(
            index='episode_name', 
            columns='character', #De donde tomar los nombres de las columnas
            values='n', #De donde tomar el valor que le corresponde a cada columna
            fill_value=0 #Para hacerlo completo. En caso de que el personaje no participe en el episodio asignar un 0.
        )
        .reset_index() #Recuperamos episode_name como columna.
    )

# Agregar comentario de como pasar a formato long? DIRIA QUE NO, PUEDE SER MUCHO

# Juntamos el conjunto de datos de episodios con el de personajes
episodios = pd.merge(episodios, personajes, #
                     on = "episode_name", #Que variable usamos para juntar.
                     how="inner") #Que metodo usamos para juntar, mismos que dplyr: inner, left, right. full_join de dplyr equivale a outer.

# EXPLICAR CUAL ES EL METODO POR DEFAULT
#TODO: Checkear lo de full_join y outer

#%% 1.4 Tu Turno

#Te animas a cargar el conjunto de datos con los creadores de cada episodio.
creadores = pd.read_csv("creadores.csv")

#Y a mergear el conjunto con el que ya tenemos?
episodios = pd.merge(episodios, creadores)


#%% 1.5 Terminamos con la preparacion
# DESCRIBIR QUE ESTAMOS HACIENDO ACA
episodios = episodios.set_index("episode_name")
print(episodios.describe())


#%% 2. VISUALIZACIÓN CON Matplotlib 
import matplotlib.pyplot as plt

#TODO: Comentar alternativas: plotly, la que es como ggplot, ...?

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

# AGREGARIA INFO SOBRE SCIKIT LEARN

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
    "Observado": y_test.values.flatten(),
    "Predicho": y_pred.flatten()
})

#%% 3.5 Evaluamos resultados.
from sklearn import metrics

print(metrics.mean_absolute_error(resultados.Observado, resultados.Predicho))

#%% 3.6 Tu turno!

## Te animas a reportar el RMSE? https://scikit-learn.org/1.5/api/sklearn.metrics.html
print(metrics.root_mean_squared_error(y_test, y_pred)) # ESTO DA ERROR

# metrics.mean_squared_error(y_test, y_pred, squared=False)

## Te animas a crear un grafico de observado vs predicho?
plt.scatter(data=resultados, x="Observado", y="Predicho")
plt.xlabel("Observado")
plt.ylabel("Predicho")
plt.title("Observado vs Predicho")
plt.plot([6.5,10],[6.5,10], color="black", linestyle="--")
plt.show()
# %%

# POR QUE NO AGREGAR LA LINEA DE LA REGRESSION?
import numpy as np

slope, intercept = np.polyfit(resultados.Observado, resultados.Predicho, 1)

x_vals = np.array([resultados.Observado.min(), resultados.Observado.max()])
y_vals = intercept + slope * x_vals

plt.scatter(data=resultados, x="Observado", y="Predicho")
plt.xlabel("Observado")
plt.ylabel("Predicho")
plt.title("Observado vs Predicho")
plt.plot(x_vals, y_vals, color='red', linestyle='-')
plt.show()
