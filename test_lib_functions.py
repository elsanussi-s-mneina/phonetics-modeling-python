"""
Unit tests for lib_functions
"""

import unittest
from lib_functions import analyze_transcription, ipa_text_to_phonet_list_report, is_glide, \
    analyze_transcription_to_sound_patterns_of_english


class TestLibFunctions(unittest.TestCase):
    def test_ipa_text_to_phonet_list_report__given_b(self) -> None:
        result = ipa_text_to_phonet_list_report("b")
        expected = "/b/ voiced bilabial plosive pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_ipa_text_to_phonet_list_report__given_l(self) -> None:
        result = ipa_text_to_phonet_list_report("l")
        expected = "/l/ voiced alveolar lateral approximant pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_ipa_text_to_phonet_list_report__given_j(self) -> None:
        """
        should be that [j] is the voiced palatal approximant pulmonic egressive consonant
        """
        result = ipa_text_to_phonet_list_report("j")
        expected = "/j/ voiced palatal approximant pulmonic egressive consonant"
        self.assertEqual(result,
                         expected)

    def test_ipa_text_to_phonet_list_report__given_two_phonemes(self) -> None:
        result = ipa_text_to_phonet_list_report("kc")
        expected = "/k/ voiceless velar plosive pulmonic egressive consonant\n" + \
                   "/c/ voiceless palatal plosive pulmonic egressive consonant"
        self.assertEqual(result, expected)  # "should be that [kc] has two lines"

    def test_is_glide_j(self) -> None:
        result = is_glide(analyze_transcription("j"))
        self.assertTrue(result, "should be that: [j] the voiced palatal approximant is a glide.")

    def test_is_glide_2(self) -> None:
        result = is_glide(analyze_transcription("ʝ"))
        self.assertFalse(result, "should be that: [ʝ] the voiced palatal fricative is not a glide.")

    def test_is_glide_3(self) -> None:
        result = is_glide(analyze_transcription("w"))
        self.assertTrue(result, "should be that: [w] is a glide.")

    def test_is_glide_4(self) -> None:
        result = is_glide(analyze_transcription("c"))
        self.assertFalse(result, "should be that: [c] is not a glide.")

    def test_is_glide_5(self) -> None:
        result = is_glide(analyze_transcription("ɥ"))
        self.assertTrue(result, "should be that: [ɥ] is a glide.")

    def sound_patterns_of_english_case_t(self) -> None:
        result = analyze_transcription_to_sound_patterns_of_english("t")
        expected = "[+consonantal; -syllabic; -continuant; -sonorant; +anterior; " + \
                   "-distributed; coronal; -round; -voice]"
        self.assertEqual(result, expected)

    def sound_patterns_of_english_case_d(self) -> None:
        result = analyze_transcription_to_sound_patterns_of_english("t")
        expected = "[+consonantal; -syllabic; -continuant; -sonorant; +anterior; " + \
                   "-distributed; coronal; -round; +voice]"
        self.assertEqual(result, expected)
