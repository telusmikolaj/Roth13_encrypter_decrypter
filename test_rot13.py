# 1.RED 2.GREEN 3.REFACTOR

import unittest

# Own
from rot_13 import Encrypter


class TestROT13(unittest.TestCase):
    def setUp(self) -> None:
        self.encrypter = Encrypter()

    def test_asert_true_false(self):
        self.assertEqual(True, True)

    def test_if_word_test_it_will_be_encrypted_correctly_by_encrypt_or_decrypt_fnc(self):
        self.assertEqual("test", self.encrypter.encrypt_or_decrypt("grfg"),
                         msg="Word 'test' should be encrypted to 'grfg'.")
        self.assertEqual("example", self.encrypter.encrypt_or_decrypt("rknzcyr"),
                         msg="Word 'example' should be encrypted to 'rknzcyr'.")

    # def test_if_word_test_will_be_saved_to_list_by_save_to_list_fnc(self):
    #     self.encrypter.save_to_list()
    #     self.assertTrue('grfg' in self.encrypter.encrypted_texts)

    # def test_if_word_given_by_user_will_be_save_to_file_by_save_to_file_fnc(self):
    #     self.encrypter.save_to_file()
    #     with open("encrypted_texts.txt", encoding="utf8") as file:
    #         self.assertTrue('beza' in file.read())
    #
    #
    # def test_if_word_test_is_in_file_by_is_text_in_file_fnc(self):
    #     word_test = 'test'
    #     self.assertTrue(self.encrypter.is_text_in_file(word_test))
    #
    # def test_if_word_selected_by_the_user_will_be_deleted_from_file_by_delete_text_from_file_fnc(self):
    #     self.encrypter.delete_text_from_file()
    #     with open("encrypted_texts.txt", encoding="utf8") as file:
    #         self.assertFalse('grfg' in file.read())


    # def test_if_word_selected_by_the_user_will_be_deleted_from_list_by_delete_from_list_fnc(self):
    #     self.encrypter.encrypted_texts.append('test')
    #     self.encrypter.delete_text_from_list()
    #     self.assertFalse('test' in self.encrypter.encrypted_texts)

    def test_if_list_is_empty_by_is_list_empty_fnc(self):
        self.encrypter.encrypted_texts.append('test')
        self.assertFalse(self.encrypter.is_list_empty())








