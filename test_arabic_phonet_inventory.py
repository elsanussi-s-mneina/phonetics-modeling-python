"""
unit tests for testing the representation
of the Arabic phoneme inventory.
"""
import unittest

from ipa import arabic_phonet_inventory_report

class ArabicPhonetInventoryTests(unittest.TestCase):
    def in_the_inventory(self, some_phoneme: str):
        not_expected = -1
        actual = arabic_phonet_inventory_report.find(some_phoneme)
        self.assertNotEqual(actual, not_expected)

    def not_in_the_inventory(self, some_phoneme: str):
        expected = -1
        actual = arabic_phonet_inventory_report.find(some_phoneme)
        self.assertEqual(actual, expected)

    def test_p_is_not_in_the_arabic_phoneme_inventory(self):
        self.not_in_the_inventory("/p/")

    def test_b_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/b/")

    def test_t_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/t/")

    def test_d_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/d/")

    def test_k_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/k/")

    def test_g_is_not_in_the_arabic_phoneme_inventory(self):
        self.not_in_the_inventory("/g/")

    def test_q_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/q/")

    def test_glottal_stop_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ʔ/")

    def test_f_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/f/")

    def test_v_is_not_in_the_arabic_phoneme_inventory(self):
        self.not_in_the_inventory("/v/")

    def test_voiceless_dental_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/θ/")

    def test_voiced_dental_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ð/")

    def test_s_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/s/")

    def test_z_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/z/")

    def test_voiceless_postalveolar_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ʃ/")

    def test_voiced_postalveolar_fricative_is_not_the_arabic_phoneme_inventory(self):
        self.not_in_the_inventory("/ʒ/")

    def test_voiceless_uvular_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/χ/")

    def test_voiced_uvular_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ʁ/")

    def test_voiceless_pharyngeal_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ħ/")

    def test_voiced_pharyngeal_fricative_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ʕ/")

    def test_r_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/r/")

    def test_j_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/j/")

    def test_l_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/l/")

    def test_w_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/w/")

    def test_pharyngealized_t_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/tˤ/")

    def test_pharyngealized_s_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/sˤ/")

    def test_pharyngealized_z_is_not_in_the_arabic_phoneme_inventory(self):
        self.not_in_the_inventory("/zˤ/")

    def test_pharyngealized_ð_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/ðˤ/")

    def test_pharyngealized_d_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/dˤ/")

    def test_a_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/a/")

    def test_u_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/u/")

    def test_i_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/i/")

    def test_long_a_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/aː/")

    def test_long_u_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/uː/")

    def test_long_i_is_in_the_arabic_phoneme_inventory(self):
        self.in_the_inventory("/iː/")
