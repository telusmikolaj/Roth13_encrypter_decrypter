class Encrypter:
    def __init__(self):
        self.key = 13
        self.encrypted_texts = []
        self.encrypted_texts_form_file = []

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

    def show_save_file_menu(self, text, encrypted_text):
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

        if len(self.encrypted_texts) == 0:
            print('List is empty \n')
        else:
            print('Encrypted texts list: ')
            for index, line in enumerate(self.encrypted_texts, start=1):
                print(f'{index}. {line}')

    def save_to_file(self, encrypted_text):

        if self.is_text_in_file(encrypted_text):
            print('Text is already in file')
        else:
            with open('encrypted_texts.txt', 'a') as f:
                f.write(encrypted_text)
                f.write('\n')

    def display_encrypted_texts_from_file(self):
        self.get_encrypted_texts_from_file()
        if len(self.encrypted_texts_form_file) == 0:
            print('File is empty \n')
        else:
            print('Encrypted Texts: ')
            for line in self.encrypted_texts_form_file:
                print(line)

        print('\n')

    def get_encrypted_texts_from_file(self):
        with open('encrypted_texts.txt') as f:
            for index, line in enumerate(f):
                self.encrypted_texts_form_file.append(line.strip())

    def is_text_in_file(self, encrypted_text):
        with open('encrypted_texts.txt') as f:
            if encrypted_text in f.read():
                return True

    def decrypt_text_from_list(self, text_id):
        for index, line in enumerate(self.encrypted_texts, start=1):
            if index == text_id:
                self.encrypt_or_decrypt(line,'decrypt')
                valid_id = True
            else:
                print('Invalid id')

    def get_number_of_text_in_list(self):
        return len(self.encrypted_texts)

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
                f'3. Display encrypted texts \n'
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
            break

    def show_display_menu(self):
        display_option = 0
        while display_option != 1 or display_option != 2:
            display_option = int(input(
                f'1. Display texts in list \n'
                f'2. Display texts in file \n'))

            self.display_decrypted_texts(display_option)
            break

    def start_encrypter(self, user):
        if user == 1:
            text_to_encrypt = str(input('Enter text to be encrypted: \n'))
            self.encrypter.encrypt_or_decrypt(text_to_encrypt, 'encrypt')
        if user == 2:
            self.show_decrypt_menu()
        if user == 3:
            self.show_display_menu()

    def start_decrypter(self, decrypt_option):
        if decrypt_option == 1:
            text_to_decrypt = str(input('Enter text to be decrypted: \n'))
            self.encrypter.encrypt_or_decrypt(text_to_decrypt, 'decrypt')
        if decrypt_option == 2:
            if self.encrypter.get_number_of_text_in_list() == 0:
                print('List is empty ')
            else:
                self.encrypter.show_list()
                text_id = int(input('Enter id of text from list to decrypt: \n'))
                self.encrypter.decrypt_text_from_list(text_id)

    def display_decrypted_texts(self, display_option):

        if display_option == 1:
            self.encrypter.show_list()
        else:
            self.encrypter.display_encrypted_texts_from_file()


menu = Menu()

# list = []
# with open('encrypted_texts.txt') as f:
#     for index, line in enumerate(f):
#         print(line)
#         list.append(line.strip())
#
# for index, line in enumerate(list):
#     print(index, line)
