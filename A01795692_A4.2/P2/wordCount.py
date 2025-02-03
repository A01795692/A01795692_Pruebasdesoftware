import time
import sys

def read_words_from_file(filename):
    """Read words from a file and count their frequency."""
    word_count = {}
    errors = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
                    if cleaned_word:
                        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return word_count, errors

def write_results_to_file(results):
    """Write the word frequency results to a file."""
    with open("WordCountResults.txt", "w", encoding='utf-8') as file:
        file.write(results)

def main():
    filename = input("Enter the filename: ")
    start_time = time.time()
    
    word_count, errors = read_words_from_file(filename)
    
    if not word_count:
        print("No valid words found in the file.")
        sys.exit(1)
    
    results = "Word Frequency:\n"
    for word, count in sorted(word_count.items()):
        results += f"{word}: {count}\n"
    
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
