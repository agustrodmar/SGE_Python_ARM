# Ejercicio 17
# Realizar una calculadora:
# Se solicita la introducción de los dos operandos y el operador por teclado
# Se muestra el resultado de la operación de tal forma: “La operación es: “
# “El resultado es “
def calcular(op1, oper, op2):
    if operador == '+':
        return op1 + op2
    elif operador == '-':
        return op1 - op2
    elif operador == '*':
        return op1 * op2
    elif operador == '/':
        if op2 != 0:
            return op1 / op2
        else:
            return "Error: División por cero"
    else:
        return "Error: Operador no válido"


operando1 = float(input("Introduce el primer operando: "))
operador = input("Introduce el operador (+, -, *, /): ")
operando2 = float(input("Introduce el segundo operando: "))

resultado = calcular(operando1, operador, operando2)

print(f"La operación es: {operando1} {operador} {operando2}")
print(f"El resultado es: {resultado}")
