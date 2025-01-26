# project_SI

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- `cryptography` library

You can install the required library using pip:

```sh
pip install cryptography
```

## How to Run

1. Navigate to the project directory.
2. Run the `menu.py` script:

```sh
python menu.py
```

## How to Use

The program provides a menu with the following options:

1. **Load message**: Load a message from a file or enter it manually.
2. **Choose hash function**: Select a hash function from the provided options.
3. **Print hashed message**: Display the hashed version of the loaded message.
4. **Generate and save keys**: Generate RSA and symmetric keys and save them to the `keys` folder.
5. **Load keys**: Load previously saved keys from the `keys` folder.
6. **Sign and encrypt message**: Sign the loaded message with the private key and encrypt it with the symmetric key.
7. **Sign but not encrypt message**: Sign the loaded message with the private key.
8. **Decrypt and verify signature**: Decrypt the signed and encrypted message and verify its signature.
9. **Verify signature**: Verify the signature of a signed message.
10. **Quit**: Exit the program.

## How It Works

- **Message Loading**: The message can be loaded from a file or entered manually.
- **Hashing**: The selected hash function is used to hash the message.
- **Key Generation**: RSA keys (private and public) and a symmetric key are generated and saved.
- **Signing**: The message is signed using the private RSA key.
- **Encryption**: The signed message is encrypted using the symmetric key with AES in CBC mode.
- **Decryption and Verification**: The encrypted message is decrypted using the symmetric key, and the signature is verified using the public RSA key.

The project uses the `cryptography` library for cryptographic operations, including hashing, signing, encryption, and decryption.