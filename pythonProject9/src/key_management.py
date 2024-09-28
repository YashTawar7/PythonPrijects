from Crypto.Random import get_random_bytes
import base64


def generate_key():
    return get_random_bytes(16)


def save_key_to_file(key, filename="encryption_key.bin"):
    with open(filename, "wb") as key_file:
        key_file.write(key)


def load_key_from_file(filename="encryption_key.bin"):
    with open(filename, "rb") as key_file:
        return key_file.read()
