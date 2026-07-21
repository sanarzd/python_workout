from pathlib import Path


def encrypt_file(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, "w") as outfile:
        for line in infile:
            for ch in line:
                outfile.write(str(ord(ch)) + " ")


def decrypt_file(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, "w") as outfile:
        for line in infile:
            numbers = line.split()

            for num in numbers:
                outfile.write(chr(int(num)))


base_dir = Path(__file__).resolve().parent

input_path = base_dir / "input.txt"
encrypt_path = base_dir / "encrypt.txt"
output_path = base_dir / "output.txt"

encrypt_file(input_path, encrypt_path)
decrypt_file(encrypt_path, output_path)

print("Encryption completed.")
print("Decryption completed.")