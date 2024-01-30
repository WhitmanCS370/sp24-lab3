import sys


# [bytes]
def same_bytes(left_name, right_name):
    """
    Compares two files as bytes
    Returns boolean true if files are the same
    """
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes
# [/bytes]


# [main]
def find_duplicates(filenames):
    """
    Compares a list of files to each other
    Returns matchin files 
    """
    matches = []
    for left in filenames:
        for right in filenames:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


# [dup]
def find_duplicates_unique(filenames):
    """
    Compers list of files to each other without any redudndant coparisons
    Returns matching files
    """
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches
# [/dup]

if __name__ == "__main__":
    duplicates = find_duplicates(sys.argv[1:]) # command line arguemnt
    for (left, right) in duplicates: # prints the duplicate files found
        print(left, right)
# [/main]
