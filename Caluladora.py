print("Calculatecmi")
print("Operaciones: +  -  *  / ^ sqr")

operacion = input("Ingresa la operación: ")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: no se puede dividir entre 0"
elif operacion == "^":
    resultado = num1 * num1
else:
    resultado = "Operación no válida"

print("Resultado:", resultado)