from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def decrypt(data, privateKey, hash_algorithm):
    if (hash_algorithm == "SHA256"):
        hash_algorithm = hashes.SHA256()
    elif (hash_algorithm == "SHA512"):
        hash_algorithm = hashes.SHA512()
    else:
        raise ValueError("Invalid hash algorithm. Use SHA256 or SHA512")
    plainText = privateKey.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hash_algorithm),
            algorithm=hash_algorithm,
            label=None
        )
    )
    return plainText