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
from typing import Final, List, Union


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


@unique
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


vocal_fold_states: Final[List[VocalFolds]] = [
	VocalFolds.VOICED,
	VocalFolds.VOICELESS,
	VocalFolds.VOICED_ASPIRATED,
	VocalFolds.VOICELESS_ASPIRATED,
	VocalFolds.CREAKY_VOICED,
]


@unique
class VowelLength(Enum):
	"""
	Represents the perceived length
	of a vowel sound.
	"""

	NORMAL = auto()
	LONG = auto()
	HALF_LONG = auto()
	EXTRA_SHORT = auto()


vowel_length_states: Final[List[VowelLength]] = [
	VowelLength.LONG,
	VowelLength.HALF_LONG,
	VowelLength.EXTRA_SHORT,
	VowelLength.NORMAL,
]


@unique
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


place_states: Final[List[Place]] = [
	Place.BILABIAL,
	Place.LABIODENTAL,
	Place.DENTAL,
	Place.ALVEOLAR,
	Place.POSTALVEOLAR,
	Place.RETROFLEX,
	Place.PALATAL,
	Place.VELAR,
	Place.UVULAR,
	Place.PHARYNGEAL,
	Place.GLOTTAL,
	Place.EPIGLOTTAL,
	Place.LABIAL_VELAR,
	Place.LABIAL_PALATAL,
	Place.ALVEOLOPALATAL,
	Place.PALATOALVEOLAR,
]


class MultiPlace:
	def __init__(self, places: List[Place]):
		self.places = places


@unique
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


manner_states: Final[List[Manner]] = [
	Manner.PLOSIVE,
	Manner.NASAL,
	Manner.TRILL,
	Manner.TAP_OR_FLAP,
	Manner.APPROXIMANT,
	Manner.FRICATIVE,
	Manner.AFFRICATE,
	Manner.LATERAL_FRICATIVE,
	Manner.LATERAL_APPROXIMANT,
	Manner.LATERAL_FLAP,
	Manner.LATERAL,
]


@unique
class Airstream(Enum):
	"""
	The source of airflow.
	  Pulmonic egressive is the most common.
	"""

	PULMONIC_EGRESSIVE = auto()
	CLICK = auto()
	IMPLOSIVE = auto()


airstream_states: Final[List[Airstream]] = [
	Airstream.PULMONIC_EGRESSIVE,
	Airstream.CLICK,
	Airstream.IMPLOSIVE,
]


@unique
class SecondaryArticulation(Enum):
	NORMAL = auto()
	LABIALIZED = auto()
	PALATALIZED = auto()
	VELARIZED = auto()
	PHARYNGEALIZED = auto()


secondary_articulation_states: List[SecondaryArticulation] = [
	SecondaryArticulation.LABIALIZED,
	SecondaryArticulation.PALATALIZED,
	SecondaryArticulation.VELARIZED,
	SecondaryArticulation.PHARYNGEALIZED,
]


class Consonant(Phonet):
	"""
	A consonant is a sound.
	Consonants have voicing, place, manner, and an airstream mechanism.
	"""

	def __init__(
		self,
		vocal_folds: VocalFolds,
		place: Union[Place, MultiPlace],
		manner: Manner,
		airstream: Airstream,
		secondary_articulation: SecondaryArticulation,
	):
		super().__init__()
		self.vocal_folds = vocal_folds
		self.place = place
		self.manner = manner
		self.airstream = airstream
		self.secondary_articulation = secondary_articulation

	def __eq__(self, other):
		try:
			return (
				self.vocal_folds == other.vocal_folds
				and self.place == other.place
				and self.manner == other.manner
				and self.airstream == other.airstream
			)
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


backness_states: Final[List[Backness]] = [
	Backness.FRONT,
	Backness.CENTRAL,
	Backness.BACK,
]


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


