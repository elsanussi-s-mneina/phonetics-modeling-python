"""
Functions for manipulating phonemes, represented in international phonetic alphabet, or
as Sound Patterns of English features.
"""

from typing import List, Optional

from english_us_text import (PLOSIVE_MANNER_TEXT, NASAL_MANNER_TEXT, TRILL_MANNER_TEXT,
                             TAP_OR_FLAP_MANNER_TEXT, APPROXIMANT_MANNER_TEXT,
                             FRICATIVE_MANNER_TEXT,
                             AFFRICATE_MANNER_TEXT, LATERAL_FRICATIVE_MANNER_TEXT,
                             LATERAL_APPROXIMANT_MANNER_TEXT,
                             LATERAL_FLAP_MANNER_TEXT, LATERAL_MANNER_TEXT,
                             CREAKY_VOICED_VOCAL_FOLDS_TEXT, IMPLOSIVE_AIRSTREAM_TEXT,
                             CLICK_AIRSTREAM_TEXT, PULMONIC_EGRESSIVE_AIRSTREAM_TEXT,
                             PALATOALVEOLAR_PLACE_TEXT, ALVEOLOPALATAL_PLACE_TEXT,
                             LABIALPALATAL_PLACE_TEXT,
                             LABIALVELAR_PLACE_TEXT, EPIGLOTTAL_PLACE_TEXT, GLOTTAL_PLACE_TEXT,
                             PHARYNGEAL_PLACE_TEXT, UVULAR_PLACE_TEXT, VELAR_PLACE_TEXT,
                             PALATAL_PLACE_TEXT, RETROFLEX_PLACE_TEXT, POSTALVEOLAR_PLACE_TEXT,
                             ALVEOLAR_PLACE_TEXT, DENTAL_PLACE_TEXT, LABIODENTAL_PLACE_TEXT,
                             BILABIAL_PLACE_TEXT, UNROUNDED_ROUNDING_TEXT, ROUNDED_ROUNDING_TEXT,
                             OPEN_HEIGHT_TEXT, NEAR_OPEN_HEIGHT_TEXT, OPEN_MID_HEIGHT_TEXT,
                             MID_HEIGHT_TEXT, CLOSE_MID_HEIGHT_TEXT, NEAR_CLOSE_HEIGHT_TEXT,
                             CLOSE_HEIGHT_TEXT, BACK_BACKNESS_TEXT, CENTRAL_BACKNESS_TEXT,
                             FRONT_BACKNESS_TEXT,
                             VOICELESS_ASPIRATED_VOCAL_FOLDS_TEXT,
                             VOICED_ASPIRATED_VOCAL_FOLDS_TEXT, VOICELESS_VOCAL_FOLDS_TEXT,
                             VOICED_VOCAL_FOLDS_TEXT, CONSONANT_TEXT, VOWEL_TEXT)
from lib_types import (Phonet, Height, Backness, Rounding, VocalFolds, Vowel, Consonant, Place,
                       Manner, Airstream,
                       MultiPlace, PhonetInventory,
                       UnmarkableConsonant, UnmarkableVowel,
                       UnmarkablePlace, UnmarkableVocalFolds, MarkedVocalFolds, UnmarkedVocalFolds,
                       UnmarkedHeight, UnmarkedBackness, MarkedManner, MarkedPlace, UnmarkedPlace,
                       UnmarkedManner, UnmarkableManner, MarkedBackness, MarkedHeight,
                       UnmarkableHeight, UnmarkableBackness, UnmarkableAirstream, MarkedAirstream,
                       UnmarkedAirstream, UnmarkedRounding, MarkedRounding, UnmarkablePhonet,
                       UnmarkableRounding, height_states, backness_states, rounding_states,
                       airstream_states, manner_states, place_states, vocal_fold_states)


