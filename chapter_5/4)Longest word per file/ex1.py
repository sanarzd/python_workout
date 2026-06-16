from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

def find_longest_word(filename):
    longest_word = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for one_line in f:
            for one_word in one_line.split():
                if len(one_word) > len(longest_word):
                    longest_word = one_word
    return longest_word

def find_all_longest_words(dirname):
    result = {}
    for file in Path(dirname).iterdir():
        if file.is_file():
            result[file.name] = find_longest_word(file)
    return result

word = find_longest_word(file_path)
print(word, len(word))
