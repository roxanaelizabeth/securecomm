from core.encoding_utils import text_to_base64, base64_to_text
from core.hashing import generate_sha256_hash, verify_hash


def main():
    message = "seguridad"

    encoded = text_to_base64(message)
    decoded = base64_to_text(encoded)
    message_hash = generate_sha256_hash(message)

    is_valid = verify_hash(message, message_hash)

    print("Original:", message)
    print("Base64 :", encoded)
    print("Decoded:", decoded)
    print("SHA256 :", message_hash)
    print("Hash valid?:", is_valid)


if __name__ == "__main__":
    main()