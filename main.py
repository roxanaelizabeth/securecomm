from core.encoding_utils import text_to_base64, base64_to_text
from core.hashing import generate_sha256_hash
from core.aes_cipher import encrypt_aes, decrypt_aes
from core.rsa_cipher import generate_rsa_keys, encrypt_rsa, decrypt_rsa


def show_menu():
    print("\n=== SecureComm v0.2 🔐 ===")
    print("1. Encode text to Base64")
    print("2. Decode Base64 to text")
    print("3. Generate SHA-256 hash")
    print("4. Encrypt text with AES")
    print("5. Decrypt AES text")
    print("6. Generate RSA key pair")
    print("7. Encrypt text with RSA")
    print("8. Decrypt RSA text")
    print("9. Exit")


def main():
    rsa_public_key = None
    rsa_private_key = None

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
            rsa_public_key, rsa_private_key = generate_rsa_keys()
            print("\nPublic Key:\n")
            print(rsa_public_key)
            print("\nPrivate Key:\n")
            print(rsa_private_key)

        elif option == "7":
            if rsa_public_key is None:
                print("Generate RSA keys first.")
                continue
            text = input("Enter text to encrypt with RSA: ")
            try:
                result = encrypt_rsa(text, rsa_public_key)
                print("Encrypted:", result)
            except Exception as e:
                print("RSA encryption error:", e)

        elif option == "8":
            if rsa_private_key is None:
                print("Generate RSA keys first.")
                continue
            encrypted_text = input("Enter RSA encrypted Base64 text: ")
            try:
                result = decrypt_rsa(encrypted_text, rsa_private_key)
                print("Decrypted:", result)
            except Exception:
                print("RSA decryption error.")

        elif option == "9":
            print("Exiting SecureComm...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()