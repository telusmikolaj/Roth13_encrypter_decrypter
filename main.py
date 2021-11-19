
class Encrypter:
    def __init__(self):
        self.key = 13
        self.encrypted_texts = []

    def encrypt(self, text):
        ciphertext = ''
        for c in text:
            if c.isupper():
                ciphertext += chr((ord(c) + self.key - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(c) + self.key - 97) % 26 + 97)

        self.show_save_file_menu(ciphertext)

    def show_save_file_menu(self, encrypted_text):
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
                print(f'Encrpyted text: {encrypted_text} \n')
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
                print ('Hallo')
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
        self.show_menu()

    def show_menu(self):
        while self.userInput:
            self.userInput = int(input(
                f'Menu \n'
                f'1. Encrpyt text \n'
                f'2. Decrypt text \n'
                f'3. Show encrypted texts \n'
                f'4. Exit \n'))

            self.start_encrypter(self.userInput)

    def start_encrypter(self, user):
        if user == 1:
            text_to_encrypt = str(input('Podaj slowo do zaszyfrowania: '))
            self.encrypter.encrypt(text_to_encrypt)



menu = Menu()
menu.show_menu()
