from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def decrypt_and_verify(encrypted_data, signature, private_key, public_key, hash_algorithm):
    
    # The private key is used to decrypt the encrypted data.
    plain_text = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hash_algorithm),  # MGF1 padding with the selected hash algorithm
            algorithm=hash_algorithm,                    # The same hash algorithm used for encryption
            label=None                                   # No label used in this case
        )
    )

   
    # The public key verifies the signature against the decrypted plain text.
    try:
        public_key.verify(
            signature,                                  # The signature to verify
            plain_text,                                 # The decrypted plain text to compare against
            padding.PSS(                                # PSS padding for RSA signature verification
                mgf=padding.MGF1(hash_algorithm),       # MGF1 padding using the selected hash algorithm
                salt_length=padding.PSS.MAX_LENGTH      # Maximum salt length for the PSS padding
            ),
            hash_algorithm                             # The hash algorithm used for signature creation
        )
        # If signature verification is successful, print confirmation.
        print("Signature verified successfully.")
    except Exception as e:
        # If signature verification fails, catch the error and print the reason.
        print(f"Signature verification failed: {e}")

    # Return the decrypted plain text, regardless of signature verification outcome.
    return plain_text
