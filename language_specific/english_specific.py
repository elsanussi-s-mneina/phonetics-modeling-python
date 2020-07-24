from lib_types import PhonetInventory, Consonant, VocalFolds, Place, Manner, Airstream, Vowel, \
    Height, Backness, Rounding

# I added some English vowels. I did not choose any specific dialect.
# I got all my information from the Wikipedia page titled
# "English Phonology"
# at the following URL: https://en.wikipedia.org/wiki/English_phonology#Vowels
# on Monday, February 24, 2020.
# To do: Get better information on English vowels from a more reliable source.
# To do: model separate dialects of English or only one.


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
