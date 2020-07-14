"""
A module for containing any user facing text in the
English language.
"""

application_title = "Phonetics Modeling Program"

menu: str = \
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

userInput_viewEnglishPhonemeInventory: str = "1"
userInput_makeAPhonemeVoiced: str = "2"
userInput_makeAPhonemeUnvoiced: str = "3"
userInput_describeAPhonemeInEnglish: str = "4"
userInput_describeAPhonemeInSPE: str = "5"
userInput_chunkIPAByPhoneme: str = "6"
userInput_openWindow: str = "7"

prompt: str = "(PROMPT:) "

sorryUnableToCalculate: str = "Sorry: str unable to calculate answer with that input."

typeAPhoneme: str = \
    """Type a phoneme using IPA symbols: str and then press the enter key:
     and the computer will display"""

phonemeToDevoiceMessage: str = \
    """Type a phoneme using IPA symbols: str and then press the enter key:
     and the computer will display
     the devoiced counterpart (on the subsequent line):"""

phonemeToVoiceMessage: str = \
    """Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     the voiced counterpart (on the subsequent line):"""

phonemeToDescribeMessage: str = \
    """
    Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     its English description (on the subsequent line):"""

phonemeToCalculateSPEMessage: str = \
    """
    Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     its SPE features (on the subsequent line):"""

ipaTextToDivideMessage: str = \
    """
    Type text using IPA symbols: and then press the enter key:
     and the computer will display
     the text you entered with separate phonemes on separate lines:"""

pleaseReadReadmeMessage: str = "Please read README.md file for instructions on how to use."
programTerminatedNormallyMessage: str = "Program terminated normally."
userSelectedMessage: str = "The user selected:"
unrecognizedSelectionMessage: str = "Unrecognized selection. No action taken."
noAnalysisFoundMessage: str = "No analysis found!"

noEnglishDescriptionFound_message: str = "(no English description found.)"

consonant_Text: str = "consonant"
vowel_Text: str = "vowel"

front_BacknessText: str = "front"
central_BacknessText: str = "central"
back_BacknessText: str = "back"

close_HeightText: str = "close"
nearClose_HeightText: str = "near-close"
closeMid_HeightText: str = "close-mid"
mid_HeightText: str = "mid"
openMid_HeightText: str = "open-mid"
nearOpen_HeightText: str = "near-open"
open_HeightText: str = "open"

rounded_RoundingText: str = "rounded"
unrounded_RoundingText: str = "unrounded"

bilabial_PlaceText: str = "bilabial"
labioDental_PlaceText: str = "labio-dental"
dental_PlaceText: str = "dental"
alveolar_PlaceText: str = "alveolar"
postAlveolar_PlaceText: str = "post-alveolar"
retroflex_PlaceText: str = "retroflex"
palatal_PlaceText: str = "palatal"
velar_PlaceText: str = "velar"
uvular_PlaceText: str = "uvular"
pharyngeal_PlaceText: str = "pharyngeal"
glottal_PlaceText: str = "glottal"
epiglottal_PlaceText: str = "epiglottal"
labialVelar_PlaceText: str = "labial-velar"
labialPalatal_PlaceText: str = "labial-palatal"
alveoloPalatal_PlaceText: str = "alveolo-palatal"
palatoAlveolar_PlaceText: str = "palato-alveolar"

plosive_MannerText: str = "plosive"
nasal_MannerText: str = "nasal"
trill_MannerText: str = "trill"
tapOrFlap_MannerText: str = "tap or flap"
approximant_MannerText: str = "approximant"
fricative_MannerText: str = "fricative"
affricate_MannerText: str = "affricate"
lateralFricative_MannerText: str = "lateral fricative"
lateralApproximant_MannerText: str = "lateral approximant"
lateralFlap_MannerText: str = "lateral flap"
lateral_MannerText: str = "lateral"

pulmonicEgressive_AirstreamText: str = "pulmonic egressive"
click_AirstreamText: str = "click"
implosive_AirstreamText: str = "implosive"

voiced_VocalFoldsText: str = "voiced"
voiceless_VocalFoldsText: str = "voiceless"
voicedAspirated_VocalFoldsText: str = "voiced aspirated"
voicelessAspirated_VocalFoldsText: str = "voiceless aspirated"
creakyVoiced_VocalFoldsText: str = "creaky voiced"

syllabic_PhonemeFeatureText: str = "syllabic"
consonantal_PhonemeFeatureText: str = "consonantal"
sonorant_PhonemeFeatureText: str = "sonorant"
continuant_PhonemeFeatureText: str = "continuant"
voice_PhonemeFeatureText: str = "voice"
atr_PhonemeFeatureText: str = "ATR"
nasal_PhonemeFeatureText: str = "nasal"
lateral_PhonemeFeatureText: str = "lateral"
delayedRelease_PhonemeFeatureText: str = "delayed release"
spreadGlottis_PhonemeFeatureText: str = "spread glottis"
constrictedGlottis_PhonemeFeatureText: str = "constricted glottis"
labial_PhonemeFeatureText: str = "labial"
coronal_PhonemeFeatureText: str = "coronal"
dorsal_PhonemeFeatureText: str = "dorsal"
pharyngeal_PhonemeFeatureText: str = "pharyngeal"
laryngeal_PhonemeFeatureText: str = "laryngeal"
round_PhonemeFeatureText: str = "round"
anterior_PhonemeFeatureText: str = "anterior"
distributed_PhonemeFeatureText: str = "distributed"
strident_PhonemeFeatureText: str = "strident"
high_PhonemeFeatureText: str = "high"
low_PhonemeFeatureText: str = "low"
back_PhonemeFeatureText: str = "back"

showPhonemeInventoryText: str = "Show English Phoneme Inventory"
makeAPhonemeVoicedText: str = "make a phoneme voiced"
quitText: str = "Quit"
makeAPhonemeUnvoicedText: str = "make a phoneme unvoiced"
describePhonemeText: str = "Describe a phoneme"
getFeaturesOfPhonemeText: str = "Get sound patterns of English features of IPA transcription"
splitTranscriptionText: str = "split IPA transcription text"
