"""
Functions for manipulating phonemes, represented in international phonetic alphabet, or
as Sound Patterns of English features.
"""

from typing import Callable, List, Optional, Tuple, Iterator
from functools import partial

from lib_types import (Phonet, Height, Backness, Rounding, VocalFolds, AdvancedTongueRootFeature,
                       Polarity, Vowel, Consonant, Place, Manner, Airstream, PhonemeFeature,
                       MultiPlace, SyllabicFeature, ConsonantalFeature, SonorantFeature,
                       ContinuantFeature, VoiceFeature, NasalFeature, LateralFeature,
                       DelayedReleaseFeature, SpreadGlottisFeature, ConstrictedGlottisFeature,
                       LabialFeature, CoronalFeature, DorsalFeature, PharyngealFeature,
                       LaryngealFeature,
                       RoundFeature, AnteriorFeature, DistributedFeature, StridentFeature,
                       HighFeature,
                       LowFeature, BackFeature, PhonetInventory,
                       UnmarkableConsonant, UnmarkableVowel,
                       UnmarkablePlace, UnmarkableVocalFolds, MarkedVocalFolds, UnmarkedVocalFolds,
                       UnmarkedHeight, UnmarkedBackness, MarkedManner, MarkedPlace, UnmarkedPlace,
                       UnmarkedManner, UnmarkableManner, MarkedBackness, MarkedHeight,
                       UnmarkableHeight, UnmarkableBackness, UnmarkableAirstream, MarkedAirstream,
                       UnmarkedAirstream, UnmarkedRounding, MarkedRounding, UnmarkablePhonet,
                       UnmarkableRounding)

from english_us_text import (BACK_PHONEME_FEATURE_TEXT,
                             LOW_PHONEME_FEATURE_TEXT, HIGH_PHONEME_FEATURE_TEXT,
                             STRIDENT_PHONEME_FEATURE_TEXT, DISTRIBUTED_PHONEME_FEATURE_TEXT,
                             ANTERIOR_PHONEME_FEATURE_TEXT, ROUND_PHONEME_FEATURE_TEXT,
                             LARYNGEAL_PHONEME_FEATURE_TEXT, PHARYNGEAL_PHONEME_FEATURE_TEXT,
                             DORSAL_PHONEME_FEATURE_TEXT, CORONAL_PHONEME_FEATURE_TEXT,
                             LABIAL_PHONEME_FEATURE_TEXT, CONSTRICTED_GLOTTIS_PHONEME_FEATURE_TEXT,
                             SPREAD_GLOTTIS_PHONEME_FEATURE_TEXT,
                             DELAYED_RELEASE_PHONEME_FEATURE_TEXT,
                             LATERAL_PHONEME_FEATURE_TEXT, NASAL_PHONEME_FEATURE_TEXT,
                             ATR_PHONEME_FEATURE_TEXT, VOICE_PHONEME_FEATURE_TEXT,
                             CONTINUANT_PHONEME_FEATURE_TEXT, SONORANT_PHONEME_FEATURE_TEXT,
                             CONSONANTAL_PHONEME_FEATURE_TEXT, SYLLABIC_PHONEME_FEATURE_TEXT,
                             PLOSIVE_MANNER_TEXT, NASAL_MANNER_TEXT, TRILL_MANNER_TEXT,
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
                             VOWEL_TEXT, CONSONANT_TEXT, VOICELESS_ASPIRATED_VOCAL_FOLDS_TEXT,
                             VOICED_ASPIRATED_VOCAL_FOLDS_TEXT, VOICELESS_VOCAL_FOLDS_TEXT,
                             VOICED_VOCAL_FOLDS_TEXT, NO_ENGLISH_DESCRIPTION_FOUND_MESSAGE,
                             SORRY_UNABLE_TO_CALCULATE)


def ipa_text_to_phonet_list_report(text: str) -> str:
    """
    Given text containing international phonetic alphabet symbols
    returns text with every phonetic alphabet symbol or sequence
    of symbols for a sound
    followed by the description of the sound it represents.
    """
    phonet_list = ipa_text_to_phonet_list(text)
    return '\n'.join(map(ipa_and_phonet_format, phonet_list))


def ipa_and_phonet_format(
        transcription_and_phonet: Tuple[str, Optional[Phonet]]) -> str:
    """
    Given a string containing IPA, and its phonetic attributes (place, manner, etc.)
    construct a line of text with the IPA phoneme,
    and its name.
    :param transcription_and_phonet: a tuple, of an IPA phoneme (e.g. "p"), and
    the Phonet instance that represents it.
    :return: a line of text with the IPA text surrounded by "/" slashes. This represents
    a phoneme in IPA notation. Then its description or name in a natural language such
    as English.
    """
    ipa_text, phonet = transcription_and_phonet
    phonet_summary = show_phonet(phonet)
    if phonet_summary is None:
        phonet_summary = "(n/a)"
    return "/" + ipa_text + "/" + " " + phonet_summary


def ipa_text_to_phonet_list(
        text: str) -> List[Tuple[str, Optional[Phonet]]]:
    """
    Split IPA text into parts.
    :param text: text to split
    :return: a list of tuples of IPA text, and possible Phonet instances
    """
    ipa_chunks = list(filter(lambda x: len(x) > 0, split_by_phonetes(text)))
    phonetes = map(analyze_transcription, ipa_chunks)
    return list(zip(ipa_chunks, phonetes))


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


def split_by_phonetes(some_text: str) -> List[str]:
    """
    Splits text in the International Phonetic Alphabet by
    phones. This is also called tokenization.

    Note: it does not recognize affricates, unless a tie-bar
    is provided.
    """
    return parse_start(some_text)


def parse_start(some_text: str) -> List[str]:
    """
    Start parsing some IPA text, in order to
    chunk it into phonemes.
    :param some_text: some text in IPA
    :return: the same text but split into a list
    """
    return split_by_phonetes_prepostdiacrtic(some_text)


def split_by_phonetes_prediacritic(text: str) -> List[str]:
    """
    Handle situations where the diacritic character occurs
    before the main character.
    Handle strings like "ⁿd".
    If it doesn't find a main character with a diacritic before
    it, it will look for a diacritic after the main character.
    :param text: text that may contain text with prediacrtic
    :return: a list of IPA characters split
    """
    result: Optional[Tuple[str, str]] = prediacritic_parser_function(text)
    if result is None:
        return split_by_phonetes_postdiacrtic(text)
    return [result[0]] + parse_start(result[1])


def split_by_phonetes_prepostdiacrtic(text: str) -> List[str]:
    """
    Handle "ⁿdʰ", "ⁿdʷʰ" and other text strings
    where a phoneme is represented in IPA by
    a segmental preceded and followed by at least
    one diacritic
    """
    result: Optional[Tuple[str, str]] = prepostdiacritic_parser_function(text)
    if result is None:
        return split_by_phonetes_prediacritic(text)

    (chunk, rest) = result
    return [chunk] + parse_start(rest)


def split_by_phonetes_postdiacrtic(text: str) -> List[str]:
    """
    Try to split IPA text into a list of IPA text, each element
     representing phonemes. Handle "dʰ", etc.

    :param text: a string of IPA text not yet split into phonemes
    :return: a list of phonemes represented by IPA text
    """
    result: Optional[Tuple[str, str]] = postdiacritic_parser_function(text)

    if result is None:
        return split_by_phonetes_nondiacrtic(text)

    (chunk, rest) = result
    return [chunk] + parse_start(rest)


def split_by_phonetes_nondiacrtic(text: str) -> List[str]:
    """
    Handle "d", "t", etc. and situations where there is no diacritic.

    :param text: text containing IPA text
    :return: a list of phonemes
    """
    result: Optional[Tuple[str, str]] = nondiacritic_parser_function(text)
    if result is None:
        return [text]  # stop parsing!

    (chunk, rest) = result
    return [chunk] + parse_start(rest)


def nondiacritic_parser_function(text: str) -> Optional[Tuple[str, str]]:
    """
    Parse the part cont containing diacritic (except the tie-bar).
    :param text: text containing IPA
    :return: a tuple with the part parsed in the frist part, and the
    part not yet parsed after.
    """
    if len(text) > 0 and is_segmental(text[0]):
        if is_tie_bar_at(1, text):
            return text[:3], text[3:]
        return text[:1], text[1:]
    return None


def is_consonant_at(index: int, some_text: str) -> bool:
    """
    Whether the character in the string at a certain place,
    represents a consonant.
    :param index: an index within the range of 0, and the length of the string argument
    :param some_text: a text string
    :return: true if it is a consonant
    """
    return is_such_at(is_consonant, index, some_text)


def is_consonant(a_char: str) -> bool:
    """
    Whether a character is one that is used in the
    International Phonetic Alphabet to represent a
    consonant.
    """
    return elem_w(consonants)(a_char)


def is_segmental_at(index: int, some_text: str) -> bool:
    """
    Whether a character in some text, at a specific place
    within the text is a "segmental" (i.e. not a diacritic or modifier).
    """
    return is_such_at(is_segmental, index, some_text)


