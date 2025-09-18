#funcion simple
def saludar():
    print("Hola a todos")

saludar()

#funcion con parametros
def saludar2(nombre):
    print(f"Hola {nombre}")

saludar2("Juan")

#funcion sumar utilizando *args
def sumar(*numeros):
    return sum(numeros)

resultado = sumar(1, 2, 3, 4, 5)
print(f"La suma es: {resultado}")

#se pueden parsar los parametros de manera forzada y no importa el orden

def saludar3(nombre, apellido):
    print(f"Hola {nombre} {apellido}")  
    
saludar3(apellido="Perez", nombre="Juan")   

#se pueden definir parametros por defecto
def saludar4(nombre="Invitado"):
    print(f"Hola {nombre}")

saludar4()   

#funciones lambda
sumar2 = lambda x, y: x + y 
resultado2 = sumar2(10, 20)
print(f"La suma es: {resultado2}")

#funcion filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Números pares: {pares}")