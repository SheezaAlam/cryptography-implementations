import numpy as np
#this is for dot product ,reshape, transpose matrix
def text_to_numbers(text):
    return[ord(char) - ord('A') for char in text.upper() if char.isalpha()]
#ord(char) means 'A'-0,'B'-1...'Z'-26
#it goes through each char in uppercase
#char checks each alphabet excludes spaces,numb,punctuation

def numbers_to_text(numbers):
    return''.join([chr(num %26 + ord('A')) for num in numbers])
#join takes the list of string and merges them into single one
#without join youll get ['H', 'E', 'L', 'L', 'O']

def hill_encrypt(plaintext,key_matrix):
    nums= text_to_numbers(plaintext)
    #it takes pt as block size 2
    if len(nums) % 2 !=0:
    #'x'- padding means adding 1 extra character -odd : hill cipher works on 2x2 
     nums.append(ord('X') - ord('A'))
    #we need exactly 2columns and -1 figure it out automatically how many rows are needed
    nums = np.array(nums).reshape(-1,2).T
    #.T here is transpose means swapping rows and columns
    encrypted_matrix = np.dot(key_matrix, nums) % 26
    encrypted_nums = encrypted_matrix.T.flatten()

    #.flatten() → turns the matrix into a simple list of numbers → ready for conversion back into a string.
    return numbers_to_text(encrypted_nums)
if __name__ == "__main__":
    # 2x2 key matrix (must be invertible mod 26)
    key = np.array([[3, 3],
                    [2, 5]])
    
    plaintext = "HELLO"
    ciphertext = hill_encrypt(plaintext, key)
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)