from core.rsa_cipher import generate_rsa_keys, encrypt_rsa, decrypt_rsa


def test_rsa_encrypt_decrypt():
    text = "Hola Rox"
    public_key, private_key = generate_rsa_keys()

    encrypted = encrypt_rsa(text, public_key)
    decrypted = decrypt_rsa(encrypted, private_key)

    assert encrypted != text
    assert decrypted == text