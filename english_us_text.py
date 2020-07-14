"""
A module for containing any user facing text in the
English language.
"""
from typing import Final

APPLICATION_TITLE: Final[str] = "Phonetics Modeling Program"

MENU: Final[str] = \
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

USER_INPUT_VIEW_ENGLISH_PHONEME_INVENTORY: Final[str] = "1"
USER_INPUT_MAKE_A_PHONEME_VOICED: Final[str] = "2"
USER_INPUT_MAKE_A_PHONEME_UNVOICED: Final[str] = "3"
USER_INPUT_DESCRIBE_A_PHONEME_IN_ENGLISH: Final[str] = "4"
USER_INPUT_DESCRIBE_A_PHONEME_IN_SPE: Final[str] = "5"
USER_INPUT_CHUNK_IPA_BY_PHONEME: Final[str] = "6"
USER_INPUT_OPEN_WINDOW: Final[str] = "7"

PROMPT: Final[str] = "(PROMPT:) "

SORRY_UNABLE_TO_CALCULATE: Final[str] = \
    "Sorry: Final[str] unable to calculate answer with that input."

TYPE_A_PHONEME: Final[str] = \
    """Type a phoneme using IPA symbols: Final[str] and then press the enter key:
     and the computer will display"""

PHONEME_TO_DEVOICE_MESSAGE: Final[str] = \
    """Type a phoneme using IPA symbols: Final[str] and then press the enter key:
     and the computer will display
     the devoiced counterpart (on the subsequent line):"""

PHONEME_TO_VOICE_MESSAGE: Final[str] = \
    """Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     the voiced counterpart (on the subsequent line):"""

PHONEME_TO_DESCRIBE_MESSAGE: Final[str] = \
    """
    Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     its English description (on the subsequent line):"""

PHONEME_TO_CALCULATE_SPE_MESSAGE: Final[str] = \
    """
    Type a phoneme using IPA symbols: and then press the enter key:
     and the computer will display
     its SPE features (on the subsequent line):"""

ipaTextToDivideMessage: Final[str] = \
    """
    Type text using IPA symbols: and then press the enter key:
     and the computer will display
     the text you entered with separate phonemes on separate lines:"""

PLEASE_READ_README_MESSAGE: Final[str] = \
    "Please read README.md file for instructions on how to use."
PROGRAM_TERMINATED_NORMALLY_MESSAGE: Final[str] = "Program terminated normally."
USER_SELECTED_MESSAGE: Final[str] = "The user selected:"
UNRECOGNIZED_SELECTION_MESSAGE: Final[str] = "Unrecognized selection. No action taken."
NO_ANALYSIS_FOUND_MESSAGE: Final[str] = "No analysis found!"

NO_ENGLISH_DESCRIPTION_FOUND_MESSAGE: Final[str] = "(no English description found.)"

CONSONANT_TEXT: Final[str] = "consonant"
VOWEL_TEXT: Final[str] = "vowel"

FRONT_BACKNESS_TEXT: Final[str] = "front"
CENTRAL_BACKNESS_TEXT: Final[str] = "central"
BACK_BACKNESS_TEXT: Final[str] = "back"

CLOSE_HEIGHT_TEXT: Final[str] = "close"
NEAR_CLOSE_HEIGHT_TEXT: Final[str] = "near-close"
CLOSE_MID_HEIGHT_TEXT: Final[str] = "close-mid"
MID_HEIGHT_TEXT: Final[str] = "mid"
OPEN_MID_HEIGHT_TEXT: Final[str] = "open-mid"
NEAR_OPEN_HEIGHT_TEXT: Final[str] = "near-open"
OPEN_HEIGHT_TEXT: Final[str] = "open"

ROUNDED_ROUNDING_TEXT: Final[str] = "rounded"
UNROUNDED_ROUNDING_TEXT: Final[str] = "unrounded"

BILABIAL_PLACE_TEXT: Final[str] = "bilabial"
LABIODENTAL_PLACE_TEXT: Final[str] = "labio-dental"
DENTAL_PLACE_TEXT: Final[str] = "dental"
ALVEOLAR_PLACE_TEXT: Final[str] = "alveolar"
POSTALVEOLAR_PLACE_TEXT: Final[str] = "post-alveolar"
RETROFLEX_PLACE_TEXT: Final[str] = "retroflex"
PALATAL_PLACE_TEXT: Final[str] = "palatal"
VELAR_PLACE_TEXT: Final[str] = "velar"
UVULAR_PLACE_TEXT: Final[str] = "uvular"
PHARYNGEAL_PLACE_TEXT: Final[str] = "pharyngeal"
GLOTTAL_PLACE_TEXT: Final[str] = "glottal"
EPIGLOTTAL_PLACE_TEXT: Final[str] = "epiglottal"
LABIALVELAR_PLACE_TEXT: Final[str] = "labial-velar"
LABIALPALATAL_PLACE_TEXT: Final[str] = "labial-palatal"
ALVEOLOPALATAL_PLACE_TEXT: Final[str] = "alveolo-palatal"
PALATOALVEOLAR_PLACE_TEXT: Final[str] = "palato-alveolar"

