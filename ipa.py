from typing import Tuple, Optional, List, Callable

from english_us_text import NO_ENGLISH_DESCRIPTION_FOUND_MESSAGE, SORRY_UNABLE_TO_CALCULATE
from grapheme_grammar import split_by_phonetes, consonants_pulmonic, consonants_nonpulmonic, \
    other_symbols, vowels, diacritics_and_suprasegmentals
from lib_functions import retract_phonet, deaspirate, decreak, \
    voiced_phonet, devoiced_phonet, spirantized_phonet, show_phonet, english_phonet_inventory
from phonetic_features import analyze_features, show_features
from lib_types import Phonet, Consonant, VocalFolds, Place, Manner, Airstream, MultiPlace, Vowel, \
    Height, Backness, Rounding, PhonetInventory


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


# To do: find a more suitable name than exponentials.
# They only look like exponentials if you consider how they
# look similar to mathematical notation for exponentials.
# Really, they should be named something different.



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
""" IPA text that is not a semantic modifier to what is before or after it.
    This includes vowels, and consonants. It excludes all diacritics.
"""

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
