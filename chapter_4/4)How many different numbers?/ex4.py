from pathlib import Path

def get_unique_http_methods(file_path):
    methods = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split('"')
            if len(parts) > 1:
                request_part = parts[1]
                request_items = request_part.split()
                if request_items:
                    methods.add(request_items[0])

    return methods


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.log'

methods = get_unique_http_methods(file_path)
print("HTTP methods:", sorted(methods))
print("Count:", len(methods))