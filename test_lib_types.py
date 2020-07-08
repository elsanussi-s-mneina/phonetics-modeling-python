"""
Unit tests for lib_types
"""

import unittest
from lib_types import Manner

class TestLibTypes(unittest.TestCase):
    def test_plosive_and_lateral_approximant_are_different_manners_of_articulation(self):
        self.assertFalse(Manner.PLOSIVE == Manner.LATERAL_APPROXIMANT)
