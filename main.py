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
from tkinter import Button, simpledialog, Tk, Frame, StringVar, Label, RAISED, LEFT

from english_us_text import phonemeToDevoiceMessage, phonemeToVoiceMessage, \
    phonemeToDescribeMessage, phonemeToCalculateSPEMessage, \
    ipaTextToDivideMessage, showPhonemeInventoryText, \
    makeAPhonemeVoicedText, describePhonemeText, getFeaturesOfPhonemeText, \
    splitTranscriptionText, quitText, prompt, pleaseReadReadmeMessage, \
    programTerminatedNormallyMessage, userSelectedMessage, application_title, \
    userInput_viewEnglishPhonemeInventory, \
    userInput_makeAPhonemeUnvoiced, \
    userInput_describeAPhonemeInEnglish, \
    userInput_describeAPhonemeInSPE, \
    userInput_chunkIPAByPhoneme, \
    userInput_makeAPhonemeVoiced, \
    userInput_openWindow, \
    unrecognizedSelectionMessage, \
    noAnalysisFoundMessage, \
    menu

from lib_functions import (analyze_transcription, construct_transcription,
                           describe_transcription, devoiced_transcription,
                           english_phonet_inventory_report, ipa_text_to_phonet_list_report,
                           show_phonet, voiced_transcription,
                           analyze_transcription_to_sound_patterns_of_english
                           )
from lib_types import (Phonet)


def put_prompt() -> None:
    """
    Print characters to the terminal, so that the
    user knows that they are expected to enter
    some text.
    """
    print(prompt, end="")


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
    prompt_for_text_and_apply(devoiced_transcription, phonemeToDevoiceMessage)


def prompt_for_phoneme_to_voice() -> None:
    """
    Ask the user for a phoneme.
    The user inputs a phoneme.
    Take the phoneme, and print the phoneme that is as similar
    to the original phoneme, but voiced.
    :return: None
    """
    prompt_for_text_and_apply(voiced_transcription, phonemeToVoiceMessage)


def prompt_for_phoneme_to_describe() -> None:
    """
    Ask the user for a phoneme.
    The user inputs a phoneme.
    Take the phoneme, and print the
    description of the phoneme.
    :return: None
    """
    prompt_for_text_and_apply(describe_transcription, phonemeToDescribeMessage)


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
                              phonemeToCalculateSPEMessage)


def prompt_for_transcription_text_to_split() -> None:
    """
    Ask the user for IPA text which may contain multiple IPA characters
    and phonemes. Take that input, and print each phoneme on
    separate lines.
    :return: None
    """
    prompt_for_text_and_apply(ipa_text_to_phonet_list_report, ipaTextToDivideMessage)


makeAPhonemeUnvoicedText: str = "make a phoneme unvoiced"


