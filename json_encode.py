"""
Converting objects to Javascript Object Notation.
"""
from lib_types import (VocalFolds, VowelLength, Phonet, PhonetInventory, Consonant, Vowel)

from lib_functions import (show_vocal_folds, show_place, show_manner,
                           show_airstream, show_height, show_backness,
                           show_rounding, show_vowel_length_verbosely,
                           show_secondary_articulation_verbosely)

def encode_vocal_folds(vocal_folds: VocalFolds) -> str:
    if vocal_folds == VocalFolds.VOICED:
        return "voiced"
    elif vocal_folds == VocalFolds.VOICELESS:
        return "voiceless"
    elif vocal_folds == VocalFolds.VOICED_ASPIRATED:
        return "voiced_aspirated"
    elif vocal_folds == VocalFolds.VOICELESS_ASPIRATED:
        return "voiceless_aspirated"
    elif vocal_folds == VocalFolds.CREAKY_VOICED:
        return "creaky_voiced"


def encode_vowel_length(vowel_length: VowelLength) -> str:
    if vowel_length == VowelLength.LONG:
        return "long"
    elif vowel_length == VowelLength.HALF_LONG:
        return "half_long"
    elif vowel_length == VowelLength.EXTRA_SHORT:
        return "extra_short"
    elif vowel_length == VowelLength.NORMAL:
        return "normal"

def encode_phoneme(phoneme: Phonet) -> str:
    if isinstance(phoneme, Consonant):
        return "{'type': 'phonete', 'subtype': 'consonant'," + \
        " 'vocal_folds': '" + show_vocal_folds(phoneme.vocal_folds) + "'," +    \
        " 'place': '" + show_place(phoneme.place) + "',"              +    \
        " 'manner': '" + show_manner(phoneme.manner) + "',"            +    \
        " 'airstream': '" + show_airstream(phoneme.airstream) + "',"      +    \
        " 'secondary_articulation': '" + show_secondary_articulation_verbosely(phoneme.secondary_articulation) + "'}"
    elif isinstance(phoneme, Vowel):
        return "{'type': 'phonete', 'subtype': 'vowel'," + \
               " 'height': '" + show_height(phoneme.height) + "'," + \
               " 'backness': '" + show_backness(phoneme.backness) + "'," + \
               " 'rounding': '" + show_rounding(phoneme.rounding) + "'," + \
               " 'vocal_folds': '" + show_vocal_folds(phoneme.vocal_folds) + "'," + \
               " 'vowel_length': '" + show_vowel_length_verbosely(phoneme.vowel_length) + "'}"


def encode_phonet_inventory(phonet_inventory: PhonetInventory) -> str:
    return "{ 'type': 'phonet_inventory', 'contents': [" + ', '.join(map(encode_phoneme, phonet_inventory.contents)) + '] }'

