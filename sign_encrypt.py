from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from sign_message import sign_message

def sign_and_encrypt(message, private_key, public_key, hash_function):
    signature = sign_message(message, private_key, hash_function)

    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hash_function),
            algorithm=hash_function,
            label=None
        )
    )

    print("Message signed and encrypted.")
    return encrypted_message, signature
