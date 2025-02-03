#pylint: disable=invalid-name
"""
Codigo para obtener metricos de archivos de datos
"""
import sys
import time

def read_numbers_from_file(filename):
    """
    Codigo para obtener los valores del archivo de texto
    """
    numbers = []
    errors = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    errors.append(f"Invalid data: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers, errors


def compute_mean(numbers):
    """
    Codigo para obtener el promedio
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0

def compute_median(numbers):
    """
    Codigo para obtener la mediana
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def compute_mode(numbers):
    """
    Codigo para obtener la moda
    """
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values(), default=0)
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes

def compute_variance(numbers, mean):
    """
    Codigo para obtener la varianza
    """
    n = len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / n if n > 0 else 0

def compute_std_dev(variance):
    """
    Codigo para obtener la desviacion  estandar
    """
    return variance ** 0.5

def write_results_to_file(results):
    """
    Codigo para guardar los resultados en el archivo StatisticsResults.txt
    """
    with open("StatisticsResults.txt", "w", encoding='utf-8') as file:
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
    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_std_dev(variance)
    elapsed_time = time.time() - start_time
    results = (f"Mean: {mean}\n"
               f"Median: {median}\n"
               f"Mode: {mode}\n" 
               f"Standard Deviation: {std_dev}\n"
               f"Variance: {variance}\n"
               f"Execution Time: {elapsed_time:.4f} seconds\n"
               f"Numeros encontrados: {len(numbers)}\n"
               f"Errores encontrados: {len(errors)}\n")
    print(results)
    write_results_to_file(results)
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(error)
if __name__ == "__main__":
    main()
