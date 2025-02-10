import json
import time


def load_json(file_path):
    """Carga de informacion de archivos JSON y manejo de errores."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error cargando el archivo {file_path}: {e}")
        return None


def create_price_lookup(price_catalogue):
    """Creacion de diccionario de titulo y precio."""
    price_lookup = {}
    for item in price_catalogue:
        if "title" in item and "price" in item:
            price_lookup[item["title"]] = item["price"]
    return price_lookup


def compute_total_sales(price_catalogue, sales_record):
    """Calculo del costo total de ventas."""
    total_cost = 0.0
    errors = []
    price_lookup = create_price_lookup(price_catalogue)

    for sale in sales_record:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_lookup:
            errors.append(f"Producto '{product}' no fue encontrado.")
            continue

        if not isinstance(quantity, (int, float)):
            errors.append(f"Cantidad invalida para '{product}': {quantity}")
            continue

        total_cost += price_lookup[product] * quantity

    return total_cost, errors


def main():
    """Codigo principal."""
    price_file = input("Introduce el nombre del catalogo de precios: ")
    sales_file = input("Introduce el nombre del catalogo de ventas: ")

    start_time = time.time()

    price_catalogue = load_json(price_file)
    sales_record = load_json(sales_file)

    if price_catalogue is None or sales_record is None:
        return

    total_cost, errors = compute_total_sales(price_catalogue, sales_record)

    elapsed_time = time.time() - start_time

    result_text = f"Costo total de ventas: ${total_cost:.2f}\n"
    result_text += f"Tiempo de ejecucion:{elapsed_time:.4f} segundos\n"

    print(result_text)
    if errors:
        print("Errores encontrados:")
        for error in errors:
            print(f"- {error}")

    with open("SalesResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(result_text)
        if errors:
            result_file.write("Errores encontrados:\n")
            for error in errors:
                result_file.write(f"- {error}\n")


if __name__ == "__main__":
    main()
