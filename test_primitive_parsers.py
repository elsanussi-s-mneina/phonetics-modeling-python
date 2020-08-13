"""
unit tests for primitive parsers
"""

import unittest
from primitive_parsers import single_char_parser, then_parser, many_parser
from functools import partial

class TestPrimitiveParsers(unittest.TestCase):
    def test_single_char_parser_empty_text(self) -> None:
        """single character parser"""
        expected = None
        actual = single_char_parser([], "")
        self.assertEqual(expected, actual,
            msg="should be that: single character parser of no characters fails to parse empty text"
            )

    def test_single_char_parser_empty_parser_and_text_of_length_3(self) -> None:
        expected = None
        actual = single_char_parser([], "abc")
        self.assertEqual(expected, actual,
            msg="should be that: single character parser of no characters fails to parse text of length 3")

    def test_single_char_parser_parser_and_text_of_length_parses_nothing(self) -> None:
        self.assertEqual(None, single_char_parser(["a"], "b"),
                         msg="should be that: single character parser of the character 'a' fails to parse the character \"b\"")

    def test_single_char_parser_parser_and_text_of_length_parses_one_character(self) -> None:
        self.assertEqual(("a", ""), single_char_parser(["a"], "a"),
                         msg="should be that: single character parser of the character 'a' does parse the character \"a\"")

    def test_single_char_parser_parser_and_text_of_length_parses_one_character_leaves_one(self) -> None:
        self.assertEqual(("a", "a"), single_char_parser(['a'], "aa"),
                         msg="should be that: single character parser of the character 'a' does parse the string containing two \"aa\" characters and leaves one left")

    def test_single_char_parser_2(self) -> None:
        self.assertEqual(single_char_parser(['a', 'b'], "ab"), ("a", "b"),
            msg="should be that: single character parser of the character 'a' does parse the string containing \"ab\"\
             \ characters and leaves \"b\"")

    def test_single_char_parser_3(self) -> None:
        self.assertEqual(single_char_parser(['a', 'b'],"abc"), ("a", "bc"),
            msg=  "should be that: single character parser of the character 'a' does parse the string containing \"abc\"\
            \ characters and leaves \"bc\"")

    def test_single_char_parser_4(self) -> None:
        self.assertEqual(single_char_parser(['a', 'b'], "cba"), None,
            msg="should be that: single character parser of the character 'a' does parse the string containing \"abc\"\
            \ characters and leaves \"bc\"")

    def test_then_parser(self) -> None:
         """then-parser"""
         self.assertEqual(then_parser(partial(single_char_parser, ['a']), partial(single_char_parser, ['b']), "abc"), ("ab", "c"),
            msg="should be that: combining two single character parsers, parses two characters in same order")

    def test_then_parser_2(self) -> None:
        self.assertEqual(then_parser(partial(single_char_parser, ['a']), partial(single_char_parser, ['b']), "abc"),
                                     ("ab", "c"),
           msg="should be that: combining two single character parsers, does not parse two characters in opposite order")

    def test_then_parser_3(self) -> None:
        self.assertEqual(then_parser(partial(single_char_parser, ['a']), partial(single_char_parser, ['b']), "bac"),
        None,
        msg="should be that: combining two single character parsers, parses two characters")

    def test_many_parser(self) -> None:
         """should be that: a many-parser on one character succeeds parsing when the character is the same."""
         self.assertEqual(many_parser(partial(single_char_parser, ['a']), "a"), ("a", ""))
         self.assertEqual(many_parser(partial(single_char_parser, ['b']), "b"), ("b", ""))
         self.assertEqual(many_parser(partial(single_char_parser, ['3']), "3"), ("3", ""))

    def test_many_parser_1(self) -> None:
         """should be that: a many-parser on one character fails when parsing a string that does not start with that character."""
         self.assertEqual(many_parser(partial(single_char_parser, ['a']), "baa"), None)
         self.assertEqual(many_parser(partial(single_char_parser, ['z']), "az"), None)

    def test_many_parser_2(self) -> None:
        """should be that: a many-parser on one characters succeeds on a string that contains only that character"""
        self.assertEqual(many_parser(partial(single_char_parser, ['f']), "fff"), ("fff", ""))
        self.assertEqual(many_parser(partial(single_char_parser, ['f']), "fffa"), ("fff", "a"))
        self.assertEqual(many_parser(partial(single_char_parser, ['d']), "ddrst"), ("dd", "rst"))
    
    # def test_or_parser_3(self) -> None:
    #     """or-parser"""
    #     it "parses \"aaaf\" successfully" $ do
    #       or_parser (many_parser (single_char_parser ['f'])) (many_parser (single_char_parser ['a'])) "aaaf" `shouldBe` Just ("aaa", "f")
    #       or_parser (single_char_parser ['f']) (many_parser $ single_char_parser ['a']) "ffffa" `shouldBe` Just ("f", "fffa")
    #     it "parse failure case" $ do
    #       or_parser (many_parser $ single_char_parser ['a', 'b']) (many_parser $ single_char_parser ['k']) "ttttnnn" `shouldBe` Nothing
    #
    # def test_optional_parser(self) -> None:
    #     """optional parser"""
    #     it "parses \"aaaf\" successfully" $ do
    #       optional_parser (many_parser (single_char_parser ['a'])) "aaaf" `shouldBe` Just ("aaa", "f")
    #     it "parses \"bbb\" successfully without consuming any input" $ do
    #       optional_parser (many_parser (single_char_parser ['a'])) "bbb" `shouldBe` Just ("", "bbb")
    #     it "parses \"f\" successfully" $ do
    #       optional_parser (single_char_parser ['f']) "f" `shouldBe` Just("f", "")
    #     it "does parse \"d\" when expecting an \"f\", but does not consume \"d\"." $ do
    #       optional_parser (single_char_parser ['f']) "d" `shouldBe` Just("", "d")
