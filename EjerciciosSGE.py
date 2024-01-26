

# Función principal del Proyecto. Sustituir el número de ejercicio para ejecutar el ejercicio que se desee comprobar.
def main():
    ejercicio5()



# Dada la siguiente cadena de texto:
# x = “Buenas Tardes”
# Usar el método len para imprimir su longitud
# Obtener su primer carácter
# Obtener los caracteres de la posición 3 a la 6 (no incluido)
def ejercicio1():
    x = "Buenas Tardes"

    # Usar el método len para imprimir su longitud
    print(len(x))

    # Obtener su primer carácter
    print((x[0]))

    # Obtener los caracteres de la posición 3 a la 6 (no incluido)
    print(x[2:5])


# Dada la siguiente cadena:
# x = “ Bienvenidos a crase “
# Devolver la cadena sin los espacios en blanco del principio y final
# Reemplazar el carácter r por l
def ejercicio2():
    x = " Bienvenidos a crase "

    # Eliminar espacios en blanco al principio y al final
    nueva_x = x.strip()

    # .replace() cambia las r por la l
    nueva_x_corregida = nueva_x.replace('r', 'l')
    resultado = print(nueva_x_corregida)

    return resultado


# Dada la siguiente lista:
# Frutas = [“manzana”, “platano”, “fresa” ]
# Imprimir el segundo ítem
# Comprobar si “patata” está en la lista en caso negativo imprime mensaje indicando
# que patata no es una fruta
# Cambiar el valor de “manzana” por “kiwi”
# Usar el método append() para añadir a la lista la “naranja”
# Usar el método insert() para añadir el limón en el tercer puesto de la lista
# Usar el método remove() para eliminar la “fresa”
# Imprimir los ítems de la lista usando un bucle
def ejercicio3():
    frutas = ["manzana", "platano", "fresa"]

    # Imprime el segundo ítem
    print("Segundo ítem:", frutas[1])

    # Comprueba si "patata" está en la lista
    if "patata" not in frutas:
        print("Patata no es una fruta.")

    # Cambia el valor de "manzana" por "kiwi"
    frutas[0] = "kiwi"

    # Usa el método append() y añade a la lista la "naranja"
    frutas.append("naranja")

    # Usa el método insert() y añade el limón en el tercer puesto de la lista
    frutas.insert(2, "limón")

    # Usa el método remove() para eliminar la "fresa"
    frutas.remove("fresa")

    # Imprime los ítems de la lista usando un bucle for
    print("Ítems de la lista:")
    for fruta in frutas:
        print(fruta)


# Dado el siguiente diccionario:
# Coche = {“marca”: “Ford”, “modelo”: “Mustang”}
# Usar el método get para imprimir el valor de la clave “modelo”
# Añadir la clave/valor: “color” : “rojo” al diccionario de coche
def ejercicio4():
    Coche = {"marca": "Ford", "modelo": "Mustang"}

    # Usa el método get para imprimir el valor de la clave "modelo"
    modelo_coche = Coche.get("modelo")
    print("Modelo del coche:", modelo_coche)

    # Añade la clave/valor: "color": "rojo" al diccionario
    Coche["color"] = "rojo"

    # Imprime el diccionario actualizado
    print("Diccionario del coche actualizado:", Coche)


# Dados dos números a y b, imprimir “Hola” si a es mayor que b y “Adiós” si a es menor que b
def ejercicio5(a=4, b=9):
    if a > b:
        print("Hola")
    elif a < b:
        print("Adiós")
    else:
        print("Los números son iguales")

main()
