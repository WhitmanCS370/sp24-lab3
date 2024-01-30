from hashlib import sha256

if __name__ == "__main__":
    # [example]
    # Create a hash of a string
    example = bytes("hash", "utf-8")
    # Create a hash object
    for i in range(1, len(example) + 1):
        substring = example[:i]
        hash = sha256(substring).hexdigest()
        print(f"{substring}\n{hash}")
    # [/example]
