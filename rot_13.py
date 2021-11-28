"""PSL"""
from typing import NoReturn

# Own
from untils import get_text_from_user
from untils import get_text_id_from_user


class Encrypter:
    """
    A class to represent a encrypter that encrypts with rot13.

    Attributes
    ----------
    key : str
        ciper key of encrypter
    encrypted_texts : list
        encrpyted texts
    encrpyted_texts_from_file : list
        encrypted texts form file

    """

    def __init__(self):
        self.key = 13
        self.encrypted_texts = []
        self.encrypted_texts_form_file = []

    def encrypt_or_decrypt(
            self,
            text_to_encrypt_or_decrypt: str = "",
            encrypted_or_decrypted_text: str = "",
    ) -> str:
        """
        Return encrypted/decrypted text
        """
        for char in text_to_encrypt_or_decrypt:
            if char.isupper():
                encrypted_or_decrypted_text += chr(
                    (ord(char) + self.key - 65) % 26 + 65
                )
            else:
                encrypted_or_decrypted_text += chr(
                    (ord(char) + self.key - 97) % 26 + 97
                )

        return encrypted_or_decrypted_text

    def encrypt_without_saving(self) -> NoReturn:
        """
        Only print encrypted text
        """
        text_to_encrypt = get_text_from_user("Enter text to encrypt")
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        print(f"Encrypted text - {encrypted_text}")

    def save_to_list(self) -> NoReturn:
        """
        Save enrypted text to list
        """
        text_to_encrypt = get_text_from_user("Enter text and save to list: ")
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        if encrypted_text in self.encrypted_texts:
            print("This text is already on list \n")
        else:
            self.encrypted_texts.append(encrypted_text)
        self.show_encrypted_texts_from_list()

    def show_encrypted_texts_from_list(self) -> NoReturn:
        """
        Display encrypted text saved on list
        """
        if not self.is_list_empty():
            print("Encrypted texts list: ")
            for index, line in enumerate(self.encrypted_texts, start=1):
                print(f"{index}. {line}")

        print("List is empty \n")

    def save_to_file(self) -> NoReturn:
        """
        Save encrypted text to file
        """
        text_to_encrypt = get_text_from_user("Enter text and save to file: ")
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        if self.is_text_in_file(encrypted_text):
            print("Text is already in file")
        else:
            with open("encrypted_texts.txt", "a", encoding="utf8") as file:
                file.write(encrypted_text)
                file.write("\n")

    @classmethod
    def is_text_in_file(cls, encrypted_text) -> bool:
        """
        Checks if the file contains text
        """
        with open("encrypted_texts.txt", encoding="utf8") as file:
            if encrypted_text in file.read():
                return True
        return False

    def show_encrypted_texts_from_file(self) -> NoReturn:
        """
        Display encrypted texts from file

        """
        self.get_encrypted_texts_from_file()
        if not self.is_file_empty():
            print("Encrypted Texts: ")
            for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                print(f"{index}. {line}")

        print("List is empty \n")

    def delete_text_from_file(self) -> NoReturn:
        """
        Delete text from the file using the given id

        """
        self.get_encrypted_texts_from_file()
        self.show_encrypted_texts_from_file()
        text_id = get_text_id_from_user("Enter text id: ")
        if self.encrypted_texts_form_file:
            with open("encrypted_texts.txt", "w", encoding="utf8") as file:
                for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                    if index != int(text_id):
                        file.write(line)
                        file.write("\n")

        else:
            print("File is empty")

    def delete_text_from_list(self) -> NoReturn:
        """
        Delete text from the list using the given id

        """
        if self.encrypted_texts:
            is_not_valid_id = True
            self.show_encrypted_texts_from_list()
            text_id = get_text_id_from_user("Enter text id: ")
            for index in enumerate(self.encrypted_texts, start=1):
                if index == int(text_id):
                    del self.encrypted_texts[int(text_id) - 1]
                    is_not_valid_id = False

            if is_not_valid_id:
                print("Invalid id")
        else:
            print("List is empty")

    def get_encrypted_texts_from_file(self) -> NoReturn:
        """
        Return encrpyted texts from file

        """
        self.encrypted_texts_form_file.clear()
        with open("encrypted_texts.txt", encoding="utf8") as file:
            for line in enumerate(file):
                self.encrypted_texts_form_file.append(line.strip())

    def is_list_empty(self) -> bool:
        """
        Checks if the list is empty

        """
        return len(self.encrypted_texts) <= 0

    def is_file_empty(self) -> bool:
        """
        Checks if the file is empty

        """
        self.get_encrypted_texts_from_file()
        return len(self.encrypted_texts_form_file) <= 0


class Decrypter(Encrypter):
    """
        A class to represent a decrypter that decrypts text encrypted with rot13.

    """

    def decrypt_text_from_user(self) -> NoReturn:
        """
        Decrpyt text given from user

        """
        text_to_decrypt = get_text_from_user("Enter text to decrypt: ")
        decrypted_text = self.encrypt_or_decrypt(text_to_decrypt)
        return print(f"Decrypted - {decrypted_text} ")

    def decrypt_text_from_list(self) -> NoReturn:
        """
        Decrpyt text from the list using id given form user

        """
        if not self.is_list_empty():
            self.show_encrypted_texts_from_list()
            text_id = get_text_id_from_user("Enter text id: ")
            is_not_valid_id = True
            for index, encrypted_text in enumerate(self.encrypted_texts, start=1):
                if index == text_id:
                    decrypted_text = self.decrypt_text(encrypted_text)
                    print(f"{encrypted_text} - {decrypted_text} ")
                    is_not_valid_id = False
            if is_not_valid_id:
                print("Invalid id")

        print("List is empty. Nothing to decrypt!")

    def decrypt_text_from_file(self) -> NoReturn:
        """
        Decrpyt text from the file using id given form user

        """
        if not self.is_file_empty():
            self.show_encrypted_texts_from_file()
            text_id = get_text_id_from_user("Enter text id: ")
            self.get_encrypted_texts_from_file()
            is_not_valid_id = True
            for index, encrypted_text in enumerate(
                    self.encrypted_texts_form_file, start=1
            ):
                if index == text_id:
                    decrypted_text = self.encrypt_or_decrypt(encrypted_text)
                    is_not_valid_id = False
                    print(f"{encrypted_text} - {decrypted_text} ")
            if is_not_valid_id:
                print("Invalid id")

        print("File is empty. Nothing to decrypt")
