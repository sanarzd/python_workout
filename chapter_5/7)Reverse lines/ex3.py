from pathlib import Path


def split_letters(infilename, vowels_file, consonants_file):
    vowels = "aeiouAEIOU"

    with open(infilename) as infile, \
         open(vowels_file, "w") as vowel_file, \
         open(consonants_file, "w") as consonant_file:

        for line in infile:
            for ch in line:
                if ch.isalpha():
                    if ch in vowels:
                        vowel_file.write(ch)
                    else:
                        consonant_file.write(ch)

            vowel_file.write("\n")
            consonant_file.write("\n")


base_dir = Path(__file__).resolve().parent

input_path = base_dir / "input.txt"
vowels_path = base_dir / "vowels.txt"
consonants_path = base_dir / "consonants.txt"

split_letters(input_path, vowels_path, consonants_path)

print("Files created successfully.")