# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
# contrario devuelve False
def ejercicio10(caracter):
    vocales = "oiaueOIAUE"
    return caracter in vocales


caracter_ingresado = input("Ingrese un carácter: ")

if len(caracter_ingresado) == 1 and ejercicio10(caracter_ingresado):
    print(f"{caracter_ingresado} es una vocal.")
else:
    print(f"{caracter_ingresado} no es una vocal.")
