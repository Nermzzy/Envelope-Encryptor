
# main.py
from key_manager import generate_rsa_keypair, load_rsa_private_key, load_rsa_public_key
from encryptor import encrypt_data
from decryptor import decrypt_data
import os
from pathlib import Path

# Generate keys (run only once)
# generate_rsa_keypair("private_key.pem", "public_key.pem")

# Load keys
private_key = load_rsa_private_key("private_key.pem")
public_key = load_rsa_public_key("public_key.pem")


plaintext = "/home/nell/Desktop/30days-python/sorted-target-emails.txt"

# ============================= Encrypt ===================================
# =========================================================================


# Read file as bytes
# with open(plaintext, 'rb') as f:
#     confidential_data = f.read()

# # Encrypt data
# encrypted_package = encrypt_data(confidential_data, public_key)

# # Overwrite file with only ciphertext
# with open(plaintext, 'wb') as f:
#     f.write(encrypted_package["ciphertext"])

# # Store the AES key + nonce for future decryption
# with open(plaintext + ".key", 'wb') as f:
#     f.write(encrypted_package["encrypted_symmetric_key"] + b"||" + encrypted_package["nonce"])



# =============================== Decrypt ======================================
# ==============================================================================

# Load encrypted file
with open(plaintext, 'rb') as f:
    ciphertext = f.read()

# Load saved wrapped key + nonce
with open(plaintext + ".key", 'rb') as f:
    wrapped_data = f.read()

encrypted_symmetric_key, nonce = wrapped_data.split(b"||")

# Decrypt data
decrypted = decrypt_data({
    "encrypted_symmetric_key": encrypted_symmetric_key,
    "nonce": nonce,
    "ciphertext": ciphertext
}, private_key)

# Write the decrypted content back to the file
with open(plaintext, 'wb') as f:
    f.write(decrypted)

print("Decryption successful! File restored.")