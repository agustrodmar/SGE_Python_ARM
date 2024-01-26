# 9. Calcular el factorial de un número
def ejercicio9(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial


numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = ejercicio9(numero_ingresado)
print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")
