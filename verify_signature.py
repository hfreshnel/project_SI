from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
from hash_message import hash_message

def verify_signature(signed_message, public_key, hash_function):
    # Assuming the original message is encoded in UTF-8 and the signature is appended
    message_length = len(signed_message) - public_key.key_size // 8
    message = signed_message[:message_length].decode()
    signature = signed_message[message_length:]

    print(message)

    # Hash the original message
    hashed_message = hash_message(message, hash_function)

    try:
        # Verify the signature
        public_key.verify(
            signature,
            hashed_message,
            padding.PSS(
                mgf=padding.MGF1(hash_function),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hash_function
        )
        print("Signature is valid.")
        return True
    except InvalidSignature:
        print("Signature is invalid.")
        return False
