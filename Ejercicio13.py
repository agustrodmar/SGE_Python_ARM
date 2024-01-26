# Ejercicio 13:
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.
def mas_larga(lista_palabras):
    if not lista_palabras:
        return None  # Devuelve None si la lista está vacía

    palabra_mas_larga = lista_palabras[0]

    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga


lista_ejemplo = ["Odoo", "SAP", "Oracle", "Bind"]

resultado = mas_larga(lista_ejemplo)
print(f"La palabra más larga es: {resultado}")
