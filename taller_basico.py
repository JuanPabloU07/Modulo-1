# 1 .Fundamentos y Variables
# 1. nombre y edad del usuario
name = input("Ingrese su nombre : ")
age = input("Ingrese su edad : ")

print(f"Hola {name} tienes {age} años.")
print("-----------------------------------")
# 2. suma de dos numeros 
print(45 + 10)
print(40 - 30)
print(6 * 7)
print(10 / 3)
print(45 % 10)
print("-----------------------------------")
#3. area de un triangulo
base = float(input("Ingresa la base del triángulo: "))

altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2

print(f"El área del triángulo es: {area}")
print("--------------------------------")
# 4. conversor de grados celsius a fahrenheit
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C es igual a {fahrenheit}°F")
print("-------------------------------")

# 5. tipo de dato con type
x = 10
y = 5.6
z = "Juan"
k = True

print(type(x), type(y), type(z), type(k))
print("----------------------------------")

# 6. Edad futura
edad_actual = int(input("¿Cuántos años tienes? "))

edad_futura = edad_actual + 10

print(f"En 10 años tendrás {edad_futura} años.")
print("------------------------")

# 2. Nivel 2 — Condicionales
# 7. Mayor de edad
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
print("------------------------")

# 8. Poaitivo, negativo o cero
numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
print("------------------------")    

# 9. Par o inpar
numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
print("------------------------")

# 10. Calculadora
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print("Operaciones disponibles: +, -, *, /")
operacion = (input("Elige una operación: "))

if operacion == "+":
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división es: {resultado}")
    else:
        print("Error: no se puede dividir entre cero.")
else:
    print("Operación no válida.")
print("-------------------------")

# 11. Calificaciónes
nota = float(input("Ingresa tu nota (0 a 5): "))

if nota >= 4:
    print("Excelente")
elif nota >= 2:
    print("Aprobado")
else:
    print("Reprobado")
print("-------------------------")

# 12. Comparador mayor y menor
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print("---------------------------")

# 3. Nivel 3 — Bucles y Repetición
# 13. Contar del 1 al 10
for i in range(1, 11):
    print(i)
print("---------------------------")

# 14. Sumatoria del 1 al n.
n = int(input("Ingresa un número: "))

suma = 0

for i in range(1, n + 1):
    suma += i 

print(f"La suma de los números del 1 al {n} es: {suma}")
print("---------------------------")

# 15. Tabla de multiplicar
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")
print("---------------------------")

# 16. Contador regresivo con while
numero = int(input("Ingresa el número desde donde quieres iniciar la cuenta regresiva: "))

print("Cuenta regresiva:")

while numero >= 0:
    print(numero)
    numero -= 1 
print("----------------------------")

# 17. Número ramdom
import random 
numero_secreto = random.randint(1, 10)

print("¡Adivina el número entre 1 y 10")

adivinanza = None

while adivinanza != numero_secreto:
    adivinanza = int(input("Ingresa tu intento: "))
    
    if adivinanza < numero_secreto:
        print("Demasiado bajo, intenta otra vez.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto, intenta otra vez.")
    else:
        print("¡Felicidades! Adivinaste el número.")
print("----------------------------")

# 18. Suma hasta que el usuario diga 0
suma = 0
print("Ingresa números para sumarlos. Escribe 0 para terminar.")

while True:
    numero = float(input("Ingresa un número: "))
    
    if numero == 0:
        break  
    
    suma += numero 

print(f"La suma total es: {suma}")
print("----------------------------")

# 4. Nivel 4 — Listas y Colecciones
# 19. Lista de frutas
frutas = ["manzana", "banana", "naranja", "kiwi", "pera"]

print(frutas)
print("----------------------------")

# 20. Agregar o eliminar frutas
frutas = ["manzana", "banana", "naranja"]

while True:
    print("\nLista de frutas:", frutas)
    print("Opciones:")
    print("1. Agregar fruta")
    print("2. Eliminar fruta")
    print("3. Salir")
    
    opcion = input("Elige una opción (1/2/3): ")
    
    if opcion == "1":
        nueva_fruta = input("Ingresa la fruta a agregar: ")
        frutas.append(nueva_fruta)
        print(f"{nueva_fruta} ha sido agregada.")
        
    elif opcion == "2":
        fruta_eliminar = input("Ingresa la fruta a eliminar: ")
        if fruta_eliminar in frutas:
            frutas.remove(fruta_eliminar)
            print(f"{fruta_eliminar} ha sido eliminada.")
        else:
            print(f"{fruta_eliminar} no está en la lista.")
            
    elif opcion == "3":
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida, intenta de nuevo.")
print("----------------------------")

