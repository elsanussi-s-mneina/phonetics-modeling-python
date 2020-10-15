"""
Handle splitting of IPA graphemes into chunks, so that
diacritics go with the non-diacritic characters they modify.
"""

from typing import List, Optional, Tuple, Callable


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
	:param text: text that may contain text with prediacrtics
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
	Parse the part containing diacritic (except the tie-bar).
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
	return a_character in ["͜", "͡"]


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
	if (
		not len(text) == 0
		and is_exponential_before(text[0])
		and is_segmental_at(1, text)
	):
		if is_tie_bar_at(2, text):
			# include tie bar and character after it.
			return text[:4], text[4:]
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
	else:
		(prepart, middle) = preresult
		if is_exponential_after_at(0, middle):
			length_of_first: int = len(prepart)
			segmental: str = prepart[(length_of_first - 1) :]
			postresult: Optional[Tuple[str, str]] = postdiacritic_parser_function(
				segmental + middle
			)
			if postresult is None:
				return None
			else:
				(postpart, rest) = postresult
				return prepart + postpart[1:], rest
		else:
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
	elif (
		is_segmental_at(0, text)
		and is_tie_bar_at(1, text)
		and is_exponential_after_at(2, text)
	):
		number_of_postdiacritics: int = count_post_diacritics_in_a_row(text, 3)
		chunk_length: int = number_of_postdiacritics + 3
		return text[:chunk_length], text[chunk_length:]
	else:
		return None


def count_post_diacritics_in_a_row(some_text: str, start_index: int) -> int:
	"""
	Count how many superscript characters occur one after another, at a
	specific place in a text (that could modify a previous character).
	"""
	if is_exponential_after_at(start_index, some_text):
		return 1 + count_post_diacritics_in_a_row(some_text, (start_index + 1))
	else:
		return 0


def is_exponential(character: str) -> bool:
	"""
	Whether an IPA character is written above the base line
	and to the right of the previous character,
	like how exponents of a power are written
	in mathematical notation.
	"""
	return character in exponentials


plosivePulmonic: List[str] = [
	"p",
	"b",
	"t",
	"d",
	"ʈ",
	"ɖ",
	"c",
	"ɟ",
	"k",
	"g",
	"q",
	"ɢ",
	"ʔ",
]
nasalPulmonic: List[str] = ["m", "ɱ", "n", "ɳ", "ɲ", "ŋ", "ɴ"]
trillPulmonic: List[str] = ["ʙ", "r", "ʀ"]
tapOrFlapPulmonic: List[str] = ["ⱱ", "ɾ", "ɽ"]
fricativePulmonic: List[str] = [
	"ɸ",
	"β",
	"f",
	"v",
	"θ",
	"ð",
	"s",
	"z",
	"ʃ",
	"ʒ",
	"ʂ",
	"ʐ",
	"ç",
	"ʝ",
	"x",
	"ɣ",
	"χ",
	"ʁ",
	"ħ",
	"ʕ",
	"h",
	"ɦ",
]
lateral_fricative_pulmonic: List[str] = ["ɬ", "ɮ"]
approximant_pulmonic: List[str] = ["ʋ", "ɹ", "ɻ", "j", "ɰ"]
lateral_approximant_pulmonic: List[str] = ["l", "ɭ", "ʎ", "ʟ"]
consonants_pulmonic: List[str] = (
	plosivePulmonic
	+ nasalPulmonic
	+ trillPulmonic
	+ tapOrFlapPulmonic
	+ fricativePulmonic
	+ lateral_fricative_pulmonic
	+ approximant_pulmonic
	+ lateral_approximant_pulmonic
)
consonants_nonpulmonic: List[str] = [
	"ʘ",
	"ɓ",  # Bilabial
	"ǀ",  # Dental
	"ɗ",  # Dental/alveolar
	"ǃ",  # (Post)alveolar
	"ʄ",
	"ǂ",
	"ɠ",
	"ǁ",
	"ʛ",
]
other_symbols: List[str] = [
	"ʍ",
	"ɕ",
	"w",
	"ʑ",
	"ɥ",
	"ɺ",
	"ʜ",
	"ɧ",
	"ʢ",
	"ʡ",
]
consonants: List[str] = consonants_pulmonic + consonants_nonpulmonic + other_symbols
vowels: List[str] = [
	"i",
	"y",
	"ɨ",
	"ʉ",
	"ɯ",
	"u",  # Close
	"ɪ",
	"ʏ",
	"ʊ",  # Close-mid
	"e",
	"ø",
	"ɘ",
	"ɵ",
	"ɤ",
	"o",  # Open-mid
	"ə",
	"ɛ",
	"œ",
	"ɜ",
	"ɞ",
	"ʌ",
	"ɔ",  # Open-mid
	"æ",
	"ɐ",
	"a",
	"ɶ",
	"ɑ",
	"ɒ",  # Open
]
strict_segmentals: List[str] = consonants + vowels
""" IPA text that is not a semantic modifier to what is before or after it.
	This includes vowels, and consonants. It excludes all diacritics.
"""

diacritics_and_suprasegmentals: List[str] = [
	"̥",  # Voiceless
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
	"̇",  # Palatalization/Centralization
]

exponentials_before: List[str] = ["ⁿ"]

exponentials_after: List[str] = diacritics_and_suprasegmentals + ["ː", "ˑ", "̆"]
exponentials: List[str] = exponentials_before + exponentials_after

# To do: find a more suitable name than exponentials.
# They only look like exponentials if you consider how they
# look similar to mathematical notation for exponentials.
# Really, they should be named something different.