height_states: List[Height] = [
	Height.CLOSE,
	Height.NEAR_CLOSE,
	Height.CLOSE_MID,
	Height.MID,
	Height.OPEN_MID,
	Height.NEAR_OPEN,
	Height.OPEN,
]


@unique
class Rounding(Enum):
	"""
	How rounded the lips are when the sound is pronounced.
	"""

	ROUNDED = auto()
	UNROUNDED = auto()


rounding_states: List[Rounding] = [Rounding.ROUNDED, Rounding.UNROUNDED]


class Vowel(Phonet):
	"""
	A vowel is a sound.
	Vowels have a height, backness, rounding, and vocal fold configuration.
	"""

	def __init__(
		self,
		height: Height,
		backness: Backness,
		rounding: Rounding,
		vocal_folds: VocalFolds,
		vowel_length: VowelLength,
	):
		super().__init__()
		self.height = height
		self.backness = backness
		self.rounding = rounding
		self.vocal_folds = vocal_folds
		self.vowel_length = vowel_length

	def __eq__(self, other):
		return (
			type(self) == type(other)
			and self.vocal_folds == other.vocal_folds
			and self.height == other.height
			and self.backness == other.backness
			and self.rounding == other.rounding
			and self.vowel_length == other.vowel_length
		)

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


class UnmarkableSecondaryArticulation:
	"""
	For matching with secondary articulations.
	"""

	def __init__(self):
		pass

	pass


class UnmarkedSecondaryArticulation(UnmarkableSecondaryArticulation):
	"""
	For matching with any secondary articulation.
	"""

	def __init__(self):
		super().__init__()

	def __eq__(self, other):
		return isinstance(other, UnmarkedSecondaryArticulation)

	def __ne__(self, other):
		return not self.__eq__(other)


class MarkedSecondaryArticulation(UnmarkableSecondaryArticulation):
	"""
	For matching with a specific secondary articulation.
	"""

	def __init__(self, secondary_articulation: SecondaryArticulation):
		super().__init__()
		self.secondary_articulation = secondary_articulation

	def __eq__(self, other):
		return self.secondary_articulation == other.secondary_articulation

	def __ne__(self, other):
		return not self.__eq__(other)


class UnmarkableConsonant(UnmarkablePhonet):
	"""
	For matching with consonants.
	"""

	def __init__(
		self,
		vocal_folds: UnmarkableVocalFolds,
		place: UnmarkablePlace,
		manner: UnmarkableManner,
		airstream: UnmarkableAirstream,
		secondary_articulation: SecondaryArticulation,
	):
		super().__init__()
		self.vocal_folds = vocal_folds
		self.place = place
		self.manner = manner
		self.airstream = airstream
		self.secondary_articulation = secondary_articulation


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


class UnmarkableVowelLength:
	"""
	For matching with kinds of vowel length.
	"""

	def __init__(self):
		pass

	pass


class UnmarkedVowelLength(UnmarkableVowelLength):
	"""
	For matching with all kinds of vowel length.
	"""

	def __init__(self):
		super().__init__()

	def __eq__(self, other):
		return isinstance(other, UnmarkedVowelLength)

	def __ne__(self, other):
		return self.__eq__(other)


class MarkedVowelLength(UnmarkableVowelLength):
	"""
	For matching with a specific kind of vowel length.
	"""

	def __init__(self, vowel_length: VowelLength):
		super().__init__()
		self.vowel_length = vowel_length

	def __eq__(self, other):
		return self.vowel_length == other.vowel_length

	def __ne__(self, other):
		return self.__eq__(other)


class UnmarkableVowel(UnmarkablePhonet):
	"""
	For matching with vowels.
	"""

	def __init__(
		self,
		height: UnmarkableHeight,
		backness: UnmarkableBackness,
		rounding: UnmarkableRounding,
		vocal_folds: UnmarkableVocalFolds,
	):
		super().__init__()
		self.height = height
		self.backness = backness
		self.rounding = rounding
		self.vocal_folds = vocal_folds
