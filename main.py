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
from tkinter import Button, simpledialog, Tk, StringVar, Label, RAISED, LEFT, N, W, E, S

from english_us_text import PHONEME_TO_DEVOICE_MESSAGE, PHONEME_TO_VOICE_MESSAGE, \
    PHONEME_TO_DESCRIBE_MESSAGE, PHONEME_TO_CALCULATE_SPE_MESSAGE, \
    IPA_TEXT_TO_DIVIDE_MESSAGE, SHOW_PHONEME_INVENTORY_TEXT, \
    MAKE_A_PHONEME_VOICED_TEXT, DESCRIBE_PHONEME_TEXT, GET_FEATURES_OF_PHONEME_TEXT, \
    SPLIT_TRANSCRIPTION_TEXT, QUIT_TEXT, PROMPT, PLEASE_READ_README_MESSAGE, \
    PROGRAM_TERMINATED_NORMALLY_MESSAGE, USER_SELECTED_MESSAGE, APPLICATION_TITLE, \
    USER_INPUT_VIEW_ENGLISH_PHONEME_INVENTORY, \
    USER_INPUT_MAKE_A_PHONEME_UNVOICED, \
    USER_INPUT_DESCRIBE_A_PHONEME_IN_ENGLISH, \
    USER_INPUT_DESCRIBE_A_PHONEME_IN_SPE, \
    USER_INPUT_CHUNK_IPA_BY_PHONEME, \
    USER_INPUT_MAKE_A_PHONEME_VOICED, \
    USER_INPUT_OPEN_WINDOW, \
    UNRECOGNIZED_SELECTION_MESSAGE, \
    NO_ANALYSIS_FOUND_MESSAGE, \
    MENU, DIALOG_WINDOW_TITLE, MAKE_A_PHONEME_UNVOICED_TEXT, VOICED_PHONEME_HEADER, \
    UNVOICED_PHONEME_HEADER, PHONEME_DESCRIPTION_HEADER, PHONEMES_SPLIT_HEADER, FEATURES_HEADER

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


