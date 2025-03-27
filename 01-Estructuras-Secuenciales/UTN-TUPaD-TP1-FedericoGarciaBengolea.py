#---------TUPaD---------
#------PROGRAMACION-1---
#---TRABAJO-PRACTICO-1--
#-PROFESOR:ARIEL-ENFERREL
#-ALUMNO:FEDERICO-GARCIA-BENGOLEA
#-FECHA:24/03/2025
#-
import math
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print(f"# Actividad 1 - Saludo")
print(f"- ¡Hola mundo!")
print(f"--------------")
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
print(f"# Actividad 2 - Saludo cordial")
print(f"Hola! ¿como es tu nombre?")
nombre = input()
print(f"- Un placer conocerte {nombre}!")
print(f"--------------")
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
print(f"# Actividad 3 - Presentación")
print(f"Ingresa tus datos personales:")
nombre = input("Nombre:")
apellido = input("Apellido:")
edad = input("Edad:")
residencia = input("Lugar de residencia:")
print(f"- Presentación: Hola! me llamo {nombre} {apellido}, tengo {edad} años y vivo actualmente en {residencia}")
print(f"--------------")
# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro
print(f"# Actividad 4 - Area y Perímetro")
radio=float(input(f"Ingresá el valor para calcular el área y perímetro:"))
print(f"- El valor del area es {math.pi * ( radio ** 2 )}")
print(f"- El valor del perímetro es {math.pi * radio * 2}")
print(f"--------------")
# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
print(f"# Actividad 5 - Tiempo")
segundos = int(input("Ingresa un número para calcular el tiempo: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes = segundos_restantes % 60
dia = horas // 24
dias = "" if horas < 24 else f"{dia} dias con "
print(f"- El número ingresado equivale a {dias}{horas} horas, {minutos} minutos y {segundos_restantes} segundos")
print(f"--------------")
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
print(f"# Actividad 6 - Tabla de multiplicación")
numero = int(input("Escribí un número: "))
for i in range(1, 11):
    print(f"- {numero} x {i} = {numero * i}")
print("--------------")
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print(f"# Actividad 7 - Operaciónes matemáticas")
num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))
if num1 != 0 and num2 != 0:
    print(f"- La suma es: {num1 + num2}")
    print(f"- La resta es: {num1 - num2}")
    print(f"- La multiplicación es: {num1 * num2}")
    print(f"- La división es: {num1 / num2}")    
else: 
    print("⛔ ERROR: Los números deben ser mayor a cero ( 0 ).")
print(f"--------------")
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 =
# 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
# (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)
# 2
print(f"# Actividad 8 - Indice de Masa Corporal")
peso_kg = float(input("Ingresa tu peso en kg: "))
altura_m = float(input("Ingresa tu altura en metros (usá el '.' para un correcto cálculo): "))
imc = peso_kg / altura_m ** 2
categoria = ""
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
elif 30 <= imc < 35:
    categoria = "Obesidad grado I"
elif 35 <= imc < 40:
    categoria = "Obesidad grado II"
else:
    categoria = "Obesidad grado III"
print(f"- El IMC es {imc:.2f}") 
print(f"- Estas en la categoría de: {categoria}") 
print(f"--------------")
# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
print(f"# Actividad 9 - Conversor de Temperaturas")
celsius = float(input("Escribí la temperatura a convertir en grados Fahrenheit °F: "))
fahr = 9/5 * celsius + 32
print(f"- La temperatura de {celsius}°C es de {fahr}°F")
print(f"--------------")
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números
print(f"# Actividad 10 - Sacar Promedio")
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercero número: "))
print(f"- El promedio es de: {(num1 + num2 + num3) / 3:.2f}")
print(f"--------------")