from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend
from verify_signature import verify_signature

def decrypt_and_verify(encrypted_data, symmetric_key, public_key, hash_algorithm):
    # Extract the IV from the encrypted data
    iv = encrypted_data[:16]
    encrypted_message = encrypted_data[16:]

    # Decrypt the message using AES in CBC mode
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_signed_message = decryptor.update(encrypted_message) + decryptor.finalize()

    # Remove the padding from the decrypted message
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    signed_message = unpadder.update(padded_signed_message) + unpadder.finalize()

    # Assuming the original message is encoded in UTF-8 and the signature is appended
    message_length = len(signed_message) - public_key.key_size // 8
    message = signed_message[:message_length].decode()
    signature = signed_message[message_length:]

    # Verify the signature
    is_valid = verify_signature(signed_message, public_key, hash_algorithm)

    if is_valid:
        print("Signature is valid.")
    
    else:
        print("Invalid signature.")
    return message