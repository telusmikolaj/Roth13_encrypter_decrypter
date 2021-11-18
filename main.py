def encrypt_or_decrypt(text):
    ciphertext = ''
    key = 13
    for c in text:
        if c.isupper():
            ciphertext += chr((ord(c) + key - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(c) + key - 97) % 26 + 97)

    return ciphertext