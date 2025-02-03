#pylint: disable=invalid-name
"""
Codigo para convertir numeros
"""
import time
import sys

def decimal_to_binary(n):
    """ 
    Codigo para convertir de decimal a binario
    """
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def decimal_to_hexadecimal(n):
    """
    Codigo para convertir de decimal a hexadecimal
    """
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

def read_numbers_from_file(filename):
    """
    Codigo para adquirir la informacion del archivo
    """
    numbers = []
    errors = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    errors.append(f"Invalid data: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers, errors

def write_results_to_file(results):
    """
    Codigo para escribir los resultados en un archivo
    """
    with open("ConvertionResults.txt", "w", encoding='utf-8') as file:
        file.write(results)

def main():
    """
    Codigo principal del programa
    """
    filename = input("Enter the filename: ")
    start_time = time.time()
    numbers, errors = read_numbers_from_file(filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)
    results = ""
    for num in numbers:
        binary = decimal_to_binary(num)
        hexadecimal = decimal_to_hexadecimal(num)
        results += f"Decimal: {num} | Binary: {binary} | Hexadecimal: {hexadecimal}\n"
    elapsed_time = time.time() - start_time
    results += f"Execution Time: {elapsed_time:.4f} seconds\n"
    print(results)
    write_results_to_file(results)
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(error)
if __name__ == "__main__":
    main()
