# 1.RED 2.GREEN 3.REFACTOR

import unittest

# Own
from rot_13 import Encrypter, Decrypter


class TestROT13(unittest.TestCase):
    def setUp(self) -> None:
        self.encrypter = Encrypter()
        self.decrypter = Decrypter(self.encrypter)

    def test_asert_true_false(self):
        self.assertEqual(True, True)

    def test_if_word_test_it_will_be_encrypted_correctly_by_encrypt_or_decrypt_fnc(self):
        self.assertEqual("test", self.encrypter.encrypt_or_decrypt("grfg"),
                         msg="Word 'test' should be encrypted to 'grfg'.")
        self.assertEqual("example", self.encrypter.encrypt_or_decrypt("rknzcyr"),
                         msg="Word 'example' should be encrypted to 'rknzcyr'.")

    def test_if_word_lorem_will_be_saved_to_the_list_by_save_encrpyted_text_to_the_list_fnc(self):
        self.encrypter.save_encrypted_text_to_the_list('lorem')
        self.assertTrue('lorem' in self.encrypter.encrypted_texts,
                        msg='Word "lorem" is not on the list')

        self.encrypter.save_encrypted_text_to_the_list('ipsum')
        self.assertTrue('ipsum' in self.encrypter.encrypted_texts,
                        msg='Word "ipsum" is not on the list')

    def test_if_word_car_will_be_save_to_file_by_save_to_file_fnc(self):
        self.encrypter.save_enrypted_text_to_the_file('car')
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue('car' in file.read(),
                            msg='Word "car" has not been save in the file')

        self.encrypter.save_enrypted_text_to_the_file('bike')
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue('bike' in file.read(),
                            msg='Word "bike" has not been save in the file')

    def test_if_word_cat_is_in_file_by_is_text_in_file_fnc(self):
        self.encrypter.save_enrypted_text_to_the_file('cat')
        self.assertTrue(self.encrypter.is_text_in_file('cat'),
                        msg='There is no word "cat" in the file')

        self.encrypter.save_enrypted_text_to_the_file('dog')
        self.assertTrue(self.encrypter.is_text_in_file('dog'),
                        msg='There is no word "dog" in the file')

    def test_if_word_test_will_be_deleted_from_file_by_delete_text_from_file_fnc(self):
        self.encrypter.save_encrypted_text_to_the_list('example')
        self.encrypter.delete_text_from_file('example')
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue('example' not in file.read(),
                            msg='Word "example" has not been removed from the file ')

        self.encrypter.save_encrypted_text_to_the_list('test')
        self.encrypter.delete_text_from_file('test')
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue('test' not in file.read(),
                            msg='Word "example" has not been removed from the file ')

    def test_if_word_selected_by_the_user_will_be_deleted_from_list_by_delete_from_list_fnc(self):
        self.encrypter.save_encrypted_text_to_the_list('snow')
        self.encrypter.delete_text_from_list('snow')
        self.assertTrue('snow' not in self.encrypter.encrypted_texts,
                        msg='Word "snow" has not been removed from the list ')

        self.encrypter.save_encrypted_text_to_the_list('snowman')
        self.encrypter.delete_text_from_list('snowman')
        self.assertTrue('snowman' not in self.encrypter.encrypted_texts,
                        msg='Word "snowman" has not been removed from the file ')
    #
    # def test_if_list_is_empty_by_is_list_empty_fnc(self):
    #     self.encrypter.encrypted_texts.append('test')
    #     self.assertFalse(self.encrypter.is_list_empty())
