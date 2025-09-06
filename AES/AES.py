# Import necessary modules from PyCryptodome
from Crypto.Cipher import AES         # AES encryption/decryption
from Crypto.Random import get_random_bytes  # For secure key generation
import base64                         # To encode bytes for printing/sharing

# --- Step 1: Create a fake password for demo ---
# In real life, this could be a database entry, API key, or sensitive data
password = "IGoToTheGym@7pm"  
print(f"Original Password: {password}")

# --- Step 2: Generate AES Key ---
# AES supports 128-bit (16 bytes), 192-bit (24 bytes), and 256-bit (32 bytes) keys.
# Here we use 128-bit for simplicity.
key = get_random_bytes(16)  

# --- Step 3: Create AES cipher object ---
# We use EAX mode here:
# - Encrypts data
# - Authenticates it (detects tampering)
# - Doesn't require padding
cipher = AES.new(key, AES.MODE_EAX)

# --- Step 4: Encrypt the password ---
# encrypt_and_digest() returns:
# - ciphertext: encrypted data
# - tag: used to verify data integrity during decryption
ciphertext, tag = cipher.encrypt_and_digest(password.encode())

# --- Step 5: Print encryption results ---
# We encode bytes in Base64 so they are readable and easy to store/transmit
print("\n--- ENCRYPTION ---")
print(f"Key (base64): {base64.b64encode(key).decode()}")
print(f"Nonce (base64): {base64.b64encode(cipher.nonce).decode()}")
print(f"Ciphertext (base64): {base64.b64encode(ciphertext).decode()}")

# --- Step 6: Decrypt the password ---
# To decrypt, you must have:
# - The same key
# - The same nonce
# - The ciphertext
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)

# Decrypt returns the original data (in bytes) so we decode to string
plaintext = cipher_dec.decrypt(ciphertext).decode()

# --- Step 7: Print decrypted result ---
print("\n--- DECRYPTION ---")
print(f"Decrypted Password: {plaintext}")
