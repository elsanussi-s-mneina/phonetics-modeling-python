"""
These functions are useful to facilitate programming using immutability.
"""
from lib_types import Consonant, Phonet, VocalFolds, Vowel, VowelLength

def is_consonant(phone: Phonet) -> bool:
    """Whether a phone is a consonant"""
    return isinstance(phone, Consonant)

def is_vowel(phone: Phonet) -> bool:
    """Whether a phone is a vowel"""
    return isinstance(phone, Vowel)

def with_vocal_folds(vocal_folds: VocalFolds, phone: Phonet) -> Phonet:
    """
    Change the voicing of a phone to a particular voicing.
    """
    if is_consonant(phone):
        return Consonant(
            vocal_folds,
            phone.place,
            phone.manner,
            phone.airstream,
            phone.secondary_articulation)
    return Vowel(
        phone.height,
        phone.backness,
        phone.rounding,
        vocal_folds,
        phone.vowel_length)


def with_vowel_length(vowel_length: VowelLength, phone: Phonet) -> Phonet:
    """
    Change the vowel length of a vowel to a particular voicing.
    Ignore consonants.
    """
    # Do not change consonants, since they do not have a vowel length.
    if is_consonant(phone):
        return phone

    # Make the vowel extra-short.
    return Vowel(
        phone.height,
        phone.backness,
        phone.rounding,
        phone.vocal_folds,
        vowel_length)


def to_extra_short(phone: Phonet):
    """
    Change the length of a vowel to
    extra short. Ignore consonants.
    """
    return with_vowel_length(VowelLength.EXTRA_SHORT, phone)
