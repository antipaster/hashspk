import hashlib

def cwel(pedal):
    sha256_hash = hashlib.sha256()
    
    with open(pedal, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    pedal = input("path: ")
    xddd = cwel(pedal)
    print(f"hash: {xddd}")
