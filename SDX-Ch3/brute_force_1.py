import sys


# [bytes]
def same_bytes(left_name, right_name):
    #opens the left and right files and returns whether or not the bites are the same
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes
# [/bytes]


# [main]
def find_duplicates(filenames):
    matches = []
    #for every character in the left file it goes through every character in the right file.
    for left in filenames:
        for right in filenames:
            #for each of these pairs of characters it calls the same bytes function
            if same_bytes(left, right):
                #if they are the same then append the match to the list matches
                matches.append((left, right))
    return matches


if __name__ == "__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)
# [/main]
