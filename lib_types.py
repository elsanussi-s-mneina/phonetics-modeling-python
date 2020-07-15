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
from typing import List, Union


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

    def __init__(self):
        pass


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
    LABIAL_VELAR = auto()
    LABIAL_PALATAL = auto()
    ALVEOLOPALATAL = auto()
    PALATOALVEOLAR = auto()  # To do: investigate what the difference
    # is between alveolopalatal, and palatoalveolar


class MultiPlace:
    def __init__(self, places: List[Place]):
        self.places = places


class Manner(Enum):
    """
    The manner is how the articulation is made. Specifically,
    how the air flows. Is it stopped? Does it go through the mouth?
    Does it go through the nose? Does it go to the sides of the tongue?
    How much friction is in the airflow.
    """
    PLOSIVE = auto()
    NASAL = auto()
    TRILL = auto()
    TAP_OR_FLAP = auto()
    APPROXIMANT = auto()
    FRICATIVE = auto()
    AFFRICATE = auto()
    LATERAL_FRICATIVE = auto()
    LATERAL_APPROXIMANT = auto()
    LATERAL_FLAP = auto()  # There are very few IPA symbols for lateral flaps
    LATERAL = auto()  # we need this one for the lateral click.


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

    def __init__(self,
                 vocal_folds: VocalFolds,
                 place: Union[Place, MultiPlace],
                 manner: Manner,
                 airstream: Airstream):
        super().__init__()
        self.vocal_folds = vocal_folds
        self.place = place
        self.manner = manner
        self.airstream = airstream

    def __eq__(self, other):
        try:
            return (self.vocal_folds == other.vocal_folds and
                    self.place == other.place and
                    self.manner == other.manner and
                    self.airstream == other.airstream)
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


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
    MID = auto()
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

    def __init__(self, height: Height, backness: Backness, rounding: Rounding,
                 vocal_folds: VocalFolds):
        super().__init__()
        self.height = height
        self.backness = backness
        self.rounding = rounding
        self.vocal_folds = vocal_folds

    def __eq__(self, other):
        return (type(self) == type(other) and
                self.vocal_folds == other.vocal_folds and
                self.height == other.height and
                self.backness == other.backness and
                self.rounding == other.rounding)

    def __ne__(self, other):
        return not self.__eq__(other)


class PhonetInventory:
    """
    A collection of phonemes. Usually,
    all the phonemes in a language.
    """

    def __init__(self, contents: List[Phonet]):
        self.contents = contents


class UnmarkablePhonet:
    """
    The data type UnmarkablePhonet was originally intended
    to represent a phoneme, or a phonete but with the additional
    ability to have unmarked properties, such as unmarked voicing.
    So far, though it has not been used in a way consistent with
    linguistics, instead it has been used to represent all values of a property.
    So for example, we would use unmarked voicing to represent all
    possible vocal fold configurations. We would use unmarked place to
    to represent all possible places of articulation.
    """

    def __init__(self):
        pass


class UnmarkableVocalFolds:
    def __init__(self):
        pass


class UnmarkedVocalFolds(UnmarkableVocalFolds):
    """
    For matching against any vocal fold
    configuration.
    """

    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, UnmarkedVocalFolds)

    def __ne__(self, other):
        return not self.__eq__(other)


class MarkedVocalFolds(UnmarkableVocalFolds):
    """
    For matching against only one vocal fold
    configuration.
    """

    def __init__(self, vocal_fold):
        super().__init__()
        self.vocal_fold = vocal_fold

    def __eq__(self, other):
        return self.vocal_fold == other.vocal_fold

    def __ne__(self, other):
        return not self.__eq__(other)


class UnmarkablePlace:
    """
    For matching with places of articulation.
    """

    def __init__(self):
        pass

    pass


class UnmarkedPlace(UnmarkablePlace):
    """
    For matching with any place of articulation.
    """

    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, UnmarkedPlace)

    def __ne__(self, other):
        return not self.__eq__(other)


class MarkedPlace(UnmarkablePlace):
    """
    For matching with a specific place of articulation.
    """

    def __init__(self, place: Place):
        super().__init__()
        self.place = place

    def __eq__(self, other):
        return self.place == other.place

    def __ne__(self, other):
        return not self.__eq__(other)


class UnmarkableManner:
    """
    For matching with manners of articulation.
    """

    def __init__(self):
        pass

    pass


class UnmarkedManner(UnmarkableManner):
    """
    For matching with any manner of articulation.
    """

    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, UnmarkedManner)

    def __ne__(self, other):
        return not self.__eq__(other)


class MarkedManner(UnmarkableManner):
    """
    For matching with a specific manner of articulation.
    """

    def __init__(self, manner):
        super().__init__()
        self.manner = manner

    def __eq__(self, other):
        return self.manner == other.manner

    def __ne__(self, other):
        return not self.__eq__(other)


class UnmarkableAirstream:
    """
    For matching with airstream mechanisms.
    """

    def __init__(self):
        pass

    pass


class UnmarkedAirstream(UnmarkableAirstream):
    """
    For matching with any airstream mechanism.
    """

    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, UnmarkedAirstream)

    def __ne__(self, other):
        return not self.__eq__(other)


