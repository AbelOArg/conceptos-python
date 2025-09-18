import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('trabajando_con_graficos\\datos.csv')

print(df)

#sns.lineplot(data=df, x='fecha', y='cantidad') #genera la grafica
sns.barplot(data=df, x='fecha', y='cantidad') #genera la grafica de barras
plt.plot('2023-01-06',12, marker='o') #genera un punto en la grafica
plt.title('Cantidad a lo largo del tiempo') #titulo de la grafica
plt.xlabel('Fecha de de los sucesos') #etiqueta del eje x
plt.ylabel('Cantidad de sucesos') #etiqueta del eje y
plt.xticks(rotation=45) #rota las etiquetas del eje x para mejor visibilidad
plt.tight_layout() #ajusta el diseño para evitar recortes
plt.grid() #agrega una cuadrícula para mejor lectura
plt.show()