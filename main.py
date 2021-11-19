
class Encrypter:
    def __init__(self):
        self.key = 13
        self.encrypted_texts = []

    def encrypt(self, text):
        ciphertext = ''
        for c in text:
            if c.isupper():
                ciphertext += chr((ord(c) + self.key - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(c) + self.key - 97) % 26 + 97)

    def show_save_file_menu(self, encrypted_text):
        userInput = str(input(f'1. Save encrypted text to list \n'
                              f'2. Save encrypted text to file \n'
                              f'3. Only show encrypted text \n '))

    def save_to_list(self, encrypted_text):
        self.encrypted_texts.append(encrypted_text)

    def show_list(self):
        print(self.encrypted_texts)

class Menu:
    def __init__(self):
        self.userInput = ' '
        self.encrypter = Encrypter()
        self.show_menu()

    def show_menu(self):
        while self.userInput:
            self.userInput = int(input(
                f'Menu \n'
                f'1. Encrpyt text and save to list \n'
                f'2. Decrypt text \n'
                f'3. List Decrypted texts'
                f'4. Exit \n'))

            self.start_encrypter(self.userInput)

    def start_encrypter(self, user):
        if user == 1:
            text_to_encrypt = str(input('Podaj slowo do zaszyfrowania: '))
            self.encrypter.encrypt(text_to_encrypt)



menu = Menu()
menu.show_menu()
