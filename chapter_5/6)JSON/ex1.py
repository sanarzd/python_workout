from pathlib import Path
import json

def print_scores(dirname):
    scores = {}
    base_dir = Path(__file__).resolve().parent
    for filename in (base_dir / dirname).glob('*.json'):
        scores[str(filename)] = {}
        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[str(filename)].setdefault(subject, [])
                    scores[str(filename)][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = sum(subject_scores) / len(subject_scores)
            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

if __name__ == '__main__':
    print_scores('scores')