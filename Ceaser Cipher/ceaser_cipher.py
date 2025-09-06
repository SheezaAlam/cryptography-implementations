print("=================================")
print("       Caesar Cipher Tool        ")
print("=================================")
print("Choose an option:")
print("1. Encrypt a message")
print("2. Decrypt a message")

# Get user choice
choice = ''
while choice not in ('1', '2'):
    choice = input("Enter 1 or 2: ").strip()

# Get user input message
message = input("Enter your message: ")

# Fixed Caesar cipher key
key = 3

def caesar_cipher(text, key, mode):
    result = []
    if mode == 'd':
        key = -key  # Reverse shift for decryption
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # (ord(char) - base) → position in alphabet (0-25)
            # + key → shift
            # % 26 → wrap around A-Z/a-z
            shifted = (ord(char) - base + key) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)  # Keep spaces/punctuation unchanged
    return ''.join(result)

# Decide mode based on choice
mode = 'e' if choice == '1' else 'd'

# Perform encryption or decryption
output = caesar_cipher(message, key, mode)

print("\nResult:")
print(output)
