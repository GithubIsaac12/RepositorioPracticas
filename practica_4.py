# ejercicio 1
#Empleo de Librerías:
'''Problema 1:
Bitcoin es una forma de moneda digital, también conocida como
criptomoneda. En lugar de depender de una autoridad central como un
banco, Bitcoin se basa en una red distribuida, también conocida como
cadena de bloques, para registrar transacciones.
En este problema debe generar un programa que realice:
- Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
de bitcoins que posee el usuario.
- Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:
import requests
try:
...
except requests.RequestException:
...
- Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
separador de miles.'''













#ejercicio 4
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


'''def guardar_tabla_multiplicar(numero):
    with open(f"tabla-{numero}.txt", "w") as archivo:
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")
    print(f"Se ha guardado la tabla de multiplicar de {numero} en el archivo tabla-{numero}.txt")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar de {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if linea <= len(lineas):
                print(lineas[linea - 1])
            else:
                print(f"La línea {linea} no existe en el archivo tabla-{numero}.txt")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe")

def menu():
    while True:
        print("----- Menú -----")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10")
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10")
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            if 1 <= numero <= 10 and linea >= 1:
                mostrar_linea_tabla_multiplicar(numero, linea)
            else:
                print("El número debe estar entre 1 y 10, y la línea debe ser mayor o igual a 1")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()'''


'''ejercicio 5
Almacene los datos de precio de Bitcoin en un archivo txt y csv según crea conveniente.'''

import csv

def guardar_precio_bitcoin_txt(precio):
    with open('bitcoin_precios.txt', 'a') as archivo:
        archivo.write(str(precio) + '\n')

def guardar_precio_bitcoin_csv(precio):
    with open('bitcoin_precios.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([precio])

# Ejemplo de uso
precio = 80000
guardar_precio_bitcoin_txt(precio)
guardar_precio_bitcoin_csv(precio)
