#las variables se adaptan al tipo de dato - tipeado dinamico

#los strings se concatenan con +

#por convencion se usa snake_case nombre_completo_del_alumno
#se puede usar camel_case nombreCompletoDelAlumno

# usa f-strings en los print para imprimir

numero= 5
mensaje = f"el numero es {numero}" #la variable entera se convirtio a texto
print(mensaje)

#se usa del para borrar una variable

del numero

#se puede buscar dentro de un string con los operadores de pertenencia in / not in

print("num" in mensaje) # o not in

#desempaquetado se puede usar con datos en tuplas y en listas

datos =("minombre","miapellido",3000000)

nombre,apellido,dni = datos

#se puede crear una tupla con tuple() recibe una lista como parametro

tupla1 = tuple(["Hola","Mundo"])
tupla2 = "dato1","dato2" #se crear una tupla sin ()
tupla3 = "datounico", #es una tupla de un solo dato, se agrega una , al final

#los conjuntos se pueden crear con una funcion set()

conjunto = set(["dato1","dato2"])
 
#la funcion frzenset() crea un conjunto que no puede modificarse y puede usarse como parametro
#para la creacion de otro conjunto

conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

conjunto1 ={1,3,5,7,9}
conjunto2 ={1,3,7}

resultado = conjunto2.issubset(conjunto1) #verifica si conjunto 2 es un sub conjunto de conjunto 1
print(resultado)                          #se puede usar operadores logicos conjunto2 <= conjunto1

resultado = conjunto1.issuperset(conjunto2) #tambien conjunto1 > conjunto2

resultado = conjunto2.isdisjoint(conjunto1) #si al menos un valor coincide, devuelve false
print(resultado)

lista = list()
lista.append("Juan")
lista.append("Pedro")
print(lista)

#los diccionarios se pueden crear con dict

diccionario1 = dict.fromkeys(["Nombre","Apellido"]) #crea un diccionario con una lista iterable con valores
                                                    #none como predeterminados
print(diccionario1)

diccionario2 = dict.fromkeys("abc","una letra") #crea un diccionario con cada caracter del string iterable
print(diccionario2)                             #y le asigane el strin " una letra"