class MarkedAirstream(UnmarkableAirstream):
    """
    For matching with a specific airstream mechanism.
    """

    def __init__(self, airstream):
        super().__init__()
        self.airstream = airstream

    def __eq__(self, other):
        return self.airstream == other.airstream

    def __ne__(self, other):
        return not self.__eq__(other)


class UnmarkableConsonant(UnmarkablePhonet):
    """
    For matching with consonants.
    """

    def __init__(self, vocal_folds: UnmarkableVocalFolds, place: UnmarkablePlace,
                 manner: UnmarkableManner, airstream: UnmarkableAirstream):
        super().__init__()
        self.vocal_folds = vocal_folds
        self.place = place
        self.manner = manner
        self.airstream = airstream


class UnmarkableBackness:
    """
    For matching with kinds of backness
    """

    def __init__(self):
        pass

    pass


class UnmarkedBackness(UnmarkableBackness):
    """
    For matching with any kind of backness.
    """

    def __init__(self):
        super().__init__()


class MarkedBackness(UnmarkableBackness):
    """
    For matching with a particular kind of backness.
    """

    def __init__(self, backness: Backness):
        super().__init__()
        self.backness = backness

    def __eq__(self, other):
        return self.backness == other.backness

    def __ne__(self, other):
        return not self.__eq__(other)


class UnmarkableHeight:
    """
    For matching with kinds of height.
    """

    def __init__(self):
        pass

    pass


class UnmarkedHeight(UnmarkableHeight):
    """
    For matching with any kind of height.
    """

    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, UnmarkedHeight)

    def __ne__(self, other):
        return not self.__eq__(other)


class MarkedHeight(UnmarkableHeight):
    """
    For matching with a specific kind of height.
    """

    def __init__(self, height: Height):
        super().__init__()
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __ne__(self, other):
        return not self.__eq__(other)


class UnmarkableRounding:
    """
    For matching with kinds of lip rounding.
    """

    def __init__(self):
        pass

    pass


class UnmarkedRounding(UnmarkableRounding):
    """
    For matching with all kinds of lip rounding.
    """

    def __init__(self):
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, UnmarkedRounding)

    def __ne__(self, other):
        return self.__eq__(other)


class MarkedRounding(UnmarkableRounding):
    """
    For matching with a specific kind of lip rounding.
    """

    def __init__(self, rounding: Rounding):
        super().__init__()
        self.rounding = rounding

    def __eq__(self, other):
        return self.rounding == other.rounding

    def __ne__(self, other):
        return self.__eq__(other)


class UnmarkableVowel(UnmarkablePhonet):
    """
    For matching with vowels.
    """

    def __init__(self, height: UnmarkableHeight, backness: UnmarkableBackness,
                 rounding: UnmarkableRounding, vocal_folds: UnmarkableVocalFolds):
        super().__init__()
        self.height = height
        self.backness = backness
        self.rounding = rounding
        self.vocal_folds = vocal_folds


@unique
class Polarity(Enum):
    """
     Represents the '+' (plus) or '-' (minus)
     of a binary feature. e.g. [+sonorant],
     [-sonorant]
    """
    PLUS = auto()
    MINUS = auto()


class PhonemeFeature:
    """
     According to Linguistics, phonemes can be
     analyzed as a set of features. One phoneme
     will have one set of features, and a different
     phoneme will have a different set of features.

     These features are well known in phonology, and
     are limited in number. There are two kinds of
     features, unary features, and binary features. The
     difference is obvious in how they are represented in
     the notation that linguists use. Unary features,
     are either present or absent. Binary features
     can be positive or negative. For example, Nasal
     is a unary feature. A phoneme is either nasal,
     or it isn't. i.e. [nasal] or not. For example,
     Voice is a binary feature, a phoneme can be
     [+voice] (can be pronounced: "plus voice")
     or [-voice] (can be pronounced: "minus voice").

     Because linguists represent phonemic features in these
     two different ways. We represent these as two
     different kinds of types.

     So [nasal] which is a unary feature would be
     represented by a value `NasalFeature` of type `PhonemeFeature`.
     And [+voice] which is a binary feature would
     be represented by a value `VoiceFeature Plus` of type
     `PhonemeFeature`.

     We represent the plus or minus symbol by
     the type Polarity.

     Notice that: Linguists write a set of features
     as a 2D matrix with one column, roughly like this:
     ⎡ +voice    ⎤
     ⎢ +sonorant ⎥
     ⎣  nasal    ⎦

    Note that certain sets of features cannot coexist,
    syntactically. For example a phoneme cannot be
    [+voice] and [-voice].

     Note that some analyses
    are language specific, so for some phonemes (not
    the usual case) whether it has feature X (say 'coronal')
    depends on the language (theoretical example: e.g. Swahili,
    vs French). This is not implemented here.
    """

    def __init__(self):
        pass


class SyllabicFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class ConsonantalFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class SonorantFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class ContinuantFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class VoiceFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class AdvancedTongueRootFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class NasalFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class LateralFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class DelayedReleaseFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class SpreadGlottisFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class ConstrictedGlottisFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class LabialFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class CoronalFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class DorsalFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class PharyngealFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class LaryngealFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class RoundFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class AnteriorFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class DistributedFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class StridentFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class HighFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class LowFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class BackFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)
