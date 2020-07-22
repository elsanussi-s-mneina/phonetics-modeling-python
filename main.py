"""
This is the main module.
This module is where the program begins running.
It first runs by showing the user text at the terminal.
First it shows a menu.
When the user enters the number for a menu item, it does what that menu item says.

One of the options is to open a window, so that the user can use the program graphically,
instead of via text.
"""

from typing import Callable

from english_us_text import PHONEME_TO_DEVOICE_MESSAGE, PHONEME_TO_VOICE_MESSAGE, \
    PHONEME_TO_DESCRIBE_MESSAGE, PHONEME_TO_CALCULATE_SPE_MESSAGE, \
    IPA_TEXT_TO_DIVIDE_MESSAGE, PROMPT, PLEASE_READ_README_MESSAGE, \
    PROGRAM_TERMINATED_NORMALLY_MESSAGE, USER_SELECTED_MESSAGE, \
    USER_INPUT_VIEW_ENGLISH_PHONEME_INVENTORY, \
    USER_INPUT_MAKE_A_PHONEME_UNVOICED, \
    USER_INPUT_DESCRIBE_A_PHONEME_IN_ENGLISH, \
    USER_INPUT_DESCRIBE_A_PHONEME_IN_SPE, \
    USER_INPUT_CHUNK_IPA_BY_PHONEME, \
    USER_INPUT_MAKE_A_PHONEME_VOICED, \
    USER_INPUT_OPEN_WINDOW, \
    UNRECOGNIZED_SELECTION_MESSAGE, \
    NO_ANALYSIS_FOUND_MESSAGE, \
    MENU

from lib_functions import (analyze_transcription, construct_transcription,
                           describe_transcription, devoiced_transcription,
                           english_phonet_inventory_report, ipa_text_to_phonet_list_report,
                           show_phonet, voiced_transcription,
                           analyze_transcription_to_sound_patterns_of_english
                           )
from lib_types import (Phonet)
from main_window import open_window


def put_prompt() -> None:
    """
    Print characters to the terminal, so that the
    user knows that they are expected to enter
    some text.
    """
    print(PROMPT, end="")


def put_blank_line() -> None:
    """
    Print a blank line on the terminal.
    :return: None
    """
    print("")


def put_blank_lines(count: int) -> None:
    """
    Print a specified number of blank lines on the terminal.
    :param count: number of lines
    :return: None
    """
    for _ in range(count):
        put_blank_line()


def prompt_for_text_and_apply(func: Callable[[str], str], instructions: str) -> None:
    """
    Given a function, and some instructions to show the user first,
    show the instructions, then get the user's input,
    and print the result of applying the function to the user's input.
    :param func: the function to apply
    :param instructions: the instructions to show the user in order to get them to give input.
    :return: None
    """
    print(instructions)
    put_prompt()
    interact(func)


def interact(func: Callable[[str], str]) -> None:
    """
    Given a function, asks the user for input,
    apply the function to the user input,
    and prints the result of the application
    of the function.
    :param func: the function to apply to the user input
    :return: None
    """
    user_input = input()
    print(func(user_input))


def prompt_for_phoneme_to_devoice() -> None:
    """
    Ask the user for a phoneme.
    The user inputs a phoneme.
    Take the phoneme, and print the phoneme that is as similar
    to the original phoneme, but unvoiced.
    :return: None
    """
    prompt_for_text_and_apply(devoiced_transcription, PHONEME_TO_DEVOICE_MESSAGE)


def prompt_for_phoneme_to_voice() -> None:
    """
    Ask the user for a phoneme.
    The user inputs a phoneme.
    Take the phoneme, and print the phoneme that is as similar
    to the original phoneme, but voiced.
    :return: None
    """
    prompt_for_text_and_apply(voiced_transcription, PHONEME_TO_VOICE_MESSAGE)


def prompt_for_phoneme_to_describe() -> None:
    """
    Ask the user for a phoneme.
    The user inputs a phoneme.
    Take the phoneme, and print the
    description of the phoneme.
    :return: None
    """
    prompt_for_text_and_apply(describe_transcription, PHONEME_TO_DESCRIBE_MESSAGE)


def prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from() -> None:
    """
    Ask the user for a phoneme.
    The user inputs a phoneme.
    Take the phoneme, calculate what
    the features of it are (according to Sound Patterns of English)
    and print those features.
    :return: None
    """
    prompt_for_text_and_apply(analyze_transcription_to_sound_patterns_of_english,
                              PHONEME_TO_CALCULATE_SPE_MESSAGE)


def prompt_for_transcription_text_to_split() -> None:
    """
    Ask the user for IPA text which may contain multiple IPA characters
    and phonemes. Take that input, and print each phoneme on
    separate lines.
    :return: None
    """
    prompt_for_text_and_apply(ipa_text_to_phonet_list_report, IPA_TEXT_TO_DIVIDE_MESSAGE)



def main() -> None:
    """
    This function is where the program starts running.
    :return: None
    """
    print(PLEASE_READ_README_MESSAGE)
    print(MENU, end="")
    put_prompt()
    selection = input()
    acknowledge_and_respond(selection)
    put_blank_line()
    print(PROGRAM_TERMINATED_NORMALLY_MESSAGE)
    put_blank_lines(2)


def acknowledge_and_respond(selection: str) -> None:
    """
    Tell the user what they selected. This is necessary
    for better user-friendliness.
    :param selection: what the user typed in
    :return: None
    """
    print()
    print(' '.join([USER_SELECTED_MESSAGE, selection]))
    put_blank_line()
    respond_to_selection(selection)




def respond_to_selection(selection: str) -> None:
    """
    Start the appropriate action according to what the user already selected.
    :param selection: the text the user put in after being shown the menu.
    :return: None
    """
    if selection == USER_INPUT_VIEW_ENGLISH_PHONEME_INVENTORY:
        print(english_phonet_inventory_report)
    elif selection == USER_INPUT_MAKE_A_PHONEME_VOICED:
        prompt_for_phoneme_to_voice()
    elif selection == USER_INPUT_MAKE_A_PHONEME_UNVOICED:
        prompt_for_phoneme_to_devoice()
    elif selection == USER_INPUT_DESCRIBE_A_PHONEME_IN_ENGLISH:
        prompt_for_phoneme_to_describe()
    elif selection == USER_INPUT_DESCRIBE_A_PHONEME_IN_SPE:
        prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from()
    elif selection == USER_INPUT_CHUNK_IPA_BY_PHONEME:
        prompt_for_transcription_text_to_split()
    elif selection == USER_INPUT_OPEN_WINDOW:
        open_window()
    else:
        print(UNRECOGNIZED_SELECTION_MESSAGE)


def do_analyze_transcription(transcription: str) -> str:
    """
    Given an IPA transcription, return the
    name of the phoneme that IPA transcription describes.
    If the IPA transcription could not be named,
    return a message saying so.
    :param transcription: text from the International Phonetic Alphabet
    :return: the name of the phoneme, or a message saying the phoneme was not recognized
    """
    result = show_phonet(analyze_transcription(transcription))
    if result is None:
        return NO_ANALYSIS_FOUND_MESSAGE
    return result


def do_construct_transcription(phonet: Phonet) -> None:
    """
    Given a set of phoneme properties that describe a phoneme, like:
    voiced velar fricative pulmonic egressive,
    print the IPA transcription of it to the terminal.
    :param phonet: The Phonete (a representation of a phoneme)
    :return: None
    """
    print(construct_transcription(phonet))


if __name__ == "__main__":
    main()
