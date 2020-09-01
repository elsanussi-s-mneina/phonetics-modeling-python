from typing import Tuple, Optional, List, Callable

from english_us_text import NO_ENGLISH_DESCRIPTION_FOUND_MESSAGE, SORRY_UNABLE_TO_CALCULATE
from grapheme_grammar import split_by_phonetes, consonants_pulmonic, consonants_nonpulmonic, \
    other_symbols, vowels, diacritics_and_suprasegmentals
from language_specific.english_specific import english_phonet_inventory
from lib_functions import retract_phonet, deaspirate, decreak, \
    voiced_phonet, devoiced_phonet, spirantized_phonet, show_phonet
from lib_types import Phonet, Consonant, VocalFolds, Place, Manner, Airstream, MultiPlace, Vowel, \
    Height, Backness, Rounding, SecondaryArticulation, PhonetInventory, VowelLength
from phonetic_features import analyze_features, show_features

from lib_type_helpers import is_consonant, is_vowel, to_extra_short, to_alveolar, \
    to_half_long, to_normal_length, to_labialized, to_long, to_palatalized, to_pharyngealized, \
    to_velarized, \
    to_voiced, to_voiced_aspirated, to_voiceless, to_voiceless_aspirated


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


def is_ascender(character: str) -> bool:
    return character in ascenders


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


def append_voiceless_diacritic(ipa_text: str) -> str:
    """
    puts a voiceless diacritic after the last character,
    in IPA text. Determines whether to place the diacritic
    above or below the character.
    """
    if is_descender(ipa_text):
        return ipa_text + "̊"  # add diacritic for voiceless that goes above
    return ipa_text + "̥"  # add diacritic for voiceless that goes below


def append_voiced_diacritic(ipa_text: str) -> str:
    return ipa_text + "̬"


def append_aspiration_diacritic(ipa_text: str) -> str:
    return ipa_text + "ʰ"


