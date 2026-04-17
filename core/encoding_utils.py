import base64


def text_to_bytes(text):
    """
    Convert text string to UTF-8 bytes
    """
    return text.encode("utf-8")


def bytes_to_text(byte_data):
    """
    Convert UTF-8 bytes back to text
    """
    return byte_data.decode("utf-8")


def bytes_to_base64(byte_data):
    """
    Convert bytes to Base64 string
    """
    return base64.b64encode(byte_data).decode("utf-8")


def base64_to_bytes(base64_text):
    """
    Convert Base64 string back to bytes
    """
    return base64.b64decode(base64_text)


def text_to_base64(text):
    """
    Convert plain text directly to Base64
    """
    return bytes_to_base64(text_to_bytes(text))


def base64_to_text(base64_text):
    """
    Convert Base64 directly back to plain text
    """
    return bytes_to_text(base64_to_bytes(base64_text))