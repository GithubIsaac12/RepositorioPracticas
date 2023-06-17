


def suma(num1, num2):
    try:
        resultado = float(num1) + float(num2)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def resta(num1, num2):
    try:
        resultado = float(num1) - float(num2)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def producto(num1, num2):
    try:
        resultado = float(num1) * float(num2)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def division(num1, num2):
    try:
        if float(num2) == 0:
            return "Error: No es posible dividir entre cero"
        else:
            resultado = float(num1) / float(num2)
            return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"




