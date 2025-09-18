while True:
    try:
        numero = int(input("Ingresa un número: "))
        print(f"Has ingresado el número: {numero}")
        break
    except ValueError:
        print("Error: Debes ingresar un número válido. Inténtalo de nuevo.")