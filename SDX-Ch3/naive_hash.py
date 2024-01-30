# [hash]
def naive_hash(data):
    return sum(data) % 13
# [/hash]

# Implement the naive_hash function
# by summing the bytes of the input data
# and returning the result modulo 13.
if __name__ == "__main__":
    # [example]
    example = bytes("hashing", "utf-8")
    for i in range(1, len(example) + 1):
        substring = example[:i]
        hash = naive_hash(substring)
        print(f"{hash:2} {substring}")
    # [/example]

result = naive_hash(bytes("what", "utf-8"))
print(result)