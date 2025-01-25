def load_message():
    print("Choose how to load the message:")
    print("1. Load from file")
    print("2. Enter message manually")
    choice = input("Enter your choice: ")

    if choice == "1":
        file_path = 'messages/plaintext.txt'  
        try:
            with open(file_path, 'r') as file:
                message = file.read().strip()  
                print(f"Message successfully loaded: {message}")
                return message
        except FileNotFoundError:
            print("File not found. Please check the path.")
            return None  
    elif choice == "2":
        message = input("Enter your message: ")
        if message.strip(): 
            print(f"Message successfully loaded: {message}")
            return message
        else:
            print("Message cannot be empty.")
            return None
    else:
        print("Invalid choice.")
        return None  
