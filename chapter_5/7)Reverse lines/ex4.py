from pathlib import Path


def shells_by_users(infilename, outfilename):
    shells = {}

    with open(infilename) as infile:
        for line in infile:
            parts = line.strip().split(":")

            username = parts[0]
            shell = parts[-1]

            if shell not in shells:
                shells[shell] = []

            shells[shell].append(username)

    with open(outfilename, "w") as outfile:
        for shell in shells:
            outfile.write(shell + ":")

            users = shells[shell]

            for i in range(len(users)):
                outfile.write(users[i])

                if i != len(users) - 1:
                    outfile.write(", ")

            outfile.write("\n")


base_dir = Path(__file__).resolve().parent

passwd_path = base_dir / "passwd.txt"
shells_path = base_dir / "shells.txt"

shells_by_users(passwd_path, shells_path)

print("Output file created.")