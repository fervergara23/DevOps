nombre = str(input("Ingresa tu Nombre:"))

devOps = int(input("Ingresa tu calificacion de la materia de Fundamento de DevOps:"))
fullStack = int(input("Ingresa tu calificaion de la materia de Desarrollo Full Stack:"))
redes = int(input("Inbresa tu calificacion de la materia Gestion de Redes:"))
ingles = int(input("Ingresa tu calificacion de la materia Ingles:"))

promedio = (devOps + fullStack + redes + ingles) / 4
print("El promedio de ",nombre," es de ",promedio)

if promedio == 100:
    print("Excelente")
elif promedio >= 90:
    print("Muy buen trabajo")
elif promedio >= 80:
    print("Bien hecho, pero puedes mejorar")
elif promedio >= 70:
    print("Panzaste")
elif promedio <= 69:
    print("Reprobaste")