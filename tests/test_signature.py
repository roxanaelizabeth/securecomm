from core.rsa_cipher import generate_rsa_keys
from core.signature import sign_message, verify_signature


def test_sign_and_verify_valid():
    message = "Hola Rox"
    public_key, private_key = generate_rsa_keys()

    signature = sign_message(message, private_key)
    result = verify_signature(message, signature, public_key)

    assert result is True


def test_sign_and_verify_invalid():
    message = "Hola Rox"
    altered_message = "Hola rox"
    public_key, private_key = generate_rsa_keys()

    signature = sign_message(message, private_key)
    result = verify_signature(altered_message, signature, public_key)

    assert result is False