# 0. Introducción

## Utilizaremos un conjunto de datos de la serie `The Office`. Cada fila del conjunto de datos es una linea de diálogo.

## Queremos predecir la calificación del episodio obtenida en la plataforma [IMDB](https://www.imdb.com/) en base a predictores que están presentes en el conjunto de datos y que iremos construyendo.

# 1. Pandas.
import pandas as pd

#%% 1.1 Como cargar un conjunto de datos.
data = pd.read_csv("theoffice.csv")

#%% Vemos las primeras lineas del conjunto de datos para ver la estructura (Podemos usar la funcionalidad de spyder también).
print(data.head())

#%% 1.2 Seleccionar columnas.

### Hay columnas que no son de nuestro interés, por lo que las eliminaremos.
data.drop(
    columns=["index", "episode", "text_w_direction", "total_votes", "air_date"], 
    inplace=True
) #inplace=True es igual a haber hecho data = data.drop(...)

### Si en vez de eliminar columnas queremos seleccionar solo algunas columnas. Podemos hacerlo utilizando loc o iloc.

#%% loc: Selecciona columnas por nombre. 
seleccion = data.loc[:, ["season", "episode_name", "director", "writer", "character", "text", "imdb_rating"]]

#%% iloc: Selecciona columnas por índice.
seleccion = data.iloc[:, [0, 1, 2, 3, 4, 5,6]]

#%% 1.3 Creacion de atributos.

""" 
Queremos crear las siguientes dos variables objetivo:
    Cantidad de lineas que tiene cada personaje en el episodio.
    Guionistas/Directores (no diferenciaremos el rol) que participan en el episodio.
"""

#%% Cantidad de lineas que tiene cada personaje en el episodio. 

#Vamos a crear un conjunto de datos con la cantida de lineas de cada personaje en un episodio
personajes = (
    data
        .groupby(['episode_name', 'character']) #Agrupamos por episodio y personaje
        .size() #Cuenta la cantidad de filas
        .reset_index(name='n') #Dejamos con la estructura episode_name, character, n
)

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
            columns='character', 
            values='n', 
            fill_value=0
        )
        .reset_index()
    )

### Q


#%% 1.4