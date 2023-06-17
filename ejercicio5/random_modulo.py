# ejercicio5
'''Desarrollar un módulo que contenga las siguientes funciones:
● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
● Mostrar la lista obtenida por pantalla.
● Ordenar los valores de la lista y mostrarla por pantalla.
Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
ejecutar las funciones'''

import random

def generate_random_modulo():
    random_modulo = []
    for _ in range(20):
        random_modulo.append(random.randint(0, 100))
    return random_modulo

def display_list(modulo):
    print("Lista de números:")
    for number in modulo:
        print(number)

def sort_list(modulo):
    sorted_modulo = sorted(modulo)
    print("Lista ordenada:")
    for number in sorted_modulo:
        print(number)


