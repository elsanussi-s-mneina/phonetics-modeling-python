"""
The graphical user interface is defined in this module.
"""
from tkinter import Button, Tk, StringVar, Label, RAISED, LEFT, N, W, E, S, Entry

from english_us_text import SHOW_PHONEME_INVENTORY_TEXT, \
    MAKE_A_PHONEME_VOICED_TEXT, DESCRIBE_PHONEME_TEXT, GET_FEATURES_OF_PHONEME_TEXT, \
    SPLIT_TRANSCRIPTION_TEXT, QUIT_TEXT, MAKE_A_PHONEME_UNVOICED_TEXT, \
    VOICED_PHONEME_HEADER, \
    UNVOICED_PHONEME_HEADER, PHONEME_DESCRIPTION_HEADER, PHONEMES_SPLIT_HEADER, FEATURES_HEADER, \
    RESULT_HEADER, ENGLISH_PHONEME_INVENTORY_HEADER, APPLICATION_TITLE, INPUT_HEADER
from lib_functions import (describe_transcription, devoiced_transcription,
                           english_phonet_inventory_report, ipa_text_to_phonet_list_report,
                           voiced_transcription,
                           analyze_transcription_to_sound_patterns_of_english
                           )


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
        self.output_to_user = StringVar()
        self.output_to_user_widget = Label(self.master,
                                           textvariable=self.output_to_user,
                                           relief=RAISED,
                                           width=100,
                                           wraplength=1000,
                                           justify=LEFT)
        self.output_to_user_widget.grid(row=1,
                                        column=1,
                                        rowspan=5,
                                        sticky=N + S,
                                        pady=20,
                                        padx=20,
                                        ipadx=5,
                                        ipady=10)

        self.output_description = StringVar()
        self.output_description_label = Label(self.master,
                                              textvariable=self.output_description,
                                              width=100,
                                              justify=LEFT)

        self.output_description_label.grid(row=0,
                                           column=1)

        self.output_description.set(RESULT_HEADER)

        input_box_label = Label(master,
                                text=INPUT_HEADER)
        input_box_label.grid(row=1,
                             column=0,
                             sticky=W)

        self.input_box = Entry(master)
        self.input_box.grid(row=2,
                            column=0,
                            sticky=W,
                            pady=20,
                            padx=10)

        show_inventory_button = Button(self.master,
                                       text=SHOW_PHONEME_INVENTORY_TEXT)
        show_inventory_button.grid(row=0,
                                   column=0,
                                   sticky=W,
                                   pady=20,
                                   padx=20,
                                   ipadx=5,
                                   ipady=10)

        voice_phoneme_button = Button(self.master,
                                      text=MAKE_A_PHONEME_VOICED_TEXT)
        voice_phoneme_button.grid(row=3,
                                  column=0,
                                  sticky=W,
                                  pady=20,
                                  padx=20,
                                  ipadx=5,
                                  ipady=10)

        devoice_phoneme_button = Button(self.master,
                                        text=MAKE_A_PHONEME_UNVOICED_TEXT)
        devoice_phoneme_button.grid(row=4,
                                    column=0,
                                    sticky=W,
                                    pady=20,
                                    padx=20,
                                    ipadx=5,
                                    ipady=10)

        describe_phoneme_button = Button(self.master,
                                         text=DESCRIBE_PHONEME_TEXT)
        describe_phoneme_button.grid(row=5,
                                     column=0,
                                     sticky=W,
                                     pady=20,
                                     padx=20,
                                     ipadx=5,
                                     ipady=10)

        featurize_phoneme_button = Button(self.master,
                                          text=GET_FEATURES_OF_PHONEME_TEXT)
        featurize_phoneme_button.grid(row=6,
                                      column=0,
                                      sticky=W,
                                      pady=20,
                                      padx=20,
                                      ipadx=5,
                                      ipady=10)

        split_transcription_button = Button(self.master,
                                            text=SPLIT_TRANSCRIPTION_TEXT)
        split_transcription_button.grid(row=7,
                                        column=0,
                                        sticky=W,
                                        pady=20,
                                        padx=20,
                                        ipadx=5,
                                        ipady=10)

        quit_button = Button(self.master, text=QUIT_TEXT, fg="red",
                             command=self.master.destroy)
        quit_button.grid(row=7, column=1, sticky=E, pady=20, padx=20, ipadx=10, ipady=10)

        voice_phoneme_button["command"] = self.prompt_for_phoneme_to_voice
        devoice_phoneme_button["command"] = self.prompt_for_phoneme_to_unvoice
        describe_phoneme_button["command"] = self.prompt_for_phoneme_to_describe
        featurize_phoneme_button["command"] = \
            self.prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from
        split_transcription_button["command"] = self.prompt_for_transcription_text_to_split
        show_inventory_button["command"] = self.show_english_phoneme_inventory

    def show_english_phoneme_inventory(self) -> None:
        """
        Show all the phonemes in English.
        :return: None
        """
        self.output_to_user.set(english_phonet_inventory_report)
        self.output_description.set(ENGLISH_PHONEME_INVENTORY_HEADER)

    def prompt_for_phoneme_to_voice(self) -> None:
        """
        Ask the user for a phoneme,
        and show the closest phoneme to it that is voiced.
        :return: None
        """
        answer = self.input_box.get()
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
        answer = self.input_box.get()
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
        answer = self.input_box.get()
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
        answer = self.input_box.get()
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
        answer = self.input_box.get()
        if answer is not None:
            report = ipa_text_to_phonet_list_report(answer)
            self.output_to_user.set(report)
            self.output_description.set(PHONEMES_SPLIT_HEADER)


def open_window() -> None:
    """
    Open a window.
    :return: None
    """
    root = Tk()
    root.wm_title(APPLICATION_TITLE)
    Application(master=root)
    root.mainloop()