def equivalent_in_place(place_1: Place, place_2: Place) -> bool:
    """
    Whether two places of articulation are equivalent.
    """
    if place_1 == Place.BILABIAL and place_2 == Place.BILABIAL:
        return True
    if place_1 == Place.LABIODENTAL and place_2 == Place.LABIODENTAL:
        return True
    if place_1 == Place.DENTAL and place_2 == Place.DENTAL:
        return True
    if place_1 == Place.ALVEOLAR and place_2 == Place.ALVEOLAR:
        return True

    if place_1 == Place.POSTALVEOLAR and place_2 == Place.POSTALVEOLAR:
        return True

    if place_1 == Place.RETROFLEX and place_2 == Place.RETROFLEX:
        return True

    if place_1 == Place.PALATAL and place_2 == Place.PALATAL:
        return True

    if place_1 == Place.VELAR and place_2 == Place.VELAR:
        return True

    if place_1 == Place.UVULAR and place_2 == Place.UVULAR:
        return True

    if place_1 == Place.PHARYNGEAL and place_2 == Place.PHARYNGEAL:
        return True

    if place_1 == Place.GLOTTAL and place_2 == Place.GLOTTAL:
        return True

    if place_1 == Place.EPIGLOTTAL and place_2 == Place.EPIGLOTTAL:
        return True

    if isinstance(place_2, MultiPlace):
        return place_1 in place_2.places

    if isinstance(place_1, MultiPlace):
        return place_2 in place_1.places

    return False


def retracted_place(place: Place) -> Place:
    """
    Given a place of articulation,
    returns the place of articulation that is
    the next more retracted.
    """
    if place == Place.BILABIAL:
        return Place.LABIODENTAL
    if place == Place.LABIODENTAL:
        return Place.DENTAL
    if place == Place.DENTAL:
        return Place.ALVEOLAR
    if place == Place.ALVEOLAR:
        return Place.POSTALVEOLAR
    if place == Place.POSTALVEOLAR:
        return Place.RETROFLEX
    if place == Place.RETROFLEX:
        return Place.PALATAL
    if place == Place.PALATAL:
        return Place.VELAR
    if place == Place.VELAR:
        return Place.UVULAR
    if place == Place.UVULAR:
        return Place.PHARYNGEAL
    if place == Place.PHARYNGEAL:
        return Place.GLOTTAL
    if place == Place.GLOTTAL:
        return Place.EPIGLOTTAL
    return place


def english_description(phone: Phonet) -> str:
    """
    Gives the English description of a phone.
    """
    return show_phonet(phone)


