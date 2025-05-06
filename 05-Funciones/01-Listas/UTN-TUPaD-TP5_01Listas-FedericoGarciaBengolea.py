#---------TUPaD---------
#------PROGRAMACION-1---
#---TRABAJO-PRACTICO----
#-PROFESOR:ARIEL-ENFERREL
#-ALUMNO:FEDERICO-GARCIA-BENGOLEA
#-COMISION: M2025-14
#-FECHA:05/05/2025
#-
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
print("# Actividad 1 ")
list = []
for i in range(0,100,4):
    list.append(i)
print("- Lista: ", list )
print("---------------")
# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!
print("# Actividad 2 ")
list = [1,2,3,4,5]
print("- Lista: ", list )
print("- Mostrando penúltimo elemento en la lista: ", list[-2] )
print("---------------")
# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo: lista_vacia = []
print("# Actividad 3 ")
list = []
print("Escribe 3 palabras ")
for i in range(3):
    list.append(input(f"Ingresa la número {i+1}: "))
print("- Lista: ", list )
print("---------------")
# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]
print("# Actividad 4 ")
animales = ["perro", "gato", "conejo", "pez"]
print("- Lista animales: ", animales)
animales[-3] = "LORO"
animales[-1] = "OSO"
print("- Lista modificada: ", animales)
print("---------------")
# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print("# Actividad 5 ")
numeros=[8,15,3,22,7]
print("- Lista: ", numeros)
numeros.remove(max(numeros))
print("- Lista nueva: ", numeros)
print(f"""- Descripción: El código créa una lista llamada 'numeros' la cual dispone de 5 valores,
a través de la función '.remove()', se busca eliminar un valor de esta lista,
se pasa como parametro otra funcion llamada 'max()' la cual recibe la lista 
y se encarga de buscar el valor más alto para retornarlo. """)
print("---------------")
# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
print("# Actividad 6 ")
list = []
for i in range(10,31,5):
    list.append(i)
print("- Lista: ", list)
for i in range(2):
    print("- Listando los primeros 2 elementos: ", list[i])
print("---------------")
# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]
print("# Actividad 7 ")
autos = ["sedan", "polo", "suran", "gol"]
print("- Lista autos: ", autos)
autos[1] = "GOLF"
autos[2] = "AMAROK"
print("- Lista actualizada: ", autos)
print("---------------")
# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla
print("# Actividad 8 ")
dobles = []
for i in range(5,16,5):
    print("- Número", i)
    dobles.append(i*2)
print("- Lista doble: ", dobles)
print("---------------")
# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
print("# Actividad 9 ")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print("- Lista de compras: ", compras)
# a)
compras[2].append("jugo")
# b)
compras[1][1] = "tallarines"
# c)
compras[0].remove("pan")
# d)
print("- Lista resultante: ", compras)
print("---------------")
# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
print("# Actividad 10 ")
lista_anidada=[15, True, [25.5, 57.9, 30.6], False]
print("- Lista: ", lista_anidada)
print("---------------")
