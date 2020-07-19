"""
Unit tests for lib_functions
"""

import unittest
from lib_functions import analyze_transcription, ipa_text_to_phonet_list_report, is_glide, \
    analyze_transcription_to_sound_patterns_of_english, voiced_transcription, devoiced_transcription


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
        result = analyze_transcription_to_sound_patterns_of_english("d")
        expected = "[+consonantal; -syllabic; -continuant; -sonorant; +anterior; " + \
                   "-distributed; coronal; -round; +voice]"
        self.assertEqual(result, expected)

    def is_voiceless_counterpart_of(self, unvoiced_phoneme: str, voiced_phoneme: str) -> None:
        """
        Tests voicing and devoicing a phoneme.
        :param unvoiced_phoneme: the unvoiced phoneme
        :param voiced_phoneme: the voiced counterpart phoneme
        :return: None
        """
        result = voiced_transcription(unvoiced_phoneme)
        expected = voiced_phoneme
        self.assertEqual(result, expected,
                         msg="should be that: [" + unvoiced_phoneme + "] voiced is [" + voiced_phoneme + "]")

        result = devoiced_transcription(voiced_phoneme)
        expected = unvoiced_phoneme
        self.assertEqual(result, expected,
                         msg= ("should be that: [" + voiced_phoneme
                               + "] devoiced is [" + unvoiced_phoneme + "]"))

    def test_voicing(self) -> None:
        self.is_voiceless_counterpart_of("t", "d")
        self.is_voiceless_counterpart_of("p", "b")
        self.is_voiceless_counterpart_of("ʈ", "ɖ")
        self.is_voiceless_counterpart_of("c", "ɟ")
        self.is_voiceless_counterpart_of("ʈ", "ɖ")
        self.is_voiceless_counterpart_of("k", "g")
        self.is_voiceless_counterpart_of("q", "ɢ")
        self.is_voiceless_counterpart_of("ɸ", "β")
        self.is_voiceless_counterpart_of("f", "v")
        self.is_voiceless_counterpart_of("θ", "ð")
        self.is_voiceless_counterpart_of("s", "z")
        self.is_voiceless_counterpart_of("ʃ", "ʒ")

        self.is_voiceless_counterpart_of("ʂ", "ʐ")
        self.is_voiceless_counterpart_of("ç", "ʝ")
        self.is_voiceless_counterpart_of("ɕ", "ʑ")
        self.is_voiceless_counterpart_of("x", "ɣ")
        self.is_voiceless_counterpart_of("x", "ɣ")
        self.is_voiceless_counterpart_of("χ", "ʁ")
        self.is_voiceless_counterpart_of("ħ", "ʕ")
        self.is_voiceless_counterpart_of("h", "ɦ")
        self.is_voiceless_counterpart_of("ɬ", "ɮ")


    def test_voicing_when_no_change(self) -> None:
        """
        voicing and devoicing a phoneme (when no change (idempotency))
        :return: None
        """
        self.assertEqual(devoiced_transcription("q"), "q",
                         msg="should be that: [q] devoiced is the same as itself")
        self.assertEqual(voiced_transcription("ɢ"), "ɢ", msg="should be that: [ɢ] voiced is the same as itself")
        self.assertEqual(voiced_transcription(voiced_transcription("k")), voiced_transcription("k"),
                         msg="voicing something twice is the same as voicing it once")
        self.assertEqual(voiced_transcription(voiced_transcription("g")), voiced_transcription("g"),
                         msg="[g]")
        self.assertEqual(devoiced_transcription(devoiced_transcription("k")), devoiced_transcription("k"))
