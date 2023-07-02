#ejercicio 2
'''Cree un programa el cual cumpla con las siguientes especificaciones:
- Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
- Solicite al usuario un texto.
- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.'''


from pyfiglet import Figlet
figlet = Figlet()'''

'''import random
from pyfiglet import Figlet

figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

fuente = input("Ingrese el nombre de la fuente a utilizar (deje en blanco para seleccionar aleatoriamente): ")
if fuente == "":
    fuente = random.choice(fuentes_disponibles)
elif fuente not in fuentes_disponibles:
    print("La fuente ingresada no es válida. Seleccionando aleatoriamente una fuente.")
    fuente = random.choice(fuentes_disponibles)

texto = input("Ingrese el texto a imprimir: ")

figlet.setFont(font=fuente)

print(figlet.renderText(texto))