import csv

def guardar_csv(inventario, ruta, incluir_header=True):

    if not inventario:
        print("No se puede guardar: el inventario está vacío.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=",")
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: no se tiene permiso para escribir en el archivo.")
    except Exception as e:
        print(f"Error desconocido al guardar: {e}")


def cargar_csv(ruta):

    productos = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            encabezado = next(reader, None)
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: encabezado inválido en CSV.")
                return None, 0

            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

                except ValueError:
                    filas_invalidas += 1

        return productos, filas_invalidas

    except FileNotFoundError:
        print("Error: archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error: archivo con codificación no válida.")
    except Exception as e:
        print(f"Error al cargar CSV: {e}")

    return None, 0
