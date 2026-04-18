from core.rsa_cipher import generate_rsa_keys
from core.hybrid_cipher import hybrid_encrypt_and_sign, hybrid_decrypt_and_verify


def test_hybrid_encrypt_decrypt_and_verify():
    message = "Hola Rox"
    public_key, private_key = generate_rsa_keys()

    encrypted_data = hybrid_encrypt_and_sign(message, public_key, private_key)
    result = hybrid_decrypt_and_verify(
        encrypted_data["encrypted_message"],
        encrypted_data["encrypted_aes_password"],
        encrypted_data["signature"],
        public_key,
        private_key
    )

    assert result["decrypted_message"] == message
    assert result["signature_valid"] is True