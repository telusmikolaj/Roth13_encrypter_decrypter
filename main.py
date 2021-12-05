# PSL
from inspect import cleandoc
from typing import Dict, NoReturn

# Own
from rot_13 import Decrypter, Encrypter


class MainMenu:
    """
    A class to represent main menu.

    Attributes
    ----------
    encrypter : class
        class of encrpyter
    decrypter : class
    class of decrypter
    """

    def __init__(self) -> NoReturn:
        self.encrypter = Encrypter()
        self.decrypter = Decrypter(self.encrypter)



    def invoke_main_loop(self) -> NoReturn:
        """
        Invokes main menu loop
        :param x: this is a random number
        :type x: int
        :return: Nothing
        """
        avalible_choices: Dict[str, str] = {
            "1": self.invoke_encrypter_menu_loop,
            "2": self.invoke_decrypter_menu_loop,
            "3": self.invoke_display_menu_loop,
            "4": self.invoke_delete_menu_loop,
        }
        while 1:
            print(self.show_main_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_choices:
                avalible_choices[user_input_]()
            elif user_input_ == "5":
                break
            else:
                print("Wrong choice!")

    @staticmethod
    def show_main_menu() -> str:
        """Return main menu"""
        return cleandoc(
            """
                1. Encrypt text and save to list or file
                2. Decrypt text from list or file
                3. Display form list or file
                4. Delete text form list or file
                5. Exit
             """
        )

    def invoke_encrypter_menu_loop(self) -> NoReturn:
        """Invokes encrypter menu loop"""
        avalible_encrypter_options: Dict[str, str] = {
            "1": self.encrypter.return_encrypted_text_without_saving,
            "2": self.encrypter.save_encrypted_text_to_the_list,
            "3": self.encrypter.save_enrypted_text_to_the_file,
        }
        while 1:
            print(self.show_encrypter_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_encrypter_options:
                avalible_encrypter_options[user_input_]()
            elif user_input_ == "4":
                break
            else:
                print("Wrong choice!")

    @classmethod
    def show_encrypter_menu(cls) -> str:
        """Return encrpyter menu"""
        return cleandoc(
            """
                1. Only print encrypted text
                2. Save encrypted text to list
                3. Save encrypted text to file
                4. Retrun
             """
        )

    def invoke_decrypter_menu_loop(self) -> NoReturn:
        """Invokes decrypter menu loop"""
        avalible_decrypter_options: Dict[str, str] = {
            "1": self.decrypter.get_decrypted_text,
            "2": self.decrypter.decrypt_text_from_list,
            "3": self.decrypter.decrypt_text_from_file,
        }
        while 1:
            print(self.show_decrypt_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_decrypter_options:
                avalible_decrypter_options[user_input_]()
            elif user_input_ == "4":
                break
            else:
                print("Wrong choice!")

    @classmethod
    def show_decrypt_menu(cls) -> str:
        """Return decrypt menu"""
        return cleandoc(
            """
                1. Decrypt given text
                2. Decrypt text form list
                3. Decrpyt text from file
                4. Return
                    """
        )

    def invoke_display_menu_loop(self) -> NoReturn:
        """Invokes display menu loop"""
        avalible_display_options: Dict[str, str] = {
            "1": self.encrypter.show_encrypted_texts_from_list,
            "2": self.encrypter.show_encrypted_texts_from_file,
        }
        while 1:
            print(self.show_display_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_display_options:
                avalible_display_options[user_input_]()
            elif user_input_ == "3":
                break
            else:
                print("Wrong choice!")

    @classmethod
    def show_display_menu(cls) -> str:
        """Return display menu"""
        return cleandoc(
            """
                1. Display texts in list
                2. Display texts in file
                3. Return
            """
        )

    def invoke_delete_menu_loop(self) -> NoReturn:
        """Invokes delete menu loop"""
        avalible_delete_options: Dict[str, str] = {
            "1": self.encrypter.delete_text_from_list,
            "2": self.encrypter.delete_text_from_file,
        }
        while 1:
            print(self.show_delete_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_delete_options:
                avalible_delete_options[user_input_]()
            elif user_input_ == "3":
                break
            else:
                print("Wrong choice!")

    @classmethod
    def show_delete_menu(cls) -> str:
        """Return delete menu"""
        return cleandoc(
            """
                1. Delete text from list
                2. Delete text from file
                3. Return
            """
        )


if __name__ == "__main__":
    MainMenu().invoke_main_loop()
