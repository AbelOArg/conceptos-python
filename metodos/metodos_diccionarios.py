diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

clave = diccionario.keys()
nombre = diccionario.get("nombre") #imprime el valor asociado a la clave "nombre" si existe, si no, devuelve None
edad = diccionario.get("edad", "No disponible") #devuelve el valor asociado a la clave "edad" si existe, si no, devuelve "No disponible"
diccionario.pop("ciudad") #elimina la clave "ciudad" y su valor asociado, devuelve el valor eliminado
diccionario["pais"] = "España" #agrega una nueva clave "pais" con el valor "España"
diccionario.update({"lenguaje": "Python", "ocupacion": "Desarrollador"}) #actualiza o agrega varias claves y valores 
diccionario_iterable = diccionario.items() #devuelve un iterable de tuplas (clave, valor) del diccionario
diccionario.clear() #elimina todas las claves y valores del diccionario
#verifica si una clave existe en el diccionario
existe_nombre = "nombre" in diccionario #devuelve True si la clave "nombre" existe, False si no 

print(diccionario)