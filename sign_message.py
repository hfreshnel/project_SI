from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def sign_message(message, private_key, hash_function):
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hash_function),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hash_function
    )
    print("Message signed.")
    return signature
