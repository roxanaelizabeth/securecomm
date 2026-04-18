from core.encoding_utils import text_to_base64, base64_to_text
from core.hashing import generate_sha256_hash
from core.aes_cipher import encrypt_aes, decrypt_aes


def show_menu():
    print("\n=== SecureComm v0.1 🔐 ===")
    print("1. Encode text to Base64")
    print("2. Decode Base64 to text")
    print("3. Generate SHA-256 hash")
    print("4. Encrypt text with AES")
    print("5. Decrypt AES text")
    print("6. Exit")


def main():
    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            text = input("Enter text: ")
            result = text_to_base64(text)
            print("Encoded:", result)

        elif option == "2":
            text = input("Enter Base64 text: ")
            try:
                result = base64_to_text(text)
                print("Decoded:", result)
            except Exception:
                print("Invalid Base64 input.")

        elif option == "3":
            text = input("Enter text: ")
            result = generate_sha256_hash(text)
            print("SHA-256:", result)

        elif option == "4":
            text = input("Enter text to encrypt: ")
            password = input("Enter password: ")
            try:
                result = encrypt_aes(text, password)
                print("Encrypted:", result)
            except Exception as e:
                print("Encryption error:", e)

        elif option == "5":
            encrypted_text = input("Enter encrypted Base64 text: ")
            password = input("Enter password: ")
            try:
                result = decrypt_aes(encrypted_text, password)
                print("Decrypted:", result)
            except Exception:
                print("Decryption error. Check the encrypted text or password.")

        elif option == "6":
            print("Exiting SecureComm...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()