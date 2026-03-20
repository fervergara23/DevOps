# 📌 Ejercicio 1 - Entrada de Datos en Python

## 📖 Descripción
Este programa en Python solicita información básica al usuario y posteriormente la muestra en pantalla en forma de mensaje.

El objetivo es practicar:
- Entrada de datos con `input()`
- Conversión de tipos de datos (`str`, `int`, `float`, `bool`)
- Salida de información con `print()`

---

##  Funcionamiento

El programa pide al usuario los siguientes datos:

- Nombre
- Edad
- Peso
- Hobbies
- Estado civil (casado o no)

Después, imprime un mensaje con toda la información ingresada.

---

##  Código

```python
nombre = str(input("Ingresa tu nombre:"))
edad = int(input("Ingresa tu edad:"))
peso = float(input("Ingresa tu peso:"))
hobbies = str(input("Ingresa tus hobbies:"))
casado = bool(input("Eres casado: t/f"))

print("Hola ", nombre,", tu edad es de ", edad, "anos, tu peso es de ", peso, "kg. Me cuentas que tus hobbies son: ", hobbies, "y estas",casado)