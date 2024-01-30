import sys
from hashlib import sha256

def txt_to_dict(file):
    pass


def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    file_object = open(r"known_files.txt", "w")

    for hash in groups.keys():
        file_object.write(hash + "\n")
        for each in groups[hash]:
            file_object.write(each + "\n")
        file_object.write("\n")
    #    print(", ".join(sorted(filenames)))

