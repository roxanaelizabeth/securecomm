from Crypto.Random import get_random_bytes
import base64

from core.aes_cipher import encrypt_aes, decrypt_aes
from core.rsa_cipher import encrypt_rsa, decrypt_rsa
from core.signature import sign_message, verify_signature


def generate_random_aes_password():
    """
    Generate a random AES password encoded in Base64.
    """
    random_bytes = get_random_bytes(32)
    return base64.b64encode(random_bytes).decode("utf-8")


def hybrid_encrypt_and_sign(message, rsa_public_key, rsa_private_key):
    """
    Hybrid encryption process:
    1. Generate random AES password
    2. Encrypt message with AES
    3. Encrypt AES password with RSA public key
    4. Sign original message with RSA private key
    """
    aes_password = generate_random_aes_password()
    encrypted_message = encrypt_aes(message, aes_password)
    encrypted_aes_password = encrypt_rsa(aes_password, rsa_public_key)
    signature = sign_message(message, rsa_private_key)

    return {
        "encrypted_message": encrypted_message,
        "encrypted_aes_password": encrypted_aes_password,
        "signature": signature,
    }


def hybrid_decrypt_and_verify(encrypted_message, encrypted_aes_password, signature, rsa_public_key, rsa_private_key):
    """
    Hybrid decryption process:
    1. Decrypt AES password using RSA private key
    2. Decrypt message using AES password
    3. Verify signature using RSA public key
    """
    aes_password = decrypt_rsa(encrypted_aes_password, rsa_private_key)
    decrypted_message = decrypt_aes(encrypted_message, aes_password)
    is_valid_signature = verify_signature(decrypted_message, signature, rsa_public_key)

    return {
        "decrypted_message": decrypted_message,
        "signature_valid": is_valid_signature,
    }