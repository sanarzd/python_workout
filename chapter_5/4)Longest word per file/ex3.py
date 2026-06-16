from pathlib import Path
import arrow
import os

base_dir = Path(__file__).resolve().parent

for file in base_dir.iterdir():
    if file.is_file():
        print(file.name)

stat_info = os.stat(base_dir)
mtime = arrow.get(stat_info.st_mtime)
print(mtime.humanize())