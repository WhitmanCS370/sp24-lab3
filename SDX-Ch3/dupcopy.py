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

def add_new_sound(filename, file='known_files.txt'):
    data = open(filename, "rb").read()
    hash_code = sha256(data).hexdigest()
    duplicate = False 
    for code in file.readlines():
        if hash_code == code: 
            duplicate = True
    if not duplicate:
        file = open(file, "a")
        file.write(f"{hash_code}\n")

    return file 


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for key in groups.keys():
        # CODE GOES HERE
        f = open('known_files.txt', 'a')
        f.write(f'{key}\n')
    f.close()