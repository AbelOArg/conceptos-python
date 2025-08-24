#con la funcion dir se pueden ver todos los metodos del tipo de dato que le enviemos
#Las funciones se ejecutan sin la necesidad de una istancia de un objeto
#Los metodos necesitan una instancia de un objeto y se llaman con el .
#dato.metodo()

print(dir("Hola"))

#upper() todo a mayuscula
#lowe() todo a minuscula
#capitalize() convierte todo a minuscula y la primera letra en mayuscula
#find("cadena a buscar") devuelve la posicion en la que se encuentra la cadena, devuelve -1 si no encuentra
#find es key-sensitive
#index("cadena a buscar") la diferencia con find es que si no encuentra devuelve una excepción
#isnumeric() devuelve tru o false si es numerico
#isalpha() devuelve true o false si solo son letras, sin espacios ni caracteres especiales
#count() devuelve cuantas veces se encontro la coincidencia 
#len() devuelve la cantidad de caracteres de una cadena - es una funcion len(cadena)
#starswith(cadena) verifica si una cadena empieza con una cadena dada
#endsith(cadena) vericfica si una cadena termina con una cadena dada
#replace("original", "a reemplazar") reemplaza un fragmento de la cadena dada por otra
#split(" ") devuelve una lista con strings separadas por el carater que le pasamos como argumento 