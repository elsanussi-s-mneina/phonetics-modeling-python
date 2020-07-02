"""
This module contains all the class and type definitions
for the program related specifically to phonetics and phonology.
Phonetics and phonology are the study of the production of sounds
using the human speech organs. It is a subfield of linguistics,
which is the study of human (natural) language.

It should not contain any functions other than those
 necessary to construct objects, or print them for
 debugging purposes on the screen.
"""
from enum import Enum, auto, unique

class Phonet:
    """
    In phonology, or phonetics, this is usually called
    a phoneme, or a phonete. In this case, we are calling it a
    "phonet" which is just a word I made up for the sake of this program.

    Both phonemes, and phonetes represent sounds. In order not to have
    to represent the fact that phonemes vary from language to language,
    we made up the term "phonet".

    Once, I actually model phonemes properly, it will make more sense,
    and we might refactor this type out of existence.
    """



class VocalFolds(Enum):
    """
    Represents the state of vocal cords.
    This is usually called voicing.
    """
    VOICED = auto()
    VOICELESS = auto()
    VOICED_ASPIRATED = auto()
    VOICELESS_ASPIRATED = auto()
    CREAKY_VOICED = auto()



class Place(Enum):
    """
    Represents the place where the sound is made.
    That is, where the tongue is positioned.
    """
    BILABIAL = auto()
    LABIODENTAL = auto()
    DENTAL = auto()
    ALVEOLAR = auto()
    POSTALVEOLAR = auto()
    RETROFLEX = auto()
    PALATAL = auto()
    VELAR = auto()
    UVULAR = auto()
    PHARYNGEAL = auto()
    GLOTTAL = auto()
    EPIGLOTTAL = auto()
    # I am unsure if the following three should be counted
    # as 6 different places of articulation, or just 3
    LABIALVELAR = auto()
    LABIALPALATAL = auto()
    ALVEOLOPALATAL = auto()
    PALATOALVEOLAR = auto() # To do: investigate what the difference
    # is between alveolopalatal, and palatoalveolar

class Manner(Enum):
    """
    The manner is how the articulation is made. Specifically,
    how the air flows. Is it stopped? Does it go through the mouth?
    Does it go through the nose? Does it go to the sides of the tongue?
    How much friction is in the airflow.
    """
    PLOSIVE = auto
    NASAL = auto
    TRILL = auto
    TAP_OR_FLAP = auto
    APPROXIMANT = auto
    FRICATIVE = auto
    AFFRICATE = auto
    LATERAL_FRICATIVE = auto
    LATERAL_APPROXIMANT = auto
    LATERAL_FLAP = auto  # There are very few IPA symbols for lateral flaps
    LATERAL = auto       # we need this one for the lateral click.

@unique
class Airstream(Enum):
    """
    The source of airflow.
      Pulmonic egressive is the most common.
    """
    PULMONIC_EGRESSIVE = auto()
    CLICK = auto()
    IMPLOSIVE = auto()

class Consonant(Phonet):
    """
    A consonant is a sound.
    Consonants have voicing, place, manner, and an airstream mechanism.
    """
    def __init__(self, vocal_folds: VocalFolds, place: Place, manner: Manner, airstream: Airstream):
        self.vocal_folds = vocal_folds
        self.place = place
        self.manner = manner
        self.airstream = airstream

@unique
class Backness(Enum):
    """
    Indicating how far back in
    the mouth the sound is pronounced.
    This is usually a property of vowels.
    """
    FRONT = auto()
    CENTRAL = auto()
    BACK = auto()

@unique
class Height(Enum):
    """
    How open the mouth is when the sound is pronounced.
    This is a property of vowels.
    """
    CLOSE = auto()
    NEAR_CLOSE = auto()
    CLOSE_MID = auto()
    OPEN_MID = auto()
    NEAR_OPEN = auto()
    OPEN = auto()

@unique
class Rounding(Enum):
    """
    How rounded the lips are when the sound is pronounced.
    """
    ROUNDED = auto()
    UNROUNDED = auto()


class Vowel(Phonet):
    """
    A vowel is a sound.
    Vowels have a height, backness, rounding, and vocal fold configuration.
    """
    def __init__(self,
                 height: Height,
                 backness: Backness,
                 rounding: Rounding,
                 vocal_folds: VocalFolds):
        self.height = height
        self.backness = backness
        self.rounding = rounding
        self.vocal_folds = vocal_folds
        