# 21. Buscar un elemento en la lista
frutas = ["manzana", "banana", "naranja", "kiwi"]
buscar = input("Ingresa la fruta que quieres buscar: ")

if buscar in frutas:
    print(f"{buscar} está en la lista.")
else:
    print(f"{buscar} NO está en la lista.")
print("----------------------------")

# 22. Lista de números y promedio
numeros = [5, 10, 15, 20, 25]
suma = sum(numeros)

promedio = suma / len(numeros)

print("Lista de números:", numeros)
print("Suma:", suma)
print("Promedio:", promedio)
print("----------------------------")

# 23. Lista de números y guardar solo los pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []

for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)

print("Números :", numeros)
print("Números pares:", numeros_pares)
print("----------------------------")

# 24. Eliminar duplicados
numeros = [1, 2, 3, 2, 4, 5, 3, 6, 1]

numeros_sin_duplicados = list(set(numeros))

print("Lista:", numeros)
print("Lista sin dupllicados:", numeros_sin_duplicados)
print("----------------------------")

# 5. Nivel 5 — Retos (Integración de todo)
# 25. Sistema de calificación
nota = float(input("Ingresa la nota del estudiante (0-5): "))

if nota >= 4:
    print("Excelente")
elif nota >= 2:
    print("Aprobado")
else:
    print("Reprobado")
print("----------------------------")

# 26. Carrito de compras
productos = []
precios = []

while True:
    nombre = input("Ingresa el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    precio = float(input(f"Ingresa el precio de {nombre}: "))
    productos.append(nombre)
    precios.append(precio)

print("\nCarrito de compras:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]:.2f}")

total = sum(precios)
print(f"\nTotal a pagar: ${total:.2f}")
print("----------------------------")

# 27. Cajero automatico
saldo = 10000.0

while True:
    print("\nBienvenido al Cajero Automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")

    elif opcion == "2":
        retirar = float(input("Ingresa el monto a retirar: "))
        if retirar <= saldo:
            saldo -= retirar
            print(f"Has retirado ${retirar:.2f}. Saldo restante: ${saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    elif opcion == "3":
        depositar = float(input("Ingresa el monto a depositar: "))
        saldo += depositar
        print(f"Has depositado ${depositar:.2f}. Nuevo saldo: ${saldo:.2f}")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
print("----------------------------")

# 28. Gestión de estudiantes
nombres = []
notas = []

while True:
    print("\nSistema de Gestión de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        nota = float(input("Nota del estudiante (0-5): "))
        nombres.append(nombre)
        notas.append(nota)
        print(f"{nombre} ha sido agregado.")

    elif opcion == "2":
        if nombres:
            print("\nLista de estudiantes:")
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} - Nota: {notas[i]}")
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "3":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
print("----------------------------")

# 29. Calculadora avanzada
import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return 

while True:
    print("\nCalculadora avanzada")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")

    opcion = input("Elige una opción (1-7): ")

    if opcion == "1":
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        print("Resultado:", sumar(x, y))

    elif opcion == "2":
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        print("Resultado:", restar(x, y))

    elif opcion == "3":
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicar(x, y))

    elif opcion == "4":
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        print("Resultado:", dividir(x, y))

    elif opcion == "5":
        x = float(input("Ingresa la base: "))
        y = float(input("Ingresa el exponente: "))
        print("Resultado:", potencia(x, y))

    elif opcion == "6":
        x = float(input("Ingresa el número: "))
        print("Resultado:", raiz_cuadrada(x))

    elif opcion == "7":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
print("----------------------------")

# 30. Agenda de contactos
nombres = []
telefonos = []

while True:
    print("\nAgenda de Contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        nombres.append(nombre)
        telefonos.append(telefono)
        print(f"Contacto {nombre} agregado.")

    elif opcion == "2":
        if nombres:
            print("\nLista de contactos:")
            for i in range(len(nombres)):
                print(f"{i+1}. Nombre: {nombres[i]}, Teléfono: {telefonos[i]}")
        else:
            print("No hay contactos en la agenda.")

    elif opcion == "3":
        buscar = input("Ingresa el nombre del contacto a buscar: ")
        encontrado = False
        for i in range(len(nombres)):
            if nombres[i].lower() == buscar.lower():
                print(f"Nombre: {nombres[i]}, Teléfono: {telefonos[i]}")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el contacto {buscar}.")

    elif opcion == "4":
        print("Saliendo de la agenda. ¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")




