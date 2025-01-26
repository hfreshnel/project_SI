from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from hash_message import hash_message

def sign_message(message, private_key, hash_function):
    hashed_message = hash_message(message, hash_function)
    signed_hash = private_key.sign(
        hashed_message,
        padding.PSS(
            mgf=padding.MGF1(hash_function),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hash_function
    )
    signed_message = message.encode() + signed_hash
    print("Message signed.")
    return signed_message