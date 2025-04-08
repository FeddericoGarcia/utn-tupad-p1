#---------TUPaD---------
#------PROGRAMACION-1---
#---TRABAJO-PRACTICO-1--
#-PROFESOR:ARIEL-ENFERREL
#-ALUMNO:FEDERICO-GARCIA-BENGOLEA
#-COMISION:M2025-14
#-FECHA:08/04/2025
#-
import random
from statistics import mode, median, mean
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
print("# Actividad 1")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Sos mayor de edad ✔")
else:
    print("No sos mayor de edad 🔞")
print("--------------")
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
print("# Actividad 2")
nota = float(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado 👍")
else:
    print("Desaprobado 👎")
print("--------------")
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
print("# Actividad 3")
num = int(input("Ingresa un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par ✌")
else:   
    print("Por favor, ingrese un número par 🤞")
print("--------------")
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
print("# Actividad 4")
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Niño/a 👦 👧")
elif edad >= 12 and edad < 18:
    print("Adolescente 👩‍🦰 👱‍♂️")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven 👨 👩")
else:
    print("Adulto/a 👴 👵")
print("--------------")
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
print("# Actividad 5")
password = (input("Ingresa tu contraseña: "))
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("--------------")
# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
print("# Actividad 6")
numero_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"Números aleatorios: {numero_aleatorios}")
moda = mode(numero_aleatorios)
mediana = median(numero_aleatorios)
media = mean(numero_aleatorios)
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")
if media > mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
print("--------------")
# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
print("# Actividad 7")
texto = input("Ingresa una frase o palabra:")
ultimoCaracter = texto[-1].upper()
if ultimoCaracter == "A" or ultimoCaracter == "E" or ultimoCaracter == "I" or ultimoCaracter == "O" or ultimoCaracter == "U":
    restoTexto = texto[:-1]
    nuevoTexto = restoTexto + "!"
    print(f"Nueva frase: {nuevoTexto.upper()}")
else:
    print(f"Frase original: {texto.upper()}")
print("--------------")
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
print("# Actividad 8")
nombre = input("Ingresá tu nombre: ")
print("Indica la opción deseada: ")
print("1 - Nombre en mayúscula")
print("2 - Nombre en minúscula")
print("3 - Nombre en minúscula")
opcion = int(input())
if opcion == 1:
    print(f"1 - Nombre: {nombre.upper()}")
elif opcion == 2:
        print(f"2 - Nombre: {nombre.lower()}")
elif opcion == 3:
        print(f"3 - Nombre: {nombre.title()}")
print("--------------")
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
print("# Actividad 9")
magnitudTerremoto = int(input("Ingresa la magnitud del terremoto: "))
if magnitudTerremoto < 3:
    print("Terremoto Muy Leve (imperceptible)")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
    print("Terremoto Leve (ligeramente perceptible)")
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
    print("Terremoto Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print("Terremoto Fuerte (puede causar daños en estructuras débiles)")
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print("Terremoto Muy Fuerte (puede causar daños significativos)")
elif magnitudTerremoto >= 7:
    print("Terremoto Extremo (puede causar graves daños a gran escala)")
print("--------------")
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
print("# Actividad 10")
hemisferio = input("Indica en que HEMISFERIO (Norte / Sur) te encontras:").lower()
mes = input("Indica en que MES te encontras:").lower()
dia = int(input("Indica en que DÍA te encontras:"))
if dia >= 1 and dia <= 31:
    if hemisferio == "norte":
        if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia < 20):
            print("- Estación Invierno")
        elif (mes == "marzo" and dia >= 20) or mes in ["abril", "mayo"] or (mes == "junio" and dia < 21):
            print("- Estación Primavera")
        elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia < 23):
            print("- Estación Verano")
        elif (mes == "septiembre" and dia >= 23) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia < 21):
            print("- Estación Otoño")
    elif hemisferio == "sur":
        if (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia < 23):
            print("- Estación Invierno")
        elif (mes == "septiembre" and dia >= 23) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia < 21):
            print("- Estación Primavera")
        elif (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia < 20):
            print("- Estación Verano")
        elif (mes == "marzo" and dia >= 20) or mes in ["abril", "mayo"] or (mes == "junio" and dia < 21):
            print("- Estación Otoño")
    else:
        print("El dato en HEMISFERIO no es valido, por favor, ingresa Norte o Sur")
else:
    print("El dato ingresado en DÍA es incorrecto.")
print("--------------")