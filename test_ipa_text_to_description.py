"""
unit tests for testing describing a phoneme given its
representation in the international phonetic alphabet

Note to software developer:
The code in this module was generated from SpecGeneratorForPython.hs,
a file in the Haskell project.
"""
import unittest

from ipa import describe_transcription

class IPATextToDescription(unittest.TestCase):
# voiceless bilabial plosive pulmonic egressive consonant
	def test_p_is_the_representation_of_the_voiceless_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p")
		self.assertEqual(actual, expected)

	def test_p̊_is_the_representation_of_the_voiceless_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̊")
		self.assertEqual(actual, expected)

	def test_p̥_is_the_representation_of_the_voiceless_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̥")
		self.assertEqual(actual, expected)

	def test_b̊_is_the_representation_of_the_voiceless_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊")
		self.assertEqual(actual, expected)

	def test_b̥_is_the_representation_of_the_voiceless_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥")
		self.assertEqual(actual, expected)

# voiceless labialized bilabial plosive pulmonic egressive consonant
	def test_pʷ_is_the_representation_of_the_voiceless_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʷ")
		self.assertEqual(actual, expected)

	def test_p̊ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̊ʷ")
		self.assertEqual(actual, expected)

	def test_p̥ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̥ʷ")
		self.assertEqual(actual, expected)

	def test_b̊ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʷ")
		self.assertEqual(actual, expected)

	def test_b̥ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized bilabial plosive pulmonic egressive consonant
	def test_pʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʲ")
		self.assertEqual(actual, expected)

	def test_p̊ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̊ʲ")
		self.assertEqual(actual, expected)

	def test_p̥ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̥ʲ")
		self.assertEqual(actual, expected)

	def test_b̊ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʲ")
		self.assertEqual(actual, expected)

	def test_b̥ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized bilabial plosive pulmonic egressive consonant
	def test_pˠ_is_the_representation_of_the_voiceless_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pˠ")
		self.assertEqual(actual, expected)

	def test_p̊ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̊ˠ")
		self.assertEqual(actual, expected)

	def test_p̥ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̥ˠ")
		self.assertEqual(actual, expected)

	def test_b̊ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ˠ")
		self.assertEqual(actual, expected)

	def test_b̥ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized bilabial plosive pulmonic egressive consonant
	def test_pˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pˤ")
		self.assertEqual(actual, expected)

	def test_p̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̊ˤ")
		self.assertEqual(actual, expected)

	def test_p̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̥ˤ")
		self.assertEqual(actual, expected)

	def test_b̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ˤ")
		self.assertEqual(actual, expected)

	def test_b̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated bilabial plosive pulmonic egressive consonant
	def test_pʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʰ")
		self.assertEqual(actual, expected)

	def test_b̥ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʰ")
		self.assertEqual(actual, expected)

	def test_b̊ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized bilabial plosive pulmonic egressive consonant
	def test_pʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʰʷ")
		self.assertEqual(actual, expected)

	def test_b̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_b̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized bilabial plosive pulmonic egressive consonant
	def test_pʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʰʲ")
		self.assertEqual(actual, expected)

	def test_b̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_b̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized bilabial plosive pulmonic egressive consonant
	def test_pʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʰˠ")
		self.assertEqual(actual, expected)

	def test_b̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_b̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized bilabial plosive pulmonic egressive consonant
	def test_pʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("pʰˤ")
		self.assertEqual(actual, expected)

	def test_b̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_b̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced bilabial plosive pulmonic egressive consonant
	def test_b_is_the_representation_of_the_voiced_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b")
		self.assertEqual(actual, expected)

	def test_p̬_is_the_representation_of_the_voiced_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬")
		self.assertEqual(actual, expected)

	def test_p̬_is_the_representation_of_the_voiced_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬")
		self.assertEqual(actual, expected)

