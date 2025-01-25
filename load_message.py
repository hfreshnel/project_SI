def load_message():
    try:
        with open("messages/plaintext.txt", "r") as file:
            message = file.read()
            print("Message loaded successfully.")
            return message
    except FileNotFoundError:
        print("Message file not found. Please place a file in 'messages/plaintext.txt'.")
        return None
