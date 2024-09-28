from cryptography.fernet import Fernet


class CustomFernet:
    def __init__(self, key):
        self.cipher_suite = Fernet(key)

    def encrypt(self, data):
        error_messages = []

        # Trim leading and trailing whitespace
        data = self.trim(data)

        # Check for special characters
        if not any(char.isalnum() for char in data):
            error_messages.append("Data must contain at least one alphanumeric character.")
        # Check for case sensitivity
        if data.islower() or data.isupper():
            error_messages.append("Data must contain both uppercase and lowercase characters.")
        # Check for spaces
        if ' ' in data:
            error_messages.append("Data cannot contain spaces.")
        # Check length
        if len(data) < 8:
            error_messages.append("Data must be at least 8 characters long.")

        # If any error messages are present, raise a ValueError
        if error_messages:
            raise ValueError('\n'.join(error_messages))

        # Encrypt the data
        return self.cipher_suite.encrypt(data.encode())

    def trim(self, data):
        return data.strip()


# Generate a key
key = Fernet.generate_key()

# Create a CustomFernet instance
custom_fernet = CustomFernet(key)

# Masking the data
original_data = " narYanaj "  # data with leading and trailing whitespace
encrypted_data = custom_fernet.encrypt(original_data)

print("Encrypted Data:", encrypted_data)  # Output: 'Hello'
print("Key: ", key)  # Output: b'your_generated_key'
