import sys
from hashlib import sha256
from os.path import exists

CHECKFILE = "./known_hashes"

# TODO modify to only accept sound type files
def find_dups(filenames):
    # check if repo of file hashes exists. better hope it does! jk, it just makes one if not
    if not exists(CHECKFILE):
        open(CHECKFILE, "w").close()
    hashes = open(CHECKFILE, "r").read()
    fn_hashes = []
    matches = []
    # for each file in the list, check if its hash is in the list already
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        # if so, its a duplicate and we want to report it
        if hash_code in hashes:
            matches.append(fn)
        # if not we'll want to add it later
        elif hash_code not in fn_hashes:
            fn_hashes.append(hash_code)
        # or it might match one we've seen previously this run
        else:
            matches.append(fn)
    # append new hashes to checkfile
    checkfile = open(CHECKFILE, "a")
    for hash in fn_hashes:
        checkfile.write(hash + '\n')
    checkfile.close()
    return matches

# call from command line with each file to parse as an argument.

if __name__ == "__main__":
    matches = find_dups(sys.argv[1:])
    for match in matches:
        print("duplicate detected: " + match)