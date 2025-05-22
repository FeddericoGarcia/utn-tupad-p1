#---------TUPaD---------
#------PROGRAMACION-1---
#---TRABAJO-PRACTICO----
#-PROFESOR:ARIEL-ENFERREL
#-ALUMNO:FEDERICO-GARCIA-BENGOLEA
#-COMISION: M2025-14
#-FECHA: 22/05/2025
#-
#----------- FUNCIONES DEL ENUNCIADO -----------
#-
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
print("- Ejercicio 1 -")
def fact_recursive(num):
    return 1 if num == 0 or num == 1 else num * fact_recursive(num-1)

def show_fact():
    num = int(input("Ingresa un número: "))
    for i in range(1, num+1):
        print(f"{i} - {fact_recursive(i)}")

show_fact()
print("--------------------------")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
print("- Ejercicio 2 -")
def recursive_fibonacci(pos):
    if pos == 0: 
        return 0
    elif pos == 1:
        return 1
    else:
        return recursive_fibonacci(pos - 1) + recursive_fibonacci(pos - 2) 


def show_fibonacci(num):
    newFibo = ""
    for i in range(1, num + 1):
        newFibo += f"{recursive_fibonacci(i)} - "
    return newFibo[:-2]


num = int(input("Ingresa un número: "))
print(f"El restulado de la seríe fabonacci hasta {num} es: {show_fibonacci(num)}")
print("--------------------------")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛(𝑚) = 𝑛 ∗ 𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general.
print("- Ejercicio 3 -")
def recursive_potency(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * recursive_potency(base, exponent -1)
    
base = int(input("Ingresa el valor de la base: "))
exponent = int(input("Ingresa el valor del exponente: "))

print(f"- El valor base {base} elevado a {exponent} es: {recursive_potency(base, exponent)}")
print("--------------------------")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. 
print("- Ejercicio 4 -")
def recursive_binary_conversion(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return recursive_binary_conversion(num // 2) + str( num % 2)
    
num = int(input("Ingresa un valor para convertirlo a binario: "))
print(f"- El resutlado es: {recursive_binary_conversion(num)}")
print("--------------------------")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
print("- Ejercicio 5 -")
def is_palindrome(word):
    if len(word) == 0:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])
    
word = input("Ingresa una palabra palíndroma: ")
print(f"¿Tu palabra '{word}' es palindroma?: {is_palindrome(word)}")
print("--------------------------")
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
print("- Ejercicio 6 -")
def add_digits(num):
    if num // 10 == 0:
        return num
    else:
        return num % 10 + add_digits(num // 10)

def verify(num):
    return num if num > 0 else verify(int(input("Ingresa un número entero positivo: ")))

num = int(input("Ingresa un número: "))
verified = verify(num)
print(f"- La suma de los dígitos de {verified} es {add_digits(verified)}")
print("--------------------------")
# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
print("- Ejercicio 7 -")
def block_count(num):
    if num == 0:
        return 0
    else:
        return num + block_count(num - 1)

num = int(input("Ingresa la cantidad de bloques que usaras en la base de la piramide: "))
print(f"- Con la base de {num} necesitaras un total de {block_count(num)} bloques!")
print("--------------------------")
# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
print("- Ejercicio 8 -")
def digit_count(num, digit):
    if num // 10 == 0:
        return 1 if num == digit else 0
    else:
        return (1 if num % 10 == digit else 0) + digit_count(num // 10, digit)

num = verify(int(input("Ingresa un número grande: ")))
digit = int(input("Ingresa un dígito: "))
digitOk = digit if digit > 0 and digit < 9 else int(input("Ingresa un dígito entre 0 y 9: "))
print(f"- El dígito {digitOk} aparece {digit_count(num, digitOk)} veces")
print("--------------------------")