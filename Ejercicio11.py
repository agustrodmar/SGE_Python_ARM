# Escribir una funcion sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
# devolver 10 y multip([1,2,3,4]) debería devolver 24
def sum(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma


def multip(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto


lista_ejemplo = [1, 2, 3, 4]

resultado_suma = sum(lista_ejemplo)
print(f"Sumar la lista da: {resultado_suma}")

resultado_producto = multip(lista_ejemplo)
print(f"El producto de la lista es: {resultado_producto}")
