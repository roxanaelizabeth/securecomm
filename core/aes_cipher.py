from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib


def generate_aes_key_from_password(password):
    """
    Generate a 32-byte AES key from a password using SHA-256.
    """
    return hashlib.sha256(password.encode("utf-8")).digest()


def pad_text(text):
    """
    Apply PKCS7-style padding to text.
    """
    padding_length = AES.block_size - len(text.encode("utf-8")) % AES.block_size
    return text + chr(padding_length) * padding_length


def unpad_text(padded_text):
    """
    Remove PKCS7-style padding.
    """
    padding_length = ord(padded_text[-1])
    return padded_text[:-padding_length]


def encrypt_aes(plain_text, password):
    """
    Encrypt text using AES-CBC.
    Returns Base64 encoded IV + ciphertext.
    """
    key = generate_aes_key_from_password(password)
    cipher = AES.new(key, AES.MODE_CBC)
    padded_text = pad_text(plain_text)
    encrypted_bytes = cipher.encrypt(padded_text.encode("utf-8"))
    encrypted_data = cipher.iv + encrypted_bytes
    return base64.b64encode(encrypted_data).decode("utf-8")


def decrypt_aes(encrypted_base64, password):
    """
    Decrypt Base64 encoded IV + ciphertext using AES-CBC.
    """
    key = generate_aes_key_from_password(password)
    encrypted_data = base64.b64decode(encrypted_base64)
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext).decode("utf-8")
    return unpad_text(decrypted_padded)