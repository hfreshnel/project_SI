from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend
from sign_message import sign_message
import os

def sign_and_encrypt(message, private_key, symmetric_key, hash_function):
    signed_message = sign_message(message, private_key, hash_function)

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Pad the signed message to be a multiple of the block size (16 bytes for AES)
    padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_signed_message = padder.update(signed_message) + padder.finalize()

    # Encrypt the padded signed message using AES in CBC mode
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_signed_message) + encryptor.finalize()

    # Combine the IV and the encrypted message
    encrypted_message_with_iv = iv + encrypted_message

    return encrypted_message_with_iv