"""
Unit tests for lib_functions
"""

import unittest

from lib_functions import is_glide
from ipa import ipa_text_to_phonet_list_report, analyze_transcription, voiced_transcription, \
    devoiced_transcription, analyze_transcription_to_sound_patterns_of_english, \
    describe_transcription


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

    def x_voiced_is_y(self, unvoiced_phoneme: str, voiced_phoneme: str) -> None:
        result = voiced_transcription(unvoiced_phoneme)
        expected = voiced_phoneme
        self.assertEqual(
            result,
            expected,
            msg="should be that: [" + unvoiced_phoneme + "] voiced is [" + voiced_phoneme + "]")

    def x_devoiced_is_y(self, unvoiced_phoneme: str, voiced_phoneme: str) -> None:
        result = devoiced_transcription(voiced_phoneme)
        expected = unvoiced_phoneme
        self.assertEqual(result, expected,
                         msg=("should be that: [" + voiced_phoneme
                              + "] devoiced is [" + unvoiced_phoneme + "]"))

    def is_voiceless_counterpart_of(self, unvoiced_phoneme: str, voiced_phoneme: str) -> None:
        """
        Tests voicing and devoicing a phoneme.
        :param unvoiced_phoneme: the unvoiced phoneme
        :param voiced_phoneme: the voiced counterpart phoneme
        :return: None
        """
        self.x_voiced_is_y(unvoiced_phoneme, voiced_phoneme)
        self.x_devoiced_is_y(unvoiced_phoneme, voiced_phoneme)

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

    def test_voicing_a_phoneme_voiceless_diacritic_above_or_below(self) -> None:
        # Nasal
        self.x_voiced_is_y("m̥", "m")

        self.x_voiced_is_y("m̊", "m")

        self.x_voiced_is_y("ɱ̥", "ɱ")
        self.x_voiced_is_y("ɱ̊", "ɱ")
        self.x_voiced_is_y("n̥", "n")
        self.x_voiced_is_y("n̊", "n")
        self.x_voiced_is_y("ɲ̥", "ɲ")
        self.x_voiced_is_y("ɲ̊", "ɲ")
        self.x_voiced_is_y("ɳ̥", "ɳ")
        self.x_voiced_is_y("ɳ̊", "ɳ")
        self.x_voiced_is_y("ŋ̥", "ŋ")
        self.x_voiced_is_y("ŋ̊", "ŋ")

        self.x_voiced_is_y("ɴ̥", "ɴ")
        self.x_voiced_is_y("ɴ̊", "ɴ")

        # Trill consonants:
        self.x_voiced_is_y("ʙ̊", "ʙ")
        self.x_voiced_is_y("ʙ̥", "ʙ")
        self.x_voiced_is_y("r̊", "r")
        self.x_voiced_is_y("r̥", "r")
        self.x_voiced_is_y("ʀ̊", "ʀ")
        self.x_voiced_is_y("ʀ̥", "ʀ")

        # Tap or flap consonants:
        self.x_voiced_is_y("ⱱ̥", "ⱱ")
        self.x_voiced_is_y("ⱱ̊", "ⱱ")
        self.x_voiced_is_y("ɾ̥", "ɾ")
        self.x_voiced_is_y("ɾ̊", "ɾ")
        self.x_voiced_is_y("ɽ̥", "ɽ")
        self.x_voiced_is_y("ɽ̊", "ɽ")

        # Approximant consonants:
        self.x_voiced_is_y("ʋ̥", "ʋ")
        self.x_voiced_is_y("ʋ̊", "ʋ")
        self.x_voiced_is_y("ɹ̥", "ɹ")
        self.x_voiced_is_y("ɹ̊", "ɹ")
        self.x_voiced_is_y("ɻ̥", "ɻ")
        self.x_voiced_is_y("ɻ̊", "ɻ")
        self.x_voiced_is_y("j̥", "j")
        self.x_voiced_is_y("j̊", "j")
        self.x_voiced_is_y("ɰ̥", "ɰ")
        self.x_voiced_is_y("ɰ̊", "ɰ")

        # Lateral approximants:
        self.x_voiced_is_y("l̥", "l")
        self.x_voiced_is_y("l̊", "l")

        self.x_voiced_is_y("ɭ̥", "ɭ")
        self.x_voiced_is_y("ɭ̊", "ɭ")

        self.x_voiced_is_y("ʎ̥", "ʎ")
        self.x_voiced_is_y("ʎ̊", "ʎ")

        self.x_voiced_is_y("ʟ̥", "ʟ")
        self.x_voiced_is_y("ʟ̊", "ʟ")

        # Vowels
        self.x_voiced_is_y("i̥", "i")
        self.x_voiced_is_y("i̊", "i")

        self.x_voiced_is_y("y̥", "y")
        self.x_voiced_is_y("ẙ", "y")

        self.x_voiced_is_y("ɨ̥", "ɨ")
        self.x_voiced_is_y("ɨ̊", "ɨ")

        self.x_voiced_is_y("ʉ̥", "ʉ")
        self.x_voiced_is_y("ʉ̊", "ʉ")

        self.x_voiced_is_y("ɯ̥", "ɯ")
        self.x_voiced_is_y("ɯ̊", "ɯ")

        self.x_voiced_is_y("u̥", "u")
        self.x_voiced_is_y("ů", "u")

        self.x_voiced_is_y("ɪ̥", "ɪ")
        self.x_voiced_is_y("ɪ̊", "ɪ")

        self.x_voiced_is_y("ʏ̥", "ʏ")
        self.x_voiced_is_y("ʏ̊", "ʏ")

        self.x_voiced_is_y("ʊ̥", "ʊ")
        self.x_voiced_is_y("ʊ̊", "ʊ")

        self.x_voiced_is_y("e̥", "e")
        self.x_voiced_is_y("e̊", "e")

        self.x_voiced_is_y("ø̥", "ø")
        self.x_voiced_is_y("ø̊", "ø")

        self.x_voiced_is_y("ɘ̥", "ɘ")
        self.x_voiced_is_y("ɘ̊", "ɘ")

        self.x_voiced_is_y("ɵ̥", "ɵ")
        self.x_voiced_is_y("ɵ̊", "ɵ")

        self.x_voiced_is_y("ɤ̥", "ɤ")
        self.x_voiced_is_y("ɤ̊", "ɤ")

        self.x_voiced_is_y("o̥", "o")
        self.x_voiced_is_y("o̊", "o")

        self.x_voiced_is_y("ə̥", "ə")
        self.x_voiced_is_y("ə̊", "ə")

        self.x_voiced_is_y("ɛ̥", "ɛ")
        self.x_voiced_is_y("ɛ̊", "ɛ")

        self.x_voiced_is_y("œ̥", "œ")
        self.x_voiced_is_y("œ̊", "œ")

        self.x_voiced_is_y("ɜ̥", "ɜ")
        self.x_voiced_is_y("ɜ̊", "ɜ")

        self.x_voiced_is_y("ɞ̥", "ɞ")
        self.x_voiced_is_y("ɞ̊", "ɞ")

        self.x_voiced_is_y("ʌ̥", "ʌ")
        self.x_voiced_is_y("ʌ̊", "ʌ")

        self.x_voiced_is_y("ɔ̥", "ɔ")
        self.x_voiced_is_y("ɔ̊", "ɔ")

        self.x_voiced_is_y("æ̥", "æ")
        self.x_voiced_is_y("æ̊", "æ")

        self.x_voiced_is_y("ɐ̥", "ɐ")
        self.x_voiced_is_y("ɐ̊", "ɐ")

        self.x_voiced_is_y("ḁ", "a")
        self.x_voiced_is_y("å", "a")

        self.x_voiced_is_y("ɶ̥", "ɶ")
        self.x_voiced_is_y("ɶ̊", "ɶ")

        self.x_voiced_is_y("ɑ̥", "ɑ")
        self.x_voiced_is_y("ɑ̊", "ɑ")

        self.x_voiced_is_y("ɒ̥", "ɒ")
        self.x_voiced_is_y("ɒ̊", "ɒ")

        self.x_voiced_is_y("w̥", "w")
        self.x_voiced_is_y("ẘ", "w")

        self.x_voiced_is_y("ɥ̥", "ɥ")
        self.x_voiced_is_y("ɥ̊", "ɥ")

        self.x_voiced_is_y("ɕ", "ʑ")
        self.x_voiced_is_y("ɕ̥", "ʑ")
        self.x_voiced_is_y("ɕ̊", "ʑ")

        self.x_voiced_is_y("ɺ̥", "ɺ")
        self.x_voiced_is_y("ɺ̊", "ɺ")

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


    def test_labialized_t(self) -> None:
        """
        labialization:
        case: t labialized
        """
        result = describe_transcription("tʷ")
        expected = "voiceless labialized alveolar plosive pulmonic egressive consonant"
        self.assertEqual(result, expected, "case: t labialized")

    def test_labialized_r(self) -> None:
        """
        case: r labialized
        """
        result = describe_transcription("rʷ")
        expected = "voiced labialized alveolar trill pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_palatalized_t(self) -> None:
        """
        case: t palatalized
        """
        result = describe_transcription("tʲ")
        expected = "voiceless palatalized alveolar plosive pulmonic egressive consonant"
        self.assertEqual(result, expected)


    def test_palatalized_r(self) -> None:
        """
        case: r palatalized
        """
        result = describe_transcription("rʲ")
        expected = "voiced palatalized alveolar trill pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_velarized_t(self) -> None:
        """
        case: t velarized
        """
        result = describe_transcription("tˠ")
        expected = "voiceless velarized alveolar plosive pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_velarized_r(self) -> None:
        """
        case: r velarized
        """
        result = describe_transcription("rˠ")
        expected = "voiced velarized alveolar trill pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_palatalized_t(self) -> None:
        """case: t pharyngealized"""
        result = describe_transcription("tˤ")
        expected = "voiceless pharyngealized alveolar plosive pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_palatalized_r(self) -> None:
        """case: r pharyngealized"""
        result = describe_transcription("rˤ")
        expected = "voiced pharyngealized alveolar trill pulmonic egressive consonant"
        self.assertEqual(result, expected)

    def test_normal_a_vowel(self) -> None:
        """
        case: [a]
        """
        result = describe_transcription("a")
        expected = "voiced unrounded open front vowel"
        self.assertEqual(result, expected)

    def test_long_a_vowel(self) -> None:
        """
        case: [aː]
        """
        result = describe_transcription("aː")
        expected = "voiced unrounded open front long vowel"
        self.assertEqual(result, expected)

    def test_half_long_a_vowel(self) -> None:
        """
        case: [aˑ]
        """
        result = describe_transcription("aˑ")
        expected = "voiced unrounded open front half-long vowel"
        self.assertEqual(result, expected)

    def test_extra_short_a_vowel(self) -> None:
        """
        case: [ă]
        """
        result = describe_transcription("ă")
        expected = "voiced unrounded open front extra-short vowel"
        self.assertEqual(result, expected)

    def test_voiceless_long_i_vowel(self) -> None:
        """
        case [i̥ː]
        """
        expected = "voiceless unrounded close front long vowel"
        actual = describe_transcription("i̥ː")
        self.assertEqual(expected, actual)

    def test_voiceless_half_long_i_vowel(self) -> None:
        """
        case [i̥ˑ]
        """
        expected = "voiceless unrounded close front half-long vowel"
        actual = describe_transcription("i̥ˑ")
        self.assertEqual(expected, actual)


    def test_voiceless_half_long_i_vowel(self) -> None:
        """
        case [ĭ̥]
        """
        expected = "voiceless unrounded close front extra-short vowel"
        actual = describe_transcription("ĭ̥")
        self.assertEqual(expected, actual)

    def test_ʑ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
        expected = "voiced aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
        actual = describe_transcription("ʑ̬ʰˤ")
        self.assertEqual(actual, expected)
