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
        avalible_choices: Dict[str, str] = {"1": self.encrypter.get_text_to_encrypt_from_user, "2": self.decrypter.show_decrypt_menu}
        while 1:
            print(self.show_main_menu())
            user_input_ = input("> ")
            if user_input_ in avalible_choices:
                avalible_choices[user_input_]()
            else:
                print("Wrong choice!")

    def show_main_menu(self) -> str:
        return cleandoc(
            """
            Menu
            1. Encrypt text and save to file or list
            2. Decrypt text
            3. Display encrypted texts
            4. Delete encrypted texts form list or file
            5. Exit
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
        elif user == "3":
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


menu = Menu()
