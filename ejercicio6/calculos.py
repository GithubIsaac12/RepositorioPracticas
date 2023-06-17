#ejercicio 6
'''Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
evitar que se quede bloqueada una funcionalidad, esto incluye:'''


import operaciones

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

resultado_suma = operaciones.suma(num1, num2)
print("Suma:", resultado_suma)

resultado_resta = operaciones.resta(num1, num2)
print("Resta:", resultado_resta)

resultado_producto = operaciones.producto(num1, num2)
print("Producto:", resultado_producto)

resultado_division = operaciones.division(num1, num2)
print("División:", resultado_division)


