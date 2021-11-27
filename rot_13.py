# PSL

from typing import Dict, Union, NoReturn

# Own
from untils import get_text_from_user
from untils import get_text_id_from_user


class Encrypter:
    def __init__(self):
        self.key = 13
        self.encrypted_texts = []
        self.encrypted_texts_form_file = []

    def encrypt_or_decrypt(self, text_to_encrypt_or_decrypt: str = '', encrypted_or_decrypted_text: str = '', ) -> str:
        for c in text_to_encrypt_or_decrypt:
            if c.isupper():
                encrypted_or_decrypted_text += chr((ord(c) + self.key - 65) % 26 + 65)
            else:
                encrypted_or_decrypted_text += chr((ord(c) + self.key - 97) % 26 + 97)

        return encrypted_or_decrypted_text

    def encrypt_without_saving(self) -> NoReturn:
        text_to_encrypt = get_text_from_user('Enter text to encrypt')
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        print(f'Encrypted text - {encrypted_text}')

    def save_to_list(self) -> NoReturn:
        text_to_encrypt = get_text_from_user("Enter text and save to list: ")
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        if encrypted_text in self.encrypted_texts:
            print("This text is already on list \n")
        else:
            self.encrypted_texts.append(encrypted_text)
        self.show_encrypted_texts_from_list()

    def show_encrypted_texts_from_list(self) -> NoReturn:
        if not self.is_list_empty():
            print("Encrypted texts list: ")
            for index, line in enumerate(self.encrypted_texts, start=1):
                print(f"{index}. {line}")

        print(f'List is empty \n')

    def save_to_file(self) -> NoReturn:
        text_to_encrypt = get_text_from_user("Enter text and save to file: ")
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        if self.is_text_in_file(encrypted_text):
            print("Text is already in file")
        else:
            with open("encrypted_texts.txt", "a") as f:
                f.write(encrypted_text)
                f.write("\n")

    def is_text_in_file(self, encrypted_text) -> bool:
        with open("encrypted_texts.txt") as f:
            if encrypted_text in f.read():
                return True
        return False

    def show_encrypted_texts_from_file(self) -> NoReturn:
        self.get_encrypted_texts_from_file()
        if not self.is_file_empty():
            print("Encrypted Texts: ")
            for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                print(f"{index}. {line}")

        print(f'List is empty \n')

    def delete_text_from_file(self) -> NoReturn:
        self.get_encrypted_texts_from_file()
        self.show_encrypted_texts_from_file()
        text_id = get_text_id_from_user('Enter text id: ')
        if self.encrypted_texts_form_file:
            with open("encrypted_texts.txt", "w") as fp:
                for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                    if index != int(text_id):
                        fp.write(line)
                        fp.write("\n")

        else:
            print("File is empty")

    def delete_text_from_list(self) -> NoReturn:
        if self.encrypted_texts:
            is_not_valid_id = True
            self.show_list()
            text_id = get_text_id_from_user('Enter text id: ')
            for index, line in enumerate(self.encrypted_texts, start=1):
                if index == int(text_id):
                    del self.encrypted_texts[int(text_id) - 1]
                    is_not_valid_id = False

            if is_not_valid_id:
                print("Invalid id")
        else:
            print("List is empty")


    def get_encrypted_texts_from_file(self) -> NoReturn:
        self.encrypted_texts_form_file.clear()
        with open("encrypted_texts.txt") as f:
            for index, line in enumerate(f):
                self.encrypted_texts_form_file.append(line.strip())

    def is_list_empty(self) -> bool:
        return len(self.encrypted_texts) <= 0

    def is_file_empty(self) -> bool:
        self.get_encrypted_texts_from_file()
        return len(self.encrypted_texts_form_file) <= 0


class Decrypter(Encrypter):

    def decrypt_text_from_user(self) -> NoReturn:
        text_to_decrypt = get_text_from_user('Enter text to decrypt: ')
        decrypted_text = self.encrypt_or_decrypt(text_to_decrypt)
        return print(f'Decrypted - {decrypted_text} ')

    def decrypt_text_from_list(self) -> str:

        if not self.is_list_empty():
            self.show_encrypted_texts_from_list()
            text_id = get_text_id_from_user('Enter text id: ')
            is_not_valid_id = True
            for index, encrypted_text in enumerate(self.encrypted_texts, start=1):
                if index == text_id:
                    decrypted_text = self.decrypt_text(encrypted_text)
                    return print(f'{encrypted_text} - {decrypted_text} ')
                    is_not_valid_id = False
            if is_not_valid_id:
                print('Invalid id')

        return print('List is empty. Nothing to decrypt!')

    def decrypt_text_from_file(self) -> str:
        if not self.is_file_empty():
            self.show_encrypted_texts_from_file()
            text_id = get_text_id_from_user('Enter text id: ')
            self.get_encrypted_texts_from_file()
            is_not_valid_id = True
            for index, encrypted_text in enumerate(self.encrypted_texts_form_file, start=1):
                if index == text_id:
                    decrypted_text = self.encrypt_or_decrypt(encrypted_text)
                    return print(f'{encrypted_text} - {decrypted_text} ')
                    is_not_valid_id = False
            if is_not_valid_id:
                return print("Invalid id")

        return print('File is empty. Nothing to decrypt')
