# A naive hashing implementation (Improvement from O(N^2) but still not O(N)

# Note that 0 bin will be overpopulated due to spacing not being accounted for.

# [hash]
def naive_hash(data):
    return sum(data) % 13
# [/hash]

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