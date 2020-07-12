from typing import Callable

from english_us_text import *
from lib_functions import (analyze_features, analyze_transcription, construct_transcription,
                           describe_transcription, devoiced_transcription,
                           english_phonet_inventory_report, ipa_text_to_phonet_list_report,
                           show_features, show_phonet, voiced_transcription
                           )
from lib_types import (Phonet)


def put_prompt() -> None:
    """
    Print characters to the terminal, so that the
    user knows that they are expected to enter
    some text.
    """
    print(prompt, end="")

def analyze_transcription_to_sound_patterns_of_english(transcription: str) -> str:
    result = show_features(analyze_features(analyze_transcription(transcription)))
    if result is None:
        return sorryUnableToCalculate
    return result

def put_blank_line() -> None:
    print("")

def put_blank_lines(count: int) -> None:
    for _ in range(count):
        put_blank_line()

def prompt_for_text_and_apply(func: Callable[[str], str], instructions: str) -> None:
    print(instructions)
    put_prompt()
    interact(func)

def interact(func: Callable[[str], str]) -> None:
    user_input = input()
    print(func(user_input))

def prompt_for_phoneme_to_devoice() -> None:
    prompt_for_text_and_apply(devoiced_transcription, phonemeToDevoiceMessage)

def prompt_for_phoneme_to_voice() -> None:
    prompt_for_text_and_apply(voiced_transcription, phonemeToVoiceMessage)

def prompt_for_phoneme_to_describe() -> None:
    prompt_for_text_and_apply(describe_transcription, phonemeToDescribeMessage)

def prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from() -> None:
    prompt_for_text_and_apply(analyze_transcription_to_sound_patterns_of_english,
                              phonemeToCalculateSPEMessage)

def prompt_for_transcription_text_to_split() -> None:
    prompt_for_text_and_apply(ipa_text_to_phonet_list_report, ipaTextToDivideMessage)

def main() -> None:
    print(pleaseReadReadmeMessage)
    print(menu, end="")
    put_prompt()
    user_input = input()
    handle_selection(user_input)
    put_blank_line()
    print(programTerminatedNormallyMessage)
    put_blank_lines(2)

def handle_selection(selection: str) -> None:
    print()
    print(' '.join([userSelectedMessage, selection]))
    put_blank_line()
    respond_to_selection(selection)


def respond_to_selection(selection: str) -> None:
    if selection == userInput_viewEnglishPhonemeInventory:
        print(english_phonet_inventory_report)
    elif selection == userInput_makeAPhonemeVoiced:
        prompt_for_phoneme_to_voice()
    elif selection == userInput_makeAPhonemeUnvoiced:
        prompt_for_phoneme_to_devoice()
    elif selection == userInput_describeAPhonemeInEnglish:
        prompt_for_phoneme_to_describe()
    elif selection == userInput_describeAPhonemeInSPE:
        prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from()
    elif selection == userInput_chunkIPAByPhoneme:
        prompt_for_transcription_text_to_split()
    else:
        print(unrecognizedSelectionMessage)

def do_analyze_transcription(x: str) -> str:
    result = show_phonet(analyze_transcription(x))
    if result is None:
        return noAnalysisFoundMessage
    return result

def do_construct_transcription(phonet: Phonet) -> None:
    print(construct_transcription(phonet))


if __name__ == "__main__":
    main()
