"""
unit tests for primitive parsers
"""

from typing import Callable, List, Optional, Tuple


def single_char_parser(char_list: List[str], text: str) -> Optional[Tuple[str, str]]:
    """
    :param char_list: list of characters that will be accepted. Anything else will not be accepted.
    :param text: text to be parsed
    :return: a tuple or none. If it was able to parse at least one character from the text,
             then it returns a tuple, with the first part of the tuple being a string containing
             only the first character of the input text. The second part contains the part of
             the input text that was not parsed.
             If it is not able to parse the text it returns None.
    """
    if len(text) == 0:
        return None
    elif text[0] in char_list:
        return text[0], text[1:]
    else:
        return None


def then_parser(
    first_parser: Callable[[str], Optional[Tuple[str, str]]],
    second_parser: Callable[[str], Optional[Tuple[str, str]]],
    text: str,
) -> Optional[Tuple[str, str]]:
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


def or_parser(
    first_parser: Callable[[str], Optional[Tuple[str, str]]],
    second_parser: Callable[[str], Optional[Tuple[str, str]]],
    text: str,
) -> Optional[Tuple[str, str]]:
    """
    combines parsers by using one or the other.
    """
    result = first_parser(text)
    if result is None:
        result_2 = second_parser(text)
        return result_2
    else:
        return result


def many_parser(
    sub_parser: Callable[[str], Optional[Tuple[str, str]]], text: str
) -> Optional[Tuple[str, str]]:
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


def optional_parser(
    sub_parser: Callable[[str], Optional[Tuple[str, str]]], text: str
) -> Optional[Tuple[str, str]]:
    """
    changes a parser by making it never return Nothing,
    that is it makes the parser optional.
    """
    result = sub_parser(text)
    if result is None:
        return ("", text)  # return text unconsumed
    else:
        return result