def voiced_phonet(phone: Phonet) -> Optional[Phonet]:
    """
    A function that given an IPA symbol will convert it to the voiced
    equivalent.
    """
    if isinstance(phone, Consonant):
        place = phone.place
        airstream = phone.airstream
        manner = phone.manner
        if phone.vocal_folds == VocalFolds.VOICELESS_ASPIRATED:
            return Consonant(VocalFolds.VOICED_ASPIRATED, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.VOICELESS or phone.vocal_folds == VocalFolds.VOICED:
            return Consonant(VocalFolds.VOICED, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.VOICED_ASPIRATED:
            return Consonant(VocalFolds.VOICED_ASPIRATED, place, manner, airstream)
        return Consonant(VocalFolds.VOICED, place, manner, airstream)
    if isinstance(phone, Vowel):
        height = phone.height
        backness = phone.backness
        rounding = phone.rounding
        return Vowel(height, backness, rounding, VocalFolds.VOICED)
    return None


def devoiced_phonet(phone: Phonet) -> Phonet:
    """
    A function that given an IPA symbol will convert it to the voiceless
    equivalent.
    """
    if isinstance(phone, Consonant):
        place = phone.place
        airstream = phone.airstream
        manner = phone.manner
        if phone.vocal_folds == VocalFolds.VOICED:
            return Consonant(VocalFolds.VOICELESS, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.CREAKY_VOICED:
            return Consonant(VocalFolds.VOICELESS, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.VOICELESS:
            return Consonant(VocalFolds.VOICELESS, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.VOICED_ASPIRATED:
            return Consonant(VocalFolds.VOICELESS_ASPIRATED, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.VOICELESS_ASPIRATED:
            return Consonant(VocalFolds.VOICELESS_ASPIRATED, place, manner, airstream)
    if isinstance(phone, Vowel):
        backness = phone.backness
        height = phone.height
        rounding = phone.rounding
        return Vowel(height, backness, rounding, VocalFolds.VOICELESS)
    return phone


def spirantized_phonet(phone: Phonet) -> Phonet:
    """
    The following is inelegant, but there is no other way in the system,
    right now. The part that is inelegant is that,
    a [t] which is considered alveolar, when spirantized becomes [θ]
    which is dental.
    So the following line implements this
    change in place of articulation.
    """
    if isinstance(phone, Consonant) and phone.manner == Manner.PLOSIVE:
        vocal_folds = phone.vocal_folds
        airstream = phone.airstream
        if phone.place == Place.ALVEOLAR:
            return Consonant(vocal_folds, Place.DENTAL, Manner.FRICATIVE, airstream)
        place = phone.place
        return Consonant(vocal_folds, place, Manner.FRICATIVE, airstream)
    return phone


def unmark_voice(voice_1: VocalFolds, voice_2: VocalFolds) -> UnmarkableVocalFolds:
    if voice_1 == voice_2:
        return MarkedVocalFolds(voice_1)
    return UnmarkedVocalFolds()


def unmark_place(place_1: Place, place_2: Place) -> UnmarkablePlace:
    if equivalent_in_place(place_1, place_2):
        return MarkedPlace(place_1)
    return UnmarkedPlace()


def unmark_manner(manner_1: Manner, manner_2: Manner) -> UnmarkableManner:
    if manner_1 == manner_2:
        return MarkedManner(manner_1)
    return UnmarkedManner()


def unmark_airstream(airstream_1: Airstream, airstream_2: Airstream) -> UnmarkableAirstream:
    if airstream_1 == airstream_2:
        return MarkedAirstream(airstream_1)
    return UnmarkedAirstream()


def unmark_height(height_1: Height, height_2: Height) -> UnmarkableHeight:
    if height_1 == height_2:
        return MarkedHeight(height_1)
    return UnmarkedHeight()


def unmark_backness(backness_1: Backness, backness_2: Backness) -> UnmarkableBackness:
    if backness_1 == backness_2:
        return MarkedBackness(backness_1)
    return UnmarkedBackness()


def unmark_rounding(rounding_1: Rounding, rounding_2: Rounding) -> UnmarkableRounding:
    if rounding_1 == rounding_2:
        return MarkedRounding(rounding_1)
    return UnmarkedRounding()


def unmark_differences(phone_1: Phonet, phone_2: Phonet) -> UnmarkablePhonet:
    if isinstance(phone_1, Consonant) and isinstance(phone_2, Consonant):
        vocal_folds: UnmarkableVocalFolds = unmark_voice(phone_1.vocal_folds, phone_2.vocal_folds)
        place: UnmarkablePlace = unmark_place(phone_1.place, phone_2.place)
        manner: UnmarkableManner = unmark_manner(phone_1.manner, phone_2.manner)
        airstream: UnmarkableAirstream = unmark_airstream(phone_1.airstream, phone_2.airstream)
        return UnmarkableConsonant(vocal_folds, place, manner, airstream)
    if isinstance(phone_1, Vowel) and isinstance(phone_2, Consonant):
        vocal_folds: UnmarkableVocalFolds = unmark_voice(phone_1.vocal_folds, phone_2.vocal_folds)
        return UnmarkableVowel(UnmarkedHeight(), UnmarkedBackness(), UnmarkedRounding(),
                               vocal_folds)
    if isinstance(phone_1, Consonant) and isinstance(phone_2, Vowel):
        return unmark_differences(phone_2, phone_1)

    if isinstance(phone_1, Vowel) and isinstance(phone_2, Vowel):
        # Both are vowels:
        vocal_folds: UnmarkableVocalFolds = unmark_voice(phone_1.vocal_folds, phone_2.vocal_folds)
        height: UnmarkableHeight = unmark_height(phone_1.height, phone_2.height)
        backness: UnmarkableBackness = unmark_backness(phone_1.backness, phone_2.backness)
        rounding: UnmarkableRounding = unmark_rounding(phone_1.rounding, phone_2.rounding)
        return UnmarkableVowel(height, backness, rounding, vocal_folds)


def similar_in_voice(voice_1: UnmarkableVocalFolds) -> List[VocalFolds]:
    if isinstance(voice_1, MarkedVocalFolds):
        return voice_1.vocal_fold
    return vocal_fold_states


def similar_in_place(place_1: UnmarkablePlace) -> List[Place]:
    if isinstance(place_1, MarkedPlace):
        return place_1.place
    return place_states


def similar_in_manner(manner_1: UnmarkableManner) -> List[Manner]:
    if isinstance(manner_1, MarkedManner):
        return manner_1.manner
    return manner_states


def similar_in_airstream(airstream_1: UnmarkableAirstream) -> List[Airstream]:
    if isinstance(airstream_1, MarkedAirstream):
        return airstream_1.airstream
    return airstream_states


def similar_in_height(height_1: UnmarkableHeight) -> List[Height]:
    if isinstance(height_1, MarkedHeight):
        return height_1.height
    return height_states


def similar_in_backness(backness_1: UnmarkableBackness) -> List[Backness]:
    if isinstance(backness_1, MarkedBackness):
        return backness_1.backness
    return backness_states


def similar_in_rounding(rounding_1: UnmarkableRounding) -> List[Rounding]:
    if isinstance(rounding_1, MarkedRounding):
        return rounding_1.rounding
    return rounding_states


def similar_consonants_to(phonet_1: UnmarkableConsonant) -> List[Phonet]:
    vocal_folds: List[VocalFolds] = similar_in_voice(phonet_1.vocal_folds)
    place: List[Place] = similar_in_place(phonet_1.place)
    manner: List[Manner] = similar_in_manner(phonet_1.manner)
    airstream: List[Airstream] = similar_in_airstream(phonet_1.airstream)
    return [Consonant(v, p, m, a)
            for p in place
            for v in vocal_folds
            for m in manner
            for a in airstream
            ]


def similar_vowels_to(phonet_1: UnmarkableVowel) -> List[Phonet]:
    vocal_folds: List[VocalFolds] = similar_in_voice(phonet_1.vocal_folds)
    height: List[Height] = similar_in_height(phonet_1.height)
    backness: List[Backness] = similar_in_backness(phonet_1.backness)
    rounding: List[Rounding] = similar_in_rounding(phonet_1.rounding)
    return [Vowel(h, b, r, v)
            for h in height
            for b in backness
            for r in rounding
            for v in vocal_folds
            ]


def similar_phonemes_to(phonet_1: UnmarkablePhonet) -> List[Phonet]:
    """
    This function
    takes any unmarked attributes in the phoneme definition,
    and returns a list with all possible phonemes that have that attribute.
    """
    if isinstance(phonet_1, UnmarkableConsonant):
        return similar_consonants_to(phonet_1)
    return similar_vowels_to(phonet_1)


def impossible(phone: Phonet) -> bool:
    """
    The following function returns whether an articulation is
    considered impossible according to the IPA (pulmonic) consonants chart.
    Does not work for other values.
    """
    if (isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICED
            and phone.place == Place.PHARYNGEAL
            and phone.manner == Manner.PLOSIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICED_ASPIRATED
            and phone.place == Place.PHARYNGEAL
            and phone.manner == Manner.PLOSIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICELESS
            and phone.place == Place.GLOTTAL
            and phone.manner == Manner.PLOSIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return False  # [ʔ] is not impossible.
    if (isinstance(phone, Consonant)
            and phone.place == Place.GLOTTAL
            and phone.manner == Manner.FRICATIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return False  # [h] and [ɦ] are not impossible.
    if (isinstance(phone, Consonant)
            and phone.place == Place.GLOTTAL
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True  # all other pulmonary egressive consonants are impossible..
    if (isinstance(phone, Consonant)
            and phone.place == Place.PHARYNGEAL
            and phone.manner == Manner.NASAL
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.PHARYNGEAL
            and phone.manner == Manner.LATERAL_FRICATIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.PHARYNGEAL
            and phone.manner == Manner.LATERAL_APPROXIMANT
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.VELAR
            and phone.manner == Manner.TRILL
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.VELAR
            and phone.manner == Manner.TAP_OR_FLAP
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.BILABIAL
            and phone.manner == Manner.LATERAL_FRICATIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.BILABIAL
            and phone.manner == Manner.LATERAL_APPROXIMANT
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.LABIODENTAL
            and phone.manner == Manner.LATERAL_FRICATIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    if (isinstance(phone, Consonant)
            and phone.place == Place.LABIODENTAL
            and phone.manner == Manner.LATERAL_APPROXIMANT
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE):
        return True
    return False  # Everything else is assumed to be possible.


def retract_phonet(phonete: Optional[Phonet]) -> Optional[Phonet]:
    """
    Return the sound produced in the next further back place in
    the mouth.
    :param phonete: a phoneme
    :return: a phoneme pronounced further back
    """
    if isinstance(phonete, Consonant):
        voicing = phonete.vocal_folds
        place = phonete.place
        manner = phonete.manner
        airstream = phonete.airstream
        return Consonant(voicing, retracted_place(place), manner, airstream)
    return None


def deaspirate(phone: Phonet) -> Phonet:
    """
    Given an aspirated phone, it will return its non-aspirated counterpart.
    """
    if isinstance(phone, Consonant):
        if phone.vocal_folds == VocalFolds.VOICED_ASPIRATED:
            place = phone.place
            manner = phone.manner
            airstream = phone.airstream
            return Consonant(VocalFolds.VOICED, place, manner, airstream)
        if phone.vocal_folds == VocalFolds.VOICELESS_ASPIRATED:
            place = phone.place
            manner = phone.manner
            airstream = phone.airstream
            return Consonant(VocalFolds.VOICELESS, place, manner, airstream)
        return phone
    return phone


def decreak(phone: Phonet) -> Phonet:
    """
    Given a creaky phone, it will return its non-creaky counterpart.
    """
    if isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.CREAKY_VOICED:
        place = phone.place
        manner = phone.manner
        airstream = phone.airstream
        return Consonant(VocalFolds.VOICED, place, manner, airstream)
    return phone


# Go to Section 12.2 of the textbook to understand
# the concept of phonological features.


def is_glide(phone: Phonet) -> bool:
    """
    Whether a segment is a glide.
    """
    if isinstance(phone, Consonant) and phone.manner == Manner.APPROXIMANT \
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return phone.place in [Place.PALATAL,
                               Place.LABIAL_VELAR,
                               Place.LABIAL_PALATAL,
                               Place.VELAR]
    return False


def show_backness(backness: Backness) -> str:
    """
    Provide user-readable text for the backness of
    a vowel.

    e.g. "central"
    """
    if backness == Backness.FRONT:
        return FRONT_BACKNESS_TEXT
    if backness == Backness.CENTRAL:
        return CENTRAL_BACKNESS_TEXT
    if backness == Backness.BACK:
        return BACK_BACKNESS_TEXT
    return "[Unrecognized vowel backness!]"


def show_height(height: Height) -> str:
    """
    Provide user readable text for reprsenting
    height of a vowel.

    e.g. "mid"
    """
    if height == Height.CLOSE:
        return CLOSE_HEIGHT_TEXT
    if height == Height.NEAR_CLOSE:
        return NEAR_CLOSE_HEIGHT_TEXT
    if height == Height.CLOSE_MID:
        return CLOSE_MID_HEIGHT_TEXT
    if height == Height.MID:
        return MID_HEIGHT_TEXT
    if height == Height.OPEN_MID:
        return OPEN_MID_HEIGHT_TEXT
    if height == Height.NEAR_OPEN:
        return NEAR_OPEN_HEIGHT_TEXT
    if height == Height.OPEN:
        return OPEN_HEIGHT_TEXT
    return "[Unrecognized vowel height!]"


def show_rounding(rounding: Rounding) -> str:
    """
    Provide user readable text for representing
    lip rounding.
    e.g. "rounded"
    """
    if rounding == Rounding.ROUNDED:
        return ROUNDED_ROUNDING_TEXT
    if rounding == Rounding.UNROUNDED:
        return UNROUNDED_ROUNDING_TEXT
    return "[Unrecognized rounding!]"


def show_place(place: Place) -> str:
    """
    Provide user readable text for representing
    the place of articulation.
    e.g. "bilabial"
    Convert place to a string that the user can read.
    """
    if place == Place.BILABIAL:
        return BILABIAL_PLACE_TEXT
    if place == Place.LABIODENTAL:
        return LABIODENTAL_PLACE_TEXT
    if place == Place.DENTAL:
        return DENTAL_PLACE_TEXT
    if place == Place.ALVEOLAR:
        return ALVEOLAR_PLACE_TEXT
    if place == Place.POSTALVEOLAR:
        return POSTALVEOLAR_PLACE_TEXT
    if place == Place.RETROFLEX:
        return RETROFLEX_PLACE_TEXT
    if place == Place.PALATAL:
        return PALATAL_PLACE_TEXT
    if place == Place.VELAR:
        return VELAR_PLACE_TEXT
    if place == Place.UVULAR:
        return UVULAR_PLACE_TEXT
    if place == Place.PHARYNGEAL:
        return PHARYNGEAL_PLACE_TEXT
    if place == Place.GLOTTAL:
        return GLOTTAL_PLACE_TEXT
    if place == Place.EPIGLOTTAL:
        return EPIGLOTTAL_PLACE_TEXT
    if place == Place.LABIAL_VELAR:
        return LABIALVELAR_PLACE_TEXT
    if place == Place.LABIAL_PALATAL:
        return LABIALPALATAL_PLACE_TEXT
    if place == Place.ALVEOLOPALATAL:
        return ALVEOLOPALATAL_PLACE_TEXT
    if place == Place.PALATOALVEOLAR:
        return PALATOALVEOLAR_PLACE_TEXT
    if isinstance(place, MultiPlace):
        return ' '.join(map(show_place, place.places()))
    return '[Error: unrecognized place!]'


def show_manner(manner1: Manner) -> str:
    """
    Provide user-readable text for representing
    the manner of articulation.
    """
    if manner1 == Manner.PLOSIVE:
        return PLOSIVE_MANNER_TEXT
    if manner1 == Manner.NASAL:
        return NASAL_MANNER_TEXT
    if manner1 == Manner.TRILL:
        return TRILL_MANNER_TEXT
    if manner1 == Manner.TAP_OR_FLAP:
        return TAP_OR_FLAP_MANNER_TEXT
    if manner1 == Manner.APPROXIMANT:
        return APPROXIMANT_MANNER_TEXT
    if manner1 == Manner.FRICATIVE:
        return FRICATIVE_MANNER_TEXT
    if manner1 == Manner.AFFRICATE:
        return AFFRICATE_MANNER_TEXT
    if manner1 == Manner.LATERAL_FRICATIVE:
        return LATERAL_FRICATIVE_MANNER_TEXT
    if manner1 == Manner.LATERAL_APPROXIMANT:
        return LATERAL_APPROXIMANT_MANNER_TEXT
    if manner1 == Manner.LATERAL_FLAP:
        return LATERAL_FLAP_MANNER_TEXT
    if manner1 == Manner.LATERAL:
        return LATERAL_MANNER_TEXT
    return "[Unrecognized manner!]"


def show_airstream(airstream_1: Airstream) -> str:
    """
    user-readable representation of a Airstream configuration.
    Converts an Airstream object to user-readable text.
    e.g. "pulmonic egressive"
    """
    if airstream_1 == Airstream.PULMONIC_EGRESSIVE:
        return PULMONIC_EGRESSIVE_AIRSTREAM_TEXT
    if airstream_1 == Airstream.CLICK:
        return CLICK_AIRSTREAM_TEXT
    if airstream_1 == Airstream.IMPLOSIVE:
        return IMPLOSIVE_AIRSTREAM_TEXT
    return "[Unrecognized airstream!]"


def show_vocal_folds(vocal_folds_1: VocalFolds) -> str:
    """
    user-readable text representation of a vocal fold configuration:
    e.g. "voiced", "creaky voiced"
    """
    if vocal_folds_1 == VocalFolds.VOICED:
        return VOICED_VOCAL_FOLDS_TEXT
    if vocal_folds_1 == VocalFolds.VOICELESS:
        return VOICELESS_VOCAL_FOLDS_TEXT
    if vocal_folds_1 == VocalFolds.VOICED_ASPIRATED:
        return VOICED_ASPIRATED_VOCAL_FOLDS_TEXT
    if vocal_folds_1 == VocalFolds.VOICELESS_ASPIRATED:
        return VOICELESS_ASPIRATED_VOCAL_FOLDS_TEXT
    if vocal_folds_1 == VocalFolds.CREAKY_VOICED:
        return CREAKY_VOICED_VOCAL_FOLDS_TEXT
    return "[Unrecognized vocal folds!]"


def show_phonet_inventory(inventory: PhonetInventory) -> str:
    """
    Prints all the phonemes from a list of phonemes without
    any spaces between it.
    :param inventory: an inventory of sounds (really just a list
    of sounds)
    :return: text containing the IPA representation of each
    phoneme in the phoneme inventory
    """
    return ''.join(map(show_phonet, inventory.contents))


def show_phonet(phonet: Phonet) -> str:
    """
    Provide user-readable text for a phonete.
    e.g. "voiced bilabial plosive pulmonic egressive"
    """
    if isinstance(phonet, Consonant):
        vocal_folds = phonet.vocal_folds
        place = phonet.place
        manner = phonet.manner
        airstream = phonet.airstream
        return ' '.join([show_vocal_folds(vocal_folds), show_place(place),
                         show_manner(manner), show_airstream(airstream), CONSONANT_TEXT])
    if isinstance(phonet, Vowel):
        height = phonet.height
        backness = phonet.backness
        rounding = phonet.rounding
        vocal_folds = phonet.vocal_folds
        return ' '.join([show_vocal_folds(vocal_folds), show_rounding(rounding),
                         show_height(height), show_backness(backness), VOWEL_TEXT])
    return "[Unrecognized kind of phonete!]"
