
class Encrypter:
    def __init__(self):
        self.key = 13
        self.encrypted_texts = []

    def encrypt_or_decrypt(self, text, mode):
        ciphertext = ''
        for c in text:
            if c.isupper():
                ciphertext += chr((ord(c) + self.key - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(c) + self.key - 97) % 26 + 97)

        if mode == 'encrypt':
            self.show_save_file_menu(text, ciphertext)
        elif mode == 'decrypt':
            print('Decrypted ' + ciphertext)


    def show_save_file_menu(self,text, encrypted_text):
        user_input = ' '
        while user_input != 1 or user_input != 2 or user_input != 3:
            user_input = int(input(f'1. Save encrypted text to list \n'
                                  f'2. Save encrypted text to file \n'
                                  f'3. Only show encrypted text \n '))
            if user_input == 1:
                self.save_to_list(encrypted_text)
                break
            elif user_input == 2:
                self.save_to_file(encrypted_text)
                break
            else:
                print(f'{text}: {encrypted_text} \n')
                break

    def save_to_list(self, encrypted_text):

        if encrypted_text in self.encrypted_texts:
            print('This text is already on list \n')
        else:
            self.encrypted_texts.append(encrypted_text)

        self.show_list()


    def show_list(self):
        print(self.encrypted_texts)

    def save_to_file(self, encrypted_text):

        if self.is_text_in_file(encrypted_text):
            print('Text is already in file')
        else:
            with open('encrypted_texts.txt', 'a') as f:
                f.write(encrypted_text)
                f.write('\n')

    def is_text_in_file(self, encrypted_text):
        with open('encrypted_texts.txt') as f:
            if encrypted_text in f.read():
                return True

class Menu:
    def __init__(self):
        self.userInput = ' '
        self.encrypter = Encrypter()
        self.show_main_menu()

    def show_main_menu(self):
        while self.userInput:
            self.userInput = int(input(
                f'Menu \n'
                f'1. Encrpyt text and save to file or list \n'
                f'2. Decrypt text \n'
                f'5. Show encrypted texts \n'
                f'4. Exit \n'))

            self.start_encrypter(self.userInput)

    def show_decrypt_menu(self):
        decrypt_option = 0
        while decrypt_option != 1 or decrypt_option != 2 or decrypt_option != 3:
            decrypt_option = int(input(
                f'1. Decrypt given text \n'
                f'2. Decrypt text form list \n'
                f'3. Decrpyt text from file \n '))

            self.start_decrypter(decrypt_option)

    def start_encrypter(self, user):
        if user == 1:
            text_to_encrypt = str(input('Enter text to be encrypted: \n'))
            self.encrypter.encrypt_or_decrypt(text_to_encrypt,'encrypt')
        if user == 2:
            self.show_decrypt_menu()

    def start_decrypter(self, decrypt_option):
        if decrypt_option == 1:
            text_to_decrypt = str(input('Enter text to be decrypted: \n'))
            self.encrypter.encrypt_or_decrypt(text_to_decrypt,'decrypt')






menu = Menu()
menu.show_menu()
