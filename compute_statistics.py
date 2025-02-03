import sys
import time
from collections import Counter
from decimal import Decimal, getcontext

# Set precision to handle large numbers accurately
getcontext().prec = 50

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else Decimal(0)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n == 0:
        return "#N/A"
    midpoint = n // 2
    return numbers[midpoint] if n % 2 == 1 else (numbers[midpoint - 1] + numbers[midpoint]) / 2

def calculate_mode(numbers):
    if not numbers:
        return "#N/A"
    frequency = Counter(numbers)
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else "#N/A"

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers) if numbers else Decimal(0)

def calculate_standard_deviation(variance):
    return variance.sqrt() if variance else Decimal(0)

def process_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = Decimal(line.strip())
                    numbers.append(number)
                except:
                    print(f"Invalid entry ignored: {line.strip()}")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return numbers

def compute_statistics(file_paths):
    results = [["TC", "COUNT", "MEAN", "MEDIAN", "MODE", "SD", "VARIANCE"]]
    for i, file_path in enumerate(file_paths, start=1):
        numbers = process_file(file_path)
        if not numbers:
            results.append([f"TC{i}", "#N/A", "#N/A", "#N/A", "#N/A", "#N/A", "#N/A"])
            continue

        mean = calculate_mean(numbers)
        median = calculate_median(numbers)
        mode = calculate_mode(numbers)
        variance = calculate_variance(numbers, mean)
        std_dev = calculate_standard_deviation(variance)

        results.append([
            f"TC{i}",
            len(numbers),
            f"{mean:.2E}",
            f"{median:.2E}" if median != "#N/A" else "#N/A",
            mode,
            f"{std_dev:.2E}",
            f"{variance:.2E}"
        ])

    return results

def save_results_to_file(results, output_file):
    with open(output_file, 'w') as file:
        for row in results:
            file.write("\t".join(map(str, row)) + "\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py <file1> <file2> ... <fileN>")
        sys.exit(1)

    file_paths = sys.argv[1:]
    start_time = time.time()

    results = compute_statistics(file_paths)
    elapsed_time = time.time() - start_time

    results.append(["Execution Time", f"{elapsed_time:.4f} seconds"])

    # Display results
    for row in results:
        print("\t".join(map(str, row)))

    # Save to file
    output_file = "StatisticsResults.txt"
    save_results_to_file(results, output_file)
    print(f"\nResults have been saved to '{output_file}'.")

if __name__ == "__main__":
    main()
