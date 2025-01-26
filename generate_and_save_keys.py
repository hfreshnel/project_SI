import os
import secrets
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_and_save_keys():
    # Generate RSA keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Generate symmetric key
    symmetric_key = secrets.token_bytes(32)  # 256-bit key for AES
    print(f"Generated symmetric key: {symmetric_key.hex()}")

    
    keys_folder = "keys"
    os.makedirs(keys_folder, exist_ok=True)

    
    with open(os.path.join(keys_folder, "private_key.pem"), "wb") as private_file:
        private_file.write(private_pem)

    
    with open(os.path.join(keys_folder, "public_key.pem"), "wb") as public_file:
        public_file.write(public_pem)

    with open(os.path.join(keys_folder, "symmetric_key.pem"), "wb") as symmetric_file:
        symmetric_file.write(symmetric_key)

    print("Keys generated and saved to the 'keys' folder.")
