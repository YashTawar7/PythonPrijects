from src.data_masking import encrypt_data, decrypt_data
from src.key_management import generate_key, save_key_to_file, load_key_from_file

# Example usage
original_data = "o Information"

# Generate and save encryption key
key = generate_key()
save_key_to_file(key)

# Print original data and key
print("Original Data:", original_data)
print("Encryption Key:", key)

# Encrypt the data
encrypted_data = encrypt_data(original_data, key)
print("Encrypted Data:", encrypted_data)

# Decrypt the data
loaded_key = load_key_from_file()
decrypted_data = decrypt_data(encrypted_data, loaded_key)
print("Decrypted Data:", decrypted_data)
