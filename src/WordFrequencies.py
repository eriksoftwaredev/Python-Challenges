from collections import Counter
import re

def calculate_word_frequencies(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Tokenize the text using regex
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word
    word_count = Counter(words)

    # Calculate total number of words
    total_words = sum(word_count.values())

    # Get the top 20 frequent words along with their occurrences
    top_20_words = word_count.most_common(20)

    return total_words, top_20_words

file_path = "text_file.txt"
total_words, top_20_words = calculate_word_frequencies(file_path)

print("Total words:", total_words)
print("Top 20 frequent words:")
for word, count in top_20_words:
    print(word, "-", count)