def analyze_transcription(ipa_text: str) -> Optional[Phonet]:
    """
    This function will allow us to convert an IPA symbol
    to its analyzed form (its phonetic features)

    Given 1 two or 3 characters of text in the Internaional Phonetic Alphabet,
    it returns the phone it represents (as a statically typed description of its properties).
    """
    # Plosives:
    if ipa_text == "p":
        return Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "b":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "t":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "d":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʈ":
        return Consonant(VocalFolds.VOICELESS, Place.RETROFLEX, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɖ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "c":
        return Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɟ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "k":
        return Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "g":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "q":
        return Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɢ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʔ":
        return Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Nasals:
    if ipa_text == "m":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɱ":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "n":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɳ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɲ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ŋ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɴ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.NASAL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Trills:
    if ipa_text == "ʙ":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.TRILL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "r":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.TRILL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʀ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.TRILL,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Taps or flaps:
    if ipa_text == "ⱱ":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.TAP_OR_FLAP,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɾ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.TAP_OR_FLAP,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɽ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.TAP_OR_FLAP,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Fricatives:
    if ipa_text == "ɸ":
        return Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "β":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "f":
        return Consonant(VocalFolds.VOICELESS, Place.LABIODENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "v":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "θ":
        return Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ð":
        return Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "s":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "z":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʃ":
        return Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʒ":
        return Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʂ":
        return Consonant(VocalFolds.VOICELESS, Place.RETROFLEX, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʐ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ç":
        return Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʝ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "x":
        return Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɣ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "χ":
        return Consonant(VocalFolds.VOICELESS, Place.UVULAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʁ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ħ":
        return Consonant(VocalFolds.VOICELESS, Place.PHARYNGEAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʕ":
        return Consonant(VocalFolds.VOICED, Place.PHARYNGEAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "h":
        return Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɦ":
        return Consonant(VocalFolds.VOICED, Place.GLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Lateral Fricatives:
    if ipa_text == "ɬ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.LATERAL_FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɮ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Approximants:
    if ipa_text == "ʋ":
        return Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɹ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɻ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "j":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɰ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Lateral Approximants:
    if ipa_text == "l":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɭ":
        return Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʎ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʟ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.LATERAL_APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Affricates
    if ipa_text in ["t͡ʃ", "t͜ʃ"]:
        return Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.AFFRICATE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text in ["d͡ʒ", "d͜ʒ"]:
        return Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.AFFRICATE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    # We should probably enforce use of the tie-bar underneath, otherwise
    # it would not be deterministic to determine whether two graphemes here
    # represent affricates or a plosive followed by a fricative.

    # Under the Other Symbols part of the IPA chart:

    if ipa_text == "w":
        return Consonant(VocalFolds.VOICED, Place.LABIAL_VELAR, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʍ":
        return Consonant(VocalFolds.VOICELESS, Place.LABIAL_VELAR, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɥ":
        return Consonant(VocalFolds.VOICED, Place.LABIAL_PALATAL, Manner.APPROXIMANT,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʜ":
        return Consonant(VocalFolds.VOICELESS, Place.EPIGLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʢ":
        return Consonant(VocalFolds.VOICED, Place.EPIGLOTTAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʡ":
        return Consonant(VocalFolds.VOICELESS, Place.EPIGLOTTAL, Manner.PLOSIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    # Is the epiglottal plosive voiceless? The IPA chart does not specify.
    if ipa_text == "ɕ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLOPALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʑ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLOPALATAL, Manner.FRICATIVE,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɺ":
        return Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_FLAP,
                         Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɧ":
        return Consonant(VocalFolds.VOICELESS, MultiPlace([Place.POSTALVEOLAR, Place.VELAR]),
                         Manner.FRICATIVE, Airstream.PULMONIC_EGRESSIVE,
                         SecondaryArticulation.NORMAL)

    # Other Consonants:
    if ipa_text == "ʘ":
        return Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE, Airstream.CLICK,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ǀ":
        return Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.PLOSIVE, Airstream.CLICK,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ǃ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE, Airstream.CLICK,
                         SecondaryArticulation.NORMAL)
    #  "ǃ" could also be PostAlveolar.
    if ipa_text == "ǂ":
        return Consonant(VocalFolds.VOICELESS, Place.PALATOALVEOLAR, Manner.PLOSIVE,
                         Airstream.CLICK,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ǁ":
        return Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.LATERAL, Airstream.CLICK,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɓ":
        return Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE, Airstream.IMPLOSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɗ":
        return Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.PLOSIVE, Airstream.IMPLOSIVE,
                         SecondaryArticulation.NORMAL)
    # "ɗ" could also be Alveolar
    if ipa_text == "ʄ":
        return Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE, Airstream.IMPLOSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ɠ":
        return Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE, Airstream.IMPLOSIVE,
                         SecondaryArticulation.NORMAL)
    if ipa_text == "ʛ":
        return Consonant(VocalFolds.VOICED, Place.UVULAR, Manner.PLOSIVE, Airstream.IMPLOSIVE,
                         SecondaryArticulation.NORMAL)

    # Close Vowels:
    if ipa_text == "i":
        return Vowel(Height.CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "y":
        return Vowel(Height.CLOSE, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɨ":
        return Vowel(Height.CLOSE, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ʉ":
        return Vowel(Height.CLOSE, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɯ":
        return Vowel(Height.CLOSE, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "u":
        return Vowel(Height.CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Near-close Vowels:
    if ipa_text == "ɪ":
        return Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ʏ":
        return Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ʊ":
        return Vowel(Height.NEAR_CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Close-mid Vowels:
    if ipa_text == "e":
        return Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ø":
        return Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɘ":
        return Vowel(Height.CLOSE_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɵ":
        return Vowel(Height.CLOSE_MID, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɤ":
        return Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "o":
        return Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Mid Vowels:
    if ipa_text == "ə":
        return Vowel(Height.MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Open-mid Vowels:
    if ipa_text == "ɛ":
        return Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "œ":
        return Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɜ":
        return Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɞ":
        return Vowel(Height.OPEN_MID, Backness.CENTRAL, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ʌ":
        return Vowel(Height.OPEN_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɔ":
        return Vowel(Height.OPEN_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Near-open
    if ipa_text == "æ":
        return Vowel(Height.NEAR_OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɐ":
        return Vowel(Height.NEAR_OPEN, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Open Vowels:
    if ipa_text == "a":
        return Vowel(Height.OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɶ":
        return Vowel(Height.OPEN, Backness.FRONT, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɑ":
        return Vowel(Height.OPEN, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)
    if ipa_text == "ɒ":
        return Vowel(Height.OPEN, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED,
                     VowelLength.NORMAL)

    # Handle Diacritics:

    if len(ipa_text) > 0:
        if ipa_text[-1] == "̥" or ipa_text[-1] == "̊":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            if full_grapheme is not None:
                return to_voiceless(full_grapheme)
            return None
        if ipa_text[-1] == "̬":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            if full_grapheme is None:
                return None
            return to_voiced(full_grapheme)

        if ipa_text[-1] == "ʷ":
            full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
            if full_grapheme is None:
                return None

            if (is_consonant(full_grapheme)
                    and full_grapheme.secondary_articulation == SecondaryArticulation.NORMAL):
                return to_labialized(full_grapheme)
            if is_vowel(full_grapheme):
                return full_grapheme  # Should never happen, but let's just ignore it

        if ipa_text[-1] == "ʲ":
            full_grapheme = analyze_transcription(ipa_text[:-1])
            if full_grapheme is None:
                return None
            return to_palatalized(full_grapheme)

    if ipa_text[-1] == "ˠ":
        full_grapheme = analyze_transcription(ipa_text[:-1])

        if full_grapheme is None:
            return None
        return to_velarized(full_grapheme)

    if ipa_text[-1] == "ˤ":
        full_grapheme = analyze_transcription(ipa_text[:-1])
        if full_grapheme is None:
            return None
        return to_pharyngealized(full_grapheme)

    # Long
    if ipa_text[-1] == "ː":
        full_grapheme = analyze_transcription(ipa_text[:-1])
        if full_grapheme is None:
            return None
        return to_long(full_grapheme)

    if ipa_text[-1] == "ˑ":
        full_grapheme = analyze_transcription(ipa_text[:-1])
        if full_grapheme is None:
            return None
        return to_half_long(full_grapheme)

    if ipa_text[-1] == "̆":
        full_grapheme = analyze_transcription(ipa_text[:-1])
        if full_grapheme is None:
            return None
        return to_extra_short(full_grapheme) # Make the vowel extra-short, but ..
        #.. ignore consonants followed by an extra-short marker.

    if ipa_text[-1] == "ʰ":
        full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
        if is_consonant(full_grapheme):
            if full_grapheme.vocal_folds == VocalFolds.VOICED:
                return to_voiced_aspirated(full_grapheme)
            if full_grapheme.vocal_folds == VocalFolds.VOICELESS:
                return to_voiceless_aspirated(full_grapheme)
        return full_grapheme # vowels cannot be aspirated. So just ignore it.
        # (About the preceding line:) It is strange but we will just
        # do nothing if they give us an aspirated vowel.
        # since we have no way to represent it in the type system.
        # to do: determine
        # if the idea of an aspirated vowel makes sense
    if ipa_text[-1] == "̠":
        full_grapheme: Optional[Phonet] = analyze_transcription(ipa_text[:-1])
        return retract_phonet(full_grapheme)
    return None  # not recognized.


def construct_transcription(phoneme: Phonet) -> str:
    """
    Given a phone, gives back its transcription in the International Phonetic Alphabet.
    """
    result = construct_transcription_recursively(3, 0, phoneme)
    if result is None:
        return "∅"
    return result


def secondary_articulation_transcription(secondary_articulation: SecondaryArticulation):
    """convert a secondary articulation to its IPA text representation"""
    if secondary_articulation == secondary_articulation.NORMAL:
        return ""
    if secondary_articulation == SecondaryArticulation.LABIALIZED:
        return "ʷ"
    if secondary_articulation == SecondaryArticulation.PALATALIZED:
        return "ʲ"
    if secondary_articulation == SecondaryArticulation.VELARIZED:
        return "ˠ"
    if secondary_articulation == secondary_articulation.PHARYNGEALIZED:
        return "ˤ"
    return ""


def length_transcription(vowel_length: VowelLength) -> str:
    """
    Convert a vowel length into its IPA text representation.
    """
    if vowel_length == VowelLength.NORMAL:
        return ""
    if vowel_length == VowelLength.EXTRA_SHORT:
        return "̆"
    if vowel_length == VowelLength.HALF_LONG:
        return "ˑ"
    if vowel_length == VowelLength.LONG:
        return "ː"
    return ""



def construct_transcription_recursively(recursion_limit: int,
                                        recursion_level: int, phone: Phonet) -> Optional[str]:
    """
    Given a Phonet instance, construct the IPA transcription representing it.
    :param recursion_limit: a number to ensure the program always halts
    :param recursion_level: the current number of times this function has called itself,
    since it was called by another function.
    :param phone: a Phonet instance
    :return: an IPA text
    """
    if recursion_level == recursion_limit:
        return None
    # Plosives:
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "p" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "b" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "t" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "d" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʈ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone == Consonant(VocalFolds.VOICED, Place.RETROFLEX, Manner.PLOSIVE,
                               Airstream.PULMONIC_EGRESSIVE,
                               SecondaryArticulation.NORMAL):
        return "ɖ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone == Consonant(VocalFolds.VOICELESS, Place.PALATAL, Manner.PLOSIVE,
                               Airstream.PULMONIC_EGRESSIVE,
                               SecondaryArticulation.NORMAL):
        return "c" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone == Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.PLOSIVE,
                               Airstream.PULMONIC_EGRESSIVE,
                               SecondaryArticulation.NORMAL):
        return "ɟ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone == Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.PLOSIVE,
                               Airstream.PULMONIC_EGRESSIVE,
                               SecondaryArticulation.NORMAL):
        return "k" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "g" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "q" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɢ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.GLOTTAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʔ" + secondary_articulation_transcription(
            phone.secondary_articulation)

    # Nasals (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "m" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.LABIODENTAL and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɱ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "n" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɳ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.PALATAL and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɲ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ŋ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.NASAL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɴ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Trills (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.TRILL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʙ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.TRILL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "r" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.TRILL and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʀ" + secondary_articulation_transcription(
            phone.secondary_articulation)  # Taps or flaps (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.LABIODENTAL and \
            phone.manner == Manner.TAP_OR_FLAP and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ⱱ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.TAP_OR_FLAP and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE and \
            phone.secondary_articulation == SecondaryArticulation.NORMAL:
        return "ɾ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.TAP_OR_FLAP and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɽ" + secondary_articulation_transcription(
            phone.secondary_articulation)  # Fricatives (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɸ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "β" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.LABIODENTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "f" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.LABIODENTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "v" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.DENTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "θ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.DENTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ð" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "s" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "z" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.POSTALVEOLAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʃ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.POSTALVEOLAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʒ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʂ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʐ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.PALATAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ç" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.PALATAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʝ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "x" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɣ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "χ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʁ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.PHARYNGEAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ħ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.PHARYNGEAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʕ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.GLOTTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "h" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.GLOTTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɦ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Lateral Fricatives (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.LATERAL_FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɬ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.LATERAL_FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɮ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Approximants (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.LABIODENTAL and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʋ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɹ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɻ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.PALATAL and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "j" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɰ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Lateral Approximants (next line)::
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.LATERAL_APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "l" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.RETROFLEX and \
            phone.manner == Manner.LATERAL_APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɭ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.PALATAL and \
            phone.manner == Manner.LATERAL_APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʎ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.LATERAL_APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʟ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Affricates (next line):
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.POSTALVEOLAR and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "t͡ʃ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.POSTALVEOLAR and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "d͡ʒ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "p͡ɸ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "t͜s" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "d͡z" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "k͡x" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.AFFRICATE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "q͡χ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Under the Other Symbols part of the IPA chart:
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.LABIAL_VELAR and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "w" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.LABIAL_VELAR and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʍ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.LABIAL_PALATAL and \
            phone.manner == Manner.APPROXIMANT and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɥ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.EPIGLOTTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʜ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.EPIGLOTTAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʢ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.EPIGLOTTAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʡ" + secondary_articulation_transcription(
            phone.secondary_articulation)  # Is the epiglottal plosive voiceless? The IPA chart
        # does not specify.
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLOPALATAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɕ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLOPALATAL and \
            phone.manner == Manner.FRICATIVE and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ʑ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.LATERAL_FLAP and \
            phone.airstream == Airstream.PULMONIC_EGRESSIVE:
        return "ɺ" + secondary_articulation_transcription(phone.secondary_articulation)
    #    if phone == Consonant(VocalFolds.VOICELESS,  (Places (PostAlveolar :| [Velar]))
    #                                        Fricative  PulmonicEgressive):
    #        return "ɧ" # Other Consonants:
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.CLICK:
        return "ʘ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.DENTAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.CLICK:
        return "ǀ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.CLICK:
        return "ǃ" + secondary_articulation_transcription(
            phone.secondary_articulation)  # Or it could be PostAlveolar.
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.PALATOALVEOLAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.CLICK:
        return "ǂ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICELESS and \
            phone.place == Place.ALVEOLAR and \
            phone.manner == Manner.LATERAL and \
            phone.airstream == Airstream.CLICK:
        return "ǁ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.BILABIAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.IMPLOSIVE:
        return "ɓ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.DENTAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.IMPLOSIVE:
        return "ɗ" + secondary_articulation_transcription(
            phone.secondary_articulation)  # Or Alveolar
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.PALATAL and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.IMPLOSIVE:
        return "ʄ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.VELAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.IMPLOSIVE:
        return "ɠ" + secondary_articulation_transcription(phone.secondary_articulation)
    if is_consonant(phone) and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.place == Place.UVULAR and \
            phone.manner == Manner.PLOSIVE and \
            phone.airstream == Airstream.IMPLOSIVE:
        return "ʛ" + secondary_articulation_transcription(
            phone.secondary_articulation)
    # Close Vowels (next line)::
    if is_vowel(phone) and \
            phone.height == Height.CLOSE and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL and \
            phone.vowel_length == VowelLength.NORMAL:
        return "i"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "y"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɨ"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ʉ"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɯ"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "u"  # Near-close Vowels (next line)::
    if is_vowel(phone) and \
            phone.height == Height.NEAR_CLOSE and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɪ"
    if is_vowel(phone) and \
            phone.height == Height.NEAR_CLOSE and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ʏ"
    if is_vowel(phone) and \
            phone.height == Height.NEAR_CLOSE and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ʊ"  # Close-mid Vowels (next line)::
    if is_vowel(phone) and \
            phone.height == Height.CLOSE_MID and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "e"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE_MID and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ø"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE_MID and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɘ"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE_MID and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɵ"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE_MID and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɤ"
    if is_vowel(phone) and \
            phone.height == Height.CLOSE_MID and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "o"
    # Mid Vowels (next line)::
    if is_vowel(phone) and \
            phone.height == Height.MID and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ə"  # Open-mid Vowels (next line)::
    if is_vowel(phone) and \
            phone.height == Height.OPEN_MID and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɛ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN_MID and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "œ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN_MID and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɜ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN_MID and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɞ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN_MID and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ʌ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN_MID and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɔ"
    # Near-open (next line):
    if is_vowel(phone) and \
            phone.height == Height.NEAR_OPEN and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "æ"
    if is_vowel(phone) and \
            phone.height == Height.NEAR_OPEN and \
            phone.backness == Backness.CENTRAL and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɐ"
    # Open Vowels (next line)::
    if is_vowel(phone) and \
            phone.height == Height.OPEN and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "a"
    if is_vowel(phone) and \
            phone.height == Height.OPEN and \
            phone.backness == Backness.FRONT and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɶ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.UNROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
        return "ɑ"
    if is_vowel(phone) and \
            phone.height == Height.OPEN and \
            phone.backness == Backness.BACK and \
            phone.rounding == Rounding.ROUNDED and \
            phone.vocal_folds == VocalFolds.VOICED and \
            phone.vowel_length == VowelLength.NORMAL:
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
    if is_consonant(phone) and phone.place == Place.POSTALVEOLAR and \
            recursion_level < recursion_limit:
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     to_alveolar(phone))
        if result is None:
            return None
        return result + "̠" # Add the diacritic for "retracted"
    if is_vowel(phone) and phone.vowel_length != VowelLength.NORMAL \
            and recursion_level < recursion_limit:
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     to_normal_length(phone))
        if result is None:
            return None
        return result + length_transcription(phone.vowel_length)

    # If there isn't a symbol, and the consonant we want is voiceless,
    # Just take the symbol for a voiced consonant,
    # and then put that diacritic that means voiceless after.
    # (The following two definitions are intended to implement that)
    # Add the small circle diacritic to consonants to make them voiceless.
    if is_consonant(phone) and phone.vocal_folds == VocalFolds.VOICELESS \
            and recursion_level < recursion_limit:
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     to_voiced(phone))
        if result is None:
            return None
        return append_voiceless_diacritic(result)

    # Add the small circle diacritic to vowels to make them voiceless.
    if is_vowel(phone) and phone.vocal_folds == VocalFolds.VOICELESS \
            and recursion_level < recursion_limit:
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     to_voiced(phone))
        if result is None:
            return None
        return append_voiceless_diacritic(result)


    # If there is no way to express a voiced consonant in a single
    # grapheme add a diacritic to the grapheme that represents
    # the voiceless counterpart.
    if is_consonant(phone) and phone.vocal_folds == VocalFolds.VOICED \
            and recursion_level < recursion_limit:
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     to_voiceless(phone))
        if result is None:
            return None
        return append_voiced_diacritic(result)
    if is_vowel(phone) and phone.vocal_folds == VocalFolds.VOICED \
            and recursion_level < recursion_limit:
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level,
                                                     to_voiceless(phone))
        if result is None:
            return None
        return append_voiced_diacritic(result)

    if (is_consonant(phone) and phone.vocal_folds == VocalFolds.VOICED_ASPIRATED
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
            and recursion_level < recursion_limit):
        result = construct_transcription_recursively(
            recursion_limit,
            1 + recursion_level,
            deaspirate(phone))
        if result is None:
            return None
        return append_aspiration_diacritic(result)

    if (is_consonant(phone) and phone.vocal_folds == VocalFolds.VOICELESS_ASPIRATED
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
            and recursion_level < recursion_limit):
        result = construct_transcription_recursively(
            recursion_limit, 1 + recursion_level, deaspirate(phone))
        if result is None:
            return None
        return append_aspiration_diacritic(result)
    if (is_consonant(phone) and phone.vocal_folds == VocalFolds.CREAKY_VOICED
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
            and recursion_level < recursion_limit):
        result = construct_transcription_recursively(recursion_limit,
                                                     1 + recursion_level, decreak(phone))
        if result is not None:
            return result + "̰"
        return None
    return None


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


ascenders: List[str] = \
    ["b", "t", "d", "k", "ʔ", "f", "θ", "ð", "ħ", "ʕ", "h", "ɦ", "ɬ", "l", "ʎ",
     "ʘ", "ɓ", "ǀ", "ɗ", "ǃ", "ǂ", "ɠ", "ʄ", "ǁ", "ʛ", "ɺ", "ʢ", "ʡ", "ɤ", "ʈ", "ɖ",
     "ɸ", "β", "ʃ", "ɮ", "ɭ", "ɧ"]
descenders: List[str] = \
    ["p", "ɟ", "g", "q", "ɱ", "ɽ", "ʒ", "ʂ", "ʐ", "ç", "ʝ", "ɣ", "χ", "ɻ", "j",
     "ɰ", "ɥ", "y", "ɳ", "ɲ", "ŋ", "ʈ", "ɖ", "ɸ", "β", "ʃ", "ɮ", "ɧ"]
# Whether a character (but not a diacritic)
# takes up space
# below the imaginary horizontal line
# on which it is written.
#
# This could be useful later for determining
# where to put diacritics so that
# they are readable.

# We don't include the retroflex l i.e <ɭ> a a descender
# because, even though it is a descender,
# There is more free space under it than above


# CONSONANTS (PULMONIC)

# See:
# www.internationalphoneticassociation.org/sites/default/files/IPA_Kiel_2015.pdf
# For the source of this information..
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
