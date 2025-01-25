from cryptography.hazmat.primitives.asymmetric import padding

def verify_signature(message, signature, public_key, hash_function):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hash_function),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hash_function
        )
        print("Signature verified successfully.")
    except Exception as e:
        print(f"Signature verification failed: {e}")
