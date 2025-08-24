lista = list(["Nombre", "Apellido", "Edad", "Ciudad"]) #crea una lista 
cantidad_de_elementos = len(lista) #cuenta la cantidad de elementos de la lista
lista.append("Pais") #agrega un elemento al final de la lista
lista.insert(2, "Estado") #inserta un elemento en la posicion 2
lista.extend(["Lenguaje", "Ocupacion"]) #agrega varios elementos al final de la lista
lista.pop(3) #elimina el elemento en la posicion 3 - -1 para eliminar el ultimo elemento y -2 para eliminar el penultimo
lista.remove("Edad") #elimina el primer elemento que coincida con el valor "Edad" - si no existe, lanza una excepción
lista.clear() #elimina todos los elementos de la lista
lista.sort() #ordena la lista en orden ascendente (numeros y booleanos) o alfabético (cadenas de texto) - se puede usar reverse=True para orden descendente
lista.reverse() #invierte el orden de los elementos de la lista
lista.count("Nombre") #cuenta la cantidad de veces que aparece el elemento "Nombre" en la lista
lista.index("Apellido") #devuelve el índice del primer elemento que coincida con "Apellido" - si no existe, lanza una excepción
nueva_lista = lista.copy() #crea una copia de la lista

#en las tuplas no se pueden agregar, eliminar o modificar elementos, pero se pueden contar y buscar elementos
tupla = tuple(["Nombre", "Apellido", "Edad", "Ciudad"]) #crea una tupla
cantidad_de_elementos_tupla = len(tupla) #cuenta la cantidad de elementos de la tupla
tupla.count("Nombre") #cuenta la cantidad de veces que aparece el elemento "Nombre" en la tupla
tupla.index("Apellido") #devuelve el índice del primer elemento que coincida con "Apellido" - si no existe, lanza una excepción