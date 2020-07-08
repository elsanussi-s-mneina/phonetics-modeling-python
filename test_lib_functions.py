"""
Unit tests for lib_functions
"""

import unittest
import lib_functions

class TestLibFunctions(unittest.TestCase):
    def test_ipa_text_to_phonet_list_report__given_b(self):
        result = lib_functions.ipa_text_to_phonet_list_report("b")
        expected = "/b/ voiced bilabial plosive pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_ipa_text_to_phonet_list_report__given_l(self):
        result = lib_functions.ipa_text_to_phonet_list_report("l")
        expected = "/l/ voiced alveolar lateral approximant pulmonic egressive consonant"
        self.assertEqual(result, expected)

