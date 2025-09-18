with open("archivos/texto.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    
# de esta manera no es necesario cerrar el archivo, se cierra automaticamente