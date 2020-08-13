"""
unit tests for primitive parsers
"""

import unittest
from typing import Callable, List, Optional, Tuple 


def single_char_parser(char_list: List[str], text: str) -> Optional[Tuple[str, str]]:
    if len(text) == 0:
        return None
    elif text[0] in char_list:
        return text[0], text[1:]
    else:
        return None


def then_parser(first_parser: Callable[[str], Optional[Tuple[str, str]]], second_parser: Callable[[str], Optional[Tuple[str, str]]], text: str) -> Optional[Tuple[str, str]]:
    """
    Uses one parser on the text,
    then uses the next parser on the remaining
    text from the first parse.
    """
    first_result = first_parser(text)
    if first_result is None:
       return None
    else:
        parsed, rest = first_result
        second_result = second_parser(rest)
        if second_result is None:
           return None
        else:
           parsed_2, rest_2 = second_result
           return parsed + parsed_2, rest_2

"""
-- | combines parsers by using one or the other.
orParser
  :: (Text -> Maybe (Text, Text))
  -> (Text -> Maybe (Text, Text))
  -> Text
  -> Maybe (Text, Text)
orParser firstParser secondParser text =
  case firstParser text of
    Nothing -> case secondParser text of
                      Nothing -> Nothing
                      Just (parsed, rest) -> Just (parsed, rest)
    Just (parsed, rest) -> Just (parsed, rest)
"""

def many_parser(sub_parser: Callable[[str], Optional[Tuple[str, str]]], text: str) -> Optional[Tuple[str, str]]:
    """
    changes a parser by repeating it an indefinite number
    of times.
    So a parser that parses only "a", will parse "aaaaa".
    A parser that parses only "@", will parse "@@@@", "@@@@@" and
    so on.
    """
    result = sub_parser(text)
    if result is None:
        return None
    else:
      parsed, rest = result
      result_2 = many_parser(sub_parser, rest) 
      if result_2 is None:
          return parsed, rest
      else:
          parsed_2, rest_2 = result_2
          return (parsed + parsed_2, rest_2)         

"""
-- | changes a parser by making it never return Nothing,
--   that is it makes the parser optional.
optionalParser
  :: (Text -> Maybe (Text, Text))
  -> Text
  -> Maybe (Text, Text)
optionalParser subParser text =
  case subParser text of
    Nothing -> Just ("", text) -- Return text unconsumed.
    Just (parsed, rest) -> Just (parsed, rest)
"""
