"""
These functions are useful to facilitate programming using immutability.
"""
from lib_types import (
    Consonant,
    Phonet,
    VocalFolds,
    Vowel,
    VowelLength,
    Place,
    Manner,
    Airstream,
    SecondaryArticulation,
)


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
            phone.secondary_articulation,
        )
    return Vowel(
        phone.height, phone.backness, phone.rounding, vocal_folds, phone.vowel_length
    )


def with_place(place: Place, phone: Phonet) -> Phonet:
    """
    Change the place of articulation of a consonant to a particular place.
    Ignore vowels.
    """
    # Do not change vowels, since they do not have a place of articulation.
    if is_vowel(phone):
        return phone

    # change the place of articulation of consonants.
    return Consonant(
        phone.vocal_folds,
        place,
        phone.manner,
        phone.airstream,
        phone.secondary_articulation,
    )


def with_manner(manner: Manner, phone: Phonet) -> Phonet:
    """
    Change the manner of articulation of a consonant to a particular manner.
    Ignore vowels.
    """
    # Do not change vowels, since they do not have a manner of articulation.
    if is_vowel(phone):
        return phone

    # change the manner of articulation of consonants.
    return Consonant(
        phone.vocal_folds,
        phone.place,
        manner,
        phone.airstream,
        phone.secondary_articulation,
    )


def with_airstream(airstream: Airstream, phone: Phonet) -> Phonet:
    """
    Change the airstream mechanism of a consonant to a particular one.
    Ignore vowels.
    """
    # Do not change vowels.
    if is_vowel(phone):
        return phone

    # change the airstream mechanism of consonants.
    return Consonant(
        phone.vocal_folds,
        phone.place,
        phone.manner,
        airstream,
        phone.secondary_articulation,
    )


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
        phone.height, phone.backness, phone.rounding, phone.vocal_folds, vowel_length
    )


def with_secondary_articulation(
    secondary_articulation: SecondaryArticulation, phone: Phonet
) -> Phonet:
    """
    Change the secondary articulation of a consonant to a particular one.
    Ignore vowels.
    """
    # Do not change vowels.
    if is_vowel(phone):
        return phone

    # change the secondary articulation of consonants.
    return Consonant(
        phone.vocal_folds,
        phone.place,
        phone.manner,
        phone.airstream,
        secondary_articulation,
    )


def to_extra_short(phone: Phonet) -> Phonet:
    """
    Change the length of a vowel to
    extra short. Ignore consonants.
    """
    return with_vowel_length(VowelLength.EXTRA_SHORT, phone)


def to_normal_length(phone: Phonet) -> Phonet:
    """
    Change the length of a vowel to
    normal. Ignore consonants.
    """
    return with_vowel_length(VowelLength.NORMAL, phone)


def to_long(phone: Phonet) -> Phonet:
    """
    Change the length of a vowel to long.
    Ignore consonants.
    """
    return with_vowel_length(VowelLength.LONG, phone)


def to_half_long(phone: Phonet) -> Phonet:
    """
    Change the length of a vowel to half-long.
    Ignore consonants.
    """
    return with_vowel_length(VowelLength.HALF_LONG, phone)


def to_alveolar(phone: Phonet) -> Phonet:
    """ Change the place of articulation to alveolar if phone is a consonant."""
    return with_place(Place.ALVEOLAR, phone)


def to_voiced(phone: Phonet) -> Phonet:
    """Change the vocal folds to voiced."""
    return with_vocal_folds(VocalFolds.VOICED, phone)


def to_voiceless(phone: Phonet) -> Phonet:
    """Change the vocal folds to voiceless."""
    return with_vocal_folds(VocalFolds.VOICELESS, phone)


def to_voiceless_aspirated(phone: Phonet) -> Phonet:
    """Change the vocal folds to voiceless aspirated."""
    return with_vocal_folds(VocalFolds.VOICELESS_ASPIRATED, phone)


def to_voiced_aspirated(phone: Phonet) -> Phonet:
    """Change the vocal folds to voiced aspirated."""
    return with_vocal_folds(VocalFolds.VOICED_ASPIRATED, phone)


def to_labialized(phone: Phonet) -> Phonet:
    """Change the secondary articulation to labialized."""
    return with_secondary_articulation(SecondaryArticulation.LABIALIZED, phone)


def to_palatalized(phone: Phonet) -> Phonet:
    """Change the secondary articulation to palatalized."""
    return with_secondary_articulation(SecondaryArticulation.PALATALIZED, phone)


def to_pharyngealized(phone: Phonet) -> Phonet:
    """Change the secondary articulation to pharyngealized."""
    return with_secondary_articulation(SecondaryArticulation.PHARYNGEALIZED, phone)


def to_velarized(phone: Phonet) -> Phonet:
    """Change the secondary articulation to velarized."""
    return with_secondary_articulation(SecondaryArticulation.VELARIZED, phone)
