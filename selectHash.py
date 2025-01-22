# menu to choose hash function
def selectHash():
    menu = {
        "1": "MD5",
        "2": "SHA-1",
        "3": "SHA-256",
        "4": "SHA-512",
        "5": "SHA-3-256",
        "6": "<- Back"
    }

    print("Choose a hash function:")

    for key, value in menu.items():
        print(f"{key}. {value}")

    choice = input("Enter choice: ")
    return menu[choice]