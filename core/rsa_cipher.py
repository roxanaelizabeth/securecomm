from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def generate_rsa_keys():
    """
    Generate RSA public and private keys.
    Returns both keys as UTF-8 strings.
    """
    key = RSA.generate(2048)
    private_key = key.export_key().decode("utf-8")
    public_key = key.publickey().export_key().decode("utf-8")
    return public_key, private_key


def encrypt_rsa(plain_text, public_key_str):
    """
    Encrypt text using RSA public key.
    Returns Base64 encoded encrypted text.
    """
    public_key = RSA.import_key(public_key_str.encode("utf-8"))
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_bytes = cipher.encrypt(plain_text.encode("utf-8"))
    return base64.b64encode(encrypted_bytes).decode("utf-8")


def decrypt_rsa(encrypted_base64, private_key_str):
    """
    Decrypt Base64 RSA encrypted text using private key.
    """
    private_key = RSA.import_key(private_key_str.encode("utf-8"))
    cipher = PKCS1_OAEP.new(private_key)
    encrypted_bytes = base64.b64decode(encrypted_base64)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return decrypted_bytes.decode("utf-8")