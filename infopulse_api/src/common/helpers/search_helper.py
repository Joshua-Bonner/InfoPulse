import hashlib


def url_to_unique_int(url: str) -> int:
    hash_object = hashlib.sha256(url.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig[:16], 16)
