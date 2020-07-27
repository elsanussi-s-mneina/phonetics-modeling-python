from lib_types import PhonetInventory, Consonant, VocalFolds, Place, Manner, Airstream, Vowel, \
    Height, Backness, Rounding


def english_phonet_inventory() -> PhonetInventory:
    """
    These are the sounds found in most native English dialects.
    This information was taken from "the speech accent archive"
    on July 27, 2020, at the following URL:
    http://accent.gmu.edu/browse_native.php?function=detail&languageid=18
    They have a note on their web page that their information
    was adapted from Ladefoged, P. (1993)
    The information on the webpage was in two charts.
    I took the information and turned it into source code
    in this file as the value titled "englishPhonetInventory".
    Note: there are 5 dipthongs that are not included here.
    """
    return PhonetInventory(
        [
            Consonant(VocalFolds.VOICELESS, Place.BILABIAL, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.VELAR, Manner.PLOSIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.VELAR, Manner.PLOSIVE, Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.BILABIAL, Manner.NASAL,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.NASAL,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.VELAR, Manner.NASAL, Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.LABIODENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.LABIODENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.DENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.DENTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.ALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.GLOTTAL, Manner.FRICATIVE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICELESS, Place.POSTALVEOLAR, Manner.AFFRICATE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.POSTALVEOLAR, Manner.AFFRICATE,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.PALATAL, Manner.APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.ALVEOLAR, Manner.LATERAL_APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),
            Consonant(VocalFolds.VOICED, Place.LABIAL_VELAR, Manner.APPROXIMANT,
                      Airstream.PULMONIC_EGRESSIVE),
            Vowel(Height.CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.NEAR_CLOSE, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.CLOSE_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.OPEN_MID, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.NEAR_OPEN, Backness.FRONT, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.MID, Backness.CENTRAL, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),
            Vowel(Height.NEAR_CLOSE, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),
            Vowel(Height.CLOSE_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),
            Vowel(Height.OPEN_MID, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED),
            Vowel(Height.OPEN_MID, Backness.BACK, Rounding.ROUNDED, VocalFolds.VOICED),
            Vowel(Height.OPEN, Backness.BACK, Rounding.UNROUNDED, VocalFolds.VOICED)
        ]
    )
