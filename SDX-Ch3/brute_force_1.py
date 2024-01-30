import sys

# [main]
def find_duplicates(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
            # added memo aspect.
            if same_bytes(left, right) and [filenames[i], filenames[j]] not in matches:
                matches.append((left, right))
    return matches
    
# [bytes]
def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes
# [/bytes]


if __name__ == "__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)
# [/main]
