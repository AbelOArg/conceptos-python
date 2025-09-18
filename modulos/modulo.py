import saludar as saludito #importamos el modulo saludar y le damos un alias saludito
# se puede importar todo el modulo o solo una funcion especifica del modulo
# from saludar import saludar, en este caso no necesitamos el alias y se llama directamente la funcion
# from saludar import *  #importa todo el modulo sin necesidad de alias
# se pueden importar varios modulos separados por comas
# se pueden importar dos o mas funciones de un mismo modulo separadas por comas
# el enrutamiento de los modulos se hace con puntos por esjemplo carpeta1.carpeta2.modulo
# si el modulo esta en otra carpeta se debe especificar la ruta completa
# si el modulo esta en la misma carpeta no es necesario especificar la ruta
# si el modulo esta en una carpeta superior se debe usar .. para subir un nivel
# si el modulo esta en una carpeta inferior se debe usar . para bajar un nivel
# si el modulo esta en una carpeta hermana se debe usar .. para subir un nivel y luego . para bajar un nivel
# se puede agregar rutas al sistema de modulos con sys.path.append('ruta')


nombre = input("Ingresa tu nombre: ")
print(saludito.saludar(nombre))