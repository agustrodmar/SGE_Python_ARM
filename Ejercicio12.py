# Ejercicio 12:
# Definir una función generar_n_caracteres() que tome un entero n y devuelva el
# caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
# devolver "xxxxx".
def generar_n_caracteres(n, caracter):
    return caracter * n


n_ejemplo = 5
caracter_ejemplo = "x"

resultado = generar_n_caracteres(n_ejemplo, caracter_ejemplo)
print(resultado)
