# PSL
from inspect import cleandoc
from typing import Dict, NoReturn

# Own
from rot_13 import Decrypter, Encrypter


class MainMenu:
    def __init__(self) -> NoReturn:
        self.encrypter = Encrypter()
        self.decrypter = Decrypter()

    def invoke_main_loop(self) -> NoReturn:
        avalible_choices: Dict[str, str] = {
            "1": self.invoke_encrypter_menu_loop,
            "2": self.invoke_decrypter_menu_loop}
        while 1:
            print(self.show_main_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_choices:
                avalible_choices[user_input_]()
            elif user_input_ == '5':
                break
            else:
                print("Wrong choice!")

    def show_main_menu(self) -> str:
        return cleandoc(
            """
            Menu
            1. Encrypt text 
            2. Decrypt text 
            3. Display encrypted texts
            4. Delete encrypted texts form list or file
            5. Exit
            """
        )

    def invoke_encrypter_menu_loop(self) -> NoReturn:
        avalible_encrypter_options: Dict[str, str] = {
            '1': self.encrypter.encrypt_without_saving,
            '2': self.encrypter.save_to_list,
            '3': self.encrypter.save_to_file,

        }
        while 1:
            print(self.show_encrypter_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_encrypter_options:
                avalible_encrypter_options[user_input_]()
            elif user_input_ == '4':
                break
            else:
                print("Wrong choice!")

    def show_encrypter_menu(self) -> str:

        return cleandoc(
            """
                1. Only print encrypted text
                2. Save encrypted text to list
                3. Save encrypted text to file
                4. Retrun
             """
        )

    def invoke_decrypter_menu_loop(self) -> NoReturn:
        avalible_decrypter_options: Dict[str, str] = {
            '1': self.decrypter.decrypt_text,
            '2': self.decrypter.decrypt_text_from_list_or_file

        }
        while 1:
            print(self.show_decrypt_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_decrypter_options:
                avalible_decrypter_options[user_input_]()
            elif user_input_ == '4':
                break
            else:
                print("Wrong choice!")

    def show_decrypt_menu(self) -> str:

        return cleandoc(
            """
                1. Decrypt given text
                2. Decrypt text form list
                3. Decrpyt text from file
                4. Return
                    """
        )

    def show_display_menu(self):
        display_option = " "
        while display_option != "1" or display_option != "2":
            display_option = input(
                f"1. Display texts in list \n" f"2. Display texts in file \n" f"3. Return \n"
            )

            self.display_decrypted_texts(display_option)
            break

    def show_delete_menu(self):
        delete_option = " "
        while delete_option != "1" or delete_option != "2" or delete_option == "3":
            delete_option = input(
                f"1. Delete text form list \n" f"2. Delete text from file \n" f"3. Return \n"
            )

            self.delete_encrypted_texts(delete_option)
            break

    def start_encrypter(self, user):
        if user == "3":
            self.show_display_menu()
        elif user == "4":
            self.show_delete_menu()



    def display_decrypted_texts(self, display_option):
        if display_option == "1":
            self.encrypter.show_list()
        elif display_option == "2":
            self.encrypter.display_encrypted_texts_from_file()
        elif display_option == "3":
            self.show_main_menu()

    def delete_encrypted_texts(self, delete_option):
        if delete_option == "1":
            self.encrypter.delete_text_from_list()
        elif delete_option == "2":
            self.encrypter.delete_text_from_file()
        elif delete_option == "3":
            self.show_main_menu()


if __name__ == "__main__":
    MainMenu().invoke_main_loop()
