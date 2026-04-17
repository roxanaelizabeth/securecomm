from core.hashing import generate_sha256_hash, verify_hash


def test_generate_sha256_hash():
    text = "Seguridad"
    result = generate_sha256_hash(text)
    assert isinstance(result, str)
    assert len(result) == 64


def test_verify_hash_valid():
    text = "Seguridad"
    hash_value = generate_sha256_hash(text)
    assert verify_hash(text, hash_value) is True


def test_verify_hash_invalid():
    text = "Seguridad"
    hash_value = generate_sha256_hash(text)
    assert verify_hash("seguridad", hash_value) is False