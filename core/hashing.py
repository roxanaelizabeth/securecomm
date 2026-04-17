import hashlib


def generate_sha256_hash(text):
    """
    Generate SHA-256 hash from a text string.
    Returns the hash as a hexadecimal string.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def verify_hash(text, expected_hash):
    """
    Verify whether the SHA-256 hash of the text
    matches the expected hash.
    """
    calculated_hash = generate_sha256_hash(text)
    return calculated_hash == expected_hash