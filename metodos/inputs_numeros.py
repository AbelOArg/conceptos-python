numero = input("Ingrese un numero: ")

# el valor de un input siempre sera una cadena, para usarlos como numeros debemos convertirlos

numero_entero = int(numero) # in() no puede recibir una cadena que represente un float 

numero_flotante = float(numero)

print(numero_entero)
print(numero_flotante)