def is_segmental(a_char: str) -> bool:
    """
    Whether a character is one that is used in the
    International Phonetic Alphabet to represent something
    that is not a diacritic, and can stand on its own.
    This means characters that can represent a
    consonant or vowel.
    """
    return elem_w(strict_segmentals)(a_char)


def is_exponential_after_at(index: int, some_text: str) -> bool:
    """
    Whether a character is a diacritic that can go after
    the main character.
    :param index: a number indicating where the character is in the text
    :param some_text: the text that contains the character
    :return: true if the character can be a diacritic after the main character
    """
    return is_such_at(is_exponential_after, index, some_text)


def is_tie_bar_at(index: int, some_text: str) -> bool:
    """
    Whether a character at a certain place in a string,
    is the tie-bar diacritic.
    :param index: a number telling which character in the string
    :param some_text: the string (some text)
    :return: true if it is a tie-bar
    """
    return is_such_at(is_tie_bar, index, some_text)


def is_such_at(func: Callable[[str], bool], index: int, text: str) -> bool:
    """
    Whether a character at a string is of a certain class.
    :param func: a function
    :param index: a number indicating which character in the text
    :param text: a string
    :return: whether it is true
    """
    return index < len(text) and func(text[index])


def is_exponential_after(a_char: str) -> bool:
    """
    Whether a character is a superscript character, that
    often goes after a full character to modify the full
    character's meaning.
    For example in the International Phonetic Alphabet,
    a superscript `h` causes the phoneme represented by the
    previous character to
    be aspirated.
    """
    return elem_w(exponentials_after)(a_char)


def is_exponential_before(a_char: str) -> bool:
    """
    ًWhether a character is a diacritic that can go
    before a main character.
    """
    return elem_w(exponentials_before)(a_char)


def is_tie_bar(a_character: str) -> bool:
    """
    Whether a character is used to tie two characters in the
    international phonetic alphabet together. The tie bar is
    usually used to indicate an affricate, or double-articulation.
    """
    return a_character in ['͜', '͡']


def elem_w(string_list: List[str]) -> Callable[[str], bool]:
    """
    Create a function that sees whether
    a character is equal to (the first character in) an element
    in a list of text
    """
    return lambda x: x in map(lambda y: y[0], string_list)


def prediacritic_parser_function(text: str) -> Optional[Tuple[str, str]]:
    """
    Gets a pre-diacritic exponential with a segmental,
    the segmental may have a tie bar.
    If it has a tie-bar the character after the tie-bar
    is also included. These
    are returned in the first part of the tuple.
    the text not yet parsed is in the second part
    of the tuple.
    """
    if (not len(text) == 0 and is_exponential_before(text[0])
            and is_segmental_at(1, text)):
        if is_tie_bar_at(2, text):
            return text[:4], text[4:]  # include tie bar and character after it.
        return text[:2], text[2:]
    return None


def prepostdiacritic_parser_function(text: str) -> Optional[Tuple[str, str]]:
    """
    Parse text that contains IPA text, can parse the next phoneme
    even if it contains diacritics before and after the main character.
    :param text: text to parse
    :return: a tuple or nothing. The first part of the tuple is a parsed
    phoneme, the second part is the part of the text not parsed yet
    """
    preresult: Optional[Tuple[str, str]] = prediacritic_parser_function(text)

    if preresult is None:
        return None
    (prepart, middle) = preresult
    if is_exponential_after_at(0, middle):
        length_of_first: int = len(prepart)
        segmental: str = prepart[(length_of_first - 1):]
        postresult: Optional[Tuple[str, str]] = postdiacritic_parser_function(segmental + middle)
        if postresult is None:
            return None
        (postpart, rest) = postresult
        return prepart + postpart[1:], rest
    return None


def postdiacritic_parser_function(text: str) -> Optional[Tuple[str, str]]:
    """
    Parse IPA text that can contain a diacritic after.
    :param text: text to attempt to parse
    :return: nothing if it was not parsable, otherwise a tuple with what
    was parsed first (IPA text representing a phoneme), and the part not
    parsed yet after.
    """
    if is_segmental_at(0, text) and is_exponential_after_at(1, text):
        number_of_postdiacritics: int = count_post_diacritics_in_a_row(text, 1)
        chunk_length: int = number_of_postdiacritics + 1
        return text[:chunk_length], text[chunk_length:]
    if is_segmental_at(0, text) and is_tie_bar_at(1, text) and is_exponential_after_at(2, text):
        number_of_postdiacritics: int = count_post_diacritics_in_a_row(text, 3)
        chunk_length: int = number_of_postdiacritics + 3
        return text[:chunk_length], text[chunk_length:]
    return None


def count_post_diacritics_in_a_row(some_text: str, start_index: int) -> int:
    """
    Count how many superscript characters occur one after another, at a
    specific place in a text (that could modify a previous character).
    """
    if is_exponential_after_at(start_index, some_text):
        return 1 + count_post_diacritics_in_a_row(some_text, (start_index + 1))
    return 0


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


