import sys
import time
from decimal import Decimal

def decimal_to_binary(number):
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def decimal_to_hexadecimal(number):
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        remainder = number % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        number //= 16
    return hexadecimal

def process_file(file_path):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    number = int(Decimal(line))
                    binary = decimal_to_binary(number)
                    hexadecimal = decimal_to_hexadecimal(number)
                    results.append((line, binary, hexadecimal))
                except Exception as e:
                    print(f"Invalid entry ignored: {line}")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return results

def save_results_to_file(results, output_file):
    with open(output_file, 'w') as file:
        file.write("Decimal\tBinary\tHexadecimal\n")
        for decimal, binary, hexadecimal in results:
            file.write(f"{decimal}\t{binary}\t{hexadecimal}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py <file1> <file2> ... <fileN>")
        sys.exit(1)

    file_paths = sys.argv[1:]
    all_results = []

    start_time = time.time()

    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        results = process_file(file_path)
        all_results.extend(results)

    elapsed_time = time.time() - start_time

    # Display results
    print("\nDecimal\tBinary\tHexadecimal")
    for decimal, binary, hexadecimal in all_results:
        print(f"{decimal}\t{binary}\t{hexadecimal}")

    print(f"\nExecution Time: {elapsed_time:.4f} seconds")

    # Save to file
    output_file = "ConvertionResults.txt"
    save_results_to_file(all_results, output_file)
    with open(output_file, 'a') as file:
        file.write(f"\nExecution Time: {elapsed_time:.4f} seconds\n")

    print(f"Results have been saved to '{output_file}'.")

if __name__ == "__main__":
    main()

