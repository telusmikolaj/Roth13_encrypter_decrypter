# PSL
from inspect import cleandoc
from typing import Dict, Union, NoReturn

# Own
from untils import get_text_from_user


class Encrypter:
    def __init__(self):
        self.key = 13
        self.encrypted_texts = []
        self.encrypted_texts_form_file = []

    def encrypt_or_decrypt(self, encrypted_text='', mode: str = "encrypt") -> Union[str, NoReturn]:
        text_to_encrypt = get_text_from_user("Enter text: ")
        for c in text_to_encrypt:
            if c.isupper():
                encrypted_text += chr((ord(c) + self.key - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(c) + self.key - 97) % 26 + 97)
        print(mode)
        if mode == "decrypt":
            return f"Decrypted: {encrypted_text}"

    def save_to_list(self, encrypted_text):
        if encrypted_text in self.encrypted_texts:
            print("This text is already on list \n")
        else:
            self.encrypted_texts.append(encrypted_text)
        self.show_list()

    def show_list(self):
        if len(self.encrypted_texts) == 0:
            print("List is empty \n")
        else:
            print("Encrypted texts list: ")
            for index, line in enumerate(self.encrypted_texts, start=1):
                print(f"{index}. {line}")

    def save_to_file(self, encrypted_text):

        if self.is_text_in_file(encrypted_text):
            print("Text is already in file")
        else:
            with open("encrypted_texts.txt", "a") as f:
                f.write(encrypted_text)
                f.write("\n")

    def display_encrypted_texts_from_file(self):
        self.get_encrypted_texts_from_file()
        if len(self.encrypted_texts_form_file) == 0:
            print("File is empty \n")
        else:
            print("Encrypted Texts: ")
            for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                print(f"{index}. {line}")

        print("\n")

    def get_encrypted_texts_from_file(self):
        self.encrypted_texts_form_file.clear()
        with open("encrypted_texts.txt") as f:
            for index, line in enumerate(f):
                self.encrypted_texts_form_file.append(line.strip())

    def is_text_in_file(self, encrypted_text):
        with open("encrypted_texts.txt") as f:
            if encrypted_text in f.read():
                return True

    def decrypt_text_from_list_or_file(self, text_id, mode):
        is_not_valid_id = True
        if mode == "list":
            for index, line in enumerate(self.encrypted_texts, start=1):
                if index == text_id:
                    self.encrypt_or_decrypt(line, "decrypt")
                    is_not_valid_id = False
            if is_not_valid_id:
                print("Invalid id")
        elif mode == "file":
            self.get_encrypted_texts_from_file()
            for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                if index == text_id:
                    self.encrypt_or_decrypt(line, "decrypt")
                    is_not_valid_id = False

            if is_not_valid_id:
                print("Invalid id")

    def delete_text_from_file(self):
        self.get_encrypted_texts_from_file()
        self.display_encrypted_texts_from_file()
        text_id = input("Enter id of text to delete: \n")
        if self.encrypted_texts_form_file:
            with open("encrypted_texts.txt", "w") as fp:
                for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                    if index != int(text_id):
                        fp.write(line)
                        fp.write("\n")

        else:
            print("File is empty")

    def delete_text_from_list(self):
        if self.encrypted_texts:
            is_not_valid_id = True
            self.show_list()
            text_id = input("Enter id of text to delete: \n")
            for index, line in enumerate(self.encrypted_texts, start=1):
                if index == int(text_id):
                    del self.encrypted_texts[int(text_id) - 1]
                    is_not_valid_id = False

            if is_not_valid_id:
                print("Invalid id")
        else:
            print("List is empty")

    def get_number_of_text_in_list(self):
        return len(self.encrypted_texts)

    def get_number_of_texts_in_file(self):
        self.get_encrypted_texts_from_file()
        return len(self.encrypted_texts_form_file)


class Decrypter(Encrypter):

    def decrypt_text(self):
        super().encrypt_or_decrypt(mode='decrypt')

    def start_decrypter(self, decrypt_option):
        if decrypt_option == "1":
            text_to_decrypt = str(input("Enter text to be decrypted: \n"))
            self.encrypter.encrypt_or_decrypt(text_to_decrypt, "decrypt")
        if decrypt_option == "2":
            if self.encrypter.get_number_of_text_in_list() == 0:
                print("List is empty ")
            else:
                self.encrypter.show_list()
                text_id = int(input("Enter id of text from list to decrypt: \n"))
                self.encrypter.decrypt_text_from_list_or_file(text_id, "list")
        if decrypt_option == "3":
            if self.encrypter.encrypted_texts_form_file == 0:
                print("File is empty")
            else:
                self.encrypter.display_encrypted_texts_from_file()
                text_id = int(input("Enter id of text from file to decrypt: \n"))
                self.encrypter.decrypt_text_from_list_or_file(text_id, "file")
        if decrypt_option == "4":
            self.show_main_menu()
