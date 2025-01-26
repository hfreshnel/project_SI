from cryptography.hazmat.primitives import hashes

def selectHash():
    menu = {
        "1": ("MD5", hashes.MD5),
        "2": ("SHA-1", hashes.SHA1),
        "3": ("SHA-256", hashes.SHA256),
        "4": ("SHA-512", hashes.SHA512),
        "5": ("SHA-3-256", hashes.SHA3_256),
    }

    print("Choose a hash function:")

    for key, (name, _) in menu.items():
        print(f"{key}. {name}")

    choice = input("Enter choice: ")

    if choice in menu:
        return menu[choice][1]()
    else:
        print("Invalid choice. Please try again.")
        return selectHash()
