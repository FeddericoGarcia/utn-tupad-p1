#---------TUPaD---------
#------PROGRAMACION-1---
#---TRABAJO-PRACTICO----
#-PROFESOR:ARIEL-ENFERREL
#-ALUMNO:FEDERICO-GARCIA-BENGOLEA
#-COMISION: M2025-14
#-FECHA:19/05/2025
#-
import math
#----------- FUNCIONES DEL ENUNCIADO -----------
#-
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    return print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return print(f"Hola {nombre.capitalize()} !")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones 
# para mostrar los resultados.
def calcular_area_circulo(radio):
    return print(f"- El área es { math.pi * radio * radio }")

def calcular_perimetro_circulo(radio):
    return print(f"- El perímetro (circunferencia) es { 2 * math.pi * radio }")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(seg):
    horas = seg // 3600
    return print(f"- El valor de {seg} segundos equivale a {horas} horas")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = { num * i}")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = "Suma: ", a + b
    resta = "Resta: ", a - b
    multiplicacion = "Multiplicación: ", a * b
    division = "División: ", a / b
    tupla = (suma, resta, multiplicacion, division)
    return print(tupla)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
# función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso/altura**2
    if imc <= 18.5:
        return print(f"Tu IMC es {imc:.2f}, estas en Bajo Peso")
    elif imc <= 24.9:
        return print(f"Tu IMC es {imc:.2f}, estas en Peso Saludable!")
    elif 25 <= imc <= 29.9:
        return print(f"Tu IMC es {imc:.2f}, estas en Sobrepeso!")
    elif imc >= 30:
        return print(f"Tu IMC es {imc:.2f}, estas en Obesidad!")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return print(f"Los {celsius} °C equivalen a {(celsius * 1.8) + 32} °F (Fahrenheit)") 

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return print(f"El promedio de los números {a, b, c} es de {((a+b+c)/3):.2f}")


#----------- MAIN -----------
#- 1
print("Ejercicio 1:")
imprimir_hola_mundo()
print("-----------")
#- 2
print("Ejercicio 2:")
saludar_usuario(input("Ingresa tu nombre: "))
print("-----------")
#- 3
print("Ejercicio 3:")
informacion_personal(input("Ingresa tu nombre: "), input("Ingresa tu apellido: "), 
                     int(input("Ingresa tu edad: ")), input("Ingresa tu ciudad: "))
print("-----------")
#- 4
print("Ejercicio 4:")
radio = int(input("Ingresa un valor para calcular el área y perímetro: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
print("-----------")
#- 5
print("Ejercicio 5:")
segundos_a_horas(int(input("Ingresa un valor en expresado en segundos: ")))
print("-----------")
#- 6
print("Ejercicio 6:")
tabla_multiplicar(int(input("Ingresa un valor para saber su tabla de multiplicación: ")))
print("-----------")
#- 7
print("Ejercicio 7:")
numA = int(input("Ingresa el primer número: "))
numB = int(input("Ingresa el segundo número: "))
operaciones_basicas(numA, numB)
print("-----------")
#- 8
print("Ejercicio 8:")
peso = float(input("Ingresa el valor de tu peso (en Kg): "))
altura = float(input("Ingresa el valor de tu altura (en mts): "))
calcular_imc(peso, altura)
print("-----------")
#- 9
print("Ejercicio 9:")
celsius = float(input("Ingresa la temperatura en grados Celsius °C: "))
celsius_a_fahrenheit(celsius)
print("-----------")
#- 10
print("Ejercicio 10:")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
calcular_promedio(a, b, c)
print("-----------")
