from cryptography.hazmat.primitives import hashes

def hash_message(message, hash_function):
    digest = hashes.Hash(hash_function)
    digest.update(message.encode())
    hashed_message = digest.finalize()
    return hashed_message
