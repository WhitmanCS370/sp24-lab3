import sys
from hashlib import sha256

def find_groups(filenames):
    # empty list
    groups = {}
    # go through filenames
    for fn in filenames:
        # open as read-bytes (binary mode)
        data = open(fn, "rb").read()
        # creating a hash code
        hash_code = sha256(data).hexdigest()

        # makes a set for empty groups.
        if hash_code not in groups:
            groups[hash_code] = set()
        # adds it to groups.
        groups[hash_code].add(fn)
    # return it.
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))
