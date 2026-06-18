import os
import json

def directory_stats(dirname):
    data = []

    for filename in os.listdir(dirname):
        fullpath = os.path.join(dirname, filename)
        if os.path.isfile(fullpath):
            stat_result = os.stat(fullpath)
            data.append({
                'filename': filename,
                'size': stat_result.st_size,
                'mtime': stat_result.st_mtime
            })

    with open('directory_stats.json', 'w') as outfile:
        json.dump(data, outfile)

    with open('directory_stats.json') as infile:
        data = json.load(infile)

    smallest = min(data, key=lambda item: item['size'])
    largest = max(data, key=lambda item: item['size'])
    oldest = min(data, key=lambda item: item['mtime'])
    newest = max(data, key=lambda item: item['mtime'])

    print(f"smallest: {smallest['filename']}")
    print(f"largest: {largest['filename']}")
    print(f"oldest: {oldest['filename']}")
    print(f"newest: {newest['filename']}")
    
directory_stats('.')