import sys
import json
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

def save_hashes(filenames, output_file = "known_files.json"):
    groups = find_groups(filenames)
    groups = {key: list(value) for key, value in groups.items()}
    with open(output_file, "w") as f:
        f.write(json.dumps(groups))
        #f.write("\n".join(groups.keys()))

def load_hashes(input_file = "known_files.json"):
    with open(input_file, 'r') as f:
        hashes = json.load(f)
        #hashes = f.readlines()
        #hashes = [name.strip() for name in hashes]
    return hashes

def check_files_exists(filenames, input_file):
    existing_hashes = load_hashes(input_file)
    duplicate_files = []
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = str(sha256(data).hexdigest())
        if hash_code in existing_hashes:
            duplicate_files.append((fn, existing_hashes[hash_code]))
    return duplicate_files


if __name__ == "__main__":
    
    print(check_files_exists(sys.argv[1:], "known_files.json"))
    #save_hashes(sys.argv[1:])
    # groups = find_groups(sys.argv[1:])
    # for filenames in groups.values():
    #     print(", ".join(sorted(filenames)))
    
    