PLOSIVE_MANNER_TEXT: Final[str] = "plosive"
NASAL_MANNER_TEXT: Final[str] = "nasal"
TRILL_MANNER_TEXT: Final[str] = "trill"
TAP_OR_FLAP_MANNER_TEXT: Final[str] = "tap or flap"
APPROXIMANT_MANNER_TEXT: Final[str] = "approximant"
FRICATIVE_MANNER_TEXT: Final[str] = "fricative"
AFFRICATE_MANNER_TEXT: Final[str] = "affricate"
LATERAL_FRICATIVE_MANNER_TEXT: Final[str] = "lateral fricative"
LATERAL_APPROXIMANT_MANNER_TEXT: Final[str] = "lateral approximant"
LATERAL_FLAP_MANNER_TEXT: Final[str] = "lateral flap"
LATERAL_MANNER_TEXT: Final[str] = "lateral"

PULMONIC_EGRESSIVE_AIRSTREAM_TEXT: Final[str] = "pulmonic egressive"
CLICK_AIRSTREAM_TEXT: Final[str] = "click"
IMPLOSIVE_AIRSTREAM_TEXT: Final[str] = "implosive"

VOICED_VOCAL_FOLDS_TEXT: Final[str] = "voiced"
VOICELESS_VOCAL_FOLDS_TEXT: Final[str] = "voiceless"
VOICED_ASPIRATED_VOCAL_FOLDS_TEXT: Final[str] = "voiced aspirated"
VOICELESS_ASPIRATED_VOCAL_FOLDS_TEXT: Final[str] = "voiceless aspirated"
CREAKY_VOICED_VOCAL_FOLDS_TEXT: Final[str] = "creaky voiced"

SYLLABIC_PHONEME_FEATURE_TEXT: Final[str] = "syllabic"
CONSONANTAL_PHONEME_FEATURE_TEXT: Final[str] = "consonantal"
SONORANT_PHONEME_FEATURE_TEXT: Final[str] = "sonorant"
CONTINUANT_PHONEME_FEATURE_TEXT: Final[str] = "continuant"
VOICE_PHONEME_FEATURE_TEXT: Final[str] = "voice"
ATR_PHONEME_FEATURE_TEXT: Final[str] = "ATR"
NASAL_PHONEME_FEATURE_TEXT: Final[str] = "nasal"
LATERAL_PHONEME_FEATURE_TEXT: Final[str] = "lateral"
DELAYED_RELEASE_PHONEME_FEATURE_TEXT: Final[str] = "delayed release"
SPREAD_GLOTTIS_PHONEME_FEATURE_TEXT: Final[str] = "spread glottis"
CONSTRICTED_GLOTTIS_PHONEME_FEATURE_TEXT: Final[str] = "constricted glottis"
LABIAL_PHONEME_FEATURE_TEXT: Final[str] = "labial"
CORONAL_PHONEME_FEATURE_TEXT: Final[str] = "coronal"
DORSAL_PHONEME_FEATURE_TEXT: Final[str] = "dorsal"
PHARYNGEAL_PHONEME_FEATURE_TEXT: Final[str] = "pharyngeal"
LARYNGEAL_PHONEME_FEATURE_TEXT: Final[str] = "laryngeal"
ROUND_PHONEME_FEATURE_TEXT: Final[str] = "round"
ANTERIOR_PHONEME_FEATURE_TEXT: Final[str] = "anterior"
DISTRIBUTED_PHONEME_FEATURE_TEXT: Final[str] = "distributed"
STRIDENT_PHONEME_FEATURE_TEXT: Final[str] = "strident"
HIGH_PHONEME_FEATURE_TEXT: Final[str] = "high"
LOW_PHONEME_FEATURE_TEXT: Final[str] = "low"
BACK_PHONEME_FEATURE_TEXT: Final[str] = "back"

SHOW_PHONEME_INVENTORY_TEXT: Final[str] = "Show English Phoneme Inventory"
MAKE_A_PHONEME_VOICED_TEXT: Final[str] = "make a phoneme voiced"
QUIT_TEXT: Final[str] = "Quit"
MAKE_A_PHONEME_UNVOICED_TEXT: Final[str] = "make a phoneme unvoiced"
DESCRIBE_PHONEME_TEXT: Final[str] = "Describe a phoneme"
GET_FEATURES_OF_PHONEME_TEXT: Final[str] = \
    "Get sound patterns of English features of IPA transcription"
SPLIT_TRANSCRIPTION_TEXT: Final[str] = "split IPA transcription text"
