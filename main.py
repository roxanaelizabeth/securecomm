from core.signature import sign_message, verify_signature
from core.encoding_utils import text_to_base64, base64_to_text
from core.hashing import generate_sha256_hash
from core.aes_cipher import encrypt_aes, decrypt_aes
from core.rsa_cipher import generate_rsa_keys, encrypt_rsa, decrypt_rsa
from core.signature import sign_message, verify_signature
from core.hybrid_cipher import hybrid_encrypt_and_sign, hybrid_decrypt_and_verify

def show_menu():
    print("\n=== SecureComm v0.4 🔐 ===")
    print("1. Encode text to Base64")
    print("2. Decode Base64 to text")
    print("3. Generate SHA-256 hash")
    print("4. Encrypt text with AES")
    print("5. Decrypt AES text")
    print("6. Generate RSA key pair")
    print("7. Encrypt text with RSA")
    print("8. Decrypt RSA text")
    print("9. Sign message")
    print("10. Verify signature")
    print("11. Hybrid encrypt + sign")
    print("12. Hybrid decrypt + verify")
    print("13. Exit")

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
            if rsa_private_key is None:
                print("Generate RSA keys first.")
                continue
            text = input("Enter message to sign: ")
            try:
                signature = sign_message(text, rsa_private_key)
                print("Signature (Base64):", signature)
            except Exception as e:
                print("Signing error:", e)

        elif option == "10":
            if rsa_public_key is None:
                print("Generate RSA keys first.")
                continue
            text = input("Enter original message: ")
            signature = input("Enter Base64 signature: ")
            try:
                is_valid = verify_signature(text, signature, rsa_public_key)
                print("Signature valid?:", is_valid)
            except Exception:
                print("Signature verification error.")
        elif option == "11":
            if rsa_public_key is None or rsa_private_key is None:
                print("Generate RSA keys first.")
                continue

            message = input("Enter message to hybrid encrypt: ")
            try:
                result = hybrid_encrypt_and_sign(message, rsa_public_key, rsa_private_key)
                print("\nEncrypted message:\n", result["encrypted_message"])
                print("\nEncrypted AES password:\n", result["encrypted_aes_password"])
                print("\nSignature:\n", result["signature"])
            except Exception as e:
                print("Hybrid encryption error:", e)

        elif option == "12":
            if rsa_public_key is None or rsa_private_key is None:
                print("Generate RSA keys first.")
                continue

            encrypted_message = input("Enter encrypted message: ")
            encrypted_aes_password = input("Enter encrypted AES password: ")
            signature = input("Enter signature: ")

            try:
                result = hybrid_decrypt_and_verify(
                    encrypted_message,
                    encrypted_aes_password,
                    signature,
                    rsa_public_key,
                    rsa_private_key
                )
                print("\nDecrypted message:", result["decrypted_message"])
                print("Signature valid?:", result["signature_valid"])
            except Exception as e:
                print("Hybrid decryption error:", e)
        elif option == "13":
            print("Exiting SecureComm...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()