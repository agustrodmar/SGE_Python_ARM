# Ejercicio 15:
# Escriba una función es_bisiesto() que determine si un año determinado es un año
# bisiesto. Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Ejemplo de uso
anio_ingresado = int(input("Ingrese un año para verificar si es bisiesto: "))

if es_bisiesto(anio_ingresado):
    print(f"{anio_ingresado} es un año bisiesto.")
else:
    print(f"{anio_ingresado} no es un año bisiesto.")