class Application:
    """
    A window where the user can select an action to do,
    and results are shown at the bottom of the window.
    """

    def __init__(self, master=None):
        """
        Initialize the main window
        :param master: the root of Tkinter
        """
        super().__init__()
        self.master = master
        self.voice_phoneme_button = Button(self.master)
        self.devoice_phoneme_button = Button(self.master)
        self.describe_phoneme_button = Button(self.master)
        self.featurize_phoneme_button = Button(self.master)
        self.split_transcription_button = Button(self.master)
        self.output_description = StringVar()
        self.output_description_label = Label(self.master, textvariable=self.output_description,
                                              width=100, justify=LEFT)
        self.output_to_user = StringVar()
        self.output_to_user_label = Label(self.master, textvariable=self.output_to_user,
                                          relief=RAISED,
                                          width=100, wraplength=1000, justify=LEFT)
        self.quit = Button(self.master, text=QUIT_TEXT, fg="red",
                           command=self.master.destroy)
        self.show_inventory_button = Button(self.master)
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create widgets that go on the window
        """
        self.show_inventory_button["text"] = SHOW_PHONEME_INVENTORY_TEXT
        self.show_inventory_button["command"] = self.show_english_phoneme_inventory
        self.show_inventory_button.grid(row=0, column=0, sticky=W, pady=20, padx=20,
                                        ipadx=5, ipady=10)

        self.voice_phoneme_button["text"] = MAKE_A_PHONEME_VOICED_TEXT
        self.voice_phoneme_button["command"] = self.prompt_for_phoneme_to_voice
        self.voice_phoneme_button.grid(row=1, column=0, sticky=W, pady=20, padx=20,
                                       ipadx=5, ipady=10)

        self.devoice_phoneme_button["text"] = MAKE_A_PHONEME_UNVOICED_TEXT
        self.devoice_phoneme_button["command"] = self.prompt_for_phoneme_to_unvoice
        self.devoice_phoneme_button.grid(row=2, column=0, sticky=W, pady=20, padx=20,
                                         ipadx=5, ipady=10)

        self.describe_phoneme_button["text"] = DESCRIBE_PHONEME_TEXT
        self.describe_phoneme_button["command"] = self.prompt_for_phoneme_to_describe
        self.describe_phoneme_button.grid(row=3, column=0, sticky=W, pady=20, padx=20,
                                          ipadx=5, ipady=10)

        self.featurize_phoneme_button["text"] = GET_FEATURES_OF_PHONEME_TEXT
        self.featurize_phoneme_button["command"] = \
            self.prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from
        self.featurize_phoneme_button.grid(row=4, column=0, sticky=W, pady=20, padx=20,
                                           ipadx=5, ipady=10)

        self.split_transcription_button["text"] = SPLIT_TRANSCRIPTION_TEXT
        self.split_transcription_button["command"] = self.prompt_for_transcription_text_to_split
        self.split_transcription_button.grid(row=5, column=0, sticky=W, pady=20, padx=20,
                                             ipadx=5, ipady=10)

        self.output_description.set("Result:")
        self.output_description_label.grid(row=0, column=1)
        self.output_to_user.set("")
        self.output_to_user_label.grid(row=1, column=1, rowspan=5, sticky=N + S, pady=20, padx=20,
                                       ipadx=5, ipady=10)

        self.quit.grid(row=7, column=1, sticky=E, pady=20, padx=20, ipadx=10, ipady=10)

    def show_english_phoneme_inventory(self) -> None:
        """
        Show all the phonemes in English.
        :return: None
        """
        self.output_to_user.set(english_phonet_inventory_report)
        self.output_description.set("English Phoneme Inventory")

    def prompt_for_phoneme_to_voice(self) -> None:
        """
        Ask the user for a phoneme,
        and show the closest phoneme to it that is voiced.
        :return: None
        """
        answer = simpledialog.askstring(DIALOG_WINDOW_TITLE, PHONEME_TO_VOICE_MESSAGE)
        if answer is not None:
            voiced_phoneme = voiced_transcription(answer)
            self.output_to_user.set(voiced_phoneme)
            self.output_description.set(VOICED_PHONEME_HEADER)

    def prompt_for_phoneme_to_unvoice(self):
        """
        Ask the user for a phoneme,
        and show the closest phoneme to it that is unvoiced.
        :return: None
        """
        answer = simpledialog.askstring(DIALOG_WINDOW_TITLE, PHONEME_TO_DEVOICE_MESSAGE)
        if answer is not None:
            devoiced_phoneme = devoiced_transcription(answer)
            self.output_to_user.set(devoiced_phoneme)
            self.output_description.set(UNVOICED_PHONEME_HEADER)

    def prompt_for_phoneme_to_describe(self) -> None:
        """
        Ask the user for a phoneme,
        and show the description of the phoneme.
        :return: None
        """
        answer = simpledialog.askstring(DIALOG_WINDOW_TITLE, PHONEME_TO_DESCRIBE_MESSAGE)
        if answer is not None:
            description = describe_transcription(answer)
            self.output_to_user.set(description)
            self.output_description.set(PHONEME_DESCRIPTION_HEADER)

    def prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from(self) -> None:
        """
        Ask the user for a phoneme,
        and show its features according to Sound Patterns of English.
        :return: None
        """
        answer = simpledialog.askstring(DIALOG_WINDOW_TITLE, PHONEME_TO_CALCULATE_SPE_MESSAGE)
        if answer is not None:
            features = analyze_transcription_to_sound_patterns_of_english(answer)
            self.output_to_user.set(features)
            self.output_description.set(FEATURES_HEADER)

    def prompt_for_transcription_text_to_split(self) -> None:
        """
        Ask the user for text in the International Phonetic Alphabet,
        and print the phonemes that are in the text in order, with its description.
        With each phoneme on separate lines.
        :return: None
        """
        answer = simpledialog.askstring(DIALOG_WINDOW_TITLE, IPA_TEXT_TO_DIVIDE_MESSAGE)
        if answer is not None:
            report = ipa_text_to_phonet_list_report(answer)
            self.output_to_user.set(report)
            self.output_description.set(PHONEMES_SPLIT_HEADER)


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


def open_window() -> None:
    """
    Open a window.
    :return: None
    """
    root = Tk()
    root.wm_title(APPLICATION_TITLE)
    Application(master=root)
    root.mainloop()


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