def english_phonet_inventory() -> PhonetInventory:
    """
    This is a list of the sounds of English. Just the basic ones.
    It is somewhat more complicated in reality, but for now this will
    suffice.
    This following sound inventory of English is from page 20 of
    (2013, Elizabeth C. Zsiga, The Sounds of Language)
    """
    return PhonetInventory(
        [
            Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.LABIODENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.AFFRICATE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.AFFRICATE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.NASAL,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.NASAL,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.VELAR, Manner.NASAL,
                      Airstream.PULMONIC_EGRESSIVE),

            # The Postalveolar version is technically correct, even though the convention
            # is to write it in IPA as if it were alveolar. See
            # Wikipedia article titled "Voiced alveolar and postalveolar approximants"
            # at the following URL:
            # https://en.wikipedia.org/wiki/Voiced_alveolar_and_postalveolar_approximants
            Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.LABIAL_VELAR, Manner.APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),

            Vowel(Height.CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),  # "i"
            Vowel(Height.CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),  # "u"

            # Near-close Vowels:
            Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ɪ"
            Vowel(Height.NEAR_CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),  # "ʊ"

            # Close-mid Vowels:
            Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),  # "e"
            Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),  # "o"

            # Mid Vowels:
            Vowel(Height.MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ə"

            # Open-mid Vowels:
            Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ɛ"
            Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ɜ"
            Vowel(Height.OPEN_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ʌ"
            Vowel(Height.OPEN_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),  # "ɔ"

            # Near-open
            Vowel(Height.NEAR_OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),  # "æ"
            Vowel(Height.NEAR_OPEN, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ɐ"

            # Open Vowels:
            Vowel(Height.OPEN, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED),  # "ɑ"
            Vowel(Height.OPEN, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED)  # "ɒ"
        ]
    )


exponentials_before: List[str] = ["ⁿ"]

diacritics_and_suprasegmentals: List[str] = \
    ["̥",  # Voiceless
     "̊",  # Voiceless (diacritic placed above symbol with descender)
     "̤",  # Breathy voiced
     # End of first row.
     "̬",  # Voiced
     "̰",  # Creaky voiced
     "̺",  # Apical
     # End of second row.
     "ʰ",  # Aspirated
     "̼",  # Linguolabial
     "̻",  # Laminal
     # End of third row.
     "̹",  # More rounded
     "ʷ",  # Labialised
     "̃",  # Nasalised
     # End of fourth row.
     "̜",  # Less rounded
     "ʲ",  # Palatalised
     "ⁿ",  # Pre/post nasalised
     "̟",  # Advanced
     "ˠ",  # Velarised
     "ˡ",  # Lateral release
     "̠",  # Retracted
     "ˤ",  # Pharyngealised
     "̚",  # No audible release
     "̈",  # Centralised
     "̽",  # Mid centralised
     "̝",  # Raised
     "̩",  # Syllabic
     "̞",  # Lowered
     "̯",  # Non-syllabic
     "̘",  # Advanced tongue root
     "˞",  # Rhoticity
     "̙",  # Retracted tongue root
     "ʼ",  # Ejective
     "̍",  # Syllabic (diacritic placed above)
     "̪",  # Dental
     "̣",  # Closer variety/Fricative
     "̇"  # Palatalization/Centralization
     ]

exponentials_after: List[str] = diacritics_and_suprasegmentals + ["ː", "ˑ"]

# To do: find a more suitable name than exponentials.
# They only look like exponentials if you consider how they
# look similar to mathematical notation for exponentials.
# Really, they should be named something different.
exponentials: List[str] = exponentials_before + exponentials_after


def is_exponential(character: str) -> bool:
    """
    Whether an IPA character is written above the base line
    and to the right of the previous character,
    like how exponents of a power are written
    in mathematical notation.
    """
    return character in exponentials


def is_diacritic_above(some_text: str) -> bool:
    """
    Whether a diacritic goes above
    the character it is placed on.
    """
    if some_text == "̊":
        return True
    return False


def is_diacritic_below(some_text: str) -> bool:
    """
    Whether a diacritic goes below
    the character which it is placed on.
    """
    if some_text == "̥":
        return True
    return False


def lower_diacritic(some_text: str) -> str:
    """
    When given a diacritic that goes above,
    replaces it with one that goes below,
    and has the same meaning.
    otherwise does nothing.
    """
    if some_text == "̊":
        return "̥"
    return some_text


def raise_diacritic(some_diacritic: str) -> str:
    """
    When given a diacritic that goes below,
    replaces it with one that goes below, and
    has the same meaning;
    otherwise it does nothing.
    """
    if some_diacritic == "̥":
        return "̊"
    return some_diacritic


# Whether a character (but not a diacritic)
# takes up space
# below the imaginary horizontal line
# on which it is written.
#
# This could be useful later for determining
# where to put diacritics so that
# they are readable.

ascenders: List[str] = \
    ["b", "t", "d", "k", "ʔ", "f", "θ", "ð", "ħ", "ʕ", "h", "ɦ", "ɬ", "l", "ʎ",
     "ʘ", "ɓ", "ǀ", "ɗ", "ǃ", "ǂ", "ɠ", "ʄ", "ǁ", "ʛ", "ɺ", "ʢ", "ʡ", "ɤ", "ʈ", "ɖ",
     "ɸ", "β", "ʃ", "ɮ", "ɭ", "ɧ"]


def is_ascender(character: str) -> bool:
    return character in ascenders


descenders: List[str] = \
    ["p", "ɟ", "g", "q", "ɱ", "ɽ", "ʒ", "ʂ", "ʐ", "ç", "ʝ", "ɣ", "χ", "ɻ", "j",
     "ɰ", "ɥ", "y", "ɳ", "ɲ", "ŋ", "ʈ", "ɖ", "ɸ", "β", "ʃ", "ɮ", "ɧ"]


# We don't include the retroflex l i.e <ɭ> a a descender
# because, even though it is a descender,
# There is more free space under it than above


def is_descender(character: str) -> bool:
    """
    Whether a character (but not a diacritic)
    takes up space
    below the imaginary horizontal line
    on which it is written.

    This could be useful later for determining
    where to put diacritics so that
    they are readable.
    """
    return character in descenders


def prevent_prohibited_combination(some_text: str) -> str:
    """
    Prevent placement of diacritics below a full-width
    character,
    when doing so would likely make the result
    difficult to read, whenever there is another
    diacritic with the same meaning, but can go above.
    And vice-versa (above - below).

    Only support the voiceless diacritic so far.
    """
    if len(some_text) == 0:
        return ""
    if len(some_text) == 1:
        return some_text
    first_character: str = some_text[0]
    second_character: str = some_text[1]
    rest = some_text[2:]
    if is_ascender(first_character) and is_diacritic_above(second_character):
        return first_character + lower_diacritic(second_character) + rest
    if is_descender(first_character) and is_diacritic_below(second_character):
        return first_character + raise_diacritic(second_character) + rest
    return some_text


plosivePulmonic: List[str] = \
    ["p", "b", "t", "d",
     "ʈ", "ɖ", "c", "ɟ", "k", "g", "q", "ɢ",
     "ʔ"]

nasalPulmonic: List[str] = ["m", "ɱ", "n", "ɳ", "ɲ", "ŋ", "ɴ"]

trillPulmonic: List[str] = ["ʙ", "r", "ʀ"]

tapOrFlapPulmonic: List[str] = ["ⱱ", "ɾ", "ɽ"]

fricativePulmonic: List[str] \
    = \
    ["ɸ", "β", "f", "v", "θ", "ð", "s", "z", "ʃ", "ʒ",
     "ʂ", "ʐ", "ç", "ʝ", "x", "ɣ", "χ", "ʁ", "ħ", "ʕ",
     "h", "ɦ"
     ]

lateral_fricative_pulmonic: List[str] = ["ɬ", "ɮ"]

approximant_pulmonic: List[str] = ["ʋ", "ɹ", "ɻ", "j", "ɰ"]

lateral_approximant_pulmonic: List[str] = ["l", "ɭ", "ʎ", "ʟ"]

# CONSONANTS (PULMONIC)
consonants_pulmonic: List[str] \
    = plosivePulmonic \
      + nasalPulmonic \
      + trillPulmonic \
      + tapOrFlapPulmonic \
      + fricativePulmonic \
      + lateral_fricative_pulmonic \
      + approximant_pulmonic \
      + lateral_approximant_pulmonic

consonants_nonpulmonic: List[str] = \
    ["ʘ",
     "ɓ",  # Bilabial
     "ǀ",  # Dental
     "ɗ",  # Dental/alveolar
     "ǃ",  # (Post)alveolar
     "ʄ",
     "ǂ",
     "ɠ",
     "ǁ",
     "ʛ"
     ]

other_symbols: List[str] = \
    ["ʍ", "ɕ",
     "w", "ʑ",
     "ɥ", "ɺ",
     "ʜ", "ɧ",
     "ʢ",
     "ʡ",
     ]

vowels: List[str] = \
    ["i", "y", "ɨ", "ʉ", "ɯ", "u",  # Close
     "ɪ", "ʏ", "ʊ",  # Close-mid
     "e", "ø", "ɘ", "ɵ", "ɤ", "o",  # Open-mid
     "ə",
     "ɛ", "œ", "ɜ", "ɞ", "ʌ", "ɔ",  # Open-mid
     "æ", "ɐ",
     "a", "ɶ", "ɑ", "ɒ"  # Open
     ]

suprasegmentals: List[str] = \
    ["ˈ",  # Primary stress
     "ˌ",  # Secondary stress
     "ː",  # Long
     "ˑ",  # Half long
     "̆",  # Extra short
     "|",  # Minor (foot) group
     "‖",  # Major (intonation) group
     ".",  # Syllable break
     "‿",  # Linking (absence of a break)
     ]

tone_and_word_accents: List[str] = \
    [  # Level:
        "˥", "̋",  # Extra high level accent
        "˦", "́",  # High level accent
        "˧", "̄",  # Mid level accent
        "˨", "̀",  # Low level accent
        "˩", "̏",  # Extra low accent
        "ꜜ",  # Downstep
        "ꜛ",  # Upstep

        # Contour:
        "̌",  # Rising contour accent
        "̂",  # Falling contour accent
        "᷄",  # High rising contour accent
        "᷅",  # Low rising contour accent
        "᷈",  # Rising-falling contour accent
        "↗",  # Global rise
        "↘"  # Global fall
    ]

graphemes_of_ipa: List[str] = \
    consonants_pulmonic \
    + consonants_nonpulmonic \
    + other_symbols \
    + vowels \
    + suprasegmentals \
    + tone_and_word_accents \
    + diacritics_and_suprasegmentals
# See:
# www.internationalphoneticassociation.org/sites/default/files/IPA_Kiel_2015.pdf
# For the source of this information..

consonants: List[str] = consonants_pulmonic + consonants_nonpulmonic + other_symbols

""" IPA text that is not a semantic modifier to what is before or after it.
    This includes vowels, and consonants. It excludes all diacritics.
"""
strict_segmentals: List[str] = consonants + vowels


#  This function will allow us to convert an IPA symbol
#  to its analyzed form (its phonetic features)

# Plosives:
def analyze_transcription(ipa_text: str) -> Optional[Phonet]:
    """
    Given 1 two or 3 characters of text in the Internaional Phonetic Alphabet,
    it returns the phone it represents (as a statically typed description of its properties).
    """
    if ipa_text == "p":
        return Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "b":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "t":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "d":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʈ":
        return Consonant(VocalFolds.VOICELESS, Place.RETROFLEX, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɖ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "c":
        return Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɟ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "k":
        return Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "g":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "q":
        return Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɢ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʔ":
        return Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)

    # Nasals:
    if ipa_text == "m":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɱ":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "n":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɳ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɲ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ŋ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɴ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE)

    # Trills:
    if ipa_text == "ʙ":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.TRILL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "r":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.TRILL,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʀ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.TRILL,
                         Airstream.PULMONIC_EGRESSIVE)

    # Taps or flaps:
    if ipa_text == "ⱱ":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.TAP_OR_FLAP,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɾ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.TAP_OR_FLAP,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɽ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.TAP_OR_FLAP,
                         Airstream.PULMONIC_EGRESSIVE)

    # Fricatives:
    if ipa_text == "ɸ":
        return Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "β":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "f":
        return Consonant(VocalFolds.VOICELESS, Place.LABIODENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "v":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "θ":
        return Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ð":
        return Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "s":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "z":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʃ":
        return Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʒ":
        return Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʂ":
        return Consonant(VocalFolds.VOICELESS, Place.RETROFLEX, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʐ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ç":
        return Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʝ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "x":
        return Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɣ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "χ":
        return Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʁ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ħ":
        return Consonant(VocalFolds.VOICELESS, Place.PHARYNGEAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʕ":
        return Consonant(VocalFolds.VOICED, Place.PHARYNGEAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "h":
        return Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɦ":
        return Consonant(VocalFolds.VOICED, Place.GLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)

    # Lateral Fricatives:
    if ipa_text == "ɬ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.LATERAL_FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɮ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)

    # Approximants:
    if ipa_text == "ʋ":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɹ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɻ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "j":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɰ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)

    # Lateral Approximants:
    if ipa_text == "l":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɭ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʎ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʟ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)

    # Affricates
    if ipa_text in ["t͡ʃ", "t͜ʃ"]:
        return Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.AFFRICATE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text in ["d͡ʒ", "d͜ʒ"]:
        return Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.AFFRICATE,
                         Airstream.PULMONIC_EGRESSIVE)
    # We should probably enforce use of the tie-bar underneath, otherwise
    # it would not be deterministic to determine whether two graphemes here
    # represent affricates or a plosive followed by a fricative.

    # Under the Other Symbols part of the IPA chart:

    if ipa_text == "w":
        return Consonant(VocalFolds.VOICED, Place.LABIAL_VELAR, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʍ":
        return Consonant(VocalFolds.VOICELESS, Place.LABIAL_VELAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɥ":
        return Consonant(VocalFolds.VOICED, Place.LABIAL_PALATAL, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʜ":
        return Consonant(VocalFolds.VOICELESS, Place.EPIGLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʢ":
        return Consonant(VocalFolds.VOICED, Place.EPIGLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʡ":
        return Consonant(VocalFolds.VOICELESS, Place.EPIGLOTTAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    # Is the epiglottal plosive voiceless? The IPA chart does not specify.
    if ipa_text == "ɕ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLOPALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ʑ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLOPALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɺ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_FLAP,
                         Airstream.PULMONIC_EGRESSIVE)
    if ipa_text == "ɧ":
        return Consonant(VocalFolds.VOICELESS, MultiPlace([Place.POSTALVEOLAR, Place.VELAR]),
                         Manner.FRICATIVE, Airstream.PULMONIC_EGRESSIVE)

    # Other Consonants:
    if ipa_text == "ʘ":
        return Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE, Airstream.CLICK)
    if ipa_text == "ǀ":
        return Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.PLOSIVE, Airstream.CLICK)
    if ipa_text == "ǃ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE, Airstream.CLICK)
    #  "ǃ" could also be PostAlveolar.
    if ipa_text == "ǂ":
        return Consonant(VocalFolds.VOICELESS, Place.PALATOALVEOLAR, Manner.PLOSIVE,
                         Airstream.CLICK)
    if ipa_text == "ǁ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.LATERAL, Airstream.CLICK)
    if ipa_text == "ɓ":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE, Airstream.IMPLOSIVE)
    if ipa_text == "ɗ":
        return Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.PLOSIVE, Airstream.IMPLOSIVE)
    # "ɗ" could also be Alveolar
    if ipa_text == "ʄ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE, Airstream.IMPLOSIVE)
    if ipa_text == "ɠ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE, Airstream.IMPLOSIVE)
    if ipa_text == "ʛ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.PLOSIVE, Airstream.IMPLOSIVE)

    # Close Vowels:
    if ipa_text == "i":
        return Vowel(Height.CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "y":
        return Vowel(Height.CLOSE, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɨ":
        return Vowel(Height.CLOSE, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ʉ":
        return Vowel(Height.CLOSE, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɯ":
        return Vowel(Height.CLOSE, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "u":
        return Vowel(Height.CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED)

    # Near-close Vowels:
    if ipa_text == "ɪ":
        return Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ʏ":
        return Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ʊ":
        return Vowel(Height.NEAR_CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED)

    # Close-mid Vowels:
    if ipa_text == "e":
        return Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ø":
        return Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɘ":
        return Vowel(Height.CLOSE_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɵ":
        return Vowel(Height.CLOSE_MID, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɤ":
        return Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "o":
        return Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED)

    # Mid Vowels:
    if ipa_text == "ə":
        return Vowel(Height.MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED)

    # Open-mid Vowels:
    if ipa_text == "ɛ":
        return Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "œ":
        return Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɜ":
        return Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɞ":
        return Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ʌ":
        return Vowel(Height.OPEN_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɔ":
        return Vowel(Height.OPEN_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED)

    # Near-open
    if ipa_text == "æ":
        return Vowel(Height.NEAR_OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɐ":
        return Vowel(Height.NEAR_OPEN, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED)

    # Open Vowels:
    if ipa_text == "a":
        return Vowel(Height.OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɶ":
        return Vowel(Height.OPEN, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɑ":
        return Vowel(Height.OPEN, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED)
    if ipa_text == "ɒ":
        return Vowel(Height.OPEN, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED)

    # Handle Diacritics:

    if len(ipa_text) > 0:
        if ipa_text[-1] == "̥" or ipa_text[-1] == "̊":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            if full_grapheme is not None:
                if isinstance(full_grapheme, Consonant):
                    place = full_grapheme.place
                    manner = full_grapheme.manner
                    airstream = full_grapheme.airstream

                    return Consonant(VocalFolds.VOICELESS, place, manner, airstream)
                if isinstance(full_grapheme, Vowel):
                    height = full_grapheme.height
                    backness = full_grapheme.backness
                    rounding = full_grapheme.rounding
                    return Vowel(height, backness, rounding, VocalFolds.VOICELESS)
            return None
        if ipa_text[-1] == "̬":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            if full_grapheme is None:
                return None
            if isinstance(full_grapheme, Consonant):
                place = full_grapheme.place
                manner = full_grapheme.manner
                airstream = full_grapheme.airstream
                return Consonant(VocalFolds.VOICED, place, manner, airstream)
            if isinstance(full_grapheme, Vowel):
                height = full_grapheme.height
                backness = full_grapheme.backness
                rounding = full_grapheme.rounding
                return Vowel(height, backness, rounding, VocalFolds.VOICED)
            return full_grapheme
        if ipa_text[-1] == "ʰ":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            if isinstance(full_grapheme, Consonant) \
                    and full_grapheme.vocal_folds == VocalFolds.VOICED:
                place = full_grapheme.place
                manner = full_grapheme.manner
                airstream = full_grapheme.airstream
                return Consonant(VocalFolds.VOICED_ASPIRATED, place, manner, airstream)
            if isinstance(full_grapheme, Consonant) \
                    and full_grapheme.vocal_folds == VocalFolds.VOICELESS:
                place = full_grapheme.place
                manner = full_grapheme.manner
                airstream = full_grapheme.airstream
                return Consonant(VocalFolds.VOICELESS_ASPIRATED, place, manner, airstream)
            if isinstance(full_grapheme, Vowel):
                height = full_grapheme.height
                backness = full_grapheme.backness
                rounding = full_grapheme.rounding
                voicing = full_grapheme.vocal_folds
                return Vowel(height, backness, rounding, voicing)
            return full_grapheme
            # (About the preceding line:) It is strange but we will just
            # do nothing if they give us an aspirated vowel.
            # since we have no way to represent it in the type system.
            # to do: determine
            # if the idea of an aspirated vowel makes sense
        if ipa_text[-1] == "̠":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            return retract_phonet(full_grapheme)
        return None  # not recognized.
    return None


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


def construct_transcription(phoneme: Phonet) -> str:
    """
    Given a phone, gives back its transcription in the International Phonetic Alphabet.
    """
    result = construct_transcription_recursively(3, 0, phoneme)
    if result is None:
        return "∅"
    return result


def construct_transcription_recursively(recursion_limit: int,
                                        recursion_level: int, phone: Phonet) -> Optional[str]:
    """
    Given a Phonet intance, construct the IPA transcription representing it.
    :param recursion_limit: a number to ensure the program always halts
    :param recursion_level: the current number of times this function has called itself,
    since it was called by another function.
    :param phone: a Phonet instance
    :return: an IPA text
    """
    if recursion_level == recursion_limit:
        return None
    # Plosives:
    if phone == Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "p"
    if phone == Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "b"
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "t"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "d"
    if phone == Consonant(VocalFolds.VOICELESS, Place.RETROFLEX, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʈ"
    if phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɖ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "c"
    if phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɟ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "k"
    if phone == Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "g"
    if phone == Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "q"
    if phone == Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɢ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʔ"  # Nasals (next line)::
    if phone == Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "m"
    if phone == Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɱ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "n"
    if phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɳ"
    if phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɲ"
    if phone == Consonant(VocalFolds.VOICED, Place.VELAR, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ŋ"
    if phone == Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.NASAL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɴ"  # Trills (next line)::
    if phone == Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.TRILL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʙ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.TRILL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "r"
    if phone == Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.TRILL,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʀ"  # Taps or flaps (next line)::
    if phone == Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.TAP_OR_FLAP,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ⱱ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.TAP_OR_FLAP,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɾ"
    if phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.TAP_OR_FLAP,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɽ"  # Fricatives (next line)::
    if phone == Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɸ"
    if phone == Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "β"
    if phone == Consonant(VocalFolds.VOICELESS, Place.LABIODENTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "f"
    if phone == Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "v"
    if phone == Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "θ"
    if phone == Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ð"
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "s"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "z"
    if phone == Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʃ"
    if phone == Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʒ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.RETROFLEX, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʂ"
    if phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʐ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ç"
    if phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʝ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "x"
    if phone == Consonant(VocalFolds.VOICED, Place.VELAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɣ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "χ"
    if phone == Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʁ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.PHARYNGEAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ħ"
    if phone == Consonant(VocalFolds.VOICED, Place.PHARYNGEAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʕ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "h"
    if phone == Consonant(VocalFolds.VOICED, Place.GLOTTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɦ"  # Lateral Fricatives (next line)::
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.LATERAL_FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɬ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɮ"  # Approximants (next line)::
    if phone == Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʋ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɹ"
    if phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɻ"
    if phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "j"
    if phone == Consonant(VocalFolds.VOICED, Place.VELAR, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɰ"  # Lateral Approximants (next line)::
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "l"
    if phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.LATERAL_APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɭ"
    if phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.LATERAL_APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʎ"
    if phone == Consonant(VocalFolds.VOICED, Place.VELAR, Manner.LATERAL_APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʟ"  # Affricates (next line):
    if phone == Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "t͡ʃ"
    if phone == Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "d͡ʒ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "p͡ɸ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "t͜s"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "d͡z"
    if phone == Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "k͡x"
    if phone == Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.AFFRICATE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "q͡χ"  # Under the Other Symbols part of the IPA chart:
    if phone == Consonant(VocalFolds.VOICED, Place.LABIAL_VELAR, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "w"
    if phone == Consonant(VocalFolds.VOICELESS, Place.LABIAL_VELAR, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʍ"
    if phone == Consonant(VocalFolds.VOICED, Place.LABIAL_PALATAL, Manner.APPROXIMANT,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɥ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.EPIGLOTTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʜ"
    if phone == Consonant(VocalFolds.VOICED, Place.EPIGLOTTAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʢ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.EPIGLOTTAL, Manner.PLOSIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʡ"  # Is the epiglottal plosive voiceless? The IPA chart
        # does not specify.
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLOPALATAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɕ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLOPALATAL, Manner.FRICATIVE,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ʑ"
    if phone == Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_FLAP,
                          Airstream.PULMONIC_EGRESSIVE):
        return "ɺ"
    #    if phone == Consonant(VocalFolds.VOICELESS,  (Places (PostAlveolar :| [Velar]))
    #                                        Fricative  PulmonicEgressive):
    #        return "ɧ" # Other Consonants:
    if phone == Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE, Airstream.CLICK):
        return "ʘ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.PLOSIVE, Airstream.CLICK):
        return "ǀ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE, Airstream.CLICK):
        return "ǃ"  # Or it could be PostAlveolar.
    if phone == Consonant(VocalFolds.VOICELESS, Place.PALATOALVEOLAR, Manner.PLOSIVE,
                          Airstream.CLICK):
        return "ǂ"
    if phone == Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.LATERAL, Airstream.CLICK):
        return "ǁ"
    if phone == Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE, Airstream.IMPLOSIVE):
        return "ɓ"
    if phone == Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.PLOSIVE, Airstream.IMPLOSIVE):
        return "ɗ"  # Or Alveolar
    if phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE, Airstream.IMPLOSIVE):
        return "ʄ"
    if phone == Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE, Airstream.IMPLOSIVE):
        return "ɠ"
    if phone == Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.PLOSIVE, Airstream.IMPLOSIVE):
        return "ʛ"  # Close Vowels (next line)::
    if phone == Vowel(Height.CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "i"
    if phone == Vowel(Height.CLOSE, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED):
        return "y"
    if phone == Vowel(Height.CLOSE, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɨ"
    if phone == Vowel(Height.CLOSE, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ʉ"
    if phone == Vowel(Height.CLOSE, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɯ"
    if phone == Vowel(Height.CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED):
        return "u"  # Near-close Vowels (next line)::
    if phone == Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɪ"
    if phone == Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ʏ"
    if phone == Vowel(Height.NEAR_CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ʊ"  # Close-mid Vowels (next line)::
    if phone == Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "e"
    if phone == Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ø"
    if phone == Vowel(Height.CLOSE_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɘ"
    if phone == Vowel(Height.CLOSE_MID, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ɵ"
    if phone == Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɤ"
    if phone == Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED):
        return "o"  # Mid Vowels (next line)::
    if phone == Vowel(Height.MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ə"  # Open-mid Vowels (next line)::
    if phone == Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɛ"
    if phone == Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED):
        return "œ"
    if phone == Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɜ"
    if phone == Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ɞ"
    if phone == Vowel(Height.OPEN_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ʌ"
    if phone == Vowel(Height.OPEN_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ɔ"  # Near-open (next line):
    if phone == Vowel(Height.NEAR_OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "æ"
    if phone == Vowel(Height.NEAR_OPEN, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɐ"  # Open Vowels (next line)::
    if phone == Vowel(Height.OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "a"
    if phone == Vowel(Height.OPEN, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ɶ"
    if phone == Vowel(Height.OPEN, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED):
        return "ɑ"
    if phone == Vowel(Height.OPEN, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED):
        return "ɒ"

    # The following two lines are commented out, because I am unsure
    # about their place of articulation:
    # if phone == Consonant(VocalFolds.VOICELESS,  Place.LABIAL_VELAR, Manner.AFFRICATE,
    #                     Airstream.PULMONIC_EGRESSIVE):
    #     return "k͡p"
    # if phone == Consonant(VocalFolds.VOICELESS, Place.PALATAL # (or PLACE.ALVEOLOPALATAL)
    #                     Manner.AFFRICATE, Airstream.PULMONIC_EGRESSIVE):
    #     return  "c͡ɕ"

    # If it can represent it as a single character it will
    # return the single character result (i.e. without diacritics),
    # otherwise
    # it will try to represent it in IPA with more than
    # one character
    if isinstance(phone, Consonant) and phone.place == Place.POSTALVEOLAR and \
            recursion_level < recursion_limit:
        vocal_folds = phone.vocal_folds
        manner = phone.manner
        airstream = phone.airstream
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     Consonant(vocal_folds,
                                                               Place.ALVEOLAR,
                                                               manner,
                                                               airstream))
        if result is None:
            return None
        return result + "̠"  # Add the diacritic for "retracted"

    # If there isn't a symbol, and the consonant we want is voiceless,
    # Just take the symbol for a voiced consonant,
    # and then put that diacritic that means voiceless after.
    # (The following two definitions are intended to implement that)
    # Add the small circle diacritic to consonants to make them voiceless.
    if isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICELESS \
            and recursion_level < recursion_limit:
        place = phone.place
        manner = phone.manner
        airstream = phone.airstream

        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     Consonant(VocalFolds.VOICED,
                                                               place,
                                                               manner,
                                                               airstream))
        if result is None:
            return None
        if is_descender(result):
            return result + "̊"  # add diacritic for voiceless that goes above
        return result + "̥"  # add diacritic for voiceless that goes below

    # Add the small circle diacritic to vowels to make them voiceless.
    if isinstance(phone, Vowel) and phone.vocal_folds == VocalFolds.VOICELESS \
            and recursion_level < recursion_limit:
        height = phone.height
        backness = phone.backness
        rounding = phone.rounding
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     Vowel(height,
                                                           backness,
                                                           rounding,
                                                           VocalFolds.VOICED))
        if result is None:
            return None
        if is_descender(result):
            return result + "̊"  # add diacritic for voiceless that goes above
        return result + "̥"  # add diacritic for voiceless that goes below

    # If there is no way to express a voiced consonant in a single
    # grapheme add a diacritic to the grapheme that represents
    # the voiceless counterpart.
    if isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICED \
            and recursion_level < recursion_limit:
        place = phone.place
        manner = phone.manner
        airstream = phone.airstream

        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     Consonant(VocalFolds.VOICELESS,
                                                               place,
                                                               manner,
                                                               airstream))
        if result is None:
            return None
        return result + "̬"
    if isinstance(phone, Vowel) and phone.vocal_folds == VocalFolds.VOICED \
            and recursion_level < recursion_limit:
        height = phone.height
        backness = phone.backness
        rounding = phone.rounding
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     Vowel(height, backness, rounding,
                                                           VocalFolds.VOICELESS))
        if result is None:
            return None
        return result + "̬"
    if (isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICED_ASPIRATED
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
            and recursion_level < recursion_limit):
        result = construct_transcription_recursively(
            recursion_limit,
            1 + recursion_level,
            deaspirate(phone))
        if result is None:
            return None
        return result + "ʰ"

    if (isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.VOICELESS_ASPIRATED
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
            and recursion_level < recursion_limit):
        result = construct_transcription_recursively(
            recursion_limit, 1 + recursion_level, deaspirate(phone))
        if result is None:
            return None
        return result + "ʰ"
    if (isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.CREAKY_VOICED
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
            and recursion_level < recursion_limit):
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level, decreak(phone))
        if result is not None:
            return result + "̰"
        return None
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


def construct_deconstruct(func: Callable[[Phonet], Phonet], some_text: str) -> str:
    """
    Given IPA text, converts it to a Phonet, applies a function,
    and then converts it to IPA text.

    This function wraps other functions so that they work for IPA text.
    :param func: a function from Phonet to Phonet
    :param some_text: IPA text
    :return: IPA text result
    """
    phonet: Optional[Phonet] = analyze_transcription(some_text)
    if phonet is None:
        return "∅"
    return construct_transcription(func(phonet))


def voiced_transcription(some_text: str) -> str:
    """
    Given some text in the International Phonetic Alphabet,
    it will convert it to its voiced counterpart.

    e.g. "t" will become "d"
    """
    return construct_deconstruct(voiced_phonet, some_text)


def devoiced_transcription(some_text: str) -> str:
    """
    Given some text in the International Phonetic Alphabet,
    it will convert it to its devoiced counterpart.

    e.g. "d" will become "t"
    """
    return construct_deconstruct(devoiced_phonet, some_text)


def spirantized_transcription(some_text: str) -> str:
    """
    Given some text in the International Phonetic Alphabet,
    it will convert it to its spirantized counterpart.

    e.g. "t" will become "θ"
    """
    return construct_deconstruct(spirantized_phonet, some_text)


def describe_transcription(some_text: str) -> str:
    """
    Return an english description of a phoneme,
    given a phoneme's representation in the
    international phonetic alphabet.
    """
    result = show_phonet(analyze_transcription(some_text))
    if result is None:
        return NO_ENGLISH_DESCRIPTION_FOUND_MESSAGE
    return result


# Go to Section 12.2 of the textbook to understand
# the concept of phonological features.


def relevant_binary(feature: Callable[[Polarity], PhonemeFeature],
                    other_feature: PhonemeFeature) -> bool:
    """
    Given a binary feature, and another feature.
    returns whether they are the same kind of feature.
    They don't have to be the same polarity.
    For example, [+voice] and [−voice] are mutually relevant features.
      As are [+sonorant] and [+sonorant].
      But [+sonorant] and [+voice] are not relevant because
    "voice" and "sonorant" are different.
    """
    return other_feature == feature(Polarity.PLUS) or other_feature == feature(Polarity.MINUS)


def binary_difference(feature: Callable[[Polarity], PhonemeFeature],
                      list1: List[PhonemeFeature],
                      list2: List[PhonemeFeature]) \
        -> Tuple[Optional[PhonemeFeature], Optional[PhonemeFeature]]:
    """
    Finds the difference between two lists of phoneme features with respect
    to a single Sound Patterns of English binary feature (e.g. +/-voice).
    """
    relevant_list_1 = list(filter(partial(relevant_binary, feature), list1))
    relevant_list_2 = list(filter(partial(relevant_binary, feature), list2))
    if relevant_list_1 == relevant_list_2:
        return None, None

    first_part = relevant_list_1[0] if len(relevant_list_1) > 0 else None
    second_part = relevant_list_2[0] if len(relevant_list_2) > 0 else None
    return first_part, second_part


def unary_difference(feature: PhonemeFeature,
                     list1: List[PhonemeFeature],
                     list2: List[PhonemeFeature]) \
        -> Tuple[Optional[PhonemeFeature], Optional[PhonemeFeature]]:
    """
    Finds the difference between two lists of phoneme features with respect
    to a single Sound Patterns of English unary feature (e.g. nasal).
    A unary feature is one that lacks polarity, that is it does not have +, or -.
    It is either present or is not present.
    """
    if (feature in list1) == (feature in list2):
        return None, None
    if feature in list1 and (feature not in list2):
        return feature, None
    return None, feature


def difference(list1: List[PhonemeFeature],
               list2: List[PhonemeFeature]) \
        -> List[Tuple[Optional[PhonemeFeature], Optional[PhonemeFeature]]]:
    """
    This function takes two lists of phoneme features
    and returns how they differ. Any phonemic
    feature present in one list, and absent in the other
    will be represented; and any phonemic
    feature that is positive in one list but absent
    in the other will be represented.
    """
    return \
        [binary_difference(SyllabicFeature, list1, list2),
         binary_difference(ConsonantalFeature, list1, list2),
         binary_difference(SonorantFeature, list1, list2),
         binary_difference(ContinuantFeature, list1, list2),
         binary_difference(VoiceFeature, list1, list2),
         binary_difference(AdvancedTongueRootFeature, list1, list2),
         unary_difference(NasalFeature(), list1, list2),
         unary_difference(LateralFeature(), list1, list2),
         unary_difference(DelayedReleaseFeature(), list1, list2),
         unary_difference(SpreadGlottisFeature(), list1, list2),
         unary_difference(ConstrictedGlottisFeature(), list1, list2),
         unary_difference(LabialFeature(), list1, list2),
         unary_difference(CoronalFeature(), list1, list2),
         unary_difference(DorsalFeature(), list1, list2),
         unary_difference(PharyngealFeature(), list1, list2),
         unary_difference(LaryngealFeature(), list1, list2),
         binary_difference(RoundFeature, list1, list2),
         binary_difference(AnteriorFeature, list1, list2),
         binary_difference(DistributedFeature, list1, list2),
         binary_difference(StridentFeature, list1, list2),
         binary_difference(HighFeature, list1, list2),
         binary_difference(LowFeature, list1, list2),
         binary_difference(BackFeature, list1, list2)
         ]


def syllabic(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Vowels are [+syllabic]
    Consonants (glides included) are [-syllabic].

    (Source: page 258)
    """
    if isinstance(phone, Vowel):
        return SyllabicFeature(Polarity.PLUS)
    if isinstance(phone, Consonant):
        return SyllabicFeature(Polarity.MINUS)
    return None


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


def consonantal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Vowels are [-consonantal].
    Glides are [-consonantal].
    Consonants (that are not glides) are [+consonantal].

    (Source: page 258)
    """
    if isinstance(phone, Vowel):
        return ConsonantalFeature(Polarity.MINUS)
    if isinstance(phone, Consonant):
        if is_glide(phone):
            return ConsonantalFeature(Polarity.MINUS)
        return ConsonantalFeature(Polarity.PLUS)
    return None


def sonorant(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Oral stops are [-sonorant].
    Affricates are [-sonorant].
    Fricatives are [-sonorant].
    Nasals are [+sonorant].
    Approximants are [+sonorant].
    Laterals are [+sonorant].
    Vowels are [+sonorant].
    Glides are [+sonorant].

    (Source: page 258)
    """
    if isinstance(phone, Consonant):
        if phone.manner in [Manner.PLOSIVE, Manner.AFFRICATE, Manner.FRICATIVE]:
            return SonorantFeature(Polarity.MINUS)
        if phone.manner in [Manner.NASAL, Manner.APPROXIMANT, Manner.LATERAL]:
            return SonorantFeature(Polarity.PLUS)
        if is_glide(phone):
            return SonorantFeature(Polarity.PLUS)
        return SonorantFeature(Polarity.MINUS)
    if isinstance(phone, Vowel):
        return SonorantFeature(Polarity.PLUS)
    return None


def continuant(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Oral stops are [-continuant].
    Nasals stops are [-continuant].
    Affricates are [-continuant].
    Fricatives are [+continuant].
    Approximants are [+continuant].
    Vowels are [+continuant].
    Glides are [+continuant].

    (Source: page 258)

      Aside: we do not define lateral approximants for [+/-continuant] because the
      textbook puts it in parentheses. Usually this means, it depends on
      the language under study or
      it depends on the linguist.
      Lateral approximants may be considered [+continuant]. (arguable)
      (see chart on page 259))
    """
    if isinstance(phone, Consonant) and phone.manner in [Manner.PLOSIVE,
                                                         Manner.NASAL,
                                                         Manner.AFFRICATE]:
        return ContinuantFeature(Polarity.MINUS)
    if isinstance(phone, Consonant) and phone.manner == Manner.APPROXIMANT:
        return ContinuantFeature(Polarity.PLUS)
    if isinstance(phone, Vowel):
        return ContinuantFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and is_glide(phone):
        return ContinuantFeature(Polarity.PLUS)
    return None


def nasal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Nasal consonants are [nasal].
    # to do: add support for nasal vowels.
    All other segments are not defined for [nasal].
    """
    if isinstance(phone, Consonant) and phone.manner == Manner.NASAL:
        return NasalFeature()
    return None


def lateral(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Lateral consonants are [lateral].
    Lateral approximant consonants are [lateral].
    Lateral fricative consonants are [lateral].
    Lateral flap consonants are [lateral].
    All other segments are not defined for [lateral].
    """
    if isinstance(phone, Consonant):
        if phone.manner in [Manner.LATERAL,
                            Manner.LATERAL_APPROXIMANT,
                            Manner.LATERAL_FRICATIVE,
                            Manner.LATERAL_FLAP]:
            return LateralFeature()
    return None


def delayed_release(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Affricates are [+delayed release].
    All other segments are [-delayed release].

    (Source: page 260)
    """
    if isinstance(phone, Consonant) and phone.manner == Manner.AFFRICATE:
        return DelayedReleaseFeature()
    return None


def labial(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Bilabial consonants are [labial].
    Labio-dental consonants are [labial].
    All other segments are undefined for [labial].

    (Source: page 264)
    """
    if isinstance(phone, Consonant):
        if phone.place == Place.BILABIAL or phone.place == Place.LABIODENTAL:
            return LabialFeature()
    return None


def coronal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Dentals are [coronal].
    Alveolars are [coronal] also.
    Alveolopalatals are [coronal] also.
    Retroflexes are [coronal] also.
    Palatals are [coronal] also.

    Post-alveolars are [coronal] also.

    All other sounds are undefined for [coronal].

    (Source: page 264)
    (The fact that Post-alveolar consonants are coronal is indicated by
     Table 12. on page 265.)
    """
    if isinstance(phone, Consonant) and phone.place in [Place.DENTAL,
                                                        Place.ALVEOLAR,
                                                        Place.ALVEOLOPALATAL,
                                                        Place.RETROFLEX,
                                                        Place.PALATAL,
                                                        Place.POSTALVEOLAR]:
        return CoronalFeature()
    return None


def dorsal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Palatals are [dorsal].

      Aside: alveolo-palatals do not seem to be dorsals,
      although the table 12.4 is confusing
      because it uses the IPA symbol for one.
      TODO: find more information on whether
      alveolo-palatals are [dorsal].

    Velars are [dorsal].
    Uvulars are [dorsal].
    All other segments are undefined for [dorsal].
    """
    if isinstance(phone, Consonant) \
            and phone.place in [Place.PALATAL, Place.VELAR, Place.UVULAR]:
        return DorsalFeature()
    return None


def pharyngeal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Pharyngeal fricatives are [pharyngeal].
    All other segments are undefined for [pharyngeal].

    (Source: page 264)
    """
    if isinstance(phone, Consonant) \
            and phone.place == Place.PHARYNGEAL and phone.manner == Manner.FRICATIVE:
        return PharyngealFeature()
    return None


def laryngeal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Glottal consonants are [laryngeal].
    All other segments are undefined for [laryngeal].

    (Source: page 265)
    """
    if isinstance(phone, Consonant) and phone.place == Place.GLOTTAL:
        return LaryngealFeature()
    return None


def voice(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Voiced Aspirated consonants are [+voice].
    Voiced consonants are [+voice].
    Voiced vowels are [+voice].
    All other segments are [-voice].
    """
    if isinstance(phone, Consonant):
        if phone.vocal_folds == VocalFolds.VOICELESS \
                and phone.place == Place.GLOTTAL \
                and phone.manner == Manner.PLOSIVE \
                and phone.airstream == Airstream.PULMONIC_EGRESSIVE:
            return VoiceFeature(Polarity.MINUS)  # The voiceless glottal plosive is [-voice]
        if phone.vocal_folds == VocalFolds.VOICED_ASPIRATED:
            return VoiceFeature(Polarity.PLUS)
        if phone.vocal_folds == VocalFolds.VOICED:
            return VoiceFeature(Polarity.PLUS)
        return VoiceFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) and phone.vocal_folds == VocalFolds.VOICED:
        return VoiceFeature(Polarity.PLUS)
    return VoiceFeature(Polarity.MINUS)


def spread_glottis(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Voiceless aspirated plosives are [spread glottis].
    Voiced aspirated plosives are [spread glottis].
    All other segments are not defined for [spread glottis].
    (Source: page 262)
    """
    if isinstance(phone, Consonant) \
            and phone.vocal_folds in [VocalFolds.VOICELESS_ASPIRATED,
                                      VocalFolds.VOICED_ASPIRATED] \
            and phone.manner == Manner.PLOSIVE:
        return SpreadGlottisFeature()
    return None


def constricted_glottis(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Ejectives have the feature [constricted glottis].
    Glottal stop have the feature [constricted glottis].
    Creaky voiced sonorants have the feature [constricted glottis].

    (Source: page 262)
    """
    if isinstance(phone, Consonant) and phone.place == Place.GLOTTAL \
            and phone.manner == Manner.PLOSIVE:
        return ConstrictedGlottisFeature()
    if isinstance(phone, Consonant) and phone.vocal_folds == VocalFolds.CREAKY_VOICED:
        if sonorant(phone) == SonorantFeature(Polarity.PLUS):
            return ConstrictedGlottisFeature()
        return None
    if isinstance(phone, Vowel) and phone.vocal_folds == VocalFolds.CREAKY_VOICED:
        if sonorant(phone) == SonorantFeature(Polarity.PLUS):
            return ConstrictedGlottisFeature()
        return None
    return None


def anterior(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Dentals are [+anterior].
    Alveolars are [+anterior].
    Post-alveolars are [-anterior].
    Retroflexes are [-anterior].
    Palatals are [-anterior].

    (Source: page 265)

    TODO: answer the question:
    Question: Are Alveolo-palatals [+anterior], or [-anterior]?
    Alveolo-palatals are [-anterior].
    (SOURCE: not found)
    """
    if isinstance(phone, Consonant) and phone.place in [Place.DENTAL, Place.ALVEOLAR]:
        return AnteriorFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place in [Place.POSTALVEOLAR,
                                                        Place.RETROFLEX,
                                                        Place.PALATAL,
                                                        Place.ALVEOLOPALATAL]:
        return AnteriorFeature(Polarity.MINUS)
    return None


def distributed(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Given a phonete, returns the relevant distributed Sound Patterns of
    English Phoneme feature.

    Returns either [+ distributed], [- distributed] or nothing.
    """
    if isinstance(phone, Consonant) and phone.place == Place.DENTAL:
        return DistributedFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.ALVEOLAR:
        return DistributedFeature(Polarity.MINUS)
    if isinstance(phone, Consonant) and phone.place == Place.POSTALVEOLAR:
        return DistributedFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.RETROFLEX:
        return DistributedFeature(Polarity.MINUS)
    if isinstance(phone, Consonant) and phone.place == Place.PALATAL:
        return DistributedFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.ALVEOLOPALATAL:
        return DistributedFeature(Polarity.PLUS)
    return None


def strident(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Alveolar fricatives are [+strident].
    Alveolar affricates are [+strident], also.
    Post-alveolar fricatives are [+strident], also.
    Post-alveolar affricates are [+strident], also.
    Labio-dental fricatives are [+strident] , also.
    Labio-dental affricates are [+strident] , also.
    Uvular fricatives are [+strident], also.
    Uvular affricates are [+strident], also.

    All other fricatives are [-strident].
    All other affricates are [-strident], also.

    All other segments are undefined for [+/-strident].

    (Source: page 266, under [+/-strident] heading, under the subsection
    "Natural classes".)
    """
    if isinstance(phone, Consonant) \
            and phone.place == Place.ALVEOLAR \
            and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]:
        return StridentFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) \
            and phone.place == Place.POSTALVEOLAR \
            and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]:
        return StridentFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) \
            and phone.place == Place.LABIODENTAL \
            and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]:
        return StridentFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) \
            and phone.place == Place.UVULAR \
            and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]:
        return StridentFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]:
        return StridentFeature(Polarity.MINUS)
    return None


def high(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Palatal consonants are [+high].
    Alveolo-palatal consonants are [+high].
    Velar consonants are [+high].

    Uvular consonants are [-high].
    All other consonants are undefined for [+/-high].
    Close vowels are [+high].
    Near-close vowels are [+high].
    All other vowels are [-high].
    """
    if isinstance(phone, Consonant) and phone.place == Place.PALATAL:
        return HighFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.ALVEOLOPALATAL:
        return HighFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.VELAR:
        return HighFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.UVULAR:
        return HighFeature(Polarity.MINUS)
    if isinstance(phone, Consonant):
        return None
    if isinstance(phone, Vowel) and phone.height == Height.CLOSE:
        return HighFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) and phone.height == Height.NEAR_CLOSE:
        return HighFeature(Polarity.PLUS)
    if isinstance(phone, Vowel):
        return HighFeature(Polarity.MINUS)
    return None


def low(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Uvular consonants are [+low].
    Pharyngeal consonants are [+low].
    Glottal consonants are [+low].
    All other consonants are undefined for [+/-low].
    Open vowels are [+low].
    Near open vowels are [+low].
    All other vowels are [-low].
    """
    if isinstance(phone, Consonant) and phone.place == Place.UVULAR:
        return LowFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.PHARYNGEAL:
        return LowFeature(Polarity.PLUS)
    if isinstance(phone, Consonant) and phone.place == Place.GLOTTAL:
        return LowFeature(Polarity.PLUS)
    if isinstance(phone, Consonant):
        return None
    if isinstance(phone, Vowel) and phone.height == Height.OPEN:
        return LowFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) and phone.height == Height.NEAR_OPEN:
        return LowFeature(Polarity.PLUS)
    if isinstance(phone, Vowel):
        return LowFeature(Polarity.MINUS)
    return None


def back(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Back vowels are [+back].
    Central vowels are [+back].
    Front vowels are [-back].
    All other segments are undefined for [+/-back].
    """
    if isinstance(phone, Vowel) and phone.backness == Backness.BACK:
        return BackFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) and phone.backness == Backness.CENTRAL:
        return BackFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) and phone.backness == Backness.FRONT:
        return BackFeature(Polarity.MINUS)
    return None


def lip_round(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Rounded vowels are [+round].
    All other vowels are [-round].
    All other segments are [-round].
    """
    if isinstance(phone, Vowel) and phone.rounding == Rounding.ROUNDED:
        return RoundFeature(Polarity.PLUS)
    if isinstance(phone, Vowel):
        return RoundFeature(Polarity.MINUS)
    return RoundFeature(Polarity.MINUS)


def atr(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Advanced tongue root
    """
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE_MID \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE \
            and phone.backness == Backness.BACK \
            and phone.rounding == Rounding.ROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE_MID \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.ROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE_MID \
            and phone.backness == Backness.BACK \
            and phone.rounding == Rounding.ROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.ROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.NEAR_OPEN \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.OPEN \
            and phone.backness == Backness.BACK \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.CLOSE \
            and phone.backness == Backness.CENTRAL \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.OPEN_MID \
            and phone.backness == Backness.BACK \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.NEAR_CLOSE \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.NEAR_CLOSE \
            and phone.backness == Backness.BACK \
            and phone.rounding == Rounding.ROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.OPEN_MID \
            and phone.backness == Backness.FRONT \
            and phone.rounding == Rounding.UNROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if isinstance(phone, Vowel) \
            and phone.height == Height.OPEN_MID \
            and phone.backness == Backness.BACK \
            and phone.rounding == Rounding.ROUNDED \
            and phone.vocal_folds == VocalFolds.VOICED:
        return AdvancedTongueRootFeature(Polarity.MINUS)
    return None


def feature_matrix(phonete: Phonet) -> List[Optional[PhonemeFeature]]:
    """
    Given a phoneme (representation)
    Gives a feature matrix.

    Note: to non-linguists, feature matrices
    are 1-dimensional, always displayed
    as a single column.

    For example:
    /phone/
    """
    return \
        [consonantal(phonete),
         syllabic(phonete),
         continuant(phonete),
         sonorant(phonete),
         delayed_release(phonete),
         anterior(phonete),
         distributed(phonete),
         strident(phonete),
         high(phonete),
         low(phonete),
         nasal(phonete),
         lateral(phonete),
         labial(phonete),
         coronal(phonete),
         dorsal(phonete),
         pharyngeal(phonete),
         laryngeal(phonete),
         back(phonete),
         lip_round(phonete),
         voice(phonete),
         atr(phonete),
         spread_glottis(phonete),
         constricted_glottis(phonete)
         ]


def analyze_features(phonete: Phonet) -> List[PhonemeFeature]:
    """
    A function that takes data representing
    how a phoneme is pronounced, and returns
    a list of phonemic features.
    """
    return list(filter(lambda x: x is not None, feature_matrix(phonete)))


def show_features(features: List[PhonemeFeature]) -> str:
    """
    Given a list of Sound Patterns of English phoneme features,
    print the phoneme features in their usual representation.
    e.g. [+ someFeature, - someOtherFeature, ...]
    """
    features_strings: Iterator[str] = map(show_phoneme_feature, features)
    return "[" + "; ".join(features_strings) + "]"


def to_text_features(phonete: Phonet) -> str:
    """
    Given a phonete, gets all the Sound Patterns of English
    features for the phonete. Then it
    provides the user readable representation of the phoneme.

    For example when given the phonete represented by /b/,
    it will return something like [+ someFeature, - someOtherFeature, ...]
    """
    features = analyze_features(phonete)
    return show_features(features)


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


def show_polarity(polarity: Polarity) -> str:
    """
    Text representation of the polarity of a sound
    patterns of English feature.
    e.g. +, or -
    """
    if polarity == Polarity.PLUS:
        return "+"
    if polarity == Polarity.MINUS:
        return "-"
    return "[Unrecognized polarity!]"


def show_phoneme_feature(feature: PhonemeFeature) -> str:
    """
    Provide a text representation of the Sound Patterns of English
    feature. For example: [+ voice]
    or [-voice]
    or [delayed release]
    """
    if isinstance(feature, SyllabicFeature):
        return show_polarity(feature.polarity) + SYLLABIC_PHONEME_FEATURE_TEXT
    if isinstance(feature, ConsonantalFeature):
        return show_polarity(feature.polarity) + CONSONANTAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, SonorantFeature):
        return show_polarity(feature.polarity) + SONORANT_PHONEME_FEATURE_TEXT
    if isinstance(feature, ContinuantFeature):
        return show_polarity(feature.polarity) + CONTINUANT_PHONEME_FEATURE_TEXT
    if isinstance(feature, VoiceFeature):
        return show_polarity(feature.polarity) + VOICE_PHONEME_FEATURE_TEXT
    if isinstance(feature, AdvancedTongueRootFeature):
        return show_polarity(feature.polarity) + ATR_PHONEME_FEATURE_TEXT
    if isinstance(feature, NasalFeature):
        return NASAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, LateralFeature):
        return LATERAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, DelayedReleaseFeature):
        return DELAYED_RELEASE_PHONEME_FEATURE_TEXT
    if isinstance(feature, SpreadGlottisFeature):
        return SPREAD_GLOTTIS_PHONEME_FEATURE_TEXT
    if isinstance(feature, ConstrictedGlottisFeature):
        return CONSTRICTED_GLOTTIS_PHONEME_FEATURE_TEXT
    if isinstance(feature, LabialFeature):
        return LABIAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, CoronalFeature):
        return CORONAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, DorsalFeature):
        return DORSAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, PharyngealFeature):
        return PHARYNGEAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, LaryngealFeature):
        return LARYNGEAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, RoundFeature):
        return show_polarity(feature.polarity) + ROUND_PHONEME_FEATURE_TEXT
    if isinstance(feature, AnteriorFeature):
        return show_polarity(feature.polarity) + ANTERIOR_PHONEME_FEATURE_TEXT
    if isinstance(feature, DistributedFeature):
        return show_polarity(feature.polarity) + DISTRIBUTED_PHONEME_FEATURE_TEXT
    if isinstance(feature, StridentFeature):
        return show_polarity(feature.polarity) + STRIDENT_PHONEME_FEATURE_TEXT
    if isinstance(feature, HighFeature):
        return show_polarity(feature.polarity) + HIGH_PHONEME_FEATURE_TEXT
    if isinstance(feature, LowFeature):
        return show_polarity(feature.polarity) + LOW_PHONEME_FEATURE_TEXT
    if isinstance(feature, BackFeature):
        return show_polarity(feature.polarity) + BACK_PHONEME_FEATURE_TEXT
    return "[Unrecognized phoneme feature!]"


# I added some English vowels. I did not choose any specific dialect.
# I got all my information from the Wikipedia page titled
# "English Phonology"
# at the following URL: https://en.wikipedia.org/wiki/English_phonology#Vowels
# on Monday, February 24, 2020.
# To do: Get better information on English vowels from a more reliable source.
# To do: model separate dialects of English or only one.


def show_transcription(inventory: PhonetInventory) -> str:
    """
    Creates text showing all the phonemes in a phoneme inventory.
    Each line shows a phoneme's International Phonetic Alphabet
    transcription, and its full English name.
    For example: one line may be thus:
    /b/  voiced bilabial plosive pulmonic egressive
    """
    phonetes: List[Phonet] = inventory.contents
    return ''.join(map(construct_transcription, phonetes))


english_phonet_inventory_report: str = ipa_text_to_phonet_list_report(
    show_transcription(english_phonet_inventory()))


def analyze_transcription_to_sound_patterns_of_english(transcription: str) -> str:
    """
    Given an IPA transcription of a phoneme,
    return text containing the Sound Patterns of English (SPE) features.
    :param transcription: IPA text
    :return: Sound Patterns of English text (between "[", "]")
    """
    result = show_features(analyze_features(analyze_transcription(transcription)))
    if result is None:
        return SORRY_UNABLE_TO_CALCULATE
    return result
