# Ejercicio 16:
# Divide el número entero del DNI entre 23. Se coge el resto. El resto será siempre un número. Ese número
# determinará la letra final del DNI Se solicita la introducción del DNI por teclado (el formato correcto
# es una sucesión de 8 números enteros NNNNNNNN)
# Si el formato del DNI es correcto se calcula la letra que corresponde y se escribe
# por pantalla “La letra que corresponde al DNI introducido es” X y el NIF completo
# es NNNNNNNNX
# Si el formato del DNI es incorrecto se escribe por pantalla “Formato de DNI
# incorrecto” y se vuelve a solicitar la introducción del DNI.
def ejercicio16(dni_usuario):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    try:
        numero = int(dni_usuario)
        if len(dni_usuario) != 8:
            raise ValueError
        letra = letras[numero % 23]
        return letra
    except ValueError:
        return "Formato de DNI incorrecto"


dni = input("Introduce tu DNI (sin la letra): ")
letra = ejercicio16(dni)

if letra == "Formato de DNI incorrecto":
    print(letra)
else:
    print(f"La letra que corresponde al DNI introducido es {letra} y el NIF completo es {dni}{letra}")
