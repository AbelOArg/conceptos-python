#bucle for

for elemento in [1,2,3,4,5]:
    print(elemento)         #imprime cada elemento de la lista
    
#se pueden iterar dos o mas listas a la vez con la funcion zip
for x, y in zip([1,2,3], ['a','b','c']):
    print(x, y)            #imprime los elementos de ambas listas en pares

#se puede iterar un rango de numeros con la funcion range
for i in range(5):
    print(i)               #imprime los numeros del 0 al 4
#si colocamos dos argumentos en range, el primero es el numero inicial y el segundo el numero final (excluido)
for i in range(2, 5):
    print(i)               #imprime los numeros del 2 al 4  
    
#con la funcion enumerate podemos obtener el indice y el valor de cada elemento en una lista
for indice, valor in enumerate(['a','b','c']):
    print(indice, valor)   #imprime el indice y el valor de cada elemento

#se puede usar else en un bucle for, se ejecuta al finalizar el bucle
for i in range(3):
    print(i)
else:
    print("Bucle finalizado")

#se puede iterar un diccionario con un bucle for
mi_diccionario = {'a': 1, 'b': 2, 'c': 3} 
for clave, valor in mi_diccionario.items(): # recorre cada par clave-valor del diccionario
    print(clave, valor)    #imprime cada clave y su valor
    
#o tambien se puede iterar solo las claves o solo los valores
for clave in mi_diccionario.keys():        # recorre solo las claves del diccionario
    print(clave)          #imprime cada clave
for valor in mi_diccionario.values():      # recorre solo los valores del diccionario
    print(valor)          #imprime cada valor
#tambien se puede recorrer un diccionario sin usar items, keys o values, en este caso se recorren las claves
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave]) #imprime cada clave y su valor
    
#La sentencia continue se usa para saltar a la siguiente iteracion del bucle
for i in range(5):
    if i == 2:
        continue            #salta el numero 2
    print(i)               #imprime los numeros del 0 al 4, excepto el 2

#La sentencia break se usa para salir del bucle
for i in range(5):
    if i == 2:
        break               #sale del bucle cuando i es 2
    print(i)               #imprime los numeros 0 y 1  

#se puede recorrer una cadena de texto
for letra in "hola":
    print(letra)          #imprime cada letra de la cadena  
    
#se puede hacer un for en una sola linea
cuadrados = [x**2 for x in range(5)]  #crea una lista con los cuadrados de los numeros del 0 al 4
print(cuadrados)        #imprime la lista [0, 1, 4, 9, 16]

#todos los for anteriores tambien se pueden usar con tuplas y conjuntos

#bucle while
contador = 0
while contador < 5:
    print(contador)       
    contador += 1 #incrementa el contador en 1