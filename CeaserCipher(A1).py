# Caesar Cipher Implementation
# 1st function ceaser_encrypt
def caesar_encrypt(text, shift):
    result = " "

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Check if character is lowercase letter
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # If not a letter, keep it same
        else:
            result += char

    return result

# 2nd function ceaser_decrypt
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


# Testing the program
# Ask user for the message to encrypt
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

#Variable Initialization
encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

#It will print the encrypted message
print("Encrypted Message:", encrypted)

#It will print the decrypted message
print("Decrypted Message:", decrypted)