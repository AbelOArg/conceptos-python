import re

texto = '''Mi número de teléfono es 123-456-7890 y mi correo es lalala@gmail.com, mi dirección es Calle Falsa 123.
También puedes contactarme en mi trabajo: 987-654-3210 o en mi correo laboral:
Esta es la tercera línea del texto.'''

resultado = re.search('puedes', texto)
#devuelve un objeto match si encuentra la coincidencia
#None si no la encuentra

resultado = re.findall('de', texto)
#devuelve una lista con todas las coincidencias

#se puede usar un tercer parámetro para indicar el número máximo de coincidencias a encontrar
#resultado = re.findall('de', texto, 1)
#se puede usar un tercer parametro para ignorar mayusculas y minusculas
#resultado = re.findall('DE', texto,flags=re.IGNORECASE)

#se pueden usar expresiones regulares para buscar patrones por ejemplo para buscar digitos
resultado = re.findall(r'\d', texto) #devuelve todos los digitos, la r antes de la cadena indica que es una raw string

#si colocamos en mayusculas la D, busca todo lo que no sea un digito
resultado = re.findall(r'\D', texto)

#con el \w buscamos caracteres alfanumericos (letras y numeros)
resultado = re.findall(r'\w', texto)

#con \W buscamos todo lo que no sea un caracter alfanumerico
resultado = re.findall(r'\W', texto)

#con \s buscamos espacios en blanco (espacios, tabulaciones, saltos de linea)
resultado = re.findall(r'\s', texto)

#con \S buscamos todo lo que no sea un espacio en blanco
resultado = re.findall(r'\S', texto)

#con . buscamos cualquier caracter excepto saltos de linea
resultado = re.findall(r'.', texto)
#con el ^ buscamos el inicio de una cadena
resultado = re.findall(r'^Mi', texto)
#con el $ buscamos el final de una cadena
resultado = re.findall(r'texto.$', texto)
#con el * buscamos el caracter anterior 0 o mas veces
resultado = re.findall(r'm*', texto)

#si uso flags=re.M el ^ y $ funcionan para cada linea
resultado = re.findall(r'^Esta', texto, flags=re.M)

#puedo buscar varios nuemeros juntos
resultado = re.findall(r'\d{3}', texto) #busca secuencias de 3 digitos juntos

#podemos buscar en un rango de coincidencias usando {}
resultado = re.findall(r'\d{2,4}', texto) #busca secuencias de 2 a 4 digitos juntos

#podemos buscar conjuntos de caracteres usando []
resultado = re.findall(r'[aeiou]', texto) #busca todas las vocales

#podemos buscar una cosa u otra usando |
resultado = re.findall(r'\d{3}-\d{3}-\d{4}|\w+@\w+\.\w+', texto) #busca numeros de telefono o correos

#podemos validar un correo electronico mas estrictamente
resultado = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)

#podemos validar una pagina web
resultado = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', texto)  #busca urls que empiecen con http o https
print(resultado)