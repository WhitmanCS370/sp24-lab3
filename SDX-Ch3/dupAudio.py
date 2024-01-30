import sys
from hashlib import sha256


def find_groups(filenames):
    groups = {}
    # keep dictionary of groups
    for fn in filenames:
        # for each file that we're trying to find groups in. the files are opened into binary to make them easier to compare.
        data = open(fn, "rb").read()
        # it makes a hash code for the binary of the file, and sha256 means that it's unlikely to generate a common hash code.
        # it uses 32-bit words
        hash_code = sha256(data).hexdigest()
        # if the file name hasn't already been used, then it shouldn't be in groups 'cuz we haven't seen it yet.
        # if the file name is a repeat, then we don't do anything with that file and move on to the next one.
        if hash_code not in groups:
            # if the file wasn't already in groups, then we have to add it.
            # to add it, we need to add the hash code to the groups dictionary, but we set it to an empty set (to save its spot)
            groups[hash_code] = set()
        # since we made a space for it, we can put a new file in the groups dictionary
        # if we've already see file name, then we could also add it but it changes nothing.
        groups[hash_code].add(fn)
    # once we've gone through all of the files send to find_groups, then we returning all of the distinct file names
    # and associated hash codes.
    return groups

# relates to if the dup.py is being imported into another file.
if __name__ == "__main__":
    f = open("known_files.txt", "a")
    groups = find_groups(sys.argv[1:])
    for file in filenames:
        f.write(groups.values())
