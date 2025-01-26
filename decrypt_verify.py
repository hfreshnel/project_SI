from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from verify_signature import verify_signature

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

   
    verify_signature(plain_text, signature, public_key, hash_algorithm)
    
    return plain_text
