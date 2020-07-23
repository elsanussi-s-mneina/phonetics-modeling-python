"""
Unit tests for lib_types
"""

import unittest

from lib_types import Manner, Airstream


class TestLibTypes(unittest.TestCase):
    def test_plosive_and_lateral_approximant_are_different_manners_of_articulation(self) -> None:
        self.assertFalse(Manner.PLOSIVE == Manner.LATERAL_APPROXIMANT)

    def test_pulmonic_and_click_are_different_airstream_mechanisms(self) -> None:
        self.assertFalse(Airstream.PULMONIC_EGRESSIVE == Airstream.CLICK)
