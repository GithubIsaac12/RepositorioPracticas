#ejercico 4

'''Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones,
también puede usar un menú para organizar su programa):
- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, donde “n” es el número introducido, y la muestre por
pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de
ello.
- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero
no existe debe mostrar un mensaje por pantalla informando de ello.
Notas:
- Note que dentro del manejo de errores existe una excepción de tipo
FileNotFoundError la cual le será de mucha utilidad.
- Revise los métodos de cadena
- Dentro del open() el método “readlines” le podría ser de utilidad.'''

def guardar_tabla():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    tabla = [f"{numero} x {i} = {numero * i}\n" for i in range(1, 11)]

    with open(f"tabla-{numero}.txt", "w") as archivo:
        archivo.writelines(tabla)

    print(f"La tabla de multiplicar del número {numero} se ha guardado en el archivo tabla-{numero}.txt.")


def mostrar_tabla():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar del número {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")


def mostrar_linea():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    linea = int(input("Ingrese el número de línea que desea mostrar: "))

    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(f"Línea {linea}: {lineas[linea - 1]}")
            else:
                print("El número de línea es inválido.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")


def menu():
    while True:
        print("\n----- Menú -----\n")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar completa")
        print("3. Mostrar línea específica")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            guardar_tabla()
        elif opcion == "2":
            mostrar_tabla()
        elif opcion == "3":
            mostrar_linea()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()