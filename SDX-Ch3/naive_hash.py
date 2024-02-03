# [hash]
def naive_hash(data):
    return sum(data) % 13
# [/hash]


# prints out the hash result of different substrings of the string "hashing"
if __name__ == "__main__":
    # [example]
    example = bytes("hashing", "utf-8")
    for i in range(1, len(example) + 1):
        substring = example[:i]
        hash = naive_hash(substring)
        print(f"{hash:2} {substring}")
    # [/example]

# what is this? when is it called? removing until someone makes a case for it
# (or something breaks lol)
'''
result = naive_hash(bytes("what", "utf-8"))
print(result)
'''