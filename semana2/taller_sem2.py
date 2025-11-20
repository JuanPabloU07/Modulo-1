#Definición de listas y variables
user_election = 0
inventory = []
all_prices = []
all_quantity = []

#Inicio del ciclo y mostrar el menú principal
while True:
    print("")
    print(" MENÚ INVENTARIO ")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("")

#Solicitar al usuario ingresar la selección del menú y sus respectivas validaciones
    try:
        user_election = int(input("Escriba el número de la opción seleccionada: "))
        print("")
        if user_election <= 0 or user_election > 4:
            print("¡ERROR!. Número no contemplado en la lista.")

#Sección para agregar producto y la información (nombre, precio y cantidad)
        elif user_election == 1:
            while True:
                try:
                    quantity = int(input("¿Cuántos productos desea ingresar?: "))
                    if quantity <= 0:
                        print("¡ERROR!. Ingrese un número positivo y diferente a 0.")
                        continue
                    else:
                        for i in range(quantity):
                            product = {}
                            print("")
                            print(f"Producto #{i+1}")
                            name_product = input("Nombre: ")
                            product["nombre"] = name_product
                            while True:
                                try:
                                    price_product = float(input("Precio: "))
                                    if price_product <= 0:
                                        print("¡ERROR!. El precio debe ser mayor a $0.")
                                        continue
                                    else:
                                        product["precio"] = price_product
                                    break
                                except ValueError:
                                    print("[91m¡ERROR!. Debe ingresar un número.")
                            while True:
                                try:
                                    quantity_product = int(input("Cantidad: "))
                                    if quantity_product <= 0:
                                        print("¡ERROR!. La cantidad debe ser mayor a 0.")
                                        continue
                                    else:
                                        total_price = price_product * quantity_product
                                        all_prices.append(total_price)
                                        all_quantity.append(quantity_product)
                                        product["cantidad"] = quantity_product
                                    break
                                except ValueError:
                                    print("¡ERROR!. Debe ingresar un número.")
                            inventory.append(product)
                    break
                except ValueError:
                    print("¡ERROR!. Debe ingresar un número entero.")

#Sección para mostrar el inventario con todos sus elementos
        elif user_election == 2:
            if len(inventory) == 0:
                print("¡El inventario está vacío!")
            else:
                for product in inventory:
                    print(f"Nombre: {product["nombre"]} | Precio: {product["precio"]} | Cantidad: {product["cantidad"]}")

#Sección para mostrar las estadísticas totales
        elif user_election == 3:
            total_prices = sum(all_prices)
            total_quantity = sum(all_quantity)
            print(f"Valor total del inventario: {total_prices}")
            print(f"Cantidad total de productos ingresados: {total_quantity}")

#Sección para salir de ciclo y cerrar el programa
        else:
            print("Usted eligió salir, ¡CHAO!")
            break
    except ValueError:
        print("")
        print("¡ERROR!. Debe ingresar un número entero.")