from cryptography.fernet import Fernet

# Generate key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load saved key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    output_file = filename.replace(".enc", "_decrypted.txt")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

# Main menu
generate_key()

while True:
    print("\n1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        file_name = input("Enter file name: ")
        encrypt_file(file_name)

    elif choice == "2":
        file_name = input("Enter encrypted file name: ")
        decrypt_file(file_name)

    elif choice == "3":
        break

    else:
        print("Invalid choice")