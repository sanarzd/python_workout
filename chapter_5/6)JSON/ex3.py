import json

def passwd_to_json_dict(passwd_path='/etc/passwd', json_path='passwd_dict.json'):
    fields = ['username', 'password', 'uid', 'gid', 'gecos', 'home', 'shell']
    with open(passwd_path) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        parts = line.strip().split(':')
        entry = dict(zip(fields, parts[:len(fields)]))
        data.append(entry)
    with open(json_path, 'w') as out:
        json.dump(data, out, indent=2)
        
passwd_to_json_dict()