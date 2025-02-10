import json
import sys
import time

def load_json(file_path):
    """Load JSON data from a file, handling errors gracefully."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return None

def compute_total_sales(price_catalogue, sales_record):
    """Compute the total cost of all sales based on the price catalogue."""
    total_cost = 0.0
    errors = []
    
    for sale in sales_record:
        product = sale.get("product")
        quantity = sale.get("quantity")
        
        if product not in price_catalogue:
            errors.append(f"Product '{product}' not found in catalogue.")
            continue
        
        if not isinstance(quantity, (int, float)) or quantity < 0:
            errors.append(f"Invalid quantity for product '{product}': {quantity}")
            continue
        
        total_cost += price_catalogue[product] * quantity
    
    return total_cost, errors

def main():
    """Main function to execute the program."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    
    price_file = sys.argv[1]
    sales_file = sys.argv[2]
    
    start_time = time.time()
    
    price_catalogue = load_json(price_file)
    sales_record = load_json(sales_file)
    
    if price_catalogue is None or sales_record is None:
        sys.exit(1)
    
    total_cost, errors = compute_total_sales(price_catalogue, sales_record)
    
    elapsed_time = time.time() - start_time
    
    result_text = f"Total Sales Cost: ${total_cost:.2f}\nExecution Time: {elapsed_time:.4f} seconds\n"
    
    print(result_text)
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(f"- {error}")
    
    with open("SalesResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(result_text)
        if errors:
            result_file.write("Errors encountered:\n")
            for error in errors:
                result_file.write(f"- {error}\n")

if __name__ == "__main__":
    main()
