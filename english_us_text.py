"""
A module for containing any user facing text in the
English language.
"""
from typing import Final

application_title : Final[str] = "Phonetics Modeling Program"

menu: Final[str] = \
    """What do you want to accomplish?
  1) view the English phoneme inventory (as IPA graphemes).
  2) make a phoneme voiced.
  3) make a phoneme unvoiced.
  4) describe a phoneme in English.
  5) describe a phoneme in SPE Features.
  6) divide IPA text into phonemes (chunk)
  7) open window (user-friendly mode)
  Enter the number representing your selection below:
  after the prompt: and press enter/return.\n\n\n"""

userInput_viewEnglishPhonemeInventory: Final[str] = "1"
userInput_makeAPhonemeVoiced: Final[str] = "2"
userInput_makeAPhonemeUnvoiced: Final[str] = "3"
userInput_describeAPhonemeInEnglish: Final[str] = "4"
userInput_describeAPhonemeInSPE: Final[str] = "5"
userInput_chunkIPAByPhoneme: Final[str] = "6"
userInput_openWindow: Final[str] = "7"

prompt: Final[str] = "(PROMPT:) "

sorryUnableToCalculate: Final[str] = "Sorry: Final[str] unable to calculate answer with that input."

typeAPhoneme: Final[str] = \
    """Type a phoneme using IPA symbols: Final[str] and then press the enter key:
     and the computer will display"""

phonemeToDevoiceMessage: Final[str] = \
    """Type a phoneme using IPA symbols: Final[str] and then press the enter key:
     and the computer will display
     the devoiced counterpart (on the subsequent line):"""

phonemeToVoiceMessage: Final[str] = \
    """Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     the voiced counterpart (on the subsequent line):"""

phonemeToDescribeMessage: Final[str] = \
    """
    Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     its English description (on the subsequent line):"""

phonemeToCalculateSPEMessage: Final[str] = \
    """
    Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     its SPE features (on the subsequent line):"""

ipaTextToDivideMessage: Final[str] = \
    """
    Type text using IPA symbols: and then press the enter key:
     and the computer will display
     the text you entered with separate phonemes on separate lines:"""

pleaseReadReadmeMessage: Final[str] = "Please read README.md file for instructions on how to use."
programTerminatedNormallyMessage: Final[str] = "Program terminated normally."
userSelectedMessage: Final[str] = "The user selected:"
unrecognizedSelectionMessage: Final[str] = "Unrecognized selection. No action taken."
noAnalysisFoundMessage: Final[str] = "No analysis found!"

noEnglishDescriptionFound_message: Final[str] = "(no English description found.)"

consonant_Text: Final[str] = "consonant"
vowel_Text: Final[str] = "vowel"

front_BacknessText: Final[str] = "front"
central_BacknessText: Final[str] = "central"
back_BacknessText: Final[str] = "back"

close_HeightText: Final[str] = "close"
nearClose_HeightText: Final[str] = "near-close"
closeMid_HeightText: Final[str] = "close-mid"
mid_HeightText: Final[str] = "mid"
openMid_HeightText: Final[str] = "open-mid"
nearOpen_HeightText: Final[str] = "near-open"
open_HeightText: Final[str] = "open"

rounded_RoundingText: Final[str] = "rounded"
unrounded_RoundingText: Final[str] = "unrounded"

bilabial_PlaceText: Final[str] = "bilabial"
labioDental_PlaceText: Final[str] = "labio-dental"
dental_PlaceText: Final[str] = "dental"
alveolar_PlaceText: Final[str] = "alveolar"
postAlveolar_PlaceText: Final[str] = "post-alveolar"
retroflex_PlaceText: Final[str] = "retroflex"
palatal_PlaceText: Final[str] = "palatal"
velar_PlaceText: Final[str] = "velar"
uvular_PlaceText: Final[str] = "uvular"
pharyngeal_PlaceText: Final[str] = "pharyngeal"
glottal_PlaceText: Final[str] = "glottal"
epiglottal_PlaceText: Final[str] = "epiglottal"
labialVelar_PlaceText: Final[str] = "labial-velar"
labialPalatal_PlaceText: Final[str] = "labial-palatal"
alveoloPalatal_PlaceText: Final[str] = "alveolo-palatal"
palatoAlveolar_PlaceText: Final[str] = "palato-alveolar"

plosive_MannerText: Final[str] = "plosive"
nasal_MannerText: Final[str] = "nasal"
trill_MannerText: Final[str] = "trill"
tapOrFlap_MannerText: Final[str] = "tap or flap"
approximant_MannerText: Final[str] = "approximant"
fricative_MannerText: Final[str] = "fricative"
affricate_MannerText: Final[str] = "affricate"
lateralFricative_MannerText: Final[str] = "lateral fricative"
lateralApproximant_MannerText: Final[str] = "lateral approximant"
lateralFlap_MannerText: Final[str] = "lateral flap"
lateral_MannerText: Final[str] = "lateral"

pulmonicEgressive_AirstreamText: Final[str] = "pulmonic egressive"
click_AirstreamText: Final[str] = "click"
implosive_AirstreamText: Final[str] = "implosive"

voiced_VocalFoldsText: Final[str] = "voiced"
voiceless_VocalFoldsText: Final[str] = "voiceless"
voicedAspirated_VocalFoldsText: Final[str] = "voiced aspirated"
voicelessAspirated_VocalFoldsText: Final[str] = "voiceless aspirated"
creakyVoiced_VocalFoldsText: Final[str] = "creaky voiced"

syllabic_PhonemeFeatureText: Final[str] = "syllabic"
consonantal_PhonemeFeatureText: Final[str] = "consonantal"
sonorant_PhonemeFeatureText: Final[str] = "sonorant"
continuant_PhonemeFeatureText: Final[str] = "continuant"
voice_PhonemeFeatureText: Final[str] = "voice"
atr_PhonemeFeatureText: Final[str] = "ATR"
nasal_PhonemeFeatureText: Final[str] = "nasal"
lateral_PhonemeFeatureText: Final[str] = "lateral"
delayedRelease_PhonemeFeatureText: Final[str] = "delayed release"
spreadGlottis_PhonemeFeatureText: Final[str] = "spread glottis"
constrictedGlottis_PhonemeFeatureText: Final[str] = "constricted glottis"
labial_PhonemeFeatureText: Final[str] = "labial"
coronal_PhonemeFeatureText: Final[str] = "coronal"
dorsal_PhonemeFeatureText: Final[str] = "dorsal"
pharyngeal_PhonemeFeatureText: Final[str] = "pharyngeal"
laryngeal_PhonemeFeatureText: Final[str] = "laryngeal"
round_PhonemeFeatureText: Final[str] = "round"
anterior_PhonemeFeatureText: Final[str] = "anterior"
distributed_PhonemeFeatureText: Final[str] = "distributed"
strident_PhonemeFeatureText: Final[str] = "strident"
high_PhonemeFeatureText: Final[str] = "high"
low_PhonemeFeatureText: Final[str] = "low"
back_PhonemeFeatureText: Final[str] = "back"

showPhonemeInventoryText: Final[str] = "Show English Phoneme Inventory"
makeAPhonemeVoicedText: Final[str] = "make a phoneme voiced"
quitText: Final[str] = "Quit"
makeAPhonemeUnvoicedText: Final[str] = "make a phoneme unvoiced"
describePhonemeText: Final[str] = "Describe a phoneme"
getFeaturesOfPhonemeText: Final[str] = "Get sound patterns of English features of IPA transcription"
splitTranscriptionText: Final[str] = "split IPA transcription text"