# voiced labialized bilabial plosive pulmonic egressive consonant
	def test_bʷ_is_the_representation_of_the_voiced_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʷ")
		self.assertEqual(actual, expected)

	def test_p̬ʷ_is_the_representation_of_the_voiced_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʷ")
		self.assertEqual(actual, expected)

	def test_p̬ʷ_is_the_representation_of_the_voiced_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized bilabial plosive pulmonic egressive consonant
	def test_bʲ_is_the_representation_of_the_voiced_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʲ")
		self.assertEqual(actual, expected)

	def test_p̬ʲ_is_the_representation_of_the_voiced_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʲ")
		self.assertEqual(actual, expected)

	def test_p̬ʲ_is_the_representation_of_the_voiced_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized bilabial plosive pulmonic egressive consonant
	def test_bˠ_is_the_representation_of_the_voiced_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bˠ")
		self.assertEqual(actual, expected)

	def test_p̬ˠ_is_the_representation_of_the_voiced_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ˠ")
		self.assertEqual(actual, expected)

	def test_p̬ˠ_is_the_representation_of_the_voiced_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized bilabial plosive pulmonic egressive consonant
	def test_bˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bˤ")
		self.assertEqual(actual, expected)

	def test_p̬ˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ˤ")
		self.assertEqual(actual, expected)

	def test_p̬ˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated bilabial plosive pulmonic egressive consonant
	def test_bʰ_is_the_representation_of_the_voiced_aspirated_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʰ")
		self.assertEqual(actual, expected)

	def test_b̬ʰ_is_the_representation_of_the_voiced_aspirated_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̬ʰ")
		self.assertEqual(actual, expected)

	def test_p̬ʰ_is_the_representation_of_the_voiced_aspirated_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized bilabial plosive pulmonic egressive consonant
	def test_bʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʰʷ")
		self.assertEqual(actual, expected)

	def test_b̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_p̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized bilabial plosive pulmonic egressive consonant
	def test_bʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʰʲ")
		self.assertEqual(actual, expected)

	def test_b̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_p̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized bilabial plosive pulmonic egressive consonant
	def test_bʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʰˠ")
		self.assertEqual(actual, expected)

	def test_b̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_p̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized bilabial plosive pulmonic egressive consonant
	def test_bʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("bʰˤ")
		self.assertEqual(actual, expected)

	def test_b̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("b̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_p̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial plosive pulmonic egressive consonant"
		actual = describe_transcription("p̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar plosive pulmonic egressive consonant
	def test_t_is_the_representation_of_the_voiceless_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t")
		self.assertEqual(actual, expected)

	def test_t̊_is_the_representation_of_the_voiceless_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̊")
		self.assertEqual(actual, expected)

	def test_t̥_is_the_representation_of_the_voiceless_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̥")
		self.assertEqual(actual, expected)

	def test_d̊_is_the_representation_of_the_voiceless_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊")
		self.assertEqual(actual, expected)

	def test_d̥_is_the_representation_of_the_voiceless_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar plosive pulmonic egressive consonant
	def test_tʷ_is_the_representation_of_the_voiceless_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʷ")
		self.assertEqual(actual, expected)

	def test_t̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̊ʷ")
		self.assertEqual(actual, expected)

	def test_t̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̥ʷ")
		self.assertEqual(actual, expected)

	def test_d̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʷ")
		self.assertEqual(actual, expected)

	def test_d̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar plosive pulmonic egressive consonant
	def test_tʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʲ")
		self.assertEqual(actual, expected)

	def test_t̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̊ʲ")
		self.assertEqual(actual, expected)

	def test_t̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̥ʲ")
		self.assertEqual(actual, expected)

	def test_d̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʲ")
		self.assertEqual(actual, expected)

	def test_d̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar plosive pulmonic egressive consonant
	def test_tˠ_is_the_representation_of_the_voiceless_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tˠ")
		self.assertEqual(actual, expected)

	def test_t̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̊ˠ")
		self.assertEqual(actual, expected)

	def test_t̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̥ˠ")
		self.assertEqual(actual, expected)

	def test_d̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ˠ")
		self.assertEqual(actual, expected)

	def test_d̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar plosive pulmonic egressive consonant
	def test_tˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tˤ")
		self.assertEqual(actual, expected)

	def test_t̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̊ˤ")
		self.assertEqual(actual, expected)

	def test_t̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̥ˤ")
		self.assertEqual(actual, expected)

	def test_d̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ˤ")
		self.assertEqual(actual, expected)

	def test_d̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar plosive pulmonic egressive consonant
	def test_tʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʰ")
		self.assertEqual(actual, expected)

	def test_d̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʰ")
		self.assertEqual(actual, expected)

	def test_d̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar plosive pulmonic egressive consonant
	def test_tʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʰʷ")
		self.assertEqual(actual, expected)

	def test_d̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_d̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar plosive pulmonic egressive consonant
	def test_tʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʰʲ")
		self.assertEqual(actual, expected)

	def test_d̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_d̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar plosive pulmonic egressive consonant
	def test_tʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʰˠ")
		self.assertEqual(actual, expected)

	def test_d̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_d̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar plosive pulmonic egressive consonant
	def test_tʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("tʰˤ")
		self.assertEqual(actual, expected)

	def test_d̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_d̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar plosive pulmonic egressive consonant
	def test_d_is_the_representation_of_the_voiced_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d")
		self.assertEqual(actual, expected)

	def test_t̬_is_the_representation_of_the_voiced_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬")
		self.assertEqual(actual, expected)

	def test_t̬_is_the_representation_of_the_voiced_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬")
		self.assertEqual(actual, expected)

# voiced labialized alveolar plosive pulmonic egressive consonant
	def test_dʷ_is_the_representation_of_the_voiced_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʷ")
		self.assertEqual(actual, expected)

	def test_t̬ʷ_is_the_representation_of_the_voiced_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʷ")
		self.assertEqual(actual, expected)

	def test_t̬ʷ_is_the_representation_of_the_voiced_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar plosive pulmonic egressive consonant
	def test_dʲ_is_the_representation_of_the_voiced_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʲ")
		self.assertEqual(actual, expected)

	def test_t̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʲ")
		self.assertEqual(actual, expected)

	def test_t̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar plosive pulmonic egressive consonant
	def test_dˠ_is_the_representation_of_the_voiced_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dˠ")
		self.assertEqual(actual, expected)

	def test_t̬ˠ_is_the_representation_of_the_voiced_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ˠ")
		self.assertEqual(actual, expected)

	def test_t̬ˠ_is_the_representation_of_the_voiced_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar plosive pulmonic egressive consonant
	def test_dˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dˤ")
		self.assertEqual(actual, expected)

	def test_t̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ˤ")
		self.assertEqual(actual, expected)

	def test_t̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar plosive pulmonic egressive consonant
	def test_dʰ_is_the_representation_of_the_voiced_aspirated_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʰ")
		self.assertEqual(actual, expected)

	def test_d̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̬ʰ")
		self.assertEqual(actual, expected)

	def test_t̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar plosive pulmonic egressive consonant
	def test_dʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʰʷ")
		self.assertEqual(actual, expected)

	def test_d̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_t̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar plosive pulmonic egressive consonant
	def test_dʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʰʲ")
		self.assertEqual(actual, expected)

	def test_d̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_t̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar plosive pulmonic egressive consonant
	def test_dʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʰˠ")
		self.assertEqual(actual, expected)

	def test_d̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_t̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar plosive pulmonic egressive consonant
	def test_dʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("dʰˤ")
		self.assertEqual(actual, expected)

	def test_d̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("d̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_t̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar plosive pulmonic egressive consonant"
		actual = describe_transcription("t̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless retroflex plosive pulmonic egressive consonant
	def test_ʈ_is_the_representation_of_the_voiceless_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ")
		self.assertEqual(actual, expected)

	def test_ʈ̊_is_the_representation_of_the_voiceless_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̊")
		self.assertEqual(actual, expected)

	def test_ʈ̥_is_the_representation_of_the_voiceless_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̥")
		self.assertEqual(actual, expected)

	def test_ɖ̊_is_the_representation_of_the_voiceless_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊")
		self.assertEqual(actual, expected)

	def test_ɖ̥_is_the_representation_of_the_voiceless_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥")
		self.assertEqual(actual, expected)

# voiceless labialized retroflex plosive pulmonic egressive consonant
	def test_ʈʷ_is_the_representation_of_the_voiceless_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʷ")
		self.assertEqual(actual, expected)

	def test_ʈ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʈ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized retroflex plosive pulmonic egressive consonant
	def test_ʈʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʲ")
		self.assertEqual(actual, expected)

	def test_ʈ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʈ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized retroflex plosive pulmonic egressive consonant
	def test_ʈˠ_is_the_representation_of_the_voiceless_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈˠ")
		self.assertEqual(actual, expected)

	def test_ʈ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʈ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized retroflex plosive pulmonic egressive consonant
	def test_ʈˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈˤ")
		self.assertEqual(actual, expected)

	def test_ʈ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʈ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated retroflex plosive pulmonic egressive consonant
	def test_ʈʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʰ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized retroflex plosive pulmonic egressive consonant
	def test_ʈʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʰʷ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized retroflex plosive pulmonic egressive consonant
	def test_ʈʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʰʲ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized retroflex plosive pulmonic egressive consonant
	def test_ʈʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʰˠ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized retroflex plosive pulmonic egressive consonant
	def test_ʈʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈʰˤ")
		self.assertEqual(actual, expected)

	def test_ɖ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɖ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced retroflex plosive pulmonic egressive consonant
	def test_ɖ_is_the_representation_of_the_voiced_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ")
		self.assertEqual(actual, expected)

	def test_ʈ̬_is_the_representation_of_the_voiced_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬")
		self.assertEqual(actual, expected)

	def test_ʈ̬_is_the_representation_of_the_voiced_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬")
		self.assertEqual(actual, expected)

# voiced labialized retroflex plosive pulmonic egressive consonant
	def test_ɖʷ_is_the_representation_of_the_voiced_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʷ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʷ_is_the_representation_of_the_voiced_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʷ_is_the_representation_of_the_voiced_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized retroflex plosive pulmonic egressive consonant
	def test_ɖʲ_is_the_representation_of_the_voiced_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʲ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʲ_is_the_representation_of_the_voiced_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʲ_is_the_representation_of_the_voiced_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized retroflex plosive pulmonic egressive consonant
	def test_ɖˠ_is_the_representation_of_the_voiced_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖˠ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ˠ_is_the_representation_of_the_voiced_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ˠ_is_the_representation_of_the_voiced_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized retroflex plosive pulmonic egressive consonant
	def test_ɖˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖˤ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated retroflex plosive pulmonic egressive consonant
	def test_ɖʰ_is_the_representation_of_the_voiced_aspirated_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʰ")
		self.assertEqual(actual, expected)

	def test_ɖ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized retroflex plosive pulmonic egressive consonant
	def test_ɖʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʰʷ")
		self.assertEqual(actual, expected)

	def test_ɖ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized retroflex plosive pulmonic egressive consonant
	def test_ɖʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʰʲ")
		self.assertEqual(actual, expected)

	def test_ɖ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized retroflex plosive pulmonic egressive consonant
	def test_ɖʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʰˠ")
		self.assertEqual(actual, expected)

	def test_ɖ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized retroflex plosive pulmonic egressive consonant
	def test_ɖʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖʰˤ")
		self.assertEqual(actual, expected)

	def test_ɖ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ɖ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʈ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex plosive pulmonic egressive consonant"
		actual = describe_transcription("ʈ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless palatal plosive pulmonic egressive consonant
	def test_c_is_the_representation_of_the_voiceless_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c")
		self.assertEqual(actual, expected)

	def test_c̊_is_the_representation_of_the_voiceless_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̊")
		self.assertEqual(actual, expected)

	def test_c̥_is_the_representation_of_the_voiceless_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̥")
		self.assertEqual(actual, expected)

	def test_ɟ̊_is_the_representation_of_the_voiceless_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊")
		self.assertEqual(actual, expected)

	def test_ɟ̥_is_the_representation_of_the_voiceless_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥")
		self.assertEqual(actual, expected)

# voiceless labialized palatal plosive pulmonic egressive consonant
	def test_cʷ_is_the_representation_of_the_voiceless_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʷ")
		self.assertEqual(actual, expected)

	def test_c̊ʷ_is_the_representation_of_the_voiceless_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̊ʷ")
		self.assertEqual(actual, expected)

	def test_c̥ʷ_is_the_representation_of_the_voiceless_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̥ʷ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʷ_is_the_representation_of_the_voiceless_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʷ_is_the_representation_of_the_voiceless_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized palatal plosive pulmonic egressive consonant
	def test_cʲ_is_the_representation_of_the_voiceless_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʲ")
		self.assertEqual(actual, expected)

	def test_c̊ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̊ʲ")
		self.assertEqual(actual, expected)

	def test_c̥ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̥ʲ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized palatal plosive pulmonic egressive consonant
	def test_cˠ_is_the_representation_of_the_voiceless_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cˠ")
		self.assertEqual(actual, expected)

	def test_c̊ˠ_is_the_representation_of_the_voiceless_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̊ˠ")
		self.assertEqual(actual, expected)

	def test_c̥ˠ_is_the_representation_of_the_voiceless_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̥ˠ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ˠ_is_the_representation_of_the_voiceless_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ˠ_is_the_representation_of_the_voiceless_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized palatal plosive pulmonic egressive consonant
	def test_cˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cˤ")
		self.assertEqual(actual, expected)

	def test_c̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̊ˤ")
		self.assertEqual(actual, expected)

	def test_c̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̥ˤ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatal plosive pulmonic egressive consonant
	def test_cʰ_is_the_representation_of_the_voiceless_aspirated_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʰ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized palatal plosive pulmonic egressive consonant
	def test_cʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʰʷ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized palatal plosive pulmonic egressive consonant
	def test_cʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʰʲ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized palatal plosive pulmonic egressive consonant
	def test_cʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʰˠ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized palatal plosive pulmonic egressive consonant
	def test_cʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("cʰˤ")
		self.assertEqual(actual, expected)

	def test_ɟ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɟ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced palatal plosive pulmonic egressive consonant
	def test_ɟ_is_the_representation_of_the_voiced_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ")
		self.assertEqual(actual, expected)

	def test_c̬_is_the_representation_of_the_voiced_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬")
		self.assertEqual(actual, expected)

	def test_c̬_is_the_representation_of_the_voiced_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬")
		self.assertEqual(actual, expected)

# voiced labialized palatal plosive pulmonic egressive consonant
	def test_ɟʷ_is_the_representation_of_the_voiced_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʷ")
		self.assertEqual(actual, expected)

	def test_c̬ʷ_is_the_representation_of_the_voiced_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʷ")
		self.assertEqual(actual, expected)

	def test_c̬ʷ_is_the_representation_of_the_voiced_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized palatal plosive pulmonic egressive consonant
	def test_ɟʲ_is_the_representation_of_the_voiced_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʲ")
		self.assertEqual(actual, expected)

	def test_c̬ʲ_is_the_representation_of_the_voiced_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʲ")
		self.assertEqual(actual, expected)

	def test_c̬ʲ_is_the_representation_of_the_voiced_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized palatal plosive pulmonic egressive consonant
	def test_ɟˠ_is_the_representation_of_the_voiced_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟˠ")
		self.assertEqual(actual, expected)

	def test_c̬ˠ_is_the_representation_of_the_voiced_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ˠ")
		self.assertEqual(actual, expected)

	def test_c̬ˠ_is_the_representation_of_the_voiced_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized palatal plosive pulmonic egressive consonant
	def test_ɟˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟˤ")
		self.assertEqual(actual, expected)

	def test_c̬ˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ˤ")
		self.assertEqual(actual, expected)

	def test_c̬ˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated palatal plosive pulmonic egressive consonant
	def test_ɟʰ_is_the_representation_of_the_voiced_aspirated_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʰ")
		self.assertEqual(actual, expected)

	def test_ɟ̬ʰ_is_the_representation_of_the_voiced_aspirated_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̬ʰ")
		self.assertEqual(actual, expected)

	def test_c̬ʰ_is_the_representation_of_the_voiced_aspirated_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized palatal plosive pulmonic egressive consonant
	def test_ɟʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʰʷ")
		self.assertEqual(actual, expected)

	def test_ɟ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_c̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized palatal plosive pulmonic egressive consonant
	def test_ɟʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʰʲ")
		self.assertEqual(actual, expected)

	def test_ɟ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_c̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized palatal plosive pulmonic egressive consonant
	def test_ɟʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʰˠ")
		self.assertEqual(actual, expected)

	def test_ɟ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_c̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized palatal plosive pulmonic egressive consonant
	def test_ɟʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟʰˤ")
		self.assertEqual(actual, expected)

	def test_ɟ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("ɟ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_c̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal plosive pulmonic egressive consonant"
		actual = describe_transcription("c̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless velar plosive pulmonic egressive consonant
	def test_k_is_the_representation_of_the_voiceless_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k")
		self.assertEqual(actual, expected)

	def test_k̊_is_the_representation_of_the_voiceless_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̊")
		self.assertEqual(actual, expected)

	def test_k̥_is_the_representation_of_the_voiceless_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̥")
		self.assertEqual(actual, expected)

	def test_g̊_is_the_representation_of_the_voiceless_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊")
		self.assertEqual(actual, expected)

	def test_g̥_is_the_representation_of_the_voiceless_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥")
		self.assertEqual(actual, expected)

# voiceless labialized velar plosive pulmonic egressive consonant
	def test_kʷ_is_the_representation_of_the_voiceless_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʷ")
		self.assertEqual(actual, expected)

	def test_k̊ʷ_is_the_representation_of_the_voiceless_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̊ʷ")
		self.assertEqual(actual, expected)

	def test_k̥ʷ_is_the_representation_of_the_voiceless_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̥ʷ")
		self.assertEqual(actual, expected)

	def test_g̊ʷ_is_the_representation_of_the_voiceless_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʷ")
		self.assertEqual(actual, expected)

	def test_g̥ʷ_is_the_representation_of_the_voiceless_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized velar plosive pulmonic egressive consonant
	def test_kʲ_is_the_representation_of_the_voiceless_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʲ")
		self.assertEqual(actual, expected)

	def test_k̊ʲ_is_the_representation_of_the_voiceless_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̊ʲ")
		self.assertEqual(actual, expected)

	def test_k̥ʲ_is_the_representation_of_the_voiceless_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̥ʲ")
		self.assertEqual(actual, expected)

	def test_g̊ʲ_is_the_representation_of_the_voiceless_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʲ")
		self.assertEqual(actual, expected)

	def test_g̥ʲ_is_the_representation_of_the_voiceless_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized velar plosive pulmonic egressive consonant
	def test_kˠ_is_the_representation_of_the_voiceless_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kˠ")
		self.assertEqual(actual, expected)

	def test_k̊ˠ_is_the_representation_of_the_voiceless_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̊ˠ")
		self.assertEqual(actual, expected)

	def test_k̥ˠ_is_the_representation_of_the_voiceless_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̥ˠ")
		self.assertEqual(actual, expected)

	def test_g̊ˠ_is_the_representation_of_the_voiceless_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ˠ")
		self.assertEqual(actual, expected)

	def test_g̥ˠ_is_the_representation_of_the_voiceless_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized velar plosive pulmonic egressive consonant
	def test_kˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kˤ")
		self.assertEqual(actual, expected)

	def test_k̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̊ˤ")
		self.assertEqual(actual, expected)

	def test_k̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̥ˤ")
		self.assertEqual(actual, expected)

	def test_g̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ˤ")
		self.assertEqual(actual, expected)

	def test_g̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated velar plosive pulmonic egressive consonant
	def test_kʰ_is_the_representation_of_the_voiceless_aspirated_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʰ")
		self.assertEqual(actual, expected)

	def test_g̥ʰ_is_the_representation_of_the_voiceless_aspirated_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʰ")
		self.assertEqual(actual, expected)

	def test_g̊ʰ_is_the_representation_of_the_voiceless_aspirated_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized velar plosive pulmonic egressive consonant
	def test_kʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʰʷ")
		self.assertEqual(actual, expected)

	def test_g̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_g̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized velar plosive pulmonic egressive consonant
	def test_kʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʰʲ")
		self.assertEqual(actual, expected)

	def test_g̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_g̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized velar plosive pulmonic egressive consonant
	def test_kʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʰˠ")
		self.assertEqual(actual, expected)

	def test_g̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_g̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized velar plosive pulmonic egressive consonant
	def test_kʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("kʰˤ")
		self.assertEqual(actual, expected)

	def test_g̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_g̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced velar plosive pulmonic egressive consonant
	def test_g_is_the_representation_of_the_voiced_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g")
		self.assertEqual(actual, expected)

	def test_k̬_is_the_representation_of_the_voiced_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬")
		self.assertEqual(actual, expected)

	def test_k̬_is_the_representation_of_the_voiced_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬")
		self.assertEqual(actual, expected)

# voiced labialized velar plosive pulmonic egressive consonant
	def test_gʷ_is_the_representation_of_the_voiced_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʷ")
		self.assertEqual(actual, expected)

	def test_k̬ʷ_is_the_representation_of_the_voiced_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʷ")
		self.assertEqual(actual, expected)

	def test_k̬ʷ_is_the_representation_of_the_voiced_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized velar plosive pulmonic egressive consonant
	def test_gʲ_is_the_representation_of_the_voiced_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʲ")
		self.assertEqual(actual, expected)

	def test_k̬ʲ_is_the_representation_of_the_voiced_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʲ")
		self.assertEqual(actual, expected)

	def test_k̬ʲ_is_the_representation_of_the_voiced_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized velar plosive pulmonic egressive consonant
	def test_gˠ_is_the_representation_of_the_voiced_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gˠ")
		self.assertEqual(actual, expected)

	def test_k̬ˠ_is_the_representation_of_the_voiced_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ˠ")
		self.assertEqual(actual, expected)

	def test_k̬ˠ_is_the_representation_of_the_voiced_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized velar plosive pulmonic egressive consonant
	def test_gˤ_is_the_representation_of_the_voiced_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gˤ")
		self.assertEqual(actual, expected)

	def test_k̬ˤ_is_the_representation_of_the_voiced_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ˤ")
		self.assertEqual(actual, expected)

	def test_k̬ˤ_is_the_representation_of_the_voiced_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated velar plosive pulmonic egressive consonant
	def test_gʰ_is_the_representation_of_the_voiced_aspirated_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʰ")
		self.assertEqual(actual, expected)

	def test_g̬ʰ_is_the_representation_of_the_voiced_aspirated_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̬ʰ")
		self.assertEqual(actual, expected)

	def test_k̬ʰ_is_the_representation_of_the_voiced_aspirated_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized velar plosive pulmonic egressive consonant
	def test_gʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʰʷ")
		self.assertEqual(actual, expected)

	def test_g̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_k̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized velar plosive pulmonic egressive consonant
	def test_gʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʰʲ")
		self.assertEqual(actual, expected)

	def test_g̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_k̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized velar plosive pulmonic egressive consonant
	def test_gʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʰˠ")
		self.assertEqual(actual, expected)

	def test_g̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_k̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized velar plosive pulmonic egressive consonant
	def test_gʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("gʰˤ")
		self.assertEqual(actual, expected)

	def test_g̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("g̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_k̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar plosive pulmonic egressive consonant"
		actual = describe_transcription("k̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless uvular plosive pulmonic egressive consonant
	def test_q_is_the_representation_of_the_voiceless_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q")
		self.assertEqual(actual, expected)

	def test_q̊_is_the_representation_of_the_voiceless_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̊")
		self.assertEqual(actual, expected)

	def test_q̥_is_the_representation_of_the_voiceless_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̥")
		self.assertEqual(actual, expected)

	def test_ɢ̊_is_the_representation_of_the_voiceless_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊")
		self.assertEqual(actual, expected)

	def test_ɢ̥_is_the_representation_of_the_voiceless_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥")
		self.assertEqual(actual, expected)

# voiceless labialized uvular plosive pulmonic egressive consonant
	def test_qʷ_is_the_representation_of_the_voiceless_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʷ")
		self.assertEqual(actual, expected)

	def test_q̊ʷ_is_the_representation_of_the_voiceless_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̊ʷ")
		self.assertEqual(actual, expected)

	def test_q̥ʷ_is_the_representation_of_the_voiceless_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̥ʷ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʷ_is_the_representation_of_the_voiceless_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʷ_is_the_representation_of_the_voiceless_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized uvular plosive pulmonic egressive consonant
	def test_qʲ_is_the_representation_of_the_voiceless_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʲ")
		self.assertEqual(actual, expected)

	def test_q̊ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̊ʲ")
		self.assertEqual(actual, expected)

	def test_q̥ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̥ʲ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized uvular plosive pulmonic egressive consonant
	def test_qˠ_is_the_representation_of_the_voiceless_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qˠ")
		self.assertEqual(actual, expected)

	def test_q̊ˠ_is_the_representation_of_the_voiceless_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̊ˠ")
		self.assertEqual(actual, expected)

	def test_q̥ˠ_is_the_representation_of_the_voiceless_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̥ˠ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ˠ_is_the_representation_of_the_voiceless_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ˠ_is_the_representation_of_the_voiceless_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized uvular plosive pulmonic egressive consonant
	def test_qˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qˤ")
		self.assertEqual(actual, expected)

	def test_q̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̊ˤ")
		self.assertEqual(actual, expected)

	def test_q̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̥ˤ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated uvular plosive pulmonic egressive consonant
	def test_qʰ_is_the_representation_of_the_voiceless_aspirated_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʰ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized uvular plosive pulmonic egressive consonant
	def test_qʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʰʷ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized uvular plosive pulmonic egressive consonant
	def test_qʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʰʲ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized uvular plosive pulmonic egressive consonant
	def test_qʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʰˠ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized uvular plosive pulmonic egressive consonant
	def test_qʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("qʰˤ")
		self.assertEqual(actual, expected)

	def test_ɢ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɢ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced uvular plosive pulmonic egressive consonant
	def test_ɢ_is_the_representation_of_the_voiced_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ")
		self.assertEqual(actual, expected)

	def test_q̬_is_the_representation_of_the_voiced_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬")
		self.assertEqual(actual, expected)

	def test_q̬_is_the_representation_of_the_voiced_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬")
		self.assertEqual(actual, expected)

# voiced labialized uvular plosive pulmonic egressive consonant
	def test_ɢʷ_is_the_representation_of_the_voiced_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʷ")
		self.assertEqual(actual, expected)

	def test_q̬ʷ_is_the_representation_of_the_voiced_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʷ")
		self.assertEqual(actual, expected)

	def test_q̬ʷ_is_the_representation_of_the_voiced_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized uvular plosive pulmonic egressive consonant
	def test_ɢʲ_is_the_representation_of_the_voiced_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʲ")
		self.assertEqual(actual, expected)

	def test_q̬ʲ_is_the_representation_of_the_voiced_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʲ")
		self.assertEqual(actual, expected)

	def test_q̬ʲ_is_the_representation_of_the_voiced_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized uvular plosive pulmonic egressive consonant
	def test_ɢˠ_is_the_representation_of_the_voiced_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢˠ")
		self.assertEqual(actual, expected)

	def test_q̬ˠ_is_the_representation_of_the_voiced_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ˠ")
		self.assertEqual(actual, expected)

	def test_q̬ˠ_is_the_representation_of_the_voiced_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized uvular plosive pulmonic egressive consonant
	def test_ɢˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢˤ")
		self.assertEqual(actual, expected)

	def test_q̬ˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ˤ")
		self.assertEqual(actual, expected)

	def test_q̬ˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated uvular plosive pulmonic egressive consonant
	def test_ɢʰ_is_the_representation_of_the_voiced_aspirated_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʰ")
		self.assertEqual(actual, expected)

	def test_ɢ̬ʰ_is_the_representation_of_the_voiced_aspirated_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̬ʰ")
		self.assertEqual(actual, expected)

	def test_q̬ʰ_is_the_representation_of_the_voiced_aspirated_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized uvular plosive pulmonic egressive consonant
	def test_ɢʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʰʷ")
		self.assertEqual(actual, expected)

	def test_ɢ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_q̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized uvular plosive pulmonic egressive consonant
	def test_ɢʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʰʲ")
		self.assertEqual(actual, expected)

	def test_ɢ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_q̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized uvular plosive pulmonic egressive consonant
	def test_ɢʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʰˠ")
		self.assertEqual(actual, expected)

	def test_ɢ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_q̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized uvular plosive pulmonic egressive consonant
	def test_ɢʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢʰˤ")
		self.assertEqual(actual, expected)

	def test_ɢ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("ɢ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_q̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular plosive pulmonic egressive consonant"
		actual = describe_transcription("q̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless glottal plosive pulmonic egressive consonant
	def test_ʔ_is_the_representation_of_the_voiceless_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ")
		self.assertEqual(actual, expected)

	def test_ʔ̊_is_the_representation_of_the_voiceless_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̊")
		self.assertEqual(actual, expected)

	def test_ʔ̥_is_the_representation_of_the_voiceless_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̥")
		self.assertEqual(actual, expected)

# voiceless labialized glottal plosive pulmonic egressive consonant
	def test_ʔʷ_is_the_representation_of_the_voiceless_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʷ")
		self.assertEqual(actual, expected)

	def test_ʔ̊ʷ_is_the_representation_of_the_voiceless_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʔ̥ʷ_is_the_representation_of_the_voiceless_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized glottal plosive pulmonic egressive consonant
	def test_ʔʲ_is_the_representation_of_the_voiceless_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʲ")
		self.assertEqual(actual, expected)

	def test_ʔ̊ʲ_is_the_representation_of_the_voiceless_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʔ̥ʲ_is_the_representation_of_the_voiceless_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized glottal plosive pulmonic egressive consonant
	def test_ʔˠ_is_the_representation_of_the_voiceless_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔˠ")
		self.assertEqual(actual, expected)

	def test_ʔ̊ˠ_is_the_representation_of_the_voiceless_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʔ̥ˠ_is_the_representation_of_the_voiceless_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized glottal plosive pulmonic egressive consonant
	def test_ʔˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔˤ")
		self.assertEqual(actual, expected)

	def test_ʔ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʔ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated glottal plosive pulmonic egressive consonant
	def test_ʔʰ_is_the_representation_of_the_voiceless_aspirated_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized glottal plosive pulmonic egressive consonant
	def test_ʔʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized glottal plosive pulmonic egressive consonant
	def test_ʔʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized glottal plosive pulmonic egressive consonant
	def test_ʔʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized glottal plosive pulmonic egressive consonant
	def test_ʔʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔʰˤ")
		self.assertEqual(actual, expected)

# voiced glottal plosive pulmonic egressive consonant
	def test_ʔ̬_is_the_representation_of_the_voiced_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬")
		self.assertEqual(actual, expected)

	def test_ʔ̬_is_the_representation_of_the_voiced_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬")
		self.assertEqual(actual, expected)

# voiced labialized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʷ_is_the_representation_of_the_voiced_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʔ̬ʷ_is_the_representation_of_the_voiced_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʲ_is_the_representation_of_the_voiced_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʔ̬ʲ_is_the_representation_of_the_voiced_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ˠ_is_the_representation_of_the_voiced_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʔ̬ˠ_is_the_representation_of_the_voiced_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʔ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʰ_is_the_representation_of_the_voiced_aspirated_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized glottal plosive pulmonic egressive consonant
	def test_ʔ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_glottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized glottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʔ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless bilabial fricative pulmonic egressive consonant
	def test_ɸ_is_the_representation_of_the_voiceless_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ")
		self.assertEqual(actual, expected)

	def test_ɸ̊_is_the_representation_of_the_voiceless_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̊")
		self.assertEqual(actual, expected)

	def test_ɸ̥_is_the_representation_of_the_voiceless_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̥")
		self.assertEqual(actual, expected)

	def test_β̊_is_the_representation_of_the_voiceless_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊")
		self.assertEqual(actual, expected)

	def test_β̥_is_the_representation_of_the_voiceless_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥")
		self.assertEqual(actual, expected)

# voiceless labialized bilabial fricative pulmonic egressive consonant
	def test_ɸʷ_is_the_representation_of_the_voiceless_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʷ")
		self.assertEqual(actual, expected)

	def test_ɸ̊ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɸ̥ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̥ʷ")
		self.assertEqual(actual, expected)

	def test_β̊ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʷ")
		self.assertEqual(actual, expected)

	def test_β̥ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized bilabial fricative pulmonic egressive consonant
	def test_ɸʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʲ")
		self.assertEqual(actual, expected)

	def test_ɸ̊ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɸ̥ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̥ʲ")
		self.assertEqual(actual, expected)

	def test_β̊ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʲ")
		self.assertEqual(actual, expected)

	def test_β̥ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized bilabial fricative pulmonic egressive consonant
	def test_ɸˠ_is_the_representation_of_the_voiceless_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸˠ")
		self.assertEqual(actual, expected)

	def test_ɸ̊ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɸ̥ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̥ˠ")
		self.assertEqual(actual, expected)

	def test_β̊ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ˠ")
		self.assertEqual(actual, expected)

	def test_β̥ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized bilabial fricative pulmonic egressive consonant
	def test_ɸˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸˤ")
		self.assertEqual(actual, expected)

	def test_ɸ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɸ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̥ˤ")
		self.assertEqual(actual, expected)

	def test_β̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ˤ")
		self.assertEqual(actual, expected)

	def test_β̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated bilabial fricative pulmonic egressive consonant
	def test_ɸʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʰ")
		self.assertEqual(actual, expected)

	def test_β̥ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʰ")
		self.assertEqual(actual, expected)

	def test_β̊ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized bilabial fricative pulmonic egressive consonant
	def test_ɸʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʰʷ")
		self.assertEqual(actual, expected)

	def test_β̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_β̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized bilabial fricative pulmonic egressive consonant
	def test_ɸʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʰʲ")
		self.assertEqual(actual, expected)

	def test_β̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_β̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized bilabial fricative pulmonic egressive consonant
	def test_ɸʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʰˠ")
		self.assertEqual(actual, expected)

	def test_β̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_β̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized bilabial fricative pulmonic egressive consonant
	def test_ɸʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸʰˤ")
		self.assertEqual(actual, expected)

	def test_β̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_β̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced bilabial fricative pulmonic egressive consonant
	def test_β_is_the_representation_of_the_voiced_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β")
		self.assertEqual(actual, expected)

	def test_ɸ̬_is_the_representation_of_the_voiced_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬")
		self.assertEqual(actual, expected)

	def test_ɸ̬_is_the_representation_of_the_voiced_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬")
		self.assertEqual(actual, expected)

# voiced labialized bilabial fricative pulmonic egressive consonant
	def test_βʷ_is_the_representation_of_the_voiced_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʷ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʷ_is_the_representation_of_the_voiced_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʷ_is_the_representation_of_the_voiced_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized bilabial fricative pulmonic egressive consonant
	def test_βʲ_is_the_representation_of_the_voiced_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʲ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʲ_is_the_representation_of_the_voiced_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʲ_is_the_representation_of_the_voiced_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized bilabial fricative pulmonic egressive consonant
	def test_βˠ_is_the_representation_of_the_voiced_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βˠ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ˠ_is_the_representation_of_the_voiced_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ˠ_is_the_representation_of_the_voiced_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized bilabial fricative pulmonic egressive consonant
	def test_βˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βˤ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated bilabial fricative pulmonic egressive consonant
	def test_βʰ_is_the_representation_of_the_voiced_aspirated_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʰ")
		self.assertEqual(actual, expected)

	def test_β̬ʰ_is_the_representation_of_the_voiced_aspirated_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̬ʰ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʰ_is_the_representation_of_the_voiced_aspirated_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized bilabial fricative pulmonic egressive consonant
	def test_βʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʰʷ")
		self.assertEqual(actual, expected)

	def test_β̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized bilabial fricative pulmonic egressive consonant
	def test_βʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʰʲ")
		self.assertEqual(actual, expected)

	def test_β̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized bilabial fricative pulmonic egressive consonant
	def test_βʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʰˠ")
		self.assertEqual(actual, expected)

	def test_β̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized bilabial fricative pulmonic egressive consonant
	def test_βʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("βʰˤ")
		self.assertEqual(actual, expected)

	def test_β̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("β̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɸ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial fricative pulmonic egressive consonant"
		actual = describe_transcription("ɸ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless labio-dental fricative pulmonic egressive consonant
	def test_f_is_the_representation_of_the_voiceless_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f")
		self.assertEqual(actual, expected)

	def test_f̊_is_the_representation_of_the_voiceless_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̊")
		self.assertEqual(actual, expected)

	def test_f̥_is_the_representation_of_the_voiceless_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̥")
		self.assertEqual(actual, expected)

	def test_v̊_is_the_representation_of_the_voiceless_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊")
		self.assertEqual(actual, expected)

	def test_v̥_is_the_representation_of_the_voiceless_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥")
		self.assertEqual(actual, expected)

# voiceless labialized labio-dental fricative pulmonic egressive consonant
	def test_fʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʷ")
		self.assertEqual(actual, expected)

	def test_f̊ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̊ʷ")
		self.assertEqual(actual, expected)

	def test_f̥ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̥ʷ")
		self.assertEqual(actual, expected)

	def test_v̊ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʷ")
		self.assertEqual(actual, expected)

	def test_v̥ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized labio-dental fricative pulmonic egressive consonant
	def test_fʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʲ")
		self.assertEqual(actual, expected)

	def test_f̊ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̊ʲ")
		self.assertEqual(actual, expected)

	def test_f̥ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̥ʲ")
		self.assertEqual(actual, expected)

	def test_v̊ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʲ")
		self.assertEqual(actual, expected)

	def test_v̥ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized labio-dental fricative pulmonic egressive consonant
	def test_fˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fˠ")
		self.assertEqual(actual, expected)

	def test_f̊ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̊ˠ")
		self.assertEqual(actual, expected)

	def test_f̥ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̥ˠ")
		self.assertEqual(actual, expected)

	def test_v̊ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ˠ")
		self.assertEqual(actual, expected)

	def test_v̥ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized labio-dental fricative pulmonic egressive consonant
	def test_fˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fˤ")
		self.assertEqual(actual, expected)

	def test_f̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̊ˤ")
		self.assertEqual(actual, expected)

	def test_f̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̥ˤ")
		self.assertEqual(actual, expected)

	def test_v̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ˤ")
		self.assertEqual(actual, expected)

	def test_v̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated labio-dental fricative pulmonic egressive consonant
	def test_fʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʰ")
		self.assertEqual(actual, expected)

	def test_v̥ʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʰ")
		self.assertEqual(actual, expected)

	def test_v̊ʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized labio-dental fricative pulmonic egressive consonant
	def test_fʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʰʷ")
		self.assertEqual(actual, expected)

	def test_v̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_v̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized labio-dental fricative pulmonic egressive consonant
	def test_fʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʰʲ")
		self.assertEqual(actual, expected)

	def test_v̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_v̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized labio-dental fricative pulmonic egressive consonant
	def test_fʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʰˠ")
		self.assertEqual(actual, expected)

	def test_v̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_v̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized labio-dental fricative pulmonic egressive consonant
	def test_fʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("fʰˤ")
		self.assertEqual(actual, expected)

	def test_v̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_v̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced labio-dental fricative pulmonic egressive consonant
	def test_v_is_the_representation_of_the_voiced_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v")
		self.assertEqual(actual, expected)

	def test_f̬_is_the_representation_of_the_voiced_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬")
		self.assertEqual(actual, expected)

	def test_f̬_is_the_representation_of_the_voiced_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬")
		self.assertEqual(actual, expected)

# voiced labialized labio-dental fricative pulmonic egressive consonant
	def test_vʷ_is_the_representation_of_the_voiced_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʷ")
		self.assertEqual(actual, expected)

	def test_f̬ʷ_is_the_representation_of_the_voiced_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʷ")
		self.assertEqual(actual, expected)

	def test_f̬ʷ_is_the_representation_of_the_voiced_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized labio-dental fricative pulmonic egressive consonant
	def test_vʲ_is_the_representation_of_the_voiced_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʲ")
		self.assertEqual(actual, expected)

	def test_f̬ʲ_is_the_representation_of_the_voiced_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʲ")
		self.assertEqual(actual, expected)

	def test_f̬ʲ_is_the_representation_of_the_voiced_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized labio-dental fricative pulmonic egressive consonant
	def test_vˠ_is_the_representation_of_the_voiced_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vˠ")
		self.assertEqual(actual, expected)

	def test_f̬ˠ_is_the_representation_of_the_voiced_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ˠ")
		self.assertEqual(actual, expected)

	def test_f̬ˠ_is_the_representation_of_the_voiced_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized labio-dental fricative pulmonic egressive consonant
	def test_vˤ_is_the_representation_of_the_voiced_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vˤ")
		self.assertEqual(actual, expected)

	def test_f̬ˤ_is_the_representation_of_the_voiced_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ˤ")
		self.assertEqual(actual, expected)

	def test_f̬ˤ_is_the_representation_of_the_voiced_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated labio-dental fricative pulmonic egressive consonant
	def test_vʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʰ")
		self.assertEqual(actual, expected)

	def test_v̬ʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̬ʰ")
		self.assertEqual(actual, expected)

	def test_f̬ʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized labio-dental fricative pulmonic egressive consonant
	def test_vʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʰʷ")
		self.assertEqual(actual, expected)

	def test_v̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_f̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized labio-dental fricative pulmonic egressive consonant
	def test_vʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʰʲ")
		self.assertEqual(actual, expected)

	def test_v̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_f̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized labio-dental fricative pulmonic egressive consonant
	def test_vʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʰˠ")
		self.assertEqual(actual, expected)

	def test_v̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_f̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized labio-dental fricative pulmonic egressive consonant
	def test_vʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("vʰˤ")
		self.assertEqual(actual, expected)

	def test_v̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("v̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_f̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental fricative pulmonic egressive consonant"
		actual = describe_transcription("f̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless dental fricative pulmonic egressive consonant
	def test_θ_is_the_representation_of_the_voiceless_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ")
		self.assertEqual(actual, expected)

	def test_θ̊_is_the_representation_of_the_voiceless_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̊")
		self.assertEqual(actual, expected)

	def test_θ̥_is_the_representation_of_the_voiceless_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̥")
		self.assertEqual(actual, expected)

	def test_ð̊_is_the_representation_of_the_voiceless_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊")
		self.assertEqual(actual, expected)

	def test_ð̥_is_the_representation_of_the_voiceless_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥")
		self.assertEqual(actual, expected)

# voiceless labialized dental fricative pulmonic egressive consonant
	def test_θʷ_is_the_representation_of_the_voiceless_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʷ")
		self.assertEqual(actual, expected)

	def test_θ̊ʷ_is_the_representation_of_the_voiceless_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̊ʷ")
		self.assertEqual(actual, expected)

	def test_θ̥ʷ_is_the_representation_of_the_voiceless_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ð̊ʷ_is_the_representation_of_the_voiceless_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʷ")
		self.assertEqual(actual, expected)

	def test_ð̥ʷ_is_the_representation_of_the_voiceless_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized dental fricative pulmonic egressive consonant
	def test_θʲ_is_the_representation_of_the_voiceless_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʲ")
		self.assertEqual(actual, expected)

	def test_θ̊ʲ_is_the_representation_of_the_voiceless_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̊ʲ")
		self.assertEqual(actual, expected)

	def test_θ̥ʲ_is_the_representation_of_the_voiceless_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ð̊ʲ_is_the_representation_of_the_voiceless_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʲ")
		self.assertEqual(actual, expected)

	def test_ð̥ʲ_is_the_representation_of_the_voiceless_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized dental fricative pulmonic egressive consonant
	def test_θˠ_is_the_representation_of_the_voiceless_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θˠ")
		self.assertEqual(actual, expected)

	def test_θ̊ˠ_is_the_representation_of_the_voiceless_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̊ˠ")
		self.assertEqual(actual, expected)

	def test_θ̥ˠ_is_the_representation_of_the_voiceless_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ð̊ˠ_is_the_representation_of_the_voiceless_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ˠ")
		self.assertEqual(actual, expected)

	def test_ð̥ˠ_is_the_representation_of_the_voiceless_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized dental fricative pulmonic egressive consonant
	def test_θˤ_is_the_representation_of_the_voiceless_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θˤ")
		self.assertEqual(actual, expected)

	def test_θ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̊ˤ")
		self.assertEqual(actual, expected)

	def test_θ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ð̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ˤ")
		self.assertEqual(actual, expected)

	def test_ð̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated dental fricative pulmonic egressive consonant
	def test_θʰ_is_the_representation_of_the_voiceless_aspirated_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʰ")
		self.assertEqual(actual, expected)

	def test_ð̥ʰ_is_the_representation_of_the_voiceless_aspirated_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʰ")
		self.assertEqual(actual, expected)

	def test_ð̊ʰ_is_the_representation_of_the_voiceless_aspirated_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized dental fricative pulmonic egressive consonant
	def test_θʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʰʷ")
		self.assertEqual(actual, expected)

	def test_ð̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ð̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized dental fricative pulmonic egressive consonant
	def test_θʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʰʲ")
		self.assertEqual(actual, expected)

	def test_ð̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ð̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized dental fricative pulmonic egressive consonant
	def test_θʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʰˠ")
		self.assertEqual(actual, expected)

	def test_ð̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ð̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized dental fricative pulmonic egressive consonant
	def test_θʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θʰˤ")
		self.assertEqual(actual, expected)

	def test_ð̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ð̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced dental fricative pulmonic egressive consonant
	def test_ð_is_the_representation_of_the_voiced_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð")
		self.assertEqual(actual, expected)

	def test_θ̬_is_the_representation_of_the_voiced_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬")
		self.assertEqual(actual, expected)

	def test_θ̬_is_the_representation_of_the_voiced_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬")
		self.assertEqual(actual, expected)

# voiced labialized dental fricative pulmonic egressive consonant
	def test_ðʷ_is_the_representation_of_the_voiced_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʷ")
		self.assertEqual(actual, expected)

	def test_θ̬ʷ_is_the_representation_of_the_voiced_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʷ")
		self.assertEqual(actual, expected)

	def test_θ̬ʷ_is_the_representation_of_the_voiced_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized dental fricative pulmonic egressive consonant
	def test_ðʲ_is_the_representation_of_the_voiced_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʲ")
		self.assertEqual(actual, expected)

	def test_θ̬ʲ_is_the_representation_of_the_voiced_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʲ")
		self.assertEqual(actual, expected)

	def test_θ̬ʲ_is_the_representation_of_the_voiced_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized dental fricative pulmonic egressive consonant
	def test_ðˠ_is_the_representation_of_the_voiced_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðˠ")
		self.assertEqual(actual, expected)

	def test_θ̬ˠ_is_the_representation_of_the_voiced_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ˠ")
		self.assertEqual(actual, expected)

	def test_θ̬ˠ_is_the_representation_of_the_voiced_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized dental fricative pulmonic egressive consonant
	def test_ðˤ_is_the_representation_of_the_voiced_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðˤ")
		self.assertEqual(actual, expected)

	def test_θ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ˤ")
		self.assertEqual(actual, expected)

	def test_θ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated dental fricative pulmonic egressive consonant
	def test_ðʰ_is_the_representation_of_the_voiced_aspirated_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʰ")
		self.assertEqual(actual, expected)

	def test_ð̬ʰ_is_the_representation_of_the_voiced_aspirated_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̬ʰ")
		self.assertEqual(actual, expected)

	def test_θ̬ʰ_is_the_representation_of_the_voiced_aspirated_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized dental fricative pulmonic egressive consonant
	def test_ðʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʰʷ")
		self.assertEqual(actual, expected)

	def test_ð̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_θ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized dental fricative pulmonic egressive consonant
	def test_ðʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʰʲ")
		self.assertEqual(actual, expected)

	def test_ð̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_θ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized dental fricative pulmonic egressive consonant
	def test_ðʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʰˠ")
		self.assertEqual(actual, expected)

	def test_ð̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_θ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized dental fricative pulmonic egressive consonant
	def test_ðʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ðʰˤ")
		self.assertEqual(actual, expected)

	def test_ð̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("ð̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_θ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_dental_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized dental fricative pulmonic egressive consonant"
		actual = describe_transcription("θ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar fricative pulmonic egressive consonant
	def test_s_is_the_representation_of_the_voiceless_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s")
		self.assertEqual(actual, expected)

	def test_s̊_is_the_representation_of_the_voiceless_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̊")
		self.assertEqual(actual, expected)

	def test_s̥_is_the_representation_of_the_voiceless_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̥")
		self.assertEqual(actual, expected)

	def test_z̊_is_the_representation_of_the_voiceless_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊")
		self.assertEqual(actual, expected)

	def test_z̥_is_the_representation_of_the_voiceless_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar fricative pulmonic egressive consonant
	def test_sʷ_is_the_representation_of_the_voiceless_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʷ")
		self.assertEqual(actual, expected)

	def test_s̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̊ʷ")
		self.assertEqual(actual, expected)

	def test_s̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̥ʷ")
		self.assertEqual(actual, expected)

	def test_z̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʷ")
		self.assertEqual(actual, expected)

	def test_z̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar fricative pulmonic egressive consonant
	def test_sʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʲ")
		self.assertEqual(actual, expected)

	def test_s̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̊ʲ")
		self.assertEqual(actual, expected)

	def test_s̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̥ʲ")
		self.assertEqual(actual, expected)

	def test_z̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʲ")
		self.assertEqual(actual, expected)

	def test_z̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar fricative pulmonic egressive consonant
	def test_sˠ_is_the_representation_of_the_voiceless_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sˠ")
		self.assertEqual(actual, expected)

	def test_s̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̊ˠ")
		self.assertEqual(actual, expected)

	def test_s̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̥ˠ")
		self.assertEqual(actual, expected)

	def test_z̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ˠ")
		self.assertEqual(actual, expected)

	def test_z̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar fricative pulmonic egressive consonant
	def test_sˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sˤ")
		self.assertEqual(actual, expected)

	def test_s̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̊ˤ")
		self.assertEqual(actual, expected)

	def test_s̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̥ˤ")
		self.assertEqual(actual, expected)

	def test_z̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ˤ")
		self.assertEqual(actual, expected)

	def test_z̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar fricative pulmonic egressive consonant
	def test_sʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʰ")
		self.assertEqual(actual, expected)

	def test_z̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʰ")
		self.assertEqual(actual, expected)

	def test_z̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar fricative pulmonic egressive consonant
	def test_sʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʰʷ")
		self.assertEqual(actual, expected)

	def test_z̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_z̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar fricative pulmonic egressive consonant
	def test_sʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʰʲ")
		self.assertEqual(actual, expected)

	def test_z̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_z̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar fricative pulmonic egressive consonant
	def test_sʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʰˠ")
		self.assertEqual(actual, expected)

	def test_z̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_z̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar fricative pulmonic egressive consonant
	def test_sʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("sʰˤ")
		self.assertEqual(actual, expected)

	def test_z̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_z̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar fricative pulmonic egressive consonant
	def test_z_is_the_representation_of_the_voiced_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z")
		self.assertEqual(actual, expected)

	def test_s̬_is_the_representation_of_the_voiced_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬")
		self.assertEqual(actual, expected)

	def test_s̬_is_the_representation_of_the_voiced_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬")
		self.assertEqual(actual, expected)

# voiced labialized alveolar fricative pulmonic egressive consonant
	def test_zʷ_is_the_representation_of_the_voiced_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʷ")
		self.assertEqual(actual, expected)

	def test_s̬ʷ_is_the_representation_of_the_voiced_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʷ")
		self.assertEqual(actual, expected)

	def test_s̬ʷ_is_the_representation_of_the_voiced_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar fricative pulmonic egressive consonant
	def test_zʲ_is_the_representation_of_the_voiced_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʲ")
		self.assertEqual(actual, expected)

	def test_s̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʲ")
		self.assertEqual(actual, expected)

	def test_s̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar fricative pulmonic egressive consonant
	def test_zˠ_is_the_representation_of_the_voiced_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zˠ")
		self.assertEqual(actual, expected)

	def test_s̬ˠ_is_the_representation_of_the_voiced_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ˠ")
		self.assertEqual(actual, expected)

	def test_s̬ˠ_is_the_representation_of_the_voiced_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar fricative pulmonic egressive consonant
	def test_zˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zˤ")
		self.assertEqual(actual, expected)

	def test_s̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ˤ")
		self.assertEqual(actual, expected)

	def test_s̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar fricative pulmonic egressive consonant
	def test_zʰ_is_the_representation_of_the_voiced_aspirated_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʰ")
		self.assertEqual(actual, expected)

	def test_z̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̬ʰ")
		self.assertEqual(actual, expected)

	def test_s̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar fricative pulmonic egressive consonant
	def test_zʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʰʷ")
		self.assertEqual(actual, expected)

	def test_z̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_s̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar fricative pulmonic egressive consonant
	def test_zʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʰʲ")
		self.assertEqual(actual, expected)

	def test_z̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_s̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar fricative pulmonic egressive consonant
	def test_zʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʰˠ")
		self.assertEqual(actual, expected)

	def test_z̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_s̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar fricative pulmonic egressive consonant
	def test_zʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("zʰˤ")
		self.assertEqual(actual, expected)

	def test_z̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("z̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_s̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("s̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless post-alveolar fricative pulmonic egressive consonant
	def test_ʃ_is_the_representation_of_the_voiceless_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ")
		self.assertEqual(actual, expected)

	def test_ʃ̊_is_the_representation_of_the_voiceless_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̊")
		self.assertEqual(actual, expected)

	def test_ʃ̥_is_the_representation_of_the_voiceless_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̥")
		self.assertEqual(actual, expected)

	def test_ʒ̊_is_the_representation_of_the_voiceless_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊")
		self.assertEqual(actual, expected)

	def test_ʒ̥_is_the_representation_of_the_voiceless_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥")
		self.assertEqual(actual, expected)

# voiceless labialized post-alveolar fricative pulmonic egressive consonant
	def test_ʃʷ_is_the_representation_of_the_voiceless_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʷ")
		self.assertEqual(actual, expected)

	def test_ʃ̊ʷ_is_the_representation_of_the_voiceless_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʃ̥ʷ_is_the_representation_of_the_voiceless_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʷ_is_the_representation_of_the_voiceless_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʷ_is_the_representation_of_the_voiceless_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized post-alveolar fricative pulmonic egressive consonant
	def test_ʃʲ_is_the_representation_of_the_voiceless_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʲ")
		self.assertEqual(actual, expected)

	def test_ʃ̊ʲ_is_the_representation_of_the_voiceless_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʃ̥ʲ_is_the_representation_of_the_voiceless_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʲ_is_the_representation_of_the_voiceless_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʲ_is_the_representation_of_the_voiceless_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized post-alveolar fricative pulmonic egressive consonant
	def test_ʃˠ_is_the_representation_of_the_voiceless_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃˠ")
		self.assertEqual(actual, expected)

	def test_ʃ̊ˠ_is_the_representation_of_the_voiceless_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʃ̥ˠ_is_the_representation_of_the_voiceless_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ˠ_is_the_representation_of_the_voiceless_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ˠ_is_the_representation_of_the_voiceless_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized post-alveolar fricative pulmonic egressive consonant
	def test_ʃˤ_is_the_representation_of_the_voiceless_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃˤ")
		self.assertEqual(actual, expected)

	def test_ʃ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʃ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated post-alveolar fricative pulmonic egressive consonant
	def test_ʃʰ_is_the_representation_of_the_voiceless_aspirated_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʰ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʰ_is_the_representation_of_the_voiceless_aspirated_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʰ_is_the_representation_of_the_voiceless_aspirated_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized post-alveolar fricative pulmonic egressive consonant
	def test_ʃʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʰʷ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized post-alveolar fricative pulmonic egressive consonant
	def test_ʃʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʰʲ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized post-alveolar fricative pulmonic egressive consonant
	def test_ʃʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʰˠ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant
	def test_ʃʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃʰˤ")
		self.assertEqual(actual, expected)

	def test_ʒ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʒ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced post-alveolar fricative pulmonic egressive consonant
	def test_ʒ_is_the_representation_of_the_voiced_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ")
		self.assertEqual(actual, expected)

	def test_ʃ̬_is_the_representation_of_the_voiced_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬")
		self.assertEqual(actual, expected)

	def test_ʃ̬_is_the_representation_of_the_voiced_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬")
		self.assertEqual(actual, expected)

# voiced labialized post-alveolar fricative pulmonic egressive consonant
	def test_ʒʷ_is_the_representation_of_the_voiced_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʷ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʷ_is_the_representation_of_the_voiced_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʷ_is_the_representation_of_the_voiced_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized post-alveolar fricative pulmonic egressive consonant
	def test_ʒʲ_is_the_representation_of_the_voiced_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʲ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʲ_is_the_representation_of_the_voiced_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʲ_is_the_representation_of_the_voiced_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized post-alveolar fricative pulmonic egressive consonant
	def test_ʒˠ_is_the_representation_of_the_voiced_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒˠ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ˠ_is_the_representation_of_the_voiced_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ˠ_is_the_representation_of_the_voiced_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized post-alveolar fricative pulmonic egressive consonant
	def test_ʒˤ_is_the_representation_of_the_voiced_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒˤ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated post-alveolar fricative pulmonic egressive consonant
	def test_ʒʰ_is_the_representation_of_the_voiced_aspirated_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʰ")
		self.assertEqual(actual, expected)

	def test_ʒ̬ʰ_is_the_representation_of_the_voiced_aspirated_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʰ_is_the_representation_of_the_voiced_aspirated_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized post-alveolar fricative pulmonic egressive consonant
	def test_ʒʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʰʷ")
		self.assertEqual(actual, expected)

	def test_ʒ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized post-alveolar fricative pulmonic egressive consonant
	def test_ʒʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʰʲ")
		self.assertEqual(actual, expected)

	def test_ʒ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized post-alveolar fricative pulmonic egressive consonant
	def test_ʒʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʰˠ")
		self.assertEqual(actual, expected)

	def test_ʒ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant
	def test_ʒʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒʰˤ")
		self.assertEqual(actual, expected)

	def test_ʒ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʒ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʃ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_post_alveolar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized post-alveolar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʃ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless retroflex fricative pulmonic egressive consonant
	def test_ʂ_is_the_representation_of_the_voiceless_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ")
		self.assertEqual(actual, expected)

	def test_ʂ̊_is_the_representation_of_the_voiceless_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̊")
		self.assertEqual(actual, expected)

	def test_ʂ̥_is_the_representation_of_the_voiceless_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̥")
		self.assertEqual(actual, expected)

	def test_ʐ̊_is_the_representation_of_the_voiceless_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊")
		self.assertEqual(actual, expected)

	def test_ʐ̥_is_the_representation_of_the_voiceless_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥")
		self.assertEqual(actual, expected)

# voiceless labialized retroflex fricative pulmonic egressive consonant
	def test_ʂʷ_is_the_representation_of_the_voiceless_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʷ")
		self.assertEqual(actual, expected)

	def test_ʂ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʂ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized retroflex fricative pulmonic egressive consonant
	def test_ʂʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʲ")
		self.assertEqual(actual, expected)

	def test_ʂ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʂ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized retroflex fricative pulmonic egressive consonant
	def test_ʂˠ_is_the_representation_of_the_voiceless_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂˠ")
		self.assertEqual(actual, expected)

	def test_ʂ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʂ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized retroflex fricative pulmonic egressive consonant
	def test_ʂˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂˤ")
		self.assertEqual(actual, expected)

	def test_ʂ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʂ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated retroflex fricative pulmonic egressive consonant
	def test_ʂʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʰ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized retroflex fricative pulmonic egressive consonant
	def test_ʂʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʰʷ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized retroflex fricative pulmonic egressive consonant
	def test_ʂʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʰʲ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized retroflex fricative pulmonic egressive consonant
	def test_ʂʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʰˠ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized retroflex fricative pulmonic egressive consonant
	def test_ʂʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂʰˤ")
		self.assertEqual(actual, expected)

	def test_ʐ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʐ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced retroflex fricative pulmonic egressive consonant
	def test_ʐ_is_the_representation_of_the_voiced_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ")
		self.assertEqual(actual, expected)

	def test_ʂ̬_is_the_representation_of_the_voiced_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬")
		self.assertEqual(actual, expected)

	def test_ʂ̬_is_the_representation_of_the_voiced_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬")
		self.assertEqual(actual, expected)

# voiced labialized retroflex fricative pulmonic egressive consonant
	def test_ʐʷ_is_the_representation_of_the_voiced_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʷ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʷ_is_the_representation_of_the_voiced_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʷ_is_the_representation_of_the_voiced_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized retroflex fricative pulmonic egressive consonant
	def test_ʐʲ_is_the_representation_of_the_voiced_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʲ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʲ_is_the_representation_of_the_voiced_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʲ_is_the_representation_of_the_voiced_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized retroflex fricative pulmonic egressive consonant
	def test_ʐˠ_is_the_representation_of_the_voiced_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐˠ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ˠ_is_the_representation_of_the_voiced_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ˠ_is_the_representation_of_the_voiced_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized retroflex fricative pulmonic egressive consonant
	def test_ʐˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐˤ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated retroflex fricative pulmonic egressive consonant
	def test_ʐʰ_is_the_representation_of_the_voiced_aspirated_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʰ")
		self.assertEqual(actual, expected)

	def test_ʐ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized retroflex fricative pulmonic egressive consonant
	def test_ʐʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʰʷ")
		self.assertEqual(actual, expected)

	def test_ʐ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized retroflex fricative pulmonic egressive consonant
	def test_ʐʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʰʲ")
		self.assertEqual(actual, expected)

	def test_ʐ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized retroflex fricative pulmonic egressive consonant
	def test_ʐʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʰˠ")
		self.assertEqual(actual, expected)

	def test_ʐ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized retroflex fricative pulmonic egressive consonant
	def test_ʐʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐʰˤ")
		self.assertEqual(actual, expected)

	def test_ʐ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʐ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʂ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex fricative pulmonic egressive consonant"
		actual = describe_transcription("ʂ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless palatal fricative pulmonic egressive consonant
	def test_ç_is_the_representation_of_the_voiceless_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç")
		self.assertEqual(actual, expected)

	def test_ç̊_is_the_representation_of_the_voiceless_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̊")
		self.assertEqual(actual, expected)

	def test_ç̥_is_the_representation_of_the_voiceless_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̥")
		self.assertEqual(actual, expected)

	def test_ʝ̊_is_the_representation_of_the_voiceless_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊")
		self.assertEqual(actual, expected)

	def test_ʝ̥_is_the_representation_of_the_voiceless_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥")
		self.assertEqual(actual, expected)

# voiceless labialized palatal fricative pulmonic egressive consonant
	def test_çʷ_is_the_representation_of_the_voiceless_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʷ")
		self.assertEqual(actual, expected)

	def test_ç̊ʷ_is_the_representation_of_the_voiceless_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̊ʷ")
		self.assertEqual(actual, expected)

	def test_ç̥ʷ_is_the_representation_of_the_voiceless_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʷ_is_the_representation_of_the_voiceless_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʷ_is_the_representation_of_the_voiceless_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized palatal fricative pulmonic egressive consonant
	def test_çʲ_is_the_representation_of_the_voiceless_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʲ")
		self.assertEqual(actual, expected)

	def test_ç̊ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̊ʲ")
		self.assertEqual(actual, expected)

	def test_ç̥ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized palatal fricative pulmonic egressive consonant
	def test_çˠ_is_the_representation_of_the_voiceless_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çˠ")
		self.assertEqual(actual, expected)

	def test_ç̊ˠ_is_the_representation_of_the_voiceless_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̊ˠ")
		self.assertEqual(actual, expected)

	def test_ç̥ˠ_is_the_representation_of_the_voiceless_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ˠ_is_the_representation_of_the_voiceless_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ˠ_is_the_representation_of_the_voiceless_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized palatal fricative pulmonic egressive consonant
	def test_çˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çˤ")
		self.assertEqual(actual, expected)

	def test_ç̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̊ˤ")
		self.assertEqual(actual, expected)

	def test_ç̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatal fricative pulmonic egressive consonant
	def test_çʰ_is_the_representation_of_the_voiceless_aspirated_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʰ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized palatal fricative pulmonic egressive consonant
	def test_çʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʰʷ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized palatal fricative pulmonic egressive consonant
	def test_çʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʰʲ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized palatal fricative pulmonic egressive consonant
	def test_çʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʰˠ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized palatal fricative pulmonic egressive consonant
	def test_çʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("çʰˤ")
		self.assertEqual(actual, expected)

	def test_ʝ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʝ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced palatal fricative pulmonic egressive consonant
	def test_ʝ_is_the_representation_of_the_voiced_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ")
		self.assertEqual(actual, expected)

	def test_ç̬_is_the_representation_of_the_voiced_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬")
		self.assertEqual(actual, expected)

	def test_ç̬_is_the_representation_of_the_voiced_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬")
		self.assertEqual(actual, expected)

# voiced labialized palatal fricative pulmonic egressive consonant
	def test_ʝʷ_is_the_representation_of_the_voiced_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʷ")
		self.assertEqual(actual, expected)

	def test_ç̬ʷ_is_the_representation_of_the_voiced_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʷ")
		self.assertEqual(actual, expected)

	def test_ç̬ʷ_is_the_representation_of_the_voiced_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized palatal fricative pulmonic egressive consonant
	def test_ʝʲ_is_the_representation_of_the_voiced_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʲ")
		self.assertEqual(actual, expected)

	def test_ç̬ʲ_is_the_representation_of_the_voiced_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʲ")
		self.assertEqual(actual, expected)

	def test_ç̬ʲ_is_the_representation_of_the_voiced_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized palatal fricative pulmonic egressive consonant
	def test_ʝˠ_is_the_representation_of_the_voiced_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝˠ")
		self.assertEqual(actual, expected)

	def test_ç̬ˠ_is_the_representation_of_the_voiced_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ˠ")
		self.assertEqual(actual, expected)

	def test_ç̬ˠ_is_the_representation_of_the_voiced_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized palatal fricative pulmonic egressive consonant
	def test_ʝˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝˤ")
		self.assertEqual(actual, expected)

	def test_ç̬ˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ˤ")
		self.assertEqual(actual, expected)

	def test_ç̬ˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated palatal fricative pulmonic egressive consonant
	def test_ʝʰ_is_the_representation_of_the_voiced_aspirated_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʰ")
		self.assertEqual(actual, expected)

	def test_ʝ̬ʰ_is_the_representation_of_the_voiced_aspirated_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ç̬ʰ_is_the_representation_of_the_voiced_aspirated_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized palatal fricative pulmonic egressive consonant
	def test_ʝʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʰʷ")
		self.assertEqual(actual, expected)

	def test_ʝ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ç̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized palatal fricative pulmonic egressive consonant
	def test_ʝʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʰʲ")
		self.assertEqual(actual, expected)

	def test_ʝ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ç̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized palatal fricative pulmonic egressive consonant
	def test_ʝʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʰˠ")
		self.assertEqual(actual, expected)

	def test_ʝ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ç̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized palatal fricative pulmonic egressive consonant
	def test_ʝʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝʰˤ")
		self.assertEqual(actual, expected)

	def test_ʝ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʝ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ç̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ç̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless velar fricative pulmonic egressive consonant
	def test_x_is_the_representation_of_the_voiceless_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x")
		self.assertEqual(actual, expected)

	def test_x̊_is_the_representation_of_the_voiceless_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̊")
		self.assertEqual(actual, expected)

	def test_x̥_is_the_representation_of_the_voiceless_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̥")
		self.assertEqual(actual, expected)

	def test_ɣ̊_is_the_representation_of_the_voiceless_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊")
		self.assertEqual(actual, expected)

	def test_ɣ̥_is_the_representation_of_the_voiceless_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥")
		self.assertEqual(actual, expected)

# voiceless labialized velar fricative pulmonic egressive consonant
	def test_xʷ_is_the_representation_of_the_voiceless_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʷ")
		self.assertEqual(actual, expected)

	def test_x̊ʷ_is_the_representation_of_the_voiceless_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̊ʷ")
		self.assertEqual(actual, expected)

	def test_x̥ʷ_is_the_representation_of_the_voiceless_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̥ʷ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʷ_is_the_representation_of_the_voiceless_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʷ_is_the_representation_of_the_voiceless_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized velar fricative pulmonic egressive consonant
	def test_xʲ_is_the_representation_of_the_voiceless_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʲ")
		self.assertEqual(actual, expected)

	def test_x̊ʲ_is_the_representation_of_the_voiceless_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̊ʲ")
		self.assertEqual(actual, expected)

	def test_x̥ʲ_is_the_representation_of_the_voiceless_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̥ʲ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʲ_is_the_representation_of_the_voiceless_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʲ_is_the_representation_of_the_voiceless_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized velar fricative pulmonic egressive consonant
	def test_xˠ_is_the_representation_of_the_voiceless_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xˠ")
		self.assertEqual(actual, expected)

	def test_x̊ˠ_is_the_representation_of_the_voiceless_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̊ˠ")
		self.assertEqual(actual, expected)

	def test_x̥ˠ_is_the_representation_of_the_voiceless_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̥ˠ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ˠ_is_the_representation_of_the_voiceless_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ˠ_is_the_representation_of_the_voiceless_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized velar fricative pulmonic egressive consonant
	def test_xˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xˤ")
		self.assertEqual(actual, expected)

	def test_x̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̊ˤ")
		self.assertEqual(actual, expected)

	def test_x̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̥ˤ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated velar fricative pulmonic egressive consonant
	def test_xʰ_is_the_representation_of_the_voiceless_aspirated_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʰ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʰ_is_the_representation_of_the_voiceless_aspirated_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʰ_is_the_representation_of_the_voiceless_aspirated_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized velar fricative pulmonic egressive consonant
	def test_xʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʰʷ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized velar fricative pulmonic egressive consonant
	def test_xʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʰʲ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized velar fricative pulmonic egressive consonant
	def test_xʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʰˠ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized velar fricative pulmonic egressive consonant
	def test_xʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("xʰˤ")
		self.assertEqual(actual, expected)

	def test_ɣ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɣ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced velar fricative pulmonic egressive consonant
	def test_ɣ_is_the_representation_of_the_voiced_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ")
		self.assertEqual(actual, expected)

	def test_x̬_is_the_representation_of_the_voiced_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬")
		self.assertEqual(actual, expected)

	def test_x̬_is_the_representation_of_the_voiced_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬")
		self.assertEqual(actual, expected)

# voiced labialized velar fricative pulmonic egressive consonant
	def test_ɣʷ_is_the_representation_of_the_voiced_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʷ")
		self.assertEqual(actual, expected)

	def test_x̬ʷ_is_the_representation_of_the_voiced_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʷ")
		self.assertEqual(actual, expected)

	def test_x̬ʷ_is_the_representation_of_the_voiced_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized velar fricative pulmonic egressive consonant
	def test_ɣʲ_is_the_representation_of_the_voiced_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʲ")
		self.assertEqual(actual, expected)

	def test_x̬ʲ_is_the_representation_of_the_voiced_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʲ")
		self.assertEqual(actual, expected)

	def test_x̬ʲ_is_the_representation_of_the_voiced_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized velar fricative pulmonic egressive consonant
	def test_ɣˠ_is_the_representation_of_the_voiced_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣˠ")
		self.assertEqual(actual, expected)

	def test_x̬ˠ_is_the_representation_of_the_voiced_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ˠ")
		self.assertEqual(actual, expected)

	def test_x̬ˠ_is_the_representation_of_the_voiced_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized velar fricative pulmonic egressive consonant
	def test_ɣˤ_is_the_representation_of_the_voiced_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣˤ")
		self.assertEqual(actual, expected)

	def test_x̬ˤ_is_the_representation_of_the_voiced_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ˤ")
		self.assertEqual(actual, expected)

	def test_x̬ˤ_is_the_representation_of_the_voiced_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated velar fricative pulmonic egressive consonant
	def test_ɣʰ_is_the_representation_of_the_voiced_aspirated_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʰ")
		self.assertEqual(actual, expected)

	def test_ɣ̬ʰ_is_the_representation_of_the_voiced_aspirated_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̬ʰ")
		self.assertEqual(actual, expected)

	def test_x̬ʰ_is_the_representation_of_the_voiced_aspirated_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized velar fricative pulmonic egressive consonant
	def test_ɣʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʰʷ")
		self.assertEqual(actual, expected)

	def test_ɣ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_x̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized velar fricative pulmonic egressive consonant
	def test_ɣʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʰʲ")
		self.assertEqual(actual, expected)

	def test_ɣ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_x̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized velar fricative pulmonic egressive consonant
	def test_ɣʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʰˠ")
		self.assertEqual(actual, expected)

	def test_ɣ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_x̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized velar fricative pulmonic egressive consonant
	def test_ɣʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣʰˤ")
		self.assertEqual(actual, expected)

	def test_ɣ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ɣ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_x̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar fricative pulmonic egressive consonant"
		actual = describe_transcription("x̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless uvular fricative pulmonic egressive consonant
	def test_χ_is_the_representation_of_the_voiceless_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ")
		self.assertEqual(actual, expected)

	def test_χ̊_is_the_representation_of_the_voiceless_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̊")
		self.assertEqual(actual, expected)

	def test_χ̥_is_the_representation_of_the_voiceless_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̥")
		self.assertEqual(actual, expected)

	def test_ʁ̊_is_the_representation_of_the_voiceless_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊")
		self.assertEqual(actual, expected)

	def test_ʁ̥_is_the_representation_of_the_voiceless_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥")
		self.assertEqual(actual, expected)

# voiceless labialized uvular fricative pulmonic egressive consonant
	def test_χʷ_is_the_representation_of_the_voiceless_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʷ")
		self.assertEqual(actual, expected)

	def test_χ̊ʷ_is_the_representation_of_the_voiceless_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̊ʷ")
		self.assertEqual(actual, expected)

	def test_χ̥ʷ_is_the_representation_of_the_voiceless_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʷ_is_the_representation_of_the_voiceless_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʷ_is_the_representation_of_the_voiceless_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized uvular fricative pulmonic egressive consonant
	def test_χʲ_is_the_representation_of_the_voiceless_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʲ")
		self.assertEqual(actual, expected)

	def test_χ̊ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̊ʲ")
		self.assertEqual(actual, expected)

	def test_χ̥ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized uvular fricative pulmonic egressive consonant
	def test_χˠ_is_the_representation_of_the_voiceless_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χˠ")
		self.assertEqual(actual, expected)

	def test_χ̊ˠ_is_the_representation_of_the_voiceless_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̊ˠ")
		self.assertEqual(actual, expected)

	def test_χ̥ˠ_is_the_representation_of_the_voiceless_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ˠ_is_the_representation_of_the_voiceless_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ˠ_is_the_representation_of_the_voiceless_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized uvular fricative pulmonic egressive consonant
	def test_χˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χˤ")
		self.assertEqual(actual, expected)

	def test_χ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̊ˤ")
		self.assertEqual(actual, expected)

	def test_χ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated uvular fricative pulmonic egressive consonant
	def test_χʰ_is_the_representation_of_the_voiceless_aspirated_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʰ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized uvular fricative pulmonic egressive consonant
	def test_χʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʰʷ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized uvular fricative pulmonic egressive consonant
	def test_χʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʰʲ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized uvular fricative pulmonic egressive consonant
	def test_χʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʰˠ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized uvular fricative pulmonic egressive consonant
	def test_χʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χʰˤ")
		self.assertEqual(actual, expected)

	def test_ʁ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʁ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced uvular fricative pulmonic egressive consonant
	def test_ʁ_is_the_representation_of_the_voiced_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ")
		self.assertEqual(actual, expected)

	def test_χ̬_is_the_representation_of_the_voiced_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬")
		self.assertEqual(actual, expected)

	def test_χ̬_is_the_representation_of_the_voiced_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬")
		self.assertEqual(actual, expected)

# voiced labialized uvular fricative pulmonic egressive consonant
	def test_ʁʷ_is_the_representation_of_the_voiced_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʷ")
		self.assertEqual(actual, expected)

	def test_χ̬ʷ_is_the_representation_of_the_voiced_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʷ")
		self.assertEqual(actual, expected)

	def test_χ̬ʷ_is_the_representation_of_the_voiced_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized uvular fricative pulmonic egressive consonant
	def test_ʁʲ_is_the_representation_of_the_voiced_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʲ")
		self.assertEqual(actual, expected)

	def test_χ̬ʲ_is_the_representation_of_the_voiced_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʲ")
		self.assertEqual(actual, expected)

	def test_χ̬ʲ_is_the_representation_of_the_voiced_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized uvular fricative pulmonic egressive consonant
	def test_ʁˠ_is_the_representation_of_the_voiced_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁˠ")
		self.assertEqual(actual, expected)

	def test_χ̬ˠ_is_the_representation_of_the_voiced_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ˠ")
		self.assertEqual(actual, expected)

	def test_χ̬ˠ_is_the_representation_of_the_voiced_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized uvular fricative pulmonic egressive consonant
	def test_ʁˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁˤ")
		self.assertEqual(actual, expected)

	def test_χ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ˤ")
		self.assertEqual(actual, expected)

	def test_χ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated uvular fricative pulmonic egressive consonant
	def test_ʁʰ_is_the_representation_of_the_voiced_aspirated_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʰ")
		self.assertEqual(actual, expected)

	def test_ʁ̬ʰ_is_the_representation_of_the_voiced_aspirated_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̬ʰ")
		self.assertEqual(actual, expected)

	def test_χ̬ʰ_is_the_representation_of_the_voiced_aspirated_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized uvular fricative pulmonic egressive consonant
	def test_ʁʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʰʷ")
		self.assertEqual(actual, expected)

	def test_ʁ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_χ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized uvular fricative pulmonic egressive consonant
	def test_ʁʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʰʲ")
		self.assertEqual(actual, expected)

	def test_ʁ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_χ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized uvular fricative pulmonic egressive consonant
	def test_ʁʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʰˠ")
		self.assertEqual(actual, expected)

	def test_ʁ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_χ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized uvular fricative pulmonic egressive consonant
	def test_ʁʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁʰˤ")
		self.assertEqual(actual, expected)

	def test_ʁ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("ʁ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_χ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular fricative pulmonic egressive consonant"
		actual = describe_transcription("χ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless pharyngeal fricative pulmonic egressive consonant
	def test_ħ_is_the_representation_of_the_voiceless_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ")
		self.assertEqual(actual, expected)

	def test_ħ̊_is_the_representation_of_the_voiceless_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̊")
		self.assertEqual(actual, expected)

	def test_ħ̥_is_the_representation_of_the_voiceless_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̥")
		self.assertEqual(actual, expected)

	def test_ʕ̊_is_the_representation_of_the_voiceless_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊")
		self.assertEqual(actual, expected)

	def test_ʕ̥_is_the_representation_of_the_voiceless_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥")
		self.assertEqual(actual, expected)

# voiceless labialized pharyngeal fricative pulmonic egressive consonant
	def test_ħʷ_is_the_representation_of_the_voiceless_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʷ")
		self.assertEqual(actual, expected)

	def test_ħ̊ʷ_is_the_representation_of_the_voiceless_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ħ̥ʷ_is_the_representation_of_the_voiceless_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʷ_is_the_representation_of_the_voiceless_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʷ_is_the_representation_of_the_voiceless_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized pharyngeal fricative pulmonic egressive consonant
	def test_ħʲ_is_the_representation_of_the_voiceless_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʲ")
		self.assertEqual(actual, expected)

	def test_ħ̊ʲ_is_the_representation_of_the_voiceless_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ħ̥ʲ_is_the_representation_of_the_voiceless_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʲ_is_the_representation_of_the_voiceless_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʲ_is_the_representation_of_the_voiceless_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized pharyngeal fricative pulmonic egressive consonant
	def test_ħˠ_is_the_representation_of_the_voiceless_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħˠ")
		self.assertEqual(actual, expected)

	def test_ħ̊ˠ_is_the_representation_of_the_voiceless_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ħ̥ˠ_is_the_representation_of_the_voiceless_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ˠ_is_the_representation_of_the_voiceless_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ˠ_is_the_representation_of_the_voiceless_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized pharyngeal fricative pulmonic egressive consonant
	def test_ħˤ_is_the_representation_of_the_voiceless_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħˤ")
		self.assertEqual(actual, expected)

	def test_ħ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ħ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngeal fricative pulmonic egressive consonant
	def test_ħʰ_is_the_representation_of_the_voiceless_aspirated_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʰ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʰ_is_the_representation_of_the_voiceless_aspirated_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʰ_is_the_representation_of_the_voiceless_aspirated_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized pharyngeal fricative pulmonic egressive consonant
	def test_ħʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʰʷ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized pharyngeal fricative pulmonic egressive consonant
	def test_ħʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʰʲ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized pharyngeal fricative pulmonic egressive consonant
	def test_ħʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʰˠ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant
	def test_ħʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħʰˤ")
		self.assertEqual(actual, expected)

	def test_ʕ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʕ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced pharyngeal fricative pulmonic egressive consonant
	def test_ʕ_is_the_representation_of_the_voiced_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ")
		self.assertEqual(actual, expected)

	def test_ħ̬_is_the_representation_of_the_voiced_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬")
		self.assertEqual(actual, expected)

	def test_ħ̬_is_the_representation_of_the_voiced_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬")
		self.assertEqual(actual, expected)

# voiced labialized pharyngeal fricative pulmonic egressive consonant
	def test_ʕʷ_is_the_representation_of_the_voiced_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʷ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʷ_is_the_representation_of_the_voiced_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʷ_is_the_representation_of_the_voiced_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized pharyngeal fricative pulmonic egressive consonant
	def test_ʕʲ_is_the_representation_of_the_voiced_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʲ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʲ_is_the_representation_of_the_voiced_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʲ_is_the_representation_of_the_voiced_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized pharyngeal fricative pulmonic egressive consonant
	def test_ʕˠ_is_the_representation_of_the_voiced_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕˠ")
		self.assertEqual(actual, expected)

	def test_ħ̬ˠ_is_the_representation_of_the_voiced_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ħ̬ˠ_is_the_representation_of_the_voiced_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized pharyngeal fricative pulmonic egressive consonant
	def test_ʕˤ_is_the_representation_of_the_voiced_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕˤ")
		self.assertEqual(actual, expected)

	def test_ħ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ħ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngeal fricative pulmonic egressive consonant
	def test_ʕʰ_is_the_representation_of_the_voiced_aspirated_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʰ")
		self.assertEqual(actual, expected)

	def test_ʕ̬ʰ_is_the_representation_of_the_voiced_aspirated_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʰ_is_the_representation_of_the_voiced_aspirated_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized pharyngeal fricative pulmonic egressive consonant
	def test_ʕʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʰʷ")
		self.assertEqual(actual, expected)

	def test_ʕ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized pharyngeal fricative pulmonic egressive consonant
	def test_ʕʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʰʲ")
		self.assertEqual(actual, expected)

	def test_ʕ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized pharyngeal fricative pulmonic egressive consonant
	def test_ʕʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʰˠ")
		self.assertEqual(actual, expected)

	def test_ʕ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant
	def test_ʕʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕʰˤ")
		self.assertEqual(actual, expected)

	def test_ʕ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʕ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ħ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_pharyngeal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized pharyngeal fricative pulmonic egressive consonant"
		actual = describe_transcription("ħ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless glottal fricative pulmonic egressive consonant
	def test_h_is_the_representation_of_the_voiceless_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h")
		self.assertEqual(actual, expected)

	def test_h̊_is_the_representation_of_the_voiceless_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̊")
		self.assertEqual(actual, expected)

	def test_h̥_is_the_representation_of_the_voiceless_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̥")
		self.assertEqual(actual, expected)

	def test_ɦ̊_is_the_representation_of_the_voiceless_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊")
		self.assertEqual(actual, expected)

	def test_ɦ̥_is_the_representation_of_the_voiceless_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥")
		self.assertEqual(actual, expected)

# voiceless labialized glottal fricative pulmonic egressive consonant
	def test_hʷ_is_the_representation_of_the_voiceless_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʷ")
		self.assertEqual(actual, expected)

	def test_h̊ʷ_is_the_representation_of_the_voiceless_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̊ʷ")
		self.assertEqual(actual, expected)

	def test_h̥ʷ_is_the_representation_of_the_voiceless_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̥ʷ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʷ_is_the_representation_of_the_voiceless_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʷ_is_the_representation_of_the_voiceless_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized glottal fricative pulmonic egressive consonant
	def test_hʲ_is_the_representation_of_the_voiceless_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʲ")
		self.assertEqual(actual, expected)

	def test_h̊ʲ_is_the_representation_of_the_voiceless_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̊ʲ")
		self.assertEqual(actual, expected)

	def test_h̥ʲ_is_the_representation_of_the_voiceless_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̥ʲ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʲ_is_the_representation_of_the_voiceless_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʲ_is_the_representation_of_the_voiceless_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized glottal fricative pulmonic egressive consonant
	def test_hˠ_is_the_representation_of_the_voiceless_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hˠ")
		self.assertEqual(actual, expected)

	def test_h̊ˠ_is_the_representation_of_the_voiceless_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̊ˠ")
		self.assertEqual(actual, expected)

	def test_h̥ˠ_is_the_representation_of_the_voiceless_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̥ˠ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ˠ_is_the_representation_of_the_voiceless_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ˠ_is_the_representation_of_the_voiceless_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized glottal fricative pulmonic egressive consonant
	def test_hˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hˤ")
		self.assertEqual(actual, expected)

	def test_h̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̊ˤ")
		self.assertEqual(actual, expected)

	def test_h̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̥ˤ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated glottal fricative pulmonic egressive consonant
	def test_hʰ_is_the_representation_of_the_voiceless_aspirated_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʰ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʰ_is_the_representation_of_the_voiceless_aspirated_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʰ_is_the_representation_of_the_voiceless_aspirated_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized glottal fricative pulmonic egressive consonant
	def test_hʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʰʷ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized glottal fricative pulmonic egressive consonant
	def test_hʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʰʲ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized glottal fricative pulmonic egressive consonant
	def test_hʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʰˠ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized glottal fricative pulmonic egressive consonant
	def test_hʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("hʰˤ")
		self.assertEqual(actual, expected)

	def test_ɦ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɦ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced glottal fricative pulmonic egressive consonant
	def test_ɦ_is_the_representation_of_the_voiced_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ")
		self.assertEqual(actual, expected)

	def test_h̬_is_the_representation_of_the_voiced_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬")
		self.assertEqual(actual, expected)

	def test_h̬_is_the_representation_of_the_voiced_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬")
		self.assertEqual(actual, expected)

# voiced labialized glottal fricative pulmonic egressive consonant
	def test_ɦʷ_is_the_representation_of_the_voiced_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʷ")
		self.assertEqual(actual, expected)

	def test_h̬ʷ_is_the_representation_of_the_voiced_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʷ")
		self.assertEqual(actual, expected)

	def test_h̬ʷ_is_the_representation_of_the_voiced_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized glottal fricative pulmonic egressive consonant
	def test_ɦʲ_is_the_representation_of_the_voiced_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʲ")
		self.assertEqual(actual, expected)

	def test_h̬ʲ_is_the_representation_of_the_voiced_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʲ")
		self.assertEqual(actual, expected)

	def test_h̬ʲ_is_the_representation_of_the_voiced_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized glottal fricative pulmonic egressive consonant
	def test_ɦˠ_is_the_representation_of_the_voiced_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦˠ")
		self.assertEqual(actual, expected)

	def test_h̬ˠ_is_the_representation_of_the_voiced_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ˠ")
		self.assertEqual(actual, expected)

	def test_h̬ˠ_is_the_representation_of_the_voiced_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized glottal fricative pulmonic egressive consonant
	def test_ɦˤ_is_the_representation_of_the_voiced_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦˤ")
		self.assertEqual(actual, expected)

	def test_h̬ˤ_is_the_representation_of_the_voiced_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ˤ")
		self.assertEqual(actual, expected)

	def test_h̬ˤ_is_the_representation_of_the_voiced_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated glottal fricative pulmonic egressive consonant
	def test_ɦʰ_is_the_representation_of_the_voiced_aspirated_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʰ")
		self.assertEqual(actual, expected)

	def test_ɦ̬ʰ_is_the_representation_of_the_voiced_aspirated_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̬ʰ")
		self.assertEqual(actual, expected)

	def test_h̬ʰ_is_the_representation_of_the_voiced_aspirated_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized glottal fricative pulmonic egressive consonant
	def test_ɦʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʰʷ")
		self.assertEqual(actual, expected)

	def test_ɦ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_h̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized glottal fricative pulmonic egressive consonant
	def test_ɦʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʰʲ")
		self.assertEqual(actual, expected)

	def test_ɦ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_h̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized glottal fricative pulmonic egressive consonant
	def test_ɦʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʰˠ")
		self.assertEqual(actual, expected)

	def test_ɦ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_h̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized glottal fricative pulmonic egressive consonant
	def test_ɦʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦʰˤ")
		self.assertEqual(actual, expected)

	def test_ɦ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɦ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_h̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_glottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized glottal fricative pulmonic egressive consonant"
		actual = describe_transcription("h̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar lateral fricative pulmonic egressive consonant
	def test_ɬ_is_the_representation_of_the_voiceless_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ")
		self.assertEqual(actual, expected)

	def test_ɬ̊_is_the_representation_of_the_voiceless_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̊")
		self.assertEqual(actual, expected)

	def test_ɬ̥_is_the_representation_of_the_voiceless_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̥")
		self.assertEqual(actual, expected)

	def test_ɮ̊_is_the_representation_of_the_voiceless_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊")
		self.assertEqual(actual, expected)

	def test_ɮ̥_is_the_representation_of_the_voiceless_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʷ_is_the_representation_of_the_voiceless_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʷ")
		self.assertEqual(actual, expected)

	def test_ɬ̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɬ̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʲ")
		self.assertEqual(actual, expected)

	def test_ɬ̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɬ̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬˠ_is_the_representation_of_the_voiceless_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬˠ")
		self.assertEqual(actual, expected)

	def test_ɬ̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɬ̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬˤ")
		self.assertEqual(actual, expected)

	def test_ɬ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɬ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʰ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʰʷ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʰʲ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʰˠ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant
	def test_ɬʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬʰˤ")
		self.assertEqual(actual, expected)

	def test_ɮ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɮ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar lateral fricative pulmonic egressive consonant
	def test_ɮ_is_the_representation_of_the_voiced_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ")
		self.assertEqual(actual, expected)

	def test_ɬ̬_is_the_representation_of_the_voiced_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬")
		self.assertEqual(actual, expected)

	def test_ɬ̬_is_the_representation_of_the_voiced_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬")
		self.assertEqual(actual, expected)

# voiced labialized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʷ_is_the_representation_of_the_voiced_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʷ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʷ_is_the_representation_of_the_voiced_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʷ_is_the_representation_of_the_voiced_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʲ_is_the_representation_of_the_voiced_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʲ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮˠ_is_the_representation_of_the_voiced_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮˠ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ˠ_is_the_representation_of_the_voiced_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ˠ_is_the_representation_of_the_voiced_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮˤ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʰ_is_the_representation_of_the_voiced_aspirated_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʰ")
		self.assertEqual(actual, expected)

	def test_ɮ̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʰʷ")
		self.assertEqual(actual, expected)

	def test_ɮ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʰʲ")
		self.assertEqual(actual, expected)

	def test_ɮ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʰˠ")
		self.assertEqual(actual, expected)

	def test_ɮ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant
	def test_ɮʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮʰˤ")
		self.assertEqual(actual, expected)

	def test_ɮ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɮ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɬ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_lateral_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar lateral fricative pulmonic egressive consonant"
		actual = describe_transcription("ɬ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless bilabial nasal pulmonic egressive consonant
	def test_m̊_is_the_representation_of_the_voiceless_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊")
		self.assertEqual(actual, expected)

	def test_m̥_is_the_representation_of_the_voiceless_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥")
		self.assertEqual(actual, expected)

# voiceless labialized bilabial nasal pulmonic egressive consonant
	def test_m̊ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʷ")
		self.assertEqual(actual, expected)

	def test_m̥ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized bilabial nasal pulmonic egressive consonant
	def test_m̊ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʲ")
		self.assertEqual(actual, expected)

	def test_m̥ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized bilabial nasal pulmonic egressive consonant
	def test_m̊ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ˠ")
		self.assertEqual(actual, expected)

	def test_m̥ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized bilabial nasal pulmonic egressive consonant
	def test_m̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ˤ")
		self.assertEqual(actual, expected)

	def test_m̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated bilabial nasal pulmonic egressive consonant
	def test_m̥ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʰ")
		self.assertEqual(actual, expected)

	def test_m̊ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized bilabial nasal pulmonic egressive consonant
	def test_m̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_m̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized bilabial nasal pulmonic egressive consonant
	def test_m̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_m̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized bilabial nasal pulmonic egressive consonant
	def test_m̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_m̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized bilabial nasal pulmonic egressive consonant
	def test_m̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_m̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced bilabial nasal pulmonic egressive consonant
	def test_m_is_the_representation_of_the_voiced_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m")
		self.assertEqual(actual, expected)

# voiced labialized bilabial nasal pulmonic egressive consonant
	def test_mʷ_is_the_representation_of_the_voiced_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʷ")
		self.assertEqual(actual, expected)

# voiced palatalized bilabial nasal pulmonic egressive consonant
	def test_mʲ_is_the_representation_of_the_voiced_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʲ")
		self.assertEqual(actual, expected)

# voiced velarized bilabial nasal pulmonic egressive consonant
	def test_mˠ_is_the_representation_of_the_voiced_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized bilabial nasal pulmonic egressive consonant
	def test_mˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mˤ")
		self.assertEqual(actual, expected)

# voiced aspirated bilabial nasal pulmonic egressive consonant
	def test_mʰ_is_the_representation_of_the_voiced_aspirated_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʰ")
		self.assertEqual(actual, expected)

	def test_m̬ʰ_is_the_representation_of_the_voiced_aspirated_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized bilabial nasal pulmonic egressive consonant
	def test_mʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʰʷ")
		self.assertEqual(actual, expected)

	def test_m̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized bilabial nasal pulmonic egressive consonant
	def test_mʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʰʲ")
		self.assertEqual(actual, expected)

	def test_m̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized bilabial nasal pulmonic egressive consonant
	def test_mʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʰˠ")
		self.assertEqual(actual, expected)

	def test_m̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized bilabial nasal pulmonic egressive consonant
	def test_mʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("mʰˤ")
		self.assertEqual(actual, expected)

	def test_m̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial nasal pulmonic egressive consonant"
		actual = describe_transcription("m̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar nasal pulmonic egressive consonant
	def test_n̊_is_the_representation_of_the_voiceless_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊")
		self.assertEqual(actual, expected)

	def test_n̥_is_the_representation_of_the_voiceless_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar nasal pulmonic egressive consonant
	def test_n̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʷ")
		self.assertEqual(actual, expected)

	def test_n̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar nasal pulmonic egressive consonant
	def test_n̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʲ")
		self.assertEqual(actual, expected)

	def test_n̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar nasal pulmonic egressive consonant
	def test_n̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ˠ")
		self.assertEqual(actual, expected)

	def test_n̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar nasal pulmonic egressive consonant
	def test_n̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ˤ")
		self.assertEqual(actual, expected)

	def test_n̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar nasal pulmonic egressive consonant
	def test_n̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʰ")
		self.assertEqual(actual, expected)

	def test_n̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar nasal pulmonic egressive consonant
	def test_n̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_n̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar nasal pulmonic egressive consonant
	def test_n̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_n̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar nasal pulmonic egressive consonant
	def test_n̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_n̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar nasal pulmonic egressive consonant
	def test_n̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_n̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar nasal pulmonic egressive consonant
	def test_n_is_the_representation_of_the_voiced_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n")
		self.assertEqual(actual, expected)

# voiced labialized alveolar nasal pulmonic egressive consonant
	def test_nʷ_is_the_representation_of_the_voiced_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar nasal pulmonic egressive consonant
	def test_nʲ_is_the_representation_of_the_voiced_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar nasal pulmonic egressive consonant
	def test_nˠ_is_the_representation_of_the_voiced_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar nasal pulmonic egressive consonant
	def test_nˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar nasal pulmonic egressive consonant
	def test_nʰ_is_the_representation_of_the_voiced_aspirated_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʰ")
		self.assertEqual(actual, expected)

	def test_n̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar nasal pulmonic egressive consonant
	def test_nʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʰʷ")
		self.assertEqual(actual, expected)

	def test_n̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar nasal pulmonic egressive consonant
	def test_nʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʰʲ")
		self.assertEqual(actual, expected)

	def test_n̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar nasal pulmonic egressive consonant
	def test_nʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʰˠ")
		self.assertEqual(actual, expected)

	def test_n̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar nasal pulmonic egressive consonant
	def test_nʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("nʰˤ")
		self.assertEqual(actual, expected)

	def test_n̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar nasal pulmonic egressive consonant"
		actual = describe_transcription("n̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless palatal nasal pulmonic egressive consonant
	def test_ɲ̊_is_the_representation_of_the_voiceless_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊")
		self.assertEqual(actual, expected)

	def test_ɲ̥_is_the_representation_of_the_voiceless_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥")
		self.assertEqual(actual, expected)

# voiceless labialized palatal nasal pulmonic egressive consonant
	def test_ɲ̊ʷ_is_the_representation_of_the_voiceless_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɲ̥ʷ_is_the_representation_of_the_voiceless_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized palatal nasal pulmonic egressive consonant
	def test_ɲ̊ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɲ̥ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized palatal nasal pulmonic egressive consonant
	def test_ɲ̊ˠ_is_the_representation_of_the_voiceless_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɲ̥ˠ_is_the_representation_of_the_voiceless_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized palatal nasal pulmonic egressive consonant
	def test_ɲ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɲ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatal nasal pulmonic egressive consonant
	def test_ɲ̥ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɲ̊ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized palatal nasal pulmonic egressive consonant
	def test_ɲ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɲ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized palatal nasal pulmonic egressive consonant
	def test_ɲ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɲ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized palatal nasal pulmonic egressive consonant
	def test_ɲ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɲ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized palatal nasal pulmonic egressive consonant
	def test_ɲ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɲ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced palatal nasal pulmonic egressive consonant
	def test_ɲ_is_the_representation_of_the_voiced_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ")
		self.assertEqual(actual, expected)

# voiced labialized palatal nasal pulmonic egressive consonant
	def test_ɲʷ_is_the_representation_of_the_voiced_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʷ")
		self.assertEqual(actual, expected)

# voiced palatalized palatal nasal pulmonic egressive consonant
	def test_ɲʲ_is_the_representation_of_the_voiced_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʲ")
		self.assertEqual(actual, expected)

# voiced velarized palatal nasal pulmonic egressive consonant
	def test_ɲˠ_is_the_representation_of_the_voiced_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized palatal nasal pulmonic egressive consonant
	def test_ɲˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲˤ")
		self.assertEqual(actual, expected)

# voiced aspirated palatal nasal pulmonic egressive consonant
	def test_ɲʰ_is_the_representation_of_the_voiced_aspirated_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʰ")
		self.assertEqual(actual, expected)

	def test_ɲ̬ʰ_is_the_representation_of_the_voiced_aspirated_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized palatal nasal pulmonic egressive consonant
	def test_ɲʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʰʷ")
		self.assertEqual(actual, expected)

	def test_ɲ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized palatal nasal pulmonic egressive consonant
	def test_ɲʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʰʲ")
		self.assertEqual(actual, expected)

	def test_ɲ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized palatal nasal pulmonic egressive consonant
	def test_ɲʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʰˠ")
		self.assertEqual(actual, expected)

	def test_ɲ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized palatal nasal pulmonic egressive consonant
	def test_ɲʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲʰˤ")
		self.assertEqual(actual, expected)

	def test_ɲ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal nasal pulmonic egressive consonant"
		actual = describe_transcription("ɲ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless retroflex nasal pulmonic egressive consonant
	def test_ɳ̊_is_the_representation_of_the_voiceless_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊")
		self.assertEqual(actual, expected)

	def test_ɳ̥_is_the_representation_of_the_voiceless_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥")
		self.assertEqual(actual, expected)

# voiceless labialized retroflex nasal pulmonic egressive consonant
	def test_ɳ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɳ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized retroflex nasal pulmonic egressive consonant
	def test_ɳ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɳ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized retroflex nasal pulmonic egressive consonant
	def test_ɳ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɳ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized retroflex nasal pulmonic egressive consonant
	def test_ɳ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɳ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated retroflex nasal pulmonic egressive consonant
	def test_ɳ̥ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɳ̊ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized retroflex nasal pulmonic egressive consonant
	def test_ɳ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɳ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized retroflex nasal pulmonic egressive consonant
	def test_ɳ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɳ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized retroflex nasal pulmonic egressive consonant
	def test_ɳ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɳ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized retroflex nasal pulmonic egressive consonant
	def test_ɳ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɳ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced retroflex nasal pulmonic egressive consonant
	def test_ɳ_is_the_representation_of_the_voiced_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ")
		self.assertEqual(actual, expected)

# voiced labialized retroflex nasal pulmonic egressive consonant
	def test_ɳʷ_is_the_representation_of_the_voiced_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʷ")
		self.assertEqual(actual, expected)

# voiced palatalized retroflex nasal pulmonic egressive consonant
	def test_ɳʲ_is_the_representation_of_the_voiced_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʲ")
		self.assertEqual(actual, expected)

# voiced velarized retroflex nasal pulmonic egressive consonant
	def test_ɳˠ_is_the_representation_of_the_voiced_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized retroflex nasal pulmonic egressive consonant
	def test_ɳˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳˤ")
		self.assertEqual(actual, expected)

# voiced aspirated retroflex nasal pulmonic egressive consonant
	def test_ɳʰ_is_the_representation_of_the_voiced_aspirated_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʰ")
		self.assertEqual(actual, expected)

	def test_ɳ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized retroflex nasal pulmonic egressive consonant
	def test_ɳʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʰʷ")
		self.assertEqual(actual, expected)

	def test_ɳ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized retroflex nasal pulmonic egressive consonant
	def test_ɳʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʰʲ")
		self.assertEqual(actual, expected)

	def test_ɳ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized retroflex nasal pulmonic egressive consonant
	def test_ɳʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʰˠ")
		self.assertEqual(actual, expected)

	def test_ɳ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized retroflex nasal pulmonic egressive consonant
	def test_ɳʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳʰˤ")
		self.assertEqual(actual, expected)

	def test_ɳ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex nasal pulmonic egressive consonant"
		actual = describe_transcription("ɳ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless velar nasal pulmonic egressive consonant
	def test_ŋ̊_is_the_representation_of_the_voiceless_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊")
		self.assertEqual(actual, expected)

	def test_ŋ̥_is_the_representation_of_the_voiceless_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥")
		self.assertEqual(actual, expected)

# voiceless labialized velar nasal pulmonic egressive consonant
	def test_ŋ̊ʷ_is_the_representation_of_the_voiceless_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ŋ̥ʷ_is_the_representation_of_the_voiceless_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized velar nasal pulmonic egressive consonant
	def test_ŋ̊ʲ_is_the_representation_of_the_voiceless_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ŋ̥ʲ_is_the_representation_of_the_voiceless_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized velar nasal pulmonic egressive consonant
	def test_ŋ̊ˠ_is_the_representation_of_the_voiceless_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ŋ̥ˠ_is_the_representation_of_the_voiceless_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized velar nasal pulmonic egressive consonant
	def test_ŋ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ŋ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated velar nasal pulmonic egressive consonant
	def test_ŋ̥ʰ_is_the_representation_of_the_voiceless_aspirated_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ŋ̊ʰ_is_the_representation_of_the_voiceless_aspirated_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized velar nasal pulmonic egressive consonant
	def test_ŋ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ŋ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized velar nasal pulmonic egressive consonant
	def test_ŋ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ŋ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized velar nasal pulmonic egressive consonant
	def test_ŋ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ŋ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized velar nasal pulmonic egressive consonant
	def test_ŋ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ŋ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced velar nasal pulmonic egressive consonant
	def test_ŋ_is_the_representation_of_the_voiced_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ")
		self.assertEqual(actual, expected)

# voiced labialized velar nasal pulmonic egressive consonant
	def test_ŋʷ_is_the_representation_of_the_voiced_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʷ")
		self.assertEqual(actual, expected)

# voiced palatalized velar nasal pulmonic egressive consonant
	def test_ŋʲ_is_the_representation_of_the_voiced_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʲ")
		self.assertEqual(actual, expected)

# voiced velarized velar nasal pulmonic egressive consonant
	def test_ŋˠ_is_the_representation_of_the_voiced_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized velar nasal pulmonic egressive consonant
	def test_ŋˤ_is_the_representation_of_the_voiced_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋˤ")
		self.assertEqual(actual, expected)

# voiced aspirated velar nasal pulmonic egressive consonant
	def test_ŋʰ_is_the_representation_of_the_voiced_aspirated_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʰ")
		self.assertEqual(actual, expected)

	def test_ŋ̬ʰ_is_the_representation_of_the_voiced_aspirated_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized velar nasal pulmonic egressive consonant
	def test_ŋʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʰʷ")
		self.assertEqual(actual, expected)

	def test_ŋ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized velar nasal pulmonic egressive consonant
	def test_ŋʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʰʲ")
		self.assertEqual(actual, expected)

	def test_ŋ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized velar nasal pulmonic egressive consonant
	def test_ŋʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʰˠ")
		self.assertEqual(actual, expected)

	def test_ŋ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized velar nasal pulmonic egressive consonant
	def test_ŋʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋʰˤ")
		self.assertEqual(actual, expected)

	def test_ŋ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar nasal pulmonic egressive consonant"
		actual = describe_transcription("ŋ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless uvular nasal pulmonic egressive consonant
	def test_ɴ̊_is_the_representation_of_the_voiceless_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊")
		self.assertEqual(actual, expected)

	def test_ɴ̥_is_the_representation_of_the_voiceless_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥")
		self.assertEqual(actual, expected)

# voiceless labialized uvular nasal pulmonic egressive consonant
	def test_ɴ̊ʷ_is_the_representation_of_the_voiceless_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɴ̥ʷ_is_the_representation_of_the_voiceless_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized uvular nasal pulmonic egressive consonant
	def test_ɴ̊ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɴ̥ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized uvular nasal pulmonic egressive consonant
	def test_ɴ̊ˠ_is_the_representation_of_the_voiceless_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɴ̥ˠ_is_the_representation_of_the_voiceless_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized uvular nasal pulmonic egressive consonant
	def test_ɴ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɴ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated uvular nasal pulmonic egressive consonant
	def test_ɴ̥ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɴ̊ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized uvular nasal pulmonic egressive consonant
	def test_ɴ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɴ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized uvular nasal pulmonic egressive consonant
	def test_ɴ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɴ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized uvular nasal pulmonic egressive consonant
	def test_ɴ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɴ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized uvular nasal pulmonic egressive consonant
	def test_ɴ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɴ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced uvular nasal pulmonic egressive consonant
	def test_ɴ_is_the_representation_of_the_voiced_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ")
		self.assertEqual(actual, expected)

# voiced labialized uvular nasal pulmonic egressive consonant
	def test_ɴʷ_is_the_representation_of_the_voiced_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʷ")
		self.assertEqual(actual, expected)

# voiced palatalized uvular nasal pulmonic egressive consonant
	def test_ɴʲ_is_the_representation_of_the_voiced_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʲ")
		self.assertEqual(actual, expected)

# voiced velarized uvular nasal pulmonic egressive consonant
	def test_ɴˠ_is_the_representation_of_the_voiced_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized uvular nasal pulmonic egressive consonant
	def test_ɴˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴˤ")
		self.assertEqual(actual, expected)

# voiced aspirated uvular nasal pulmonic egressive consonant
	def test_ɴʰ_is_the_representation_of_the_voiced_aspirated_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʰ")
		self.assertEqual(actual, expected)

	def test_ɴ̬ʰ_is_the_representation_of_the_voiced_aspirated_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized uvular nasal pulmonic egressive consonant
	def test_ɴʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʰʷ")
		self.assertEqual(actual, expected)

	def test_ɴ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized uvular nasal pulmonic egressive consonant
	def test_ɴʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʰʲ")
		self.assertEqual(actual, expected)

	def test_ɴ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized uvular nasal pulmonic egressive consonant
	def test_ɴʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʰˠ")
		self.assertEqual(actual, expected)

	def test_ɴ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized uvular nasal pulmonic egressive consonant
	def test_ɴʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴʰˤ")
		self.assertEqual(actual, expected)

	def test_ɴ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_nasal_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular nasal pulmonic egressive consonant"
		actual = describe_transcription("ɴ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless bilabial trill pulmonic egressive consonant
	def test_ʙ̊_is_the_representation_of_the_voiceless_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊")
		self.assertEqual(actual, expected)

	def test_ʙ̥_is_the_representation_of_the_voiceless_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥")
		self.assertEqual(actual, expected)

# voiceless labialized bilabial trill pulmonic egressive consonant
	def test_ʙ̊ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʙ̥ʷ_is_the_representation_of_the_voiceless_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized bilabial trill pulmonic egressive consonant
	def test_ʙ̊ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʙ̥ʲ_is_the_representation_of_the_voiceless_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized bilabial trill pulmonic egressive consonant
	def test_ʙ̊ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʙ̥ˠ_is_the_representation_of_the_voiceless_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized bilabial trill pulmonic egressive consonant
	def test_ʙ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʙ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated bilabial trill pulmonic egressive consonant
	def test_ʙ̥ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʙ̊ʰ_is_the_representation_of_the_voiceless_aspirated_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized bilabial trill pulmonic egressive consonant
	def test_ʙ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʙ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized bilabial trill pulmonic egressive consonant
	def test_ʙ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʙ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized bilabial trill pulmonic egressive consonant
	def test_ʙ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʙ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized bilabial trill pulmonic egressive consonant
	def test_ʙ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʙ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced bilabial trill pulmonic egressive consonant
	def test_ʙ_is_the_representation_of_the_voiced_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ")
		self.assertEqual(actual, expected)

# voiced labialized bilabial trill pulmonic egressive consonant
	def test_ʙʷ_is_the_representation_of_the_voiced_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʷ")
		self.assertEqual(actual, expected)

# voiced palatalized bilabial trill pulmonic egressive consonant
	def test_ʙʲ_is_the_representation_of_the_voiced_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʲ")
		self.assertEqual(actual, expected)

# voiced velarized bilabial trill pulmonic egressive consonant
	def test_ʙˠ_is_the_representation_of_the_voiced_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized bilabial trill pulmonic egressive consonant
	def test_ʙˤ_is_the_representation_of_the_voiced_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙˤ")
		self.assertEqual(actual, expected)

# voiced aspirated bilabial trill pulmonic egressive consonant
	def test_ʙʰ_is_the_representation_of_the_voiced_aspirated_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʰ")
		self.assertEqual(actual, expected)

	def test_ʙ̬ʰ_is_the_representation_of_the_voiced_aspirated_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized bilabial trill pulmonic egressive consonant
	def test_ʙʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʰʷ")
		self.assertEqual(actual, expected)

	def test_ʙ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized bilabial trill pulmonic egressive consonant
	def test_ʙʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʰʲ")
		self.assertEqual(actual, expected)

	def test_ʙ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized bilabial trill pulmonic egressive consonant
	def test_ʙʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʰˠ")
		self.assertEqual(actual, expected)

	def test_ʙ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized bilabial trill pulmonic egressive consonant
	def test_ʙʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙʰˤ")
		self.assertEqual(actual, expected)

	def test_ʙ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_bilabial_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized bilabial trill pulmonic egressive consonant"
		actual = describe_transcription("ʙ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar trill pulmonic egressive consonant
	def test_r̊_is_the_representation_of_the_voiceless_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊")
		self.assertEqual(actual, expected)

	def test_r̥_is_the_representation_of_the_voiceless_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar trill pulmonic egressive consonant
	def test_r̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʷ")
		self.assertEqual(actual, expected)

	def test_r̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar trill pulmonic egressive consonant
	def test_r̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʲ")
		self.assertEqual(actual, expected)

	def test_r̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar trill pulmonic egressive consonant
	def test_r̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ˠ")
		self.assertEqual(actual, expected)

	def test_r̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar trill pulmonic egressive consonant
	def test_r̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ˤ")
		self.assertEqual(actual, expected)

	def test_r̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar trill pulmonic egressive consonant
	def test_r̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʰ")
		self.assertEqual(actual, expected)

	def test_r̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar trill pulmonic egressive consonant
	def test_r̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_r̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar trill pulmonic egressive consonant
	def test_r̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_r̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar trill pulmonic egressive consonant
	def test_r̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_r̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar trill pulmonic egressive consonant
	def test_r̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_r̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar trill pulmonic egressive consonant
	def test_r_is_the_representation_of_the_voiced_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r")
		self.assertEqual(actual, expected)

# voiced labialized alveolar trill pulmonic egressive consonant
	def test_rʷ_is_the_representation_of_the_voiced_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar trill pulmonic egressive consonant
	def test_rʲ_is_the_representation_of_the_voiced_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar trill pulmonic egressive consonant
	def test_rˠ_is_the_representation_of_the_voiced_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar trill pulmonic egressive consonant
	def test_rˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar trill pulmonic egressive consonant
	def test_rʰ_is_the_representation_of_the_voiced_aspirated_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʰ")
		self.assertEqual(actual, expected)

	def test_r̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar trill pulmonic egressive consonant
	def test_rʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʰʷ")
		self.assertEqual(actual, expected)

	def test_r̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar trill pulmonic egressive consonant
	def test_rʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʰʲ")
		self.assertEqual(actual, expected)

	def test_r̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar trill pulmonic egressive consonant
	def test_rʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʰˠ")
		self.assertEqual(actual, expected)

	def test_r̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar trill pulmonic egressive consonant
	def test_rʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("rʰˤ")
		self.assertEqual(actual, expected)

	def test_r̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar trill pulmonic egressive consonant"
		actual = describe_transcription("r̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless uvular trill pulmonic egressive consonant
	def test_ʀ̊_is_the_representation_of_the_voiceless_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊")
		self.assertEqual(actual, expected)

	def test_ʀ̥_is_the_representation_of_the_voiceless_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥")
		self.assertEqual(actual, expected)

# voiceless labialized uvular trill pulmonic egressive consonant
	def test_ʀ̊ʷ_is_the_representation_of_the_voiceless_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʀ̥ʷ_is_the_representation_of_the_voiceless_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized uvular trill pulmonic egressive consonant
	def test_ʀ̊ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʀ̥ʲ_is_the_representation_of_the_voiceless_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized uvular trill pulmonic egressive consonant
	def test_ʀ̊ˠ_is_the_representation_of_the_voiceless_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʀ̥ˠ_is_the_representation_of_the_voiceless_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized uvular trill pulmonic egressive consonant
	def test_ʀ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʀ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated uvular trill pulmonic egressive consonant
	def test_ʀ̥ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʀ̊ʰ_is_the_representation_of_the_voiceless_aspirated_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized uvular trill pulmonic egressive consonant
	def test_ʀ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʀ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized uvular trill pulmonic egressive consonant
	def test_ʀ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʀ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized uvular trill pulmonic egressive consonant
	def test_ʀ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʀ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized uvular trill pulmonic egressive consonant
	def test_ʀ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʀ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced uvular trill pulmonic egressive consonant
	def test_ʀ_is_the_representation_of_the_voiced_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ")
		self.assertEqual(actual, expected)

# voiced labialized uvular trill pulmonic egressive consonant
	def test_ʀʷ_is_the_representation_of_the_voiced_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʷ")
		self.assertEqual(actual, expected)

# voiced palatalized uvular trill pulmonic egressive consonant
	def test_ʀʲ_is_the_representation_of_the_voiced_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʲ")
		self.assertEqual(actual, expected)

# voiced velarized uvular trill pulmonic egressive consonant
	def test_ʀˠ_is_the_representation_of_the_voiced_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized uvular trill pulmonic egressive consonant
	def test_ʀˤ_is_the_representation_of_the_voiced_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀˤ")
		self.assertEqual(actual, expected)

# voiced aspirated uvular trill pulmonic egressive consonant
	def test_ʀʰ_is_the_representation_of_the_voiced_aspirated_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʰ")
		self.assertEqual(actual, expected)

	def test_ʀ̬ʰ_is_the_representation_of_the_voiced_aspirated_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized uvular trill pulmonic egressive consonant
	def test_ʀʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʰʷ")
		self.assertEqual(actual, expected)

	def test_ʀ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized uvular trill pulmonic egressive consonant
	def test_ʀʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʰʲ")
		self.assertEqual(actual, expected)

	def test_ʀ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized uvular trill pulmonic egressive consonant
	def test_ʀʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʰˠ")
		self.assertEqual(actual, expected)

	def test_ʀ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized uvular trill pulmonic egressive consonant
	def test_ʀʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀʰˤ")
		self.assertEqual(actual, expected)

	def test_ʀ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_uvular_trill_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized uvular trill pulmonic egressive consonant"
		actual = describe_transcription("ʀ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̊_is_the_representation_of_the_voiceless_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊")
		self.assertEqual(actual, expected)

	def test_ⱱ̥_is_the_representation_of_the_voiceless_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥")
		self.assertEqual(actual, expected)

# voiceless labialized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̊ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ⱱ̥ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̊ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ⱱ̥ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̊ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ⱱ̥ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ⱱ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̥ʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ⱱ̊ʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ⱱ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ⱱ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ⱱ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ⱱ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱ_is_the_representation_of_the_voiced_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ")
		self.assertEqual(actual, expected)

# voiced labialized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʷ_is_the_representation_of_the_voiced_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʷ")
		self.assertEqual(actual, expected)

# voiced palatalized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʲ_is_the_representation_of_the_voiced_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʲ")
		self.assertEqual(actual, expected)

# voiced velarized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱˠ_is_the_representation_of_the_voiced_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱˤ_is_the_representation_of_the_voiced_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱˤ")
		self.assertEqual(actual, expected)

# voiced aspirated labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʰ")
		self.assertEqual(actual, expected)

	def test_ⱱ̬ʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʰʷ")
		self.assertEqual(actual, expected)

	def test_ⱱ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʰʲ")
		self.assertEqual(actual, expected)

	def test_ⱱ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʰˠ")
		self.assertEqual(actual, expected)

	def test_ⱱ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized labio-dental tap or flap pulmonic egressive consonant
	def test_ⱱʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱʰˤ")
		self.assertEqual(actual, expected)

	def test_ⱱ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ⱱ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̊_is_the_representation_of_the_voiceless_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊")
		self.assertEqual(actual, expected)

	def test_ɾ̥_is_the_representation_of_the_voiceless_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɾ̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɾ̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɾ̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɾ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɾ̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɾ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɾ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɾ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar tap or flap pulmonic egressive consonant
	def test_ɾ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɾ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar tap or flap pulmonic egressive consonant
	def test_ɾ_is_the_representation_of_the_voiced_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ")
		self.assertEqual(actual, expected)

# voiced labialized alveolar tap or flap pulmonic egressive consonant
	def test_ɾʷ_is_the_representation_of_the_voiced_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar tap or flap pulmonic egressive consonant
	def test_ɾʲ_is_the_representation_of_the_voiced_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar tap or flap pulmonic egressive consonant
	def test_ɾˠ_is_the_representation_of_the_voiced_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar tap or flap pulmonic egressive consonant
	def test_ɾˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar tap or flap pulmonic egressive consonant
	def test_ɾʰ_is_the_representation_of_the_voiced_aspirated_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʰ")
		self.assertEqual(actual, expected)

	def test_ɾ̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar tap or flap pulmonic egressive consonant
	def test_ɾʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʰʷ")
		self.assertEqual(actual, expected)

	def test_ɾ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar tap or flap pulmonic egressive consonant
	def test_ɾʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʰʲ")
		self.assertEqual(actual, expected)

	def test_ɾ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar tap or flap pulmonic egressive consonant
	def test_ɾʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʰˠ")
		self.assertEqual(actual, expected)

	def test_ɾ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar tap or flap pulmonic egressive consonant
	def test_ɾʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾʰˤ")
		self.assertEqual(actual, expected)

	def test_ɾ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɾ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̊_is_the_representation_of_the_voiceless_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊")
		self.assertEqual(actual, expected)

	def test_ɽ̥_is_the_representation_of_the_voiceless_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥")
		self.assertEqual(actual, expected)

# voiceless labialized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɽ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɽ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɽ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɽ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̥ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɽ̊ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɽ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɽ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɽ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized retroflex tap or flap pulmonic egressive consonant
	def test_ɽ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɽ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced retroflex tap or flap pulmonic egressive consonant
	def test_ɽ_is_the_representation_of_the_voiced_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ")
		self.assertEqual(actual, expected)

# voiced labialized retroflex tap or flap pulmonic egressive consonant
	def test_ɽʷ_is_the_representation_of_the_voiced_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʷ")
		self.assertEqual(actual, expected)

# voiced palatalized retroflex tap or flap pulmonic egressive consonant
	def test_ɽʲ_is_the_representation_of_the_voiced_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʲ")
		self.assertEqual(actual, expected)

# voiced velarized retroflex tap or flap pulmonic egressive consonant
	def test_ɽˠ_is_the_representation_of_the_voiced_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized retroflex tap or flap pulmonic egressive consonant
	def test_ɽˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽˤ")
		self.assertEqual(actual, expected)

# voiced aspirated retroflex tap or flap pulmonic egressive consonant
	def test_ɽʰ_is_the_representation_of_the_voiced_aspirated_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʰ")
		self.assertEqual(actual, expected)

	def test_ɽ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized retroflex tap or flap pulmonic egressive consonant
	def test_ɽʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʰʷ")
		self.assertEqual(actual, expected)

	def test_ɽ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized retroflex tap or flap pulmonic egressive consonant
	def test_ɽʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʰʲ")
		self.assertEqual(actual, expected)

	def test_ɽ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized retroflex tap or flap pulmonic egressive consonant
	def test_ɽʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʰˠ")
		self.assertEqual(actual, expected)

	def test_ɽ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized retroflex tap or flap pulmonic egressive consonant
	def test_ɽʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽʰˤ")
		self.assertEqual(actual, expected)

	def test_ɽ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_tap_or_flap_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex tap or flap pulmonic egressive consonant"
		actual = describe_transcription("ɽ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless labio-dental approximant pulmonic egressive consonant
	def test_ʋ̊_is_the_representation_of_the_voiceless_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊")
		self.assertEqual(actual, expected)

	def test_ʋ̥_is_the_representation_of_the_voiceless_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥")
		self.assertEqual(actual, expected)

# voiceless labialized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̊ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʋ̥ʷ_is_the_representation_of_the_voiceless_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̊ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʋ̥ʲ_is_the_representation_of_the_voiceless_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̊ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʋ̥ˠ_is_the_representation_of_the_voiceless_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʋ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated labio-dental approximant pulmonic egressive consonant
	def test_ʋ̥ʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʋ̊ʰ_is_the_representation_of_the_voiceless_aspirated_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʋ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʋ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʋ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized labio-dental approximant pulmonic egressive consonant
	def test_ʋ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʋ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced labio-dental approximant pulmonic egressive consonant
	def test_ʋ_is_the_representation_of_the_voiced_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ")
		self.assertEqual(actual, expected)

# voiced labialized labio-dental approximant pulmonic egressive consonant
	def test_ʋʷ_is_the_representation_of_the_voiced_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʷ")
		self.assertEqual(actual, expected)

# voiced palatalized labio-dental approximant pulmonic egressive consonant
	def test_ʋʲ_is_the_representation_of_the_voiced_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʲ")
		self.assertEqual(actual, expected)

# voiced velarized labio-dental approximant pulmonic egressive consonant
	def test_ʋˠ_is_the_representation_of_the_voiced_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized labio-dental approximant pulmonic egressive consonant
	def test_ʋˤ_is_the_representation_of_the_voiced_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋˤ")
		self.assertEqual(actual, expected)

# voiced aspirated labio-dental approximant pulmonic egressive consonant
	def test_ʋʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʰ")
		self.assertEqual(actual, expected)

	def test_ʋ̬ʰ_is_the_representation_of_the_voiced_aspirated_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized labio-dental approximant pulmonic egressive consonant
	def test_ʋʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʰʷ")
		self.assertEqual(actual, expected)

	def test_ʋ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized labio-dental approximant pulmonic egressive consonant
	def test_ʋʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʰʲ")
		self.assertEqual(actual, expected)

	def test_ʋ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized labio-dental approximant pulmonic egressive consonant
	def test_ʋʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʰˠ")
		self.assertEqual(actual, expected)

	def test_ʋ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized labio-dental approximant pulmonic egressive consonant
	def test_ʋʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋʰˤ")
		self.assertEqual(actual, expected)

	def test_ʋ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labio_dental_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labio-dental approximant pulmonic egressive consonant"
		actual = describe_transcription("ʋ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolar approximant pulmonic egressive consonant
	def test_ɹ̊_is_the_representation_of_the_voiceless_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊")
		self.assertEqual(actual, expected)

	def test_ɹ̥_is_the_representation_of_the_voiceless_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolar approximant pulmonic egressive consonant
	def test_ɹ̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɹ̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolar approximant pulmonic egressive consonant
	def test_ɹ̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɹ̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolar approximant pulmonic egressive consonant
	def test_ɹ̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɹ̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolar approximant pulmonic egressive consonant
	def test_ɹ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɹ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolar approximant pulmonic egressive consonant
	def test_ɹ̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɹ̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolar approximant pulmonic egressive consonant
	def test_ɹ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɹ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolar approximant pulmonic egressive consonant
	def test_ɹ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɹ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolar approximant pulmonic egressive consonant
	def test_ɹ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɹ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolar approximant pulmonic egressive consonant
	def test_ɹ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɹ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolar approximant pulmonic egressive consonant
	def test_ɹ_is_the_representation_of_the_voiced_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ")
		self.assertEqual(actual, expected)

# voiced labialized alveolar approximant pulmonic egressive consonant
	def test_ɹʷ_is_the_representation_of_the_voiced_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolar approximant pulmonic egressive consonant
	def test_ɹʲ_is_the_representation_of_the_voiced_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolar approximant pulmonic egressive consonant
	def test_ɹˠ_is_the_representation_of_the_voiced_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolar approximant pulmonic egressive consonant
	def test_ɹˤ_is_the_representation_of_the_voiced_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolar approximant pulmonic egressive consonant
	def test_ɹʰ_is_the_representation_of_the_voiced_aspirated_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʰ")
		self.assertEqual(actual, expected)

	def test_ɹ̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolar approximant pulmonic egressive consonant
	def test_ɹʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʰʷ")
		self.assertEqual(actual, expected)

	def test_ɹ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolar approximant pulmonic egressive consonant
	def test_ɹʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʰʲ")
		self.assertEqual(actual, expected)

	def test_ɹ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolar approximant pulmonic egressive consonant
	def test_ɹʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʰˠ")
		self.assertEqual(actual, expected)

	def test_ɹ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolar approximant pulmonic egressive consonant
	def test_ɹʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹʰˤ")
		self.assertEqual(actual, expected)

	def test_ɹ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolar approximant pulmonic egressive consonant"
		actual = describe_transcription("ɹ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̊_is_the_representation_of_the_voiceless_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊")
		self.assertEqual(actual, expected)

	def test_ɭ̥_is_the_representation_of_the_voiceless_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥")
		self.assertEqual(actual, expected)

# voiceless labialized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̊ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɭ̥ʷ_is_the_representation_of_the_voiceless_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̊ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɭ̥ʲ_is_the_representation_of_the_voiceless_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̊ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɭ̥ˠ_is_the_representation_of_the_voiceless_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɭ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̥ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ɭ̊ʰ_is_the_representation_of_the_voiceless_aspirated_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɭ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɭ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɭ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɭ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced retroflex lateral approximant pulmonic egressive consonant
	def test_ɭ_is_the_representation_of_the_voiced_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ")
		self.assertEqual(actual, expected)

# voiced labialized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʷ_is_the_representation_of_the_voiced_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʷ")
		self.assertEqual(actual, expected)

# voiced palatalized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʲ_is_the_representation_of_the_voiced_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʲ")
		self.assertEqual(actual, expected)

# voiced velarized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭˠ_is_the_representation_of_the_voiced_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭˤ_is_the_representation_of_the_voiced_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭˤ")
		self.assertEqual(actual, expected)

# voiced aspirated retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʰ_is_the_representation_of_the_voiced_aspirated_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʰ")
		self.assertEqual(actual, expected)

	def test_ɭ̬ʰ_is_the_representation_of_the_voiced_aspirated_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʰʷ")
		self.assertEqual(actual, expected)

	def test_ɭ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʰʲ")
		self.assertEqual(actual, expected)

	def test_ɭ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʰˠ")
		self.assertEqual(actual, expected)

	def test_ɭ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized retroflex lateral approximant pulmonic egressive consonant
	def test_ɭʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭʰˤ")
		self.assertEqual(actual, expected)

	def test_ɭ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_retroflex_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized retroflex lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ɭ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̊_is_the_representation_of_the_voiceless_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊")
		self.assertEqual(actual, expected)

	def test_ʎ̥_is_the_representation_of_the_voiceless_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥")
		self.assertEqual(actual, expected)

# voiceless labialized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̊ʷ_is_the_representation_of_the_voiceless_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʎ̥ʷ_is_the_representation_of_the_voiceless_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̊ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʎ̥ʲ_is_the_representation_of_the_voiceless_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̊ˠ_is_the_representation_of_the_voiceless_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʎ̥ˠ_is_the_representation_of_the_voiceless_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʎ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̥ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʎ̊ʰ_is_the_representation_of_the_voiceless_aspirated_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʎ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʎ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʎ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized palatal lateral approximant pulmonic egressive consonant
	def test_ʎ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʎ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced palatal lateral approximant pulmonic egressive consonant
	def test_ʎ_is_the_representation_of_the_voiced_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ")
		self.assertEqual(actual, expected)

# voiced labialized palatal lateral approximant pulmonic egressive consonant
	def test_ʎʷ_is_the_representation_of_the_voiced_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʷ")
		self.assertEqual(actual, expected)

# voiced palatalized palatal lateral approximant pulmonic egressive consonant
	def test_ʎʲ_is_the_representation_of_the_voiced_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʲ")
		self.assertEqual(actual, expected)

# voiced velarized palatal lateral approximant pulmonic egressive consonant
	def test_ʎˠ_is_the_representation_of_the_voiced_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized palatal lateral approximant pulmonic egressive consonant
	def test_ʎˤ_is_the_representation_of_the_voiced_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎˤ")
		self.assertEqual(actual, expected)

# voiced aspirated palatal lateral approximant pulmonic egressive consonant
	def test_ʎʰ_is_the_representation_of_the_voiced_aspirated_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʰ")
		self.assertEqual(actual, expected)

	def test_ʎ̬ʰ_is_the_representation_of_the_voiced_aspirated_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized palatal lateral approximant pulmonic egressive consonant
	def test_ʎʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʰʷ")
		self.assertEqual(actual, expected)

	def test_ʎ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized palatal lateral approximant pulmonic egressive consonant
	def test_ʎʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʰʲ")
		self.assertEqual(actual, expected)

	def test_ʎ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized palatal lateral approximant pulmonic egressive consonant
	def test_ʎʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʰˠ")
		self.assertEqual(actual, expected)

	def test_ʎ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized palatal lateral approximant pulmonic egressive consonant
	def test_ʎʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎʰˤ")
		self.assertEqual(actual, expected)

	def test_ʎ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_palatal_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized palatal lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʎ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless velar lateral approximant pulmonic egressive consonant
	def test_ʟ̊_is_the_representation_of_the_voiceless_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊")
		self.assertEqual(actual, expected)

	def test_ʟ̥_is_the_representation_of_the_voiceless_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥")
		self.assertEqual(actual, expected)

# voiceless labialized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̊ʷ_is_the_representation_of_the_voiceless_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʟ̥ʷ_is_the_representation_of_the_voiceless_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̊ʲ_is_the_representation_of_the_voiceless_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʟ̥ʲ_is_the_representation_of_the_voiceless_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̊ˠ_is_the_representation_of_the_voiceless_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʟ̥ˠ_is_the_representation_of_the_voiceless_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʟ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated velar lateral approximant pulmonic egressive consonant
	def test_ʟ̥ʰ_is_the_representation_of_the_voiceless_aspirated_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʟ̊ʰ_is_the_representation_of_the_voiceless_aspirated_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʟ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʟ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʟ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized velar lateral approximant pulmonic egressive consonant
	def test_ʟ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʟ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced velar lateral approximant pulmonic egressive consonant
	def test_ʟ_is_the_representation_of_the_voiced_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ")
		self.assertEqual(actual, expected)

# voiced labialized velar lateral approximant pulmonic egressive consonant
	def test_ʟʷ_is_the_representation_of_the_voiced_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʷ")
		self.assertEqual(actual, expected)

# voiced palatalized velar lateral approximant pulmonic egressive consonant
	def test_ʟʲ_is_the_representation_of_the_voiced_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʲ")
		self.assertEqual(actual, expected)

# voiced velarized velar lateral approximant pulmonic egressive consonant
	def test_ʟˠ_is_the_representation_of_the_voiced_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized velar lateral approximant pulmonic egressive consonant
	def test_ʟˤ_is_the_representation_of_the_voiced_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟˤ")
		self.assertEqual(actual, expected)

# voiced aspirated velar lateral approximant pulmonic egressive consonant
	def test_ʟʰ_is_the_representation_of_the_voiced_aspirated_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʰ")
		self.assertEqual(actual, expected)

	def test_ʟ̬ʰ_is_the_representation_of_the_voiced_aspirated_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized velar lateral approximant pulmonic egressive consonant
	def test_ʟʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʰʷ")
		self.assertEqual(actual, expected)

	def test_ʟ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized velar lateral approximant pulmonic egressive consonant
	def test_ʟʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʰʲ")
		self.assertEqual(actual, expected)

	def test_ʟ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized velar lateral approximant pulmonic egressive consonant
	def test_ʟʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʰˠ")
		self.assertEqual(actual, expected)

	def test_ʟ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized velar lateral approximant pulmonic egressive consonant
	def test_ʟʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟʰˤ")
		self.assertEqual(actual, expected)

	def test_ʟ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_velar_lateral_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized velar lateral approximant pulmonic egressive consonant"
		actual = describe_transcription("ʟ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless labial-velar approximant pulmonic egressive consonant
	def test_ẘ_is_the_representation_of_the_voiceless_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘ")
		self.assertEqual(actual, expected)

	def test_w̥_is_the_representation_of_the_voiceless_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥")
		self.assertEqual(actual, expected)

# voiceless labialized labial-velar approximant pulmonic egressive consonant
	def test_ẘʷ_is_the_representation_of_the_voiceless_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʷ")
		self.assertEqual(actual, expected)

	def test_w̥ʷ_is_the_representation_of_the_voiceless_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized labial-velar approximant pulmonic egressive consonant
	def test_ẘʲ_is_the_representation_of_the_voiceless_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʲ")
		self.assertEqual(actual, expected)

	def test_w̥ʲ_is_the_representation_of_the_voiceless_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized labial-velar approximant pulmonic egressive consonant
	def test_ẘˠ_is_the_representation_of_the_voiceless_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘˠ")
		self.assertEqual(actual, expected)

	def test_w̥ˠ_is_the_representation_of_the_voiceless_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized labial-velar approximant pulmonic egressive consonant
	def test_ẘˤ_is_the_representation_of_the_voiceless_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘˤ")
		self.assertEqual(actual, expected)

	def test_w̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated labial-velar approximant pulmonic egressive consonant
	def test_w̥ʰ_is_the_representation_of_the_voiceless_aspirated_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʰ")
		self.assertEqual(actual, expected)

	def test_ẘʰ_is_the_representation_of_the_voiceless_aspirated_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized labial-velar approximant pulmonic egressive consonant
	def test_w̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ẘʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized labial-velar approximant pulmonic egressive consonant
	def test_w̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ẘʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized labial-velar approximant pulmonic egressive consonant
	def test_w̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ẘʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized labial-velar approximant pulmonic egressive consonant
	def test_w̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ẘʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("ẘʰˤ")
		self.assertEqual(actual, expected)

# voiced labial-velar approximant pulmonic egressive consonant
	def test_w_is_the_representation_of_the_voiced_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w")
		self.assertEqual(actual, expected)

# voiced labialized labial-velar approximant pulmonic egressive consonant
	def test_wʷ_is_the_representation_of_the_voiced_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʷ")
		self.assertEqual(actual, expected)

# voiced palatalized labial-velar approximant pulmonic egressive consonant
	def test_wʲ_is_the_representation_of_the_voiced_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʲ")
		self.assertEqual(actual, expected)

# voiced velarized labial-velar approximant pulmonic egressive consonant
	def test_wˠ_is_the_representation_of_the_voiced_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized labial-velar approximant pulmonic egressive consonant
	def test_wˤ_is_the_representation_of_the_voiced_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wˤ")
		self.assertEqual(actual, expected)

# voiced aspirated labial-velar approximant pulmonic egressive consonant
	def test_wʰ_is_the_representation_of_the_voiced_aspirated_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʰ")
		self.assertEqual(actual, expected)

	def test_w̬ʰ_is_the_representation_of_the_voiced_aspirated_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized labial-velar approximant pulmonic egressive consonant
	def test_wʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʰʷ")
		self.assertEqual(actual, expected)

	def test_w̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized labial-velar approximant pulmonic egressive consonant
	def test_wʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʰʲ")
		self.assertEqual(actual, expected)

	def test_w̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized labial-velar approximant pulmonic egressive consonant
	def test_wʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʰˠ")
		self.assertEqual(actual, expected)

	def test_w̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized labial-velar approximant pulmonic egressive consonant
	def test_wʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("wʰˤ")
		self.assertEqual(actual, expected)

	def test_w̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labial_velar_approximant_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labial-velar approximant pulmonic egressive consonant"
		actual = describe_transcription("w̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless labial-velar fricative pulmonic egressive consonant
	def test_ʍ_is_the_representation_of_the_voiceless_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ")
		self.assertEqual(actual, expected)

	def test_ʍ̊_is_the_representation_of_the_voiceless_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̊")
		self.assertEqual(actual, expected)

	def test_ʍ̥_is_the_representation_of_the_voiceless_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̥")
		self.assertEqual(actual, expected)

# voiceless labialized labial-velar fricative pulmonic egressive consonant
	def test_ʍʷ_is_the_representation_of_the_voiceless_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʷ")
		self.assertEqual(actual, expected)

	def test_ʍ̊ʷ_is_the_representation_of_the_voiceless_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʍ̥ʷ_is_the_representation_of_the_voiceless_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized labial-velar fricative pulmonic egressive consonant
	def test_ʍʲ_is_the_representation_of_the_voiceless_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʲ")
		self.assertEqual(actual, expected)

	def test_ʍ̊ʲ_is_the_representation_of_the_voiceless_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʍ̥ʲ_is_the_representation_of_the_voiceless_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized labial-velar fricative pulmonic egressive consonant
	def test_ʍˠ_is_the_representation_of_the_voiceless_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍˠ")
		self.assertEqual(actual, expected)

	def test_ʍ̊ˠ_is_the_representation_of_the_voiceless_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʍ̥ˠ_is_the_representation_of_the_voiceless_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized labial-velar fricative pulmonic egressive consonant
	def test_ʍˤ_is_the_representation_of_the_voiceless_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍˤ")
		self.assertEqual(actual, expected)

	def test_ʍ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʍ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated labial-velar fricative pulmonic egressive consonant
	def test_ʍʰ_is_the_representation_of_the_voiceless_aspirated_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized labial-velar fricative pulmonic egressive consonant
	def test_ʍʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized labial-velar fricative pulmonic egressive consonant
	def test_ʍʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized labial-velar fricative pulmonic egressive consonant
	def test_ʍʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized labial-velar fricative pulmonic egressive consonant
	def test_ʍʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍʰˤ")
		self.assertEqual(actual, expected)

# voiced labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬_is_the_representation_of_the_voiced_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬")
		self.assertEqual(actual, expected)

	def test_ʍ̬_is_the_representation_of_the_voiced_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬")
		self.assertEqual(actual, expected)

# voiced labialized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʷ_is_the_representation_of_the_voiced_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʍ̬ʷ_is_the_representation_of_the_voiced_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʲ_is_the_representation_of_the_voiced_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʍ̬ʲ_is_the_representation_of_the_voiced_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ˠ_is_the_representation_of_the_voiced_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʍ̬ˠ_is_the_representation_of_the_voiced_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʍ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʰ_is_the_representation_of_the_voiced_aspirated_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized labial-velar fricative pulmonic egressive consonant
	def test_ʍ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_labial_velar_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized labial-velar fricative pulmonic egressive consonant"
		actual = describe_transcription("ʍ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless epiglottal plosive pulmonic egressive consonant
	def test_ʡ_is_the_representation_of_the_voiceless_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ")
		self.assertEqual(actual, expected)

	def test_ʡ̊_is_the_representation_of_the_voiceless_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̊")
		self.assertEqual(actual, expected)

	def test_ʡ̥_is_the_representation_of_the_voiceless_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̥")
		self.assertEqual(actual, expected)

# voiceless labialized epiglottal plosive pulmonic egressive consonant
	def test_ʡʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʷ")
		self.assertEqual(actual, expected)

	def test_ʡ̊ʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʡ̥ʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized epiglottal plosive pulmonic egressive consonant
	def test_ʡʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʲ")
		self.assertEqual(actual, expected)

	def test_ʡ̊ʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʡ̥ʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized epiglottal plosive pulmonic egressive consonant
	def test_ʡˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡˠ")
		self.assertEqual(actual, expected)

	def test_ʡ̊ˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʡ̥ˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized epiglottal plosive pulmonic egressive consonant
	def test_ʡˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡˤ")
		self.assertEqual(actual, expected)

	def test_ʡ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʡ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated epiglottal plosive pulmonic egressive consonant
	def test_ʡʰ_is_the_representation_of_the_voiceless_aspirated_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized epiglottal plosive pulmonic egressive consonant
	def test_ʡʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized epiglottal plosive pulmonic egressive consonant
	def test_ʡʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized epiglottal plosive pulmonic egressive consonant
	def test_ʡʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized epiglottal plosive pulmonic egressive consonant
	def test_ʡʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡʰˤ")
		self.assertEqual(actual, expected)

# voiced epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬_is_the_representation_of_the_voiced_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬")
		self.assertEqual(actual, expected)

	def test_ʡ̬_is_the_representation_of_the_voiced_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬")
		self.assertEqual(actual, expected)

# voiced labialized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʷ_is_the_representation_of_the_voiced_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʡ̬ʷ_is_the_representation_of_the_voiced_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʲ_is_the_representation_of_the_voiced_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʡ̬ʲ_is_the_representation_of_the_voiced_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ˠ_is_the_representation_of_the_voiced_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʡ̬ˠ_is_the_representation_of_the_voiced_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʡ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʰ_is_the_representation_of_the_voiced_aspirated_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized epiglottal plosive pulmonic egressive consonant
	def test_ʡ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_epiglottal_plosive_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized epiglottal plosive pulmonic egressive consonant"
		actual = describe_transcription("ʡ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless epiglottal fricative pulmonic egressive consonant
	def test_ʜ_is_the_representation_of_the_voiceless_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ")
		self.assertEqual(actual, expected)

	def test_ʜ̊_is_the_representation_of_the_voiceless_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̊")
		self.assertEqual(actual, expected)

	def test_ʜ̥_is_the_representation_of_the_voiceless_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̥")
		self.assertEqual(actual, expected)

	def test_ʢ̊_is_the_representation_of_the_voiceless_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊")
		self.assertEqual(actual, expected)

	def test_ʢ̥_is_the_representation_of_the_voiceless_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥")
		self.assertEqual(actual, expected)

# voiceless labialized epiglottal fricative pulmonic egressive consonant
	def test_ʜʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʷ")
		self.assertEqual(actual, expected)

	def test_ʜ̊ʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʜ̥ʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʷ_is_the_representation_of_the_voiceless_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized epiglottal fricative pulmonic egressive consonant
	def test_ʜʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʲ")
		self.assertEqual(actual, expected)

	def test_ʜ̊ʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʜ̥ʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʲ_is_the_representation_of_the_voiceless_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized epiglottal fricative pulmonic egressive consonant
	def test_ʜˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜˠ")
		self.assertEqual(actual, expected)

	def test_ʜ̊ˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʜ̥ˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ˠ_is_the_representation_of_the_voiceless_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized epiglottal fricative pulmonic egressive consonant
	def test_ʜˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜˤ")
		self.assertEqual(actual, expected)

	def test_ʜ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʜ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated epiglottal fricative pulmonic egressive consonant
	def test_ʜʰ_is_the_representation_of_the_voiceless_aspirated_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʰ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʰ_is_the_representation_of_the_voiceless_aspirated_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʰ_is_the_representation_of_the_voiceless_aspirated_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized epiglottal fricative pulmonic egressive consonant
	def test_ʜʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʰʷ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized epiglottal fricative pulmonic egressive consonant
	def test_ʜʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʰʲ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized epiglottal fricative pulmonic egressive consonant
	def test_ʜʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʰˠ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized epiglottal fricative pulmonic egressive consonant
	def test_ʜʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜʰˤ")
		self.assertEqual(actual, expected)

	def test_ʢ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʢ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced epiglottal fricative pulmonic egressive consonant
	def test_ʢ_is_the_representation_of_the_voiced_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ")
		self.assertEqual(actual, expected)

	def test_ʜ̬_is_the_representation_of_the_voiced_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬")
		self.assertEqual(actual, expected)

	def test_ʜ̬_is_the_representation_of_the_voiced_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬")
		self.assertEqual(actual, expected)

# voiced labialized epiglottal fricative pulmonic egressive consonant
	def test_ʢʷ_is_the_representation_of_the_voiced_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʷ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʷ_is_the_representation_of_the_voiced_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʷ_is_the_representation_of_the_voiced_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized epiglottal fricative pulmonic egressive consonant
	def test_ʢʲ_is_the_representation_of_the_voiced_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʲ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʲ_is_the_representation_of_the_voiced_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʲ_is_the_representation_of_the_voiced_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized epiglottal fricative pulmonic egressive consonant
	def test_ʢˠ_is_the_representation_of_the_voiced_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢˠ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ˠ_is_the_representation_of_the_voiced_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ˠ_is_the_representation_of_the_voiced_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized epiglottal fricative pulmonic egressive consonant
	def test_ʢˤ_is_the_representation_of_the_voiced_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢˤ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated epiglottal fricative pulmonic egressive consonant
	def test_ʢʰ_is_the_representation_of_the_voiced_aspirated_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʰ")
		self.assertEqual(actual, expected)

	def test_ʢ̬ʰ_is_the_representation_of_the_voiced_aspirated_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʰ_is_the_representation_of_the_voiced_aspirated_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized epiglottal fricative pulmonic egressive consonant
	def test_ʢʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʰʷ")
		self.assertEqual(actual, expected)

	def test_ʢ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized epiglottal fricative pulmonic egressive consonant
	def test_ʢʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʰʲ")
		self.assertEqual(actual, expected)

	def test_ʢ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized epiglottal fricative pulmonic egressive consonant
	def test_ʢʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʰˠ")
		self.assertEqual(actual, expected)

	def test_ʢ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized epiglottal fricative pulmonic egressive consonant
	def test_ʢʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢʰˤ")
		self.assertEqual(actual, expected)

	def test_ʢ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʢ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʜ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_epiglottal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized epiglottal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʜ̬ʰˤ")
		self.assertEqual(actual, expected)

# voiceless alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕ_is_the_representation_of_the_voiceless_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ")
		self.assertEqual(actual, expected)

	def test_ɕ̊_is_the_representation_of_the_voiceless_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̊")
		self.assertEqual(actual, expected)

	def test_ɕ̥_is_the_representation_of_the_voiceless_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̥")
		self.assertEqual(actual, expected)

	def test_ʑ̊_is_the_representation_of_the_voiceless_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊")
		self.assertEqual(actual, expected)

	def test_ʑ̥_is_the_representation_of_the_voiceless_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥")
		self.assertEqual(actual, expected)

# voiceless labialized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʷ_is_the_representation_of_the_voiceless_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʷ")
		self.assertEqual(actual, expected)

	def test_ɕ̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ɕ̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̥ʷ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʷ_is_the_representation_of_the_voiceless_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʷ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʷ_is_the_representation_of_the_voiceless_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʷ")
		self.assertEqual(actual, expected)

# voiceless palatalized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʲ_is_the_representation_of_the_voiceless_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʲ")
		self.assertEqual(actual, expected)

	def test_ɕ̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ɕ̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̥ʲ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʲ_is_the_representation_of_the_voiceless_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʲ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʲ_is_the_representation_of_the_voiceless_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʲ")
		self.assertEqual(actual, expected)

# voiceless velarized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕˠ_is_the_representation_of_the_voiceless_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕˠ")
		self.assertEqual(actual, expected)

	def test_ɕ̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ɕ̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̥ˠ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ˠ_is_the_representation_of_the_voiceless_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ˠ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ˠ_is_the_representation_of_the_voiceless_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ˠ")
		self.assertEqual(actual, expected)

# voiceless pharyngealized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕˤ")
		self.assertEqual(actual, expected)

	def test_ɕ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ɕ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̥ˤ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ˤ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ˤ_is_the_representation_of_the_voiceless_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ˤ")
		self.assertEqual(actual, expected)

# voiceless aspirated alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʰ_is_the_representation_of_the_voiceless_aspirated_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʰ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʰ_is_the_representation_of_the_voiceless_aspirated_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʰ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʰ_is_the_representation_of_the_voiceless_aspirated_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʰ")
		self.assertEqual(actual, expected)

# voiceless aspirated labialized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʰʷ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʰʷ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʰʷ_is_the_representation_of_the_voiceless_aspirated_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʰʷ")
		self.assertEqual(actual, expected)

# voiceless aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʰʲ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʰʲ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʰʲ_is_the_representation_of_the_voiceless_aspirated_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʰʲ")
		self.assertEqual(actual, expected)

# voiceless aspirated velarized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʰˠ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʰˠ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʰˠ_is_the_representation_of_the_voiceless_aspirated_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʰˠ")
		self.assertEqual(actual, expected)

# voiceless aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant
	def test_ɕʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕʰˤ")
		self.assertEqual(actual, expected)

	def test_ʑ̥ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̥ʰˤ")
		self.assertEqual(actual, expected)

	def test_ʑ̊ʰˤ_is_the_representation_of_the_voiceless_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiceless aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̊ʰˤ")
		self.assertEqual(actual, expected)

# voiced alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑ_is_the_representation_of_the_voiced_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ")
		self.assertEqual(actual, expected)

	def test_ɕ̬_is_the_representation_of_the_voiced_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬")
		self.assertEqual(actual, expected)

	def test_ɕ̬_is_the_representation_of_the_voiced_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬")
		self.assertEqual(actual, expected)

# voiced labialized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʷ_is_the_representation_of_the_voiced_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʷ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʷ_is_the_representation_of_the_voiced_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʷ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʷ_is_the_representation_of_the_voiced_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʷ")
		self.assertEqual(actual, expected)

# voiced palatalized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʲ_is_the_representation_of_the_voiced_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʲ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʲ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʲ_is_the_representation_of_the_voiced_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʲ")
		self.assertEqual(actual, expected)

# voiced velarized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑˠ_is_the_representation_of_the_voiced_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑˠ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ˠ_is_the_representation_of_the_voiced_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ˠ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ˠ_is_the_representation_of_the_voiced_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ˠ")
		self.assertEqual(actual, expected)

# voiced pharyngealized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑˤ_is_the_representation_of_the_voiced_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑˤ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ˤ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ˤ_is_the_representation_of_the_voiced_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ˤ")
		self.assertEqual(actual, expected)

# voiced aspirated alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʰ_is_the_representation_of_the_voiced_aspirated_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʰ")
		self.assertEqual(actual, expected)

	def test_ʑ̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̬ʰ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʰ_is_the_representation_of_the_voiced_aspirated_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʰ")
		self.assertEqual(actual, expected)

# voiced aspirated labialized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʰʷ")
		self.assertEqual(actual, expected)

	def test_ʑ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̬ʰʷ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʰʷ_is_the_representation_of_the_voiced_aspirated_labialized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated labialized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʰʷ")
		self.assertEqual(actual, expected)

# voiced aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʰʲ")
		self.assertEqual(actual, expected)

	def test_ʑ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̬ʰʲ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʰʲ_is_the_representation_of_the_voiced_aspirated_palatalized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated palatalized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʰʲ")
		self.assertEqual(actual, expected)

# voiced aspirated velarized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʰˠ")
		self.assertEqual(actual, expected)

	def test_ʑ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̬ʰˠ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʰˠ_is_the_representation_of_the_voiced_aspirated_velarized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated velarized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʰˠ")
		self.assertEqual(actual, expected)

# voiced aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant
	def test_ʑʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑʰˤ")
		self.assertEqual(actual, expected)

	def test_ʑ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ʑ̬ʰˤ")
		self.assertEqual(actual, expected)

	def test_ɕ̬ʰˤ_is_the_representation_of_the_voiced_aspirated_pharyngealized_alveolo_palatal_fricative_pulmonic_egressive_consonant(self):
		expected = "voiced aspirated pharyngealized alveolo-palatal fricative pulmonic egressive consonant"
		actual = describe_transcription("ɕ̬ʰˤ")
		self.assertEqual(actual, expected)