class Application(Frame):
    """
    A window where the user can select an action to do,
    and results are shown at the bottom of the window.
    """
    def __init__(self, master=None):
        """
        Initialize the main window
        :param master: the root of Tkinter
        """
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create widgets that go on the window
        """
        self.show_inventory_button = Button(self)
        self.show_inventory_button["text"] = showPhonemeInventoryText
        self.show_inventory_button["command"] = self.show_english_phoneme_inventory
        self.show_inventory_button.pack(side="top")

        self.voice_phoneme_button = Button(self)
        self.voice_phoneme_button["text"] = makeAPhonemeVoicedText
        self.voice_phoneme_button["command"] = self.prompt_for_phoneme_to_voice
        self.voice_phoneme_button.pack(side="top")

        self.devoice_phoneme_button = Button(self)
        self.devoice_phoneme_button["text"] = makeAPhonemeUnvoicedText
        self.devoice_phoneme_button["command"] = self.prompt_for_phoneme_to_unvoice
        self.devoice_phoneme_button.pack(side="top")

        self.describe_phoneme_button = Button(self)
        self.describe_phoneme_button["text"] = describePhonemeText
        self.describe_phoneme_button["command"] = self.prompt_for_phoneme_to_describe
        self.describe_phoneme_button.pack(side="top")

        self.featurize_phoneme_button = Button(self)
        self.featurize_phoneme_button["text"] = getFeaturesOfPhonemeText
        self.featurize_phoneme_button[
            "command"] = \
            self.prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from
        self.featurize_phoneme_button.pack(side="top")

        self.split_transcription_button = Button(self)
        self.split_transcription_button["text"] = splitTranscriptionText
        self.split_transcription_button["command"] = self.prompt_for_transcription_text_to_split
        self.split_transcription_button.pack(side="top")
        self.output_to_user = StringVar()
        self.output_to_user_label = Label(self, textvariable=self.output_to_user, relief=RAISED,
                                          width=100, wraplength=1000, justify=LEFT)

        self.output_to_user.set("")
        self.output_to_user_label.pack(side="top")

        self.quit = Button(self, text=quitText, fg="red",
                           command=self.master.destroy)
        self.quit.pack(side="right", padx=30)

    def show_english_phoneme_inventory(self) -> None:
        """
        Show all the phonemes in English.
        :return: None
        """
        self.output_to_user.set(english_phonet_inventory_report)

    def prompt_for_phoneme_to_voice(self) -> None:
        """
        Ask the user for a phoneme,
        and show the closest phoneme to it that is voiced.
        :return: None
        """
        answer = simpledialog.askstring("title", phonemeToVoiceMessage)
        voiced_phoneme = voiced_transcription(answer)
        self.output_to_user.set(voiced_phoneme)

    def prompt_for_phoneme_to_unvoice(self):
        """
        Ask the user for a phoneme,
        and show the closest phoneme to it that is unvoiced.
        :return: None
        """
        answer = simpledialog.askstring("title", phonemeToDevoiceMessage)
        devoiced_phoneme = devoiced_transcription(answer)
        self.output_to_user.set(devoiced_phoneme)

    def prompt_for_phoneme_to_describe(self) -> None:
        """
        Ask the user for a phoneme,
        and show the description of the phoneme.
        :return: None
        """
        answer = simpledialog.askstring("title", phonemeToDescribeMessage)
        description = describe_transcription(answer)
        self.output_to_user.set(description)

    def prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from(self) -> None:
        """
        Ask the user for a phoneme,
        and show its features according to Sound Patterns of English.
        :return: None
        """
        answer = simpledialog.askstring("title", phonemeToCalculateSPEMessage)
        features = analyze_transcription_to_sound_patterns_of_english(answer)
        self.output_to_user.set(features)

    def prompt_for_transcription_text_to_split(self) -> None:
        """
        Ask the user for text in the International Phonetic Alphabet,
        and print the phonemes that are in the text in order, with its description.
        With each phoneme on separate lines.
        :return: None
        """
        answer = simpledialog.askstring("title", ipaTextToDivideMessage)
        report = ipa_text_to_phonet_list_report(answer)
        self.output_to_user.set(report)


def main() -> None:
    """
    This function is where the program starts running.
    :return: None
    """
    print(pleaseReadReadmeMessage)
    print(menu, end="")
    put_prompt()
    selection = input()
    acknowledge_and_respond(selection)
    put_blank_line()
    print(programTerminatedNormallyMessage)
    put_blank_lines(2)


def acknowledge_and_respond(selection: str) -> None:
    """
    Tell the user what they selected. This is necessary
    for better user-friendliness.
    :param selection: what the user typed in
    :return: None
    """
    print()
    print(' '.join([userSelectedMessage, selection]))
    put_blank_line()
    respond_to_selection(selection)

def open_window() -> None:
    """
    Open a window.
    :return: None
    """
    root = Tk()
    root.wm_title(application_title)
    app = Application(master=root)
    app.mainloop()


def respond_to_selection(selection: str) -> None:
    """
    Start the appropriate action according to what the user already selected.
    :param selection: the text the user put in after being shown the menu.
    :return: None
    """
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
    elif selection == userInput_openWindow:
        open_window()
    else:
        print(unrecognizedSelectionMessage)


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
        return noAnalysisFoundMessage
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
