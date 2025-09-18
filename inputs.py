nombre = input("Ingrese su nombre: ")
print("Hola, " + nombre + "!")

# los inputs siempre ingresan strings
edad = input("Ingrese su edad: ")
edad = int(edad)  # Convertir a entero
nueva_edad = edad + 1 # si usabamos el input sin convertir a int, esto concatenaria strings