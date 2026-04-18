from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64


def sign_message(message, private_key_str):
    """
    Sign a message using RSA private key.
    Returns the signature encoded in Base64.
    """
    private_key = RSA.import_key(private_key_str.encode("utf-8"))
    message_hash = SHA256.new(message.encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(message_hash)
    return base64.b64encode(signature).decode("utf-8")


def verify_signature(message, signature_base64, public_key_str):
    """
    Verify a message signature using RSA public key.
    Returns True if valid, False otherwise.
    """
    public_key = RSA.import_key(public_key_str.encode("utf-8"))
    message_hash = SHA256.new(message.encode("utf-8"))
    signature = base64.b64decode(signature_base64)

    try:
        pkcs1_15.new(public_key).verify(message_hash, signature)
        return True
    except (ValueError, TypeError):
        return False