

        




#ejerccicio 2
'''Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)'''

def obtener_calificaciones():
    while True:
        calificaciones = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones = calificaciones.replace(" ", "")  # Eliminamos los espacios en blanco
        try:
            calificaciones_lista = [int(calificacion) for calificacion in calificaciones.split(",")]
            return calificaciones_lista
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

calificaciones = obtener_calificaciones()
print("Calificaciones:", calificaciones)


# ejercicio 3
# Escribe una función de Python que imprima las primeras n filas del triángulo de Pascal.

def triangulo_pascal(n):
    if n <= 0:
        print("El valor de n debe ser mayor que cero.")
        return
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1] 
        prev_row = triangle[i - 1]
        
        for j in range(1, i):
            element = prev_row[j - 1] + prev_row[j]
            row.append(element)
        
        row.append(1) 
        triangle.append(row)
        
    max_width = len(str(max(triangle[-1])))
     
    for row in triangle:
        formatted_row = [str(num).rjust(max_width) for num in row]
        print(" ".join(formatted_row).center(max_width * n))

n = 10
triangulo_pascal(n)


# ejercicio 4
'''Escriba una función que, dado un string, retorne la longitud de la última palabra. Se considera
que las palabras están separadas por uno o más espacios. También podría haber espacios al
principio o al final del string pasado por parámetro.'''

def longitud_ultima_palabra(string):
    string = string.strip()
    palabras = string.split()
    
    if len(palabras) == 0:
        return 0  
    
    ultima_palabra = palabras[-1]
    return len(ultima_palabra)
texto = "Hola amigo" # tiene 5 caracteres por lo tanto la respuesta sera 5
longitud = longitud_ultima_palabra(texto)
print(longitud)  





