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

def check_sounds(filenames):
    outfile = open("dup_save.out", 'r')
    hash_list  = []
    for i in outfile.readlines():
        hash_list.append(i[:-1])
    #print(hash_list)
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        hash = str(hash_code)
        #print(hash)
        
        if hash not in hash_list:
            save_sound(fn)

def save_sound(filename):
    data = open(filename, "rb").read()
    hash_code = sha256(data).hexdigest()
    print(hash_code)
    outfile = open("dup_save.out", 'a')
    outfile.write(str(hash_code)+"\n")
    outfile.close()

def save_sounds(filenames):
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        print(hash_code)
        #data.close()
        outfile = open("dup_save.out", 'a')
        outfile.write(str(hash_code))
        outfile.close()

if __name__ == "__main__":
    check_sounds(sys.argv[1:])
    # groups = find_groups(sys.argv[1:])
    # for filenames in groups.values():
    #     print(", ".join(sorted(filenames)))
