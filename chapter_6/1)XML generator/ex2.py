from pathlib import Path

def copyfile(source, *targets):
    with open(source, "r") as infile:
        data = infile.read()

    for target in targets:
        with open(target, "w") as outfile:
            outfile.write(data)

base_dir = Path(__file__).resolve().parent

copyfile(
    base_dir / "myfile.txt",
    base_dir / "copy1.txt",
    base_dir / "copy2.txt",
    base_dir / "copy3.txt"
)

print("Files copied successfully.")