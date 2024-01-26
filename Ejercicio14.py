# Ejercicio 14:
# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
# que evaluar la cadena y decir cuántas letras mayúsculas tiene.

def ejercicio14(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador


# Solicita al usuario que ingrese una cadena
cadena_ingresada = input("Ingrese una cadena: ")

# Calcula y muestra el número de letras mayúsculas en la cadena
num_mayusculas = ejercicio14(cadena_ingresada)
print(f"La cadena tiene {num_mayusculas} letras mayúsculas.")
