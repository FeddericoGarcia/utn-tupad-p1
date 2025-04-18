#---------TUPaD---------
#------PROGRAMACION-1---
#---TRABAJO-PRACTICO----
#-PROFESOR:ARIEL-ENFERREL
#-ALUMNO:FEDERICO-GARCIA-BENGOLEA
#-COMISION: M2025-14
#-FECHA:18/04/2025
#-
import random 
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("# Actividad 1 ")
for i in range(1,101):
    print("#", i)
print("---------------")
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
print("# Actividad 2 ")
num = input("Ingresa un número: ")
print(f"- El número {num} contiene {len(num)} dígitos")
print("---------------")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("# Actividad 3 ")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print(f"- A continuación se muestran los números enteros desde", num1, "hasta", num2, "(excluyendo los mismos)")
for i in range(num1 + 1, num2):
    print(f"#", i)
print("---------------")
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
print("# Actividad 4 ")
num = int(input("Ingresa un número: (Toca el 0 para finalizar) "))
newNum = 1
while newNum > 0:
    newNum = int(input("Ingresa otro número: "))
    num += newNum
print(f"==============")
print(f"La suma total de los números enteros ingresados es de: {num}")
print("---------------")
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("# Actividad 5 ")
print("Juego de adivinanza! ")
num = int(input("Ingresa un número del 0 al 9: "))
secretNum = random.randint(0, 9)
rounds = 0 
while num != secretNum:
    rounds += 1
    if num > secretNum:
        print("Uy muy cerca!, pero el número es más chico")
        num = int(input("Ingresa otro número: "))
    elif num < secretNum:
        print("Casi casi... El número es más grande!!")
        num = int(input("Ingresa otro número: "))
print("===================")
print("¡¡Juego finalizado!!")
print(f"El número secreto es {secretNum}")
print(f"Lo lograste en {rounds} intentos")
print("---------------")
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("# Actividad 6 ")
for i in range(100,-1,-2):
    print("#", i)
print("---------------")
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario
print("# Actividad 7 ")
num = int(input("Ingresa un número: "))
count = 0
numAux = num
if num > 0:
    for i in range(0, num):
        count += numAux 
        numAux -= 1
else:
    print("El número debe ser entero positivo.")
print(f"- Desde 0 (cero) hasta el número ingresado ({num})")
print(f"- La suma de todos da {count}")
print("---------------")
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("# Actividad 8 ")
negNum = 0
posNum = 0
evenNum = 0
oddNum = 0
for i in range(0, 100):
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        evenNum += 1
    elif num % 3 == 0 or num == 1:
        oddNum += 1
    elif num > 0:
        posNum += 1
    else:
        negNum += 1
print(f"- Números pares: {evenNum}")
print(f"- Números impares: {oddNum}")
print(f"- Números positivos: {posNum}")
print(f"- Números negativos: {negNum}")
print("---------------")
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("# Actividad 9 ")
count = 0
maxRange = 100
for i in range(0, maxRange):
    num = int(input("Ingresa un número: "))
    count += num
print(f"- La media de todos los números es {count / maxRange}")
print("---------------")
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("# Actividad 10 ")
num = input("Ingresa un número: ")
print(f"El número ingresado {num} quedo al revés {int(num[::-1])} !")
print("---------------")