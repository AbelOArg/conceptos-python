#lista se pueden modificar
lista = ["Mi nombre","Mi apellido",True,1.80]

#tuplas - no se pueden modificar luego --> tupla[0] = "otro nombre" -- da error
#para mostrar se usa corchetes, el parentesis es solo para crear

tupla = ("Mi nombre","Mi apellido",True,1.80)

#conjuntos - podemos redefinirlos pero no podemos modificar al igual que las tuplas
#no se puede acceder al indice ejem conjunto[0]
#no puede tener datos cuplicados en sus campos

conjunto = {"Mi nombre","Mi apellido",True,1.80}

#diccionario - es el equivalente al struct de C
#podemos llamar sus elementos por medio del nombre de sus campos print(diccionario['nombre'])
#la estructura del diccionario es key : value, se separan con ,
diccionario ={
    'nombre' : "mi nombre",
    'apellido': "mi apelledo",
    'altura' : 180
}
print(diccionario['nombre'])