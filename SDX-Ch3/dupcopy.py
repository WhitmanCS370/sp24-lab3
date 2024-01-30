import sys
from hashlib import sha256

def find_groups(filename):
    groups = {}
    for fn in filename:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

def find_similar_file(filename, file='known_files.txt'):
    groups = {}
    for fn in filename:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        # if hash code in known_files
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for key in groups.keys():
        # CODE GOES HERE
        f = open('known_files.txt', 'a')
        f.write(f'{key}\n')
    f.close()