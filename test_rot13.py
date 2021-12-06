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

    def test_if_word_test_it_will_be_encrypted_correctly_by_encrypt_or_decrypt_fnc(
        self,
    ):
        """Test if word 'test' will be encrypted correctly to 'grfg' """
        self.assertEqual(
            "test",
            self.encrypter.encrypt_or_decrypt("grfg"),
            msg="Word 'test' should be encrypted to 'grfg'.",
        )
        self.assertEqual(
            "example",
            self.encrypter.encrypt_or_decrypt("rknzcyr"),
            msg="Word 'example' should be encrypted to 'rknzcyr'.",
        )

    def test_if_word_lorem_will_be_saved_to_the_list_by_save_encrpyted_text_to_the_list_fnc(
        self,
    ):
        """Test if word 'lorem' will saved to the list """

        self.encrypter.save_encrypted_text_to_the_list("lorem")
        self.assertTrue(
            "lorem" in self.encrypter.encrypted_texts,
            msg='Word "lorem" is not on the list',
        )

        self.encrypter.save_encrypted_text_to_the_list("ipsum")
        self.assertTrue(
            "ipsum" in self.encrypter.encrypted_texts,
            msg='Word "ipsum" is not on the list',
        )

    def test_if_word_car_will_be_save_to_file_by_save_to_file_fnc(self):
        """Test if word 'car' will saved to the file """
        self.encrypter.save_enrypted_text_to_the_file("car")
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue(
                "car" in file.read(), msg='Word "car" has not been save in the file'
            )

        self.encrypter.save_enrypted_text_to_the_file("bike")
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue(
                "bike" in file.read(), msg='Word "bike" has not been save in the file'
            )

    def test_if_word_cat_is_in_file_by_is_text_in_file_fnc(self):
        """Test if word 'cat' is in the file """

        self.encrypter.save_enrypted_text_to_the_file("cat")
        self.assertTrue(
            self.encrypter.is_text_in_file("cat"),
            msg='There is no word "cat" in the file',
        )

        self.encrypter.save_enrypted_text_to_the_file("dog")
        self.assertTrue(
            self.encrypter.is_text_in_file("dog"),
            msg='There is no word "dog" in the file',
        )

    def test_if_word_test_will_be_deleted_from_file_by_delete_text_from_file_fnc(self):
        """Test if word 'example' will be removed from file """

        self.encrypter.save_encrypted_text_to_the_list("example")
        self.encrypter.delete_text_from_file("example")
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue(
                "example" not in file.read(),
                msg='Word "example" has not been removed from the file ',
            )

        self.encrypter.save_encrypted_text_to_the_list("test")
        self.encrypter.delete_text_from_file("test")
        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertTrue(
                "test" not in file.read(),
                msg='Word "example" has not been removed from the file ',
            )

    def test_if_word_snow_will_be_deleted_from_list_by_delete_from_list_fnc(
        self,
    ):
        """Test if word 'snow' will be removed from list """

        self.encrypter.save_encrypted_text_to_the_list("snow")
        self.encrypter.delete_text_from_list("snow")
        self.assertTrue(
            "snow" not in self.encrypter.encrypted_texts,
            msg='Word "snow" has not been removed from the list ',
        )

        self.encrypter.save_encrypted_text_to_the_list("snowman")
        self.encrypter.delete_text_from_list("snowman")
        self.assertTrue(
            "snowman" not in self.encrypter.encrypted_texts,
            msg='Word "snowman" has not been removed from the file ',
        )

    def test_if_list_is_empty_by_is_list_empty_fnc(self):
        """Test if list  is empty """

        self.encrypter.save_encrypted_text_to_the_list("audi")
        self.assertFalse(self.encrypter.is_list_empty(), msg="List is not empty")

    def test_if_file_is_empty_by_is_file_empty_fnc(self):
        """Test if file  is empty """

        self.encrypter.save_enrypted_text_to_the_file("mercedes")
        self.assertFalse(self.encrypter.is_file_empty(), msg="File is not empty")

    def test_if_text_is_in_the_file_by_is_text_in_the_file_fnc(self):
        """Test if word book is in the file """

        self.encrypter.save_enrypted_text_to_the_file("book")
        self.assertTrue(self.encrypter.is_text_in_file("book"))

    def test_if_text_rknzcyr_will_be_decrypted_by_decrypt_text_fnc(self):
        """Test if text 'rknzcyr' will be decrypted correctly to 'example' """

        self.assertEqual(
            "grfg",
            self.decrypter.get_decrypted_text("test"),
            msg="Word 'grfg' should be encrypted to 'test'.",
        )
        self.assertEqual(
            "rknzcyr",
            self.decrypter.get_decrypted_text("example"),
            msg="Word 'rknzcyr' should be encrypted to 'example'.",
        )

    def test_if_text_with_index_1_from_list_will_be_decrypted_by_derypt_text_from_list_fnc(
        self,
    ):
        """Test if text from list with index 1 will be decrypted """

        encrpyted_text_with_index_1 = self.encrypter.encrypt_or_decrypt("test")
        self.encrypter.save_encrypted_text_to_the_list(encrpyted_text_with_index_1)

        self.assertEqual(
            "test",
            self.decrypter.get_decrypted_text_from_list_by_id(1),
            msg="Decrypted word should be 'test' ",
        )

        encrpyted_text_with_index_2 = self.encrypter.encrypt_or_decrypt("example")
        self.encrypter.save_encrypted_text_to_the_list(encrpyted_text_with_index_2)
        self.assertEqual(
            "example",
            self.decrypter.get_decrypted_text_from_list_by_id(2),
            msg="Decrypted word should be 'example' ",
        )

    def test_if_text_with_index_1_from_file_will_be_decrypted_by_derypted_text_from_file_by_id_fnc(
        self,
    ):

        with open("encrypted_texts.txt", encoding="utf8") as file:
            self.assertEqual(
                'car',
                self.decrypter.get_decrypted_text_from_file_by_id(1),
                msg="Decrypted word should be 'car' ",
            )
