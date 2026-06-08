from pathlib import Path


def count_words_by_length(filename):
    lengths = {}

    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                word = word.strip('.,!?;:"()[]{}').lower()
                n = len(word)
                if n == 0:
                    continue
                lengths[n] = lengths.get(n, 0) + 1

    for length, count in sorted(lengths.items()):
        print(f'{length}-letter words: {count}')


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
count_words_by_length(file_path)