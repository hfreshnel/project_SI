from cryptography.hazmat.primitives import hashes

def print_hashed_message(message, hash_function):
    digest = hashes.Hash(hash_function)
    digest.update(message.encode())
    hashed_message = digest.finalize()
    print(f"Hashed message: {hashed_message.hex()}")
