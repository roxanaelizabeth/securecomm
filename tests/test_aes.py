from core.aes_cipher import encrypt_aes, decrypt_aes


def test_aes_encrypt_decrypt():
    text = "Hola Rox"
    password = "clave123"
    encrypted = encrypt_aes(text, password)
    decrypted = decrypt_aes(encrypted, password)

    assert encrypted != text
    assert decrypted == text