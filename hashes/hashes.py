import hashlib

key = b"str"

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)