from lib_types import Consonant, Phonet, VocalFolds, Vowel, VowelLength

def is_consonant(phone: Phonet) -> bool:
    return isinstance(phone, Consonant)

def is_vowel(phone: Phonet) -> bool:
    return isinstance(phone, Vowel)

def with_vocal_folds(vocal_folds: VocalFolds, phone: Phonet) -> Phonet:
    if is_consonant(phone):
        place = phone.place
        airstream = phone.airstream
        manner = phone.manner
        secondary_articulation = phone.secondary_articulation
        return Consonant(vocal_folds, place, manner, airstream, secondary_articulation)

    height = phone.height
    backness = phone.backness
    rounding = phone.rounding
    vowel_length = phone.vowel_length
    return Vowel(height, backness, rounding, vocal_folds, vowel_length)


def with_vowel_length(vowel_length: VowelLength, phone: Phonet) -> Phonet:
    if is_consonant(phone):
        return phone
    height = phone.height
    backness = phone.backness
    rounding = phone.rounding
    vocal_folds = phone.vocal_folds

    # Make the vowel extra-short.
    return Vowel(height, backness, rounding, vocal_folds,
                 vowel_length)


def to_extra_short(phone: Phonet):
    return with_vowel_length(VowelLength.EXTRA_SHORT, phone)