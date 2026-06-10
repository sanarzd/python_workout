from pathlib import Path

def get_unique_response_codes(file_path):
    unique_codes = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:
                code = parts[-2]
                if code.isdigit():
                    unique_codes.add(code)

    return unique_codes


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.log'

codes = get_unique_response_codes(file_path)
print("Unique response codes:", sorted(codes))
print("Count:", len(codes))