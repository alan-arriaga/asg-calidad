import sys
import time
import re

def count_words(text):
    word_frequency = {}
    word = ""
    for char in text:
        if char.isalnum() or char == "'":
            word += char.lower()
        else:
            if word:
                word_frequency[word] = word_frequency.get(word, 0) + 1
                word = ""
    if word:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def process_file(file_path):
    word_frequency = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    line_frequency = count_words(line)
                    for word, count in line_frequency.items():
                        word_frequency[word] = word_frequency.get(word, 0) + count
                except Exception as e:
                    print(f"Error processing line '{line.strip()}': {e}")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return word_frequency

def save_results_to_file(results, output_file, elapsed_time):
    with open(output_file, 'w') as file:
        file.write("Word\tFrequency\n")
        for word, frequency in sorted(results.items()):
            file.write(f"{word}\t{frequency}\n")
        file.write(f"\nExecution Time: {elapsed_time:.4f} seconds\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    print(f"Processing file: {file_path}")
    word_frequency = process_file(file_path)

    elapsed_time = time.time() - start_time

    # Display results
    print("\nWord\tFrequency")
    for word, frequency in sorted(word_frequency.items()):
        print(f"{word}\t{frequency}")

    print(f"\nExecution Time: {elapsed_time:.4f} seconds")

    # Save results to file
    output_file = "WordCountResults.txt"
    save_results_to_file(word_frequency, output_file, elapsed_time)

    print(f"Results have been saved to '{output_file}'.")

if __name__ == "__main__":
    main()
