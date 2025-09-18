#si abrimos el archivo en modo 'w' (write), si el archivo ya existe, se sobrescribe.
#si el archivo no existe, se crea uno nuevo.
#si queremos agregar contenido sin borrar lo que ya existe, usamos 'a' (append).


with open('archivos/texto.txt', 'a',encoding="UTF-8") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Estamos escribiendo en un archivo usando Python.\n")
    archivo.write("¡Es muy sencillo!\n")
    
    #podemos escribir varias lineas a la vez usando una lista, con witelines
    lineas = ["Esta es la cuarta linea.\n", "Esta es la quinta linea.\n"]
    archivo.writelines(lineas)