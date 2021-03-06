"""PSL"""
from typing import NoReturn, Optional

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
            encrypted_or_decrypted_text: Optional[str] = "",
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

    def return_encrypted_text_without_saving(self) -> str:
        """
        Return and print encrypted text
        """
        text_to_encrypt = get_text_from_user("Enter text to encrypt")
        encrypted_text = self.encrypt_or_decrypt(text_to_encrypt)
        print(f"Encrypted text - {encrypted_text}")
        return encrypted_text

    def save_encrypted_text_to_the_list(self, encrypted_text_to_save: str = '') -> bool:
        """
        Save enrypted text to list
        """
        result = True
        if not encrypted_text_to_save:
            text_to_encrypt_from_user = get_text_from_user('Enter text to save on list: ')
            encrypted_text_to_save = self.encrypt_or_decrypt(text_to_encrypt_from_user)

        if encrypted_text_to_save in self.encrypted_texts:
            print("This text is already on list \n")
            result = False
        else:
            self.encrypted_texts.append(encrypted_text_to_save)
            print('Saved!')
        self.show_encrypted_texts_from_list()

        return result

    def show_encrypted_texts_from_list(self) -> NoReturn:
        """
        Display encrypted text saved on list
        """
        if not self.is_list_empty():
            print("Encrypted texts list: ")
            for index, line in enumerate(self.encrypted_texts, start=1):
                print(f"{index}. {line}")
        else:
            print("List is empty \n")

    def save_enrypted_text_to_the_file(self, encrypted_text_to_save: str = '') -> NoReturn:
        """
        Save encrypted text to file
        """
        if not encrypted_text_to_save:
            text_from_user = get_text_from_user("Enter text and save to file: ")
            encrypted_text_to_save = self.encrypt_or_decrypt(text_from_user)

        if self.is_text_in_file(encrypted_text_to_save):
            print("Text is already in file")
        else:
            with open("encrypted_texts.txt", "a", encoding="utf8") as file:
                file.write(encrypted_text_to_save)
                file.write("\n")

    @staticmethod
    def is_text_in_file(encrypted_text) -> bool:
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
        else:
            print("File is empty \n")

    def delete_text_from_file(self, text_to_delete: str = '') -> NoReturn:
        """
        Delete text from the file using the given id

        """

        self.get_encrypted_texts_from_file()
        self.show_encrypted_texts_from_file()

        if not text_to_delete:
            text_to_delete = get_text_from_user('Enter text to delete: ')

        if self.encrypted_texts_form_file:
            with open("encrypted_texts.txt", "w", encoding="utf8") as file:
                for index, line in enumerate(self.encrypted_texts_form_file, start=1):
                    if line != text_to_delete:
                        file.write(line)
                        file.write("\n")

        else:
            print("File is empty")

    def delete_text_from_list(self, text_to_delete: str = '') -> NoReturn:
        """
        Delete text from the list using the given id

        """

        if self.encrypted_texts:
            is_not_valid_id = True
            self.show_encrypted_texts_from_list()
            if not text_to_delete:
                text_to_delete = get_text_from_user('Enter text to delete: ')
            for index, line in enumerate(self.encrypted_texts, start=1):
                if line == text_to_delete:
                    print('Thwre')
                    self.encrypted_texts.remove(text_to_delete)
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
            for index, line in enumerate(file):
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


class Decrypter:
    """
        A class to represent a decrypter that decrypts text encrypted with rot13.
    """

    def __init__(self, encrypter):
        self.encrypter = encrypter

    def get_decrypted_text(self, text_to_decrypt: str = '') -> str:
        """
        Decrpyt text given from user

        """

        if not text_to_decrypt:
            text_to_decrypt = get_text_from_user("Enter text to decrypt: ")

        decrypted_text = self.encrypter.encrypt_or_decrypt(text_to_decrypt)
        print(f"{text_to_decrypt}- {decrypted_text} ")
        return decrypted_text

    def get_decrypted_text_from_list_by_id(self, text_id: int = -1, decrypted_text: str = '') -> str:
        """
        Get Decrpyted text from the list using id given form user

        """
        if not self.encrypter.is_list_empty():
            self.encrypter.show_encrypted_texts_from_list()
            if text_id == -1:
                text_id = get_text_id_from_user("Enter text id: ")
            is_not_valid_id = True

            for index, encrypted_text in enumerate(self.encrypter.encrypted_texts, start=1):
                if index == text_id:
                    is_not_valid_id = False
                    decrypted_text = self.encrypter.encrypt_or_decrypt(encrypted_text)
                    print(f"{encrypted_text} - {decrypted_text} ")

            if is_not_valid_id:
                print("Invalid id")
        else:
            print("List is empty. Nothing to decrypt!")

        return decrypted_text

    def get_decrypted_text_from_file_by_id(self, text_id: int = -1, decrypted_text: str = '') -> str:
        """
        Get Decrpyted text from the file using id given form user

        """
        if not self.encrypter.is_file_empty():
            self.encrypter.show_encrypted_texts_from_file()
            if text_id == -1:
                text_id = get_text_id_from_user("Enter text id: ")
            self.encrypter.get_encrypted_texts_from_file()
            is_not_valid_id = True
            for index, encrypted_text in enumerate(
                    self.encrypter.encrypted_texts_form_file, start=1
            ):
                if index == text_id:
                    decrypted_text = self.encrypter.encrypt_or_decrypt(encrypted_text)
                    is_not_valid_id = False
                    print(f"{encrypted_text} - {decrypted_text} ")
            if is_not_valid_id:
                print("Invalid id")
        else:
            print("File is empty. Nothing to decrypt")

        return decrypted_text
