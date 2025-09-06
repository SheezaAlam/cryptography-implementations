# ----------------------------------------------
# RSA ENCRYPTION & DECRYPTION EXAMPLE IN PYTHON
# Encrypt and decrypt an Instagram password
# ----------------------------------------------

# Install dependency:
# pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# STEP 1: GENERATE RSA KEY PAIR
# RSA is an asymmetric encryption algorithm, meaning it uses 2 keys:
#   - Public key for encryption
#   - Private key for decryption
key_pair = RSA.generate(2048)  # 2048-bit key length is secure enough for most uses

# Export private key (used for decryption)
private_key = key_pair.export_key()

# Export public key (used for encryption)
public_key = key_pair.publickey().export_key()

# Save keys to files so we can reuse them
with open('private.pem', 'wb') as f:
    f.write(private_key)

with open('public.pem', 'wb') as f:
    f.write(public_key)

print("✅ RSA key pair generated and saved to 'private.pem' & 'public.pem'")

# STEP 2: ENCRYPT A PASSWORD
# Let's say you want to securely store or send your Instagram password
instagram_password = "Instagram@123"  # Example password

# Load the public key for encryption
public_key_obj = RSA.import_key(open('public.pem').read())

# Create an RSA cipher object using PKCS1_OAEP (Optimal Asymmetric Encryption Padding)
# This padding makes RSA more secure and prevents certain attacks
cipher_rsa = PKCS1_OAEP.new(public_key_obj)

# Encrypt the password (convert to bytes first)
encrypted_password = cipher_rsa.encrypt(instagram_password.encode())

print("\n🔒 Encrypted password (unreadable gibberish):")
print(encrypted_password)

# STEP 3: DECRYPT THE PASSWORD
# Load the private key for decryption
private_key_obj = RSA.import_key(open('private.pem').read())

# Create a new cipher object with the private key
cipher_rsa = PKCS1_OAEP.new(private_key_obj)

# Decrypt the encrypted password (convert bytes back to string)
decrypted_password = cipher_rsa.decrypt(encrypted_password).decode()

print("\n🔓 Decrypted password (original text):")
print(decrypted_password)

