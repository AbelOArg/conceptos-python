archivo_sin_leer = open("archivos\\texto.txt",encoding="utf-8" )
#leer el archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea
#linea1 = archivo_sin_leer.readline()
#print(linea1)
#linea2 = archivo_sin_leer.readline()
#print(linea2)

#leer todas las lineas y guardarlas en una lista
lineas = archivo_sin_leer.readlines()
print(lineas)
archivo_sin_leer.close()