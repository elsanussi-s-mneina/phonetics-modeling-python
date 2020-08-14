from lib_types import Consonant, Phonet, VocalFolds, Vowel

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
    else:
        height = phone.height
        backness = phone.backness
        rounding = phone.rounding
        vowel_length = phone.vowel_length
        return Vowel(height, backness, rounding, vocal_folds, vowel_length)
