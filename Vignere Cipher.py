def encrypt(plaintext, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

plaintext = "Hello, World"
key = "KEY"

encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
