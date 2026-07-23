# Proyecto del Dia
nombre = input("Cual es tu nombre?: ")
edad = int(input("Que edad tienes?: "))
promedio = float(input("Cual es tu promedio?: "))

print(f"Hola, {nombre} bienvenido !")

if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

if promedio >= 5 and promedio < 8:
    print("Estas aprobado")
elif promedio >= 8 and promedio < 10:
    print("Eres un excelente estudiante")
elif promedio >= 10:
    print("Eres un genio !!!")
else:
    print("Estas reprobado.")