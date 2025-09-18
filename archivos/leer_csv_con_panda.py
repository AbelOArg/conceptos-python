import pandas as pd

#leemos el archivo csv y lo guardamos en un dataframe
df = pd.read_csv('archivos\\archivo_texto.csv')
df2 = pd.read_csv('archivos\\archivo_texto.csv')

#de esta manera accedemos a la columna 'nombre'
nombres = df['nombre']

#podemos ordenar el dataframe por una columna
df_ordenado = df.sort_values(by='edad')
#podemos ordenar de manera descendente colocando el parametro ascending en False
df_ordenado = df.sort_values(by='edad', ascending=False)

#podemos concatenar dataframes
df_concatenado = pd.concat([df, df2])

#con head() mostramos las primeras filas del dataframe
print(df_concatenado.head(3))

#con tail() mostramos las ultimas filas del dataframe
print(df_concatenado.tail(1))

#con shape mostramos la cantidad de filas y columnas del dataframe
print(df_concatenado.shape)

#con describe() mostramos un resumen estadistico del dataframe
print(df_concatenado.describe())

#se puede acceder a un elemento especifico del dataframe con iloc
print(df_concatenado.iloc[0, 1]) #primera fila, segunda columna

#se puede acceder a todos los elementos de una fila especifica
print(df_concatenado.iloc[0]) #primera fila

#se puede acceder a alguna fila con una condicion
print(df_concatenado[df_concatenado['edad'] > 30])

#se pueden convertir los tipos de datos de una columna
df_concatenado['edad'] = df_concatenado['edad'].astype(str) #convierte la columna edad a string

#se puede reemplazar valores en una columna
df_concatenado['nombre'] = df_concatenado['nombre'].replace('Abel', 'Pedro')
#si usamos inplace=True, se modifica el dataframe original sin la necesidad de reasignarlo
#df_concatenado['nombre'].replace('Pedro', 'Abel', inplace=True)

#se pueden eliminar filas con datos vacios
df_concatenado.dropna(inplace=True)
#si queremos eliminar columnas, usamos axis=1
df_concatenado.dropna(axis=1, inplace=True)

#podemos eliminar filas duplicadas
df_concatenado.drop_duplicates(inplace=True)

#podemos crear un nuevo archivo csv a partir del dataframe
df_concatenado.to_csv('archivos\\archivo_salida.csv', index=False)



print(df_concatenado)