from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

def menu():
    inventario = []

    while True:
        print("""--- MENÚ PRINCIPAL ---
        1. Agregar producto
        2. Mostrar inventario
        3. Buscar producto
        4. Actualizar producto
        5. Eliminar producto
        6. Estadísticas
        7. Guardar CSV
        8. Cargar CSV
        9. Salir
        """)

        opcion = input("Elige una opción: ")
## isdigit verifica si es un número entero positivo y valida la entrada del usuario
        if not opcion.isdigit() or not (1 <= int(opcion) <= 9):
            print("Opción inválida.\n")
            continue

        opcion = int(opcion)

        if opcion == 1:
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    raise ValueError
            except ValueError:
                print("Error: precio y cantidad deben ser numéricos y no negativos.")
                continue

            agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto agregado.\n")

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre = input("Buscar nombre: ")
            p = buscar_producto(inventario, nombre)
            if p:
                print("Encontrado:", p)
            else:
                print("Producto no encontrado.")

        elif opcion == 4:
            nombre = input("Nombre a actualizar: ")
            if not buscar_producto(inventario, nombre):
                print("No existe ese producto.")
                continue

            try:
                nuevo_precio = input("Nuevo precio (enter para dejar igual): ")
                nueva_cantidad = input("Nueva cantidad (enter para dejar igual): ")

                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            except ValueError:
                print("Datos inválidos.")
                continue

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            print("Producto actualizado.\n")

        elif opcion == 5:
            nombre = input("Nombre a eliminar: ")
            if eliminar_producto(inventario, nombre):
                print("Producto eliminado.")
            else:
                print("No existe ese producto.")

        elif opcion == 6:
            stats = calcular_estadisticas(inventario)
            if not stats:
                print("Inventario vacío.")
            else:
                print("\n--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total: {stats['valor_total']:.2f}")
                print(f"Producto más caro: {stats['producto_mas_caro']['nombre']} "
                      f"(${stats['producto_mas_caro']['precio']})")
                print(f"Mayor stock: {stats['producto_mayor_stock']['nombre']} "
                      f"({stats['producto_mayor_stock']['cantidad']} unidades)\n")

        elif opcion == 7:
            ruta = input("Ruta del archivo CSV a guardar: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta del CSV a cargar: ")
            productos, errores = cargar_csv(ruta)

            if productos is None:
                continue

            print(f"{len(productos)} productos cargados. {errores} filas inválidas omitidas.")

            decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

            if decision == "S":
                inventario = productos
                print("Inventario reemplazado.")
            else:
                print("Fusión: se suman cantidades y se actualiza precio si difiere.")
                for nuevo in productos:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        existente["cantidad"] += nuevo["cantidad"]
                        existente["precio"] = nuevo["precio"]
                    else:
                        inventario.append(nuevo)

        elif opcion == 9:
            print("Saliendo del programa...")
            break

    return

if __name__ == "__main__":
    menu()
