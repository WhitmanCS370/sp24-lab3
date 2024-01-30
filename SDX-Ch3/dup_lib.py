import sys
from hashlib import sha256

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

def compare_to_known(filename):
    # hash a new file and compare it against existing hash values in known_files.txt
    data = open(filename, "rb").read()
    known_files = open("known_files.txt" "rb").read()
    hash_code = sha256(data).hexdigest()
    if hash_code in known_files:
        print(filename + " may be identical with existing file")
if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))

