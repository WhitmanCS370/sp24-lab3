import sys
from hashlib import sha256

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        k = open("known_files.txt", "a")
        k.write(hash_code + "\n")
        k.close()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

def check_sounds_hash(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        k = open("known_files.txt", "r")
        klines = k.readlines()
        if( hash_code not in klines) and ( hash_code not in groups):
            groups[hash_code] = set()
        else:
            print(f"{fn} already exists")
            continue
        groups[hash_code].add(fn)
    return groups
        


if __name__ == "__main__":
    groups = check_sounds_hash(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))

