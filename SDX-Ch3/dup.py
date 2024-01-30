import sys
from hashlib import sha256

def find_groups(filenames):
    #creates a dictionary groups
    groups = {}
    #for each file in filenames
    for fn in filenames:
        #open files
        data = open(fn, "rb").read()
        #creates a string for the file
        hash_code = sha256(data).hexdigest()
        if hash_code not in groups:
            #if the string is not in groups then create a set as the value and the hash code as the key
            groups[hash_code] = set()
        #if a set is already created or just created add the file as the value and the hash code as the key.
        groups[hash_code].add(fn)
        
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))

