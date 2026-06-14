from pathlib import Path

def wordcount(file_path):
    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()

    for one_line in open(file_path):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())

    counts['unique words'] = len(unique_words)

    for key, value in counts.items():
        print(f'{key}: {value}')


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
wordcount(file_path)