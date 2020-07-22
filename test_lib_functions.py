"""
Unit tests for lib_functions
"""

import unittest
from lib_functions import analyze_transcription, ipa_text_to_phonet_list_report, is_glide, \
    analyze_transcription_to_sound_patterns_of_english, voiced_transcription, devoiced_transcription


class TestLibFunctions(unittest.TestCase):
    """
    Class containing unit tests for lib_functions module.
    """
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

    def test_ipa_text_to_phonet_list_report__given_one_affricate(self) -> None:
        result = ipa_text_to_phonet_list_report("t͡ʃ")
        expected = "/t͡ʃ/ voiceless post-alveolar affricate pulmonic egressive consonant"
        self.assertEqual(result, expected,
                         msg="should be that [t͡ʃ] ..")

    def test_ipa_text_to_phonet_list_report__given_one_affricate_accept_other_tie_bar(self) -> None:
        result = ipa_text_to_phonet_list_report("t͜ʃ")
        expected = "/t͜ʃ/ voiceless post-alveolar affricate pulmonic egressive consonant"
        self.assertEqual(result, expected,
                         msg="should accept opposite tie-bar")


    def test_ipa_text_to_phonet_list_report__given_two_phonemes(self) -> None:
        result = ipa_text_to_phonet_list_report("kc")
        expected = "/k/ voiceless velar plosive pulmonic egressive consonant\n" + \
                   "/c/ voiceless palatal plosive pulmonic egressive consonant"
        self.assertEqual(result, expected, msg="should be that [kc] has two lines")

    def test_ipa_text_to_phonet_list_report__given_a_plosive_then_fricative(self) -> None:
        result = ipa_text_to_phonet_list_report("tʃ")
        expected = "/t/ voiceless alveolar plosive pulmonic egressive consonant\n" + \
                   "/ʃ/ voiceless post-alveolar fricative pulmonic egressive consonant"
        self.assertEqual(result, expected, msg="should be that (tʃ) with no tie bar is 2 phonemes.")

    def test_ipa_text_to_phonet_list_report__given_2_affricates_and_a_plosive(self) -> None:
        result = ipa_text_to_phonet_list_report("t͜ʃdd͜ʒ")
        expected = "/t͜ʃ/ voiceless post-alveolar affricate pulmonic egressive consonant\n" + \
                   "/d/ voiced alveolar plosive pulmonic egressive consonant\n" + \
                   "/d͜ʒ/ voiced post-alveolar affricate pulmonic egressive consonant"
        self.assertEqual(result,
                         expected,
                         msg="should be that (t͜ʃdd͜ʒ) is properly split into 3 phonemes")

    def test_ipa_text_to_phonet_list_report__four_phonemes_two_affricates(self) -> None:
        result = ipa_text_to_phonet_list_report("t͜ʃdd͜ʒʒ")
        expected = "/t͜ʃ/ voiceless post-alveolar affricate pulmonic egressive consonant\n" + \
                   "/d/ voiced alveolar plosive pulmonic egressive consonant\n" + \
                   "/d͜ʒ/ voiced post-alveolar affricate pulmonic egressive consonant\n" + \
                   "/ʒ/ voiced post-alveolar fricative pulmonic egressive consonant"
        self.assertEqual(result,
                         expected,
                         msg="should be that (t͜ʃdd͜ʒʒ) is properly split into 4 phonemes")


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
        self.assertEqual(
            result,
            expected,
            msg="should be that: [" + unvoiced_phoneme + "] voiced is [" + voiced_phoneme + "]")

        result = devoiced_transcription(voiced_phoneme)
        expected = unvoiced_phoneme
        self.assertEqual(result, expected,
                         msg=("should be that: [" + voiced_phoneme
                              + "] devoiced is [" + unvoiced_phoneme + "]"))

    def test_voicing_no_diacritics(self) -> None:
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

    def test_voicing_with_voiceless_diacritic_usual(self) -> None:
        """
        Test that phonemes that in IPA require the diacritic symbol
        to express voicelessness are handled correctly
        :return: None
        """
        # Nasal consonants:
        self.is_voiceless_counterpart_of("m̥", "m")
        self.is_voiceless_counterpart_of("ɱ̊", "ɱ")
        self.is_voiceless_counterpart_of("n̥", "n")
        self.is_voiceless_counterpart_of("ɲ̊", "ɲ")
        self.is_voiceless_counterpart_of("ɳ̊", "ɳ")
        self.is_voiceless_counterpart_of("ŋ̊", "ŋ")
        self.is_voiceless_counterpart_of("ɴ̥", "ɴ")

        # Trill consonants:
        self.is_voiceless_counterpart_of("ʙ̥", "ʙ")
        self.is_voiceless_counterpart_of("r̥", "r")
        self.is_voiceless_counterpart_of("ʀ̥", "ʀ")

        # Tap or flap consonants:
        self.is_voiceless_counterpart_of("ⱱ̥", "ⱱ")
        self.is_voiceless_counterpart_of("ɾ̥", "ɾ")
        self.is_voiceless_counterpart_of("ɽ̊", "ɽ")

        # Approximant consonants:
        self.is_voiceless_counterpart_of("ʋ̥", "ʋ")
        self.is_voiceless_counterpart_of("ɹ̥", "ɹ")
        self.is_voiceless_counterpart_of("ɻ̊", "ɻ")
        self.is_voiceless_counterpart_of("j̊", "j")
        self.is_voiceless_counterpart_of("ɰ̊", "ɰ")

        # Lateral approximants:
        self.is_voiceless_counterpart_of("l̥", "l")
        self.is_voiceless_counterpart_of("ɭ̥", "ɭ")
        self.is_voiceless_counterpart_of("ʎ̥", "ʎ")
        self.is_voiceless_counterpart_of("ʟ̥", "ʟ")

        # Vowels
        self.is_voiceless_counterpart_of("i̥", "i")
        self.is_voiceless_counterpart_of("ẙ", "y")
        self.is_voiceless_counterpart_of("ɨ̥", "ɨ")
        self.is_voiceless_counterpart_of("ʉ̥", "ʉ")
        self.is_voiceless_counterpart_of("ɯ̥", "ɯ")
        self.is_voiceless_counterpart_of("u̥", "u")
        self.is_voiceless_counterpart_of("ɪ̥", "ɪ")
        self.is_voiceless_counterpart_of("ʏ̥", "ʏ")
        self.is_voiceless_counterpart_of("ʊ̥", "ʊ")
        self.is_voiceless_counterpart_of("e̥", "e")
        self.is_voiceless_counterpart_of("ø̥", "ø")
        self.is_voiceless_counterpart_of("ɘ̥", "ɘ")
        self.is_voiceless_counterpart_of("ɵ̥", "ɵ")
        self.is_voiceless_counterpart_of("ɤ̥", "ɤ")
        self.is_voiceless_counterpart_of("o̥", "o")
        self.is_voiceless_counterpart_of("ə̥", "ə")
        self.is_voiceless_counterpart_of("ɛ̥", "ɛ")
        self.is_voiceless_counterpart_of("œ̥", "œ")
        self.is_voiceless_counterpart_of("ɜ̥", "ɜ")
        self.is_voiceless_counterpart_of("ɜ̥", "ɜ")
        self.is_voiceless_counterpart_of("ɞ̥", "ɞ")
        self.is_voiceless_counterpart_of("ʌ̥", "ʌ")
        self.is_voiceless_counterpart_of("ɔ̥", "ɔ")
        self.is_voiceless_counterpart_of("æ̥", "æ")
        self.is_voiceless_counterpart_of("ɐ̥", "ɐ")
        self.is_voiceless_counterpart_of("ḁ", "a")
        self.is_voiceless_counterpart_of("ɶ̥", "ɶ")
        self.is_voiceless_counterpart_of("ɑ̥", "ɑ")
        self.is_voiceless_counterpart_of("ɒ̥", "ɒ")
        self.is_voiceless_counterpart_of("w̥", "w")
        self.is_voiceless_counterpart_of("ɥ̊", "ɥ")
        self.is_voiceless_counterpart_of("ɕ", "ʑ")
        self.is_voiceless_counterpart_of("ɺ̥", "ɺ")



    def test_voicing_with_voiced_diacritic(self) -> None:
        self.is_voiceless_counterpart_of("ʔ", "ʔ̬")
        self.is_voiceless_counterpart_of("ʡ", "ʡ̬")
        self.is_voiceless_counterpart_of("ʍ", "ʍ̬")



    def test_voicing_when_no_change(self) -> None:
        """
        voicing and devoicing a phoneme (when no change (idempotency))
        :return: None
        """
        self.assertEqual(devoiced_transcription("q"),
                         "q",
                         msg="should be that: [q] devoiced is the same as itself")
        self.assertEqual(voiced_transcription("ɢ"),
                         "ɢ",
                         msg="should be that: [ɢ] voiced is the same as itself")
        self.assertEqual(voiced_transcription(voiced_transcription("k")),
                         voiced_transcription("k"),
                         msg="voicing something twice is the same as voicing it once")
        self.assertEqual(voiced_transcription(voiced_transcription("g")),
                         voiced_transcription("g"),
                         msg="[g]")
        self.assertEqual(devoiced_transcription(devoiced_transcription("k")),
                         devoiced_transcription("k"))
