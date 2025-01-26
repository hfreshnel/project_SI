from load_message import load_message
from selectHash import selectHash
from hash_message import hash_message
from generate_and_save_keys import generate_and_save_keys
from load_keys import load_keys
from sign_encrypt import sign_and_encrypt
from sign_message import sign_message
from decrypt_verify import decrypt_and_verify
from verify_signature import verify_signature

def menu():
    message = None
    hash_function = None
    keys = None

    while True:
        print("\n--- Main Menu ---")
        print("1. Load message")
        print("2. Choose hash function")
        print("3. Print hashed message")
        print("4. Generate and save keys")
        print("5. Load keys")
        print("6. Sign and encrypt message")
        print("7. Sign but not encrypt message")
        print("8. Decrypt and verify signature")
        print("9. Verify signature")
        print("10. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            message = load_message()  
            print(f"Message loaded: {message}")

        elif choice == '2':
            hash_function = selectHash() 
            if hash_function:
                print(f"Hash function selected: {hash_function.name}")
            else:
                print("No hash function selected.")

        elif choice == '3':
            if message and hash_function:
                hashed_message = hash_message(message, hash_function) 
                print(f"Hashed message: {hashed_message.hex()}")
            else:
                print("Please load a message and choose a hash function first.")

        elif choice == '4':
            keys = generate_and_save_keys()  
            

        elif choice == '5':
            keys = load_keys() 
            print(keys)

        elif choice == '6':
            if message and keys:
                message_sign_encrypt = sign_and_encrypt(message, keys[0],keys[1],hash_function) 
            else:
                print("Please load a message and keys first.")

        elif choice == '7':
            if message and keys:
                signature = sign_message(message, keys[0],hash_function) 
            else:
                print("Please load a message and keys first.")

        elif choice == '8':
            if keys and message_sign_encrypt:
                decrypt_and_verify(message_sign_encrypt[0],message_sign_encrypt[1],keys[0],keys[1],hash_function)  
            else:
                print("Please load keys and encrypt first  ")

        elif choice == '9':
            if keys:
                verify_signature(signature, keys[1], hash_function) 
            else:
                print("Please load keys first.")

        elif choice == '10':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
