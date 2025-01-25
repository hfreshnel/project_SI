from cryptography.hazmat.primitives import serialization

def load_keys():
    try:
        with open("keys/private_key.pem", "rb") as private_file:
            private_key = serialization.load_pem_private_key(
                private_file.read().strip(),
                password=None
            )

        with open("keys/public_key.pem", "rb") as public_file:
            public_key = serialization.load_pem_public_key(public_file.read().strip())

        print("Keys successfully loaded.")
        return private_key, public_key
    except FileNotFoundError:
        print("Key files not found. Please generate or save keys first.")
        return None, None
