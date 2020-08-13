from lib_types import Phonet

def is_consonant(phone: Phonet) -> bool:
  return isinstance(phone, Consonant)

def is_vowel(phone: Phonet) -> bool:
  return isinstance(phone, Vowel)