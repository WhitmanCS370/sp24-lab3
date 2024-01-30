# This file gives us an example of how to use one of Pythons built-in cryptographic hashing functions

from hashlib import sha256

if __name__ == "__main__":
    # [example]
    example = bytes("hash", "utf-8")
    for i in range(1, len(example) + 1):
        substring = example[:i]
        hash = sha256(substring).hexdigest()
        print(f"{substring}\n{hash}")
    # [/example]
