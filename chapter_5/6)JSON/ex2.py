import json

def passwd_to_json_tuple(passwd_path='/etc/passwd', json_path='passwd.json'):
    with open(passwd_path) as f:
        lines = f.readlines()
    data = [tuple(line.strip().split(':')) for line in lines]
    with open(json_path, 'w') as out:
        json.dump(data, out, indent=2)

passwd_to_json_tuple()