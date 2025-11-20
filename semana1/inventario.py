#Mensaje de guía y contextualización para el usuario.
print("Bienvenido al software de Inventario")

#Solicitud de información al usurio
print("Escriba los siguientes datos del producto a ingresar")
nombre = input("Nombre: ")

#Bucle cuyo objetivo solicitar un dato y validar el formato del mismo
while True:
    try:
        precio = float(input("Precio: "))
        break
    except ValueError:
        print("El precio debe ser un valor numérico con decimales. Intentar de nuevo.")

#Bucle cuyo objetivo solicitar un dato y validar el formato del mismo
while True:
    try:
        cantidad = int(input("Cantidad: "))
        break
    except ValueError:
        print("La cantidad debe ser un valor númerico. Intentar de nuevo.")

#Operar matemáticamente la información para encontrar el costo total
costo_total = precio*cantidad

#Mostrar al usuario un resumen del producto ingresado
print(f"Usted ingresó: Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

#Este ejercicio práctico es un software que buscar ingresar información de producto a un sistema de inventario. Las funciones "Try" y "Except". Este tema se vio en clase y reforce en internet.