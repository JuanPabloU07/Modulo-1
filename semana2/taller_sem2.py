#Definición de listas y variables
user_election = 0
inventory = []
all_prices = []
all_quantity = []

#Inicio del ciclo y mostrar el menú principal
while True:
    print("")
    print("\033[95m-- MENÚ INVENTARIO --\033[0m")
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
            print("\033[91m¡ERROR!. Número no contemplado en la lista.\033[0m")

#Sección para agregar producto y la información (nombre, precio y cantidad)
        elif user_election == 1:
            while True:
                try:
                    quantity = int(input("¿Cuántos productos desea ingresar?: "))
                    if quantity <= 0:
                        print("\033[91m¡ERROR!. Ingrese un número positivo y diferente a 0.\033[0m")
                        continue
                    else:
                        for i in range(quantity):
                            product = {}
                            print("")
                            print(f"\033[96mProducto #{i+1}\033[0m")
                            name_product = input("Nombre: ")
                            product["nombre"] = name_product
                            while True:
                                try:
                                    price_product = float(input("Precio: "))
                                    if price_product <= 0:
                                        print("\033[91m¡ERROR!. El precio debe ser mayor a $0.\033[0m")
                                        continue
                                    else:
                                        product["precio"] = price_product
                                    break
                                except ValueError:
                                    print("\033[91m¡ERROR!. Debe ingresar un número.\033[0m")
                            while True:
                                try:
                                    quantity_product = int(input("Cantidad: "))
                                    if quantity_product <= 0:
                                        print("\033[91m¡ERROR!. La cantidad debe ser mayor a 0.\033[0m")
                                        continue
                                    else:
                                        total_price = price_product * quantity_product
                                        all_prices.append(total_price)
                                        all_quantity.append(quantity_product)
                                        product["cantidad"] = quantity_product
                                    break
                                except ValueError:
                                    print("\033[91m¡ERROR!. Debe ingresar un número.\033[0m")
                            inventory.append(product)
                    break
                except ValueError:
                    print("\033[91m¡ERROR!. Debe ingresar un número entero.\033[0m")

#Sección para mostrar el inventario con todos sus elementos
        elif user_election == 2:
            if len(inventory) == 0:
                print("\033[93m¡El inventario está vacío!\033[0m")
            else:
                for product in inventory:
                    print(f"\033[92mNombre: {product["nombre"]} | Precio: {product["precio"]} | Cantidad: {product["cantidad"]}\033[0m")

#Sección para mostrar las estadísticas totales
        elif user_election == 3:
            total_prices = sum(all_prices)
            total_quantity = sum(all_quantity)
            print(f"\033[92mValor total del inventario: {total_prices}\033[0m")
            print(f"\033[92mCantidad total de productos ingresados: {total_quantity}\033[0m")

#Sección para salir de ciclo y cerrar el programa
        else:
            print("\033[94mUsted eligió salir, ¡CHAO!\033[0m")
            break
    except ValueError:
        print("")
        print("\033[91m¡ERROR!. Debe ingresar un número entero.\033[0m")