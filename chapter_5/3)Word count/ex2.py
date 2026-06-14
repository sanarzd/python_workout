from pathlib import Path

def count_selected_words(file_path, user_words):
    word_counts = {word: 0 for word in user_words}
    for one_line in open(file_path):
        for word in one_line.split():
            if word in word_counts:
                word_counts[word] += 1
    return word_counts


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
result = count_selected_words(file_path, ['It', 'contains', 'This', 'is', 'file'])
for word, count in result.items():
    print(f"'{word}': {count}")