from typing import Callable
from tkinter import Button, simpledialog, Tk, Frame, StringVar, Label, RAISED, LEFT, E

from english_us_text import *
from lib_functions import (analyze_features, analyze_transcription, construct_transcription,
                           describe_transcription, devoiced_transcription,
                           english_phonet_inventory_report, ipa_text_to_phonet_list_report,
                           show_features, show_phonet, voiced_transcription,
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


makeAPhonemeUnvoicedText: str = "make a phoneme unvoiced"


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.show_inventory_button = Button(self)
        self.show_inventory_button["text"] = showPhonemeInventoryText
        self.show_inventory_button["command"] = self.show_english_phoneme_inventory
        self.show_inventory_button.pack(side="top")

        self.voice_phoneme_button = Button(self)
        self.voice_phoneme_button["text"] = makeAPhonemeVoicedText
        self.voice_phoneme_button["command"] = self.make_phoneme_voiced
        self.voice_phoneme_button.pack(side="top")

        self.devoice_phoneme_button = Button(self)
        self.devoice_phoneme_button["text"] = makeAPhonemeUnvoicedText
        self.devoice_phoneme_button["command"] = self.make_phoneme_unvoiced
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

    def show_english_phoneme_inventory(self):
        self.output_to_user.set(english_phonet_inventory_report)

    def make_phoneme_voiced(self):
        self.prompt_for_phoneme_to_voice()

    def prompt_for_phoneme_to_voice(self) -> None:
        answer = simpledialog.askstring("title", phonemeToVoiceMessage)
        voiced_phoneme = voiced_transcription(answer)
        self.output_to_user.set(voiced_phoneme)

    def make_phoneme_unvoiced(self):
        self.prompt_for_phoneme_to_unvoice()

    def prompt_for_phoneme_to_unvoice(self):
        answer = simpledialog.askstring("title", phonemeToDevoiceMessage)
        devoiced_phoneme = devoiced_transcription(answer)
        self.output_to_user.set(devoiced_phoneme)

    def prompt_for_phoneme_to_describe(self) -> None:
        answer = simpledialog.askstring("title", phonemeToDescribeMessage)
        description = describe_transcription(answer)
        self.output_to_user.set(description)

    def prompt_for_phoneme_to_calculate_sound_patterns_of_english_features_from(self) -> None:
        answer = simpledialog.askstring("title", phonemeToCalculateSPEMessage)
        features = analyze_transcription_to_sound_patterns_of_english(answer)
        self.output_to_user.set(features)

    def prompt_for_transcription_text_to_split(self) -> None:
        answer = simpledialog.askstring("title", ipaTextToDivideMessage)
        report = ipa_text_to_phonet_list_report(answer)
        self.output_to_user.set(report)


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


def open_window():
    root = Tk()
    root.wm_title(application_title)
    app = Application(master=root)
    app.mainloop()


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
    elif selection == userInput_openWindow:
        open_window()
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
