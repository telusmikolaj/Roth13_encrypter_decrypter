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
        while user_input != '1' or user_input != '2' or user_input != '3':
            user_input = input(f'1. Save encrypted text to list \n'
                               f'2. Save encrypted text to file \n'
                               f'3. Only show encrypted text \n '
                               f'4. Return')
            if user_input == '1':
                self.save_to_list(encrypted_text)
                break
            elif user_input == '2':
                self.save_to_file(encrypted_text)
                break
            elif user_input == '3':
                print(f'{text}: {encrypted_text} \n')
                break
            elif user_input == '4':
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
            for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                print(f'{index}. {line}')

        print('\n')

    def get_encrypted_texts_from_file(self):
        self.encrypted_texts_form_file.clear()
        with open('encrypted_texts.txt') as f:
            for index, line in enumerate(f):
                self.encrypted_texts_form_file.append(line.strip())

    def is_text_in_file(self, encrypted_text):
        with open('encrypted_texts.txt') as f:
            if encrypted_text in f.read():
                return True

    def decrypt_text_from_list_or_file(self, text_id, mode):
        is_not_valid_id = True
        if mode == 'list':
            for index, line in enumerate(self.encrypted_texts, start=1):
                if index == text_id:
                    self.encrypt_or_decrypt(line, 'decrypt')
                    is_not_valid_id = False
            if is_not_valid_id:
                print('Invalid id')
        elif mode == 'file':
            self.get_encrypted_texts_from_file()
            for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                if index == text_id:
                    self.encrypt_or_decrypt(line, 'decrypt')
                    is_not_valid_id = False

            if is_not_valid_id:
                print('Invalid id')

    def delete_text_from_list(self):
        if self.encrypted_texts:
            is_not_valid_id = True
            self.show_list()
            text_id = input('Enter id of text to delete: \n')
            for index, line in enumerate(self.encrypted_texts, start=1):
                if index == int(text_id):
                    print('das')
                    del self.encrypted_texts[int(text_id)-1]
                    is_not_valid_id = False

            if is_not_valid_id:
                print('Invalid id')
        else:
            print('List is empty')



    def get_number_of_text_in_list(self):
        return len(self.encrypted_texts)

    def get_number_of_texts_in_file(self):
        self.get_encrypted_texts_from_file()
        return len(self.encrypted_texts_form_file)


class Menu:
    def __init__(self):
        self.user_input = ' '
        self.encrypter = Encrypter()
        self.show_main_menu()

    def show_main_menu(self):
        while self.user_input != '1' or self.user_input != '2' or self.user_input != '3' or self.user_input != '4':
            self.user_input = input(
                f'Menu \n'
                f'1. Encrpyt text and save to file or list \n'
                f'2. Decrypt text \n'
                f'3. Display encrypted texts \n'
                f'4. Delete encrypted texts form list or file'
                f'5. Exit \n')

            if self.user_input == '5':
                break

            self.start_encrypter(self.user_input)

    def show_decrypt_menu(self):
        decrypt_option = 0
        while decrypt_option != '1' or decrypt_option != '2' or decrypt_option != '3':
            decrypt_option = input(
                f'1. Decrypt given text \n'
                f'2. Decrypt text form list \n'
                f'3. Decrpyt text from file \n '
                f'4. Return \n')

            self.start_decrypter(decrypt_option)
            break

    def show_display_menu(self):
        display_option = ' '
        while display_option != '1' or display_option != '2':
            display_option = input(
                f'1. Display texts in list \n'
                f'2. Display texts in file \n'
                f'3. Return \n')

            self.display_decrypted_texts(display_option)
            break

    def show_delete_menu(self):
        delete_option = ' '
        while delete_option != '1' or delete_option != '2' or delete_option == '3':
            delete_option = input(
                f'1. Delete text form list \n'
                f'2. Delete text from file \n'
                f'3. Return \n')

            self.delete_encrypted_texts(delete_option)
            break

    def start_encrypter(self, user):
        if user == '1':
            text_to_encrypt = str(input('Enter text to be encrypted: \n'))
            self.encrypter.encrypt_or_decrypt(text_to_encrypt, 'encrypt')
        elif user == '2':
            self.show_decrypt_menu()
        elif user == '3':
            self.show_display_menu()
        elif user == '4':
            self.show_delete_menu()

    def start_decrypter(self, decrypt_option):
        if decrypt_option == '1':
            text_to_decrypt = str(input('Enter text to be decrypted: \n'))
            self.encrypter.encrypt_or_decrypt(text_to_decrypt, 'decrypt')
        if decrypt_option == '2':
            if self.encrypter.get_number_of_text_in_list() == 0:
                print('List is empty ')
            else:
                self.encrypter.show_list()
                text_id = int(input('Enter id of text from list to decrypt: \n'))
                self.encrypter.decrypt_text_from_list_or_file(text_id, 'list')
        if decrypt_option == '3':
            if self.encrypter.encrypted_texts_form_file == 0:
                print('File is empty')
            else:
                self.encrypter.display_encrypted_texts_from_file()
                text_id = int(input('Enter id of text from file to decrypt: \n'))
                self.encrypter.decrypt_text_from_list_or_file(text_id, 'file')
        if decrypt_option == '4':
            self.show_main_menu()

    def display_decrypted_texts(self, display_option):
        if display_option == '1':
            self.encrypter.show_list()
        elif display_option == '2':
            self.encrypter.display_encrypted_texts_from_file()
        elif display_option == '3':
            self.show_main_menu()

    def delete_encrypted_texts(self, delete_option):
        if delete_option == '1':
            self.encrypter.delete_text_from_list()
        elif delete_option == '2':
            print('2')
        elif delete_option == '3':
            self.show_main_menu()


menu = Menu()
