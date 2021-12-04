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

    def test_if_word_test_will_be_saved_to_list(self):
        self.encrypter.save_to_list()
        self.assertTrue('grfg' in self.encrypter.encrypted_texts)




