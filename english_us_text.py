menu : str
menu = \
  "What do you want to accomplish? \n\
  \ 1) view the English phoneme inventory (as IPA graphemes). \n\
  \ 2) make a phoneme voiced. \n\
  \ 3) make a phoneme unvoiced. \n\
  \ 4) describe a phoneme in English. \n\
  \ 5) describe a phoneme in SPE Features. \n\
  \ 6) divide IPA text into phonemes (chunk) \n\
  \  \n\
  \ Enter the number representing your selection below : str \n\
  \ after the prompt : str and press enter/return. \n\
  \ \n\
  \ \n\
  \ \n" 

userInput_viewEnglishPhonemeInventory : str
userInput_makeAPhonemeVoiced : str
userInput_makeAPhonemeUnvoiced : str
userInput_describeAPhonemeInEnglish : str
userInput_describeAPhonemeInSPE : str
userInput_chunkIPAByPhoneme : str
userInput_viewEnglishPhonemeInventory = "1"
userInput_makeAPhonemeVoiced = "2"
userInput_makeAPhonemeUnvoiced = "3"
userInput_describeAPhonemeInEnglish = "4"
userInput_describeAPhonemeInSPE = "5"
userInput_chunkIPAByPhoneme = "6"

prompt : str
prompt = "(PROMPT:) "



sorryUnableToCalculate : str
sorryUnableToCalculate = "Sorry : str unable to calculate answer with that input."

typeAPhoneme :  str
typeAPhoneme = \
  "Type a phoneme using IPA symbols : str and then press the enter key : str \
  \ and the computer will display"


phonemeToDevoiceMessage : str
phonemeToVoiceMessage : str
phonemeToDescribeMessage : str
phonemeToCalculateSPEMessage : str
pleaseReadReadmeMessage : str
programTerminatedNormallyMessage : str
userSelectedMessage : str
unrecognizedSelectionMessage : str
noAnalysisFoundMessage : str 
ipaTextToDivideMessage : str
phonemeToDevoiceMessage = \
  "Type a phoneme using IPA symbols : str and then press the enter key : str\
  \ and the computer will display\
  \ the devoiced counterpart (on the subsequent line):"

phonemeToVoiceMessage = \
  "Type a phoneme using IPA symbols : str and then press the enter key : str\
  \ and the computer will display\
  \ the voiced counterpart (on the subsequent line):"

phonemeToDescribeMessage = \
  "Type a phoneme using IPA symbols : str and then press the enter key : str\
  \ and the computer will display\
  \ its English description (on the subsequent line):"

phonemeToCalculateSPEMessage = \
  "Type a phoneme using IPA symbols : str and then press the enter key : str\
  \ and the computer will display\
  \ its SPE features (on the subsequent line):"

ipaTextToDivideMessage = \
  "Type text using IPA symbols : str and then press the enter key : str\
  \ and the computer will display\
  \ the text you entered with separate phonemes on separate lines:"

pleaseReadReadmeMessage = "Please read README.md file for instructions on how to use."
programTerminatedNormallyMessage = "Program terminated normally."
userSelectedMessage = "The user selected:"
unrecognizedSelectionMessage =  "Unrecognized selection. No action taken."
noAnalysisFoundMessage = "No analysis found!"



noEnglishDescriptionFound_message : str
noEnglishDescriptionFound_message = "(no English description found.)"


consonant_Text : str
vowel_Text : str
front_BacknessText : str
central_BacknessText : str
back_BacknessText : str
close_HeightText : str
nearClose_HeightText : str
closeMid_HeightText : str
mid_HeightText : str
openMid_HeightText : str
nearOpen_HeightText : str
open_HeightText : str
rounded_RoundingText : str
unrounded_RoundingText : str
bilabial_PlaceText : str
labioDental_PlaceText : str
dental_PlaceText : str
alveolar_PlaceText : str
postAlveolar_PlaceText : str
retroflex_PlaceText : str
palatal_PlaceText : str
velar_PlaceText : str
uvular_PlaceText : str
pharyngeal_PlaceText : str
glottal_PlaceText : str
epiglottal_PlaceText : str
labialVelar_PlaceText : str
labialPalatal_PlaceText : str
alveoloPalatal_PlaceText : str
palatoAlveolar_PlaceText : str
plosive_MannerText : str
nasal_MannerText : str
trill_MannerText : str
tapOrFlap_MannerText : str
approximant_MannerText : str
fricative_MannerText : str
affricate_MannerText : str
lateralFricative_MannerText : str
lateralApproximant_MannerText : str
lateralFlap_MannerText : str
lateral_MannerText : str
pulmonicEgressive_AirstreamText : str
click_AirstreamText : str
implosive_AirstreamText : str
voiced_VocalFoldsText : str
voiceless_VocalFoldsText : str
voicedAspirated_VocalFoldsText : str
voicelessAspirated_VocalFoldsText : str
creakyVoiced_VocalFoldsText : str
syllabic_PhonemeFeatureText : str
consonantal_PhonemeFeatureText : str
sonorant_PhonemeFeatureText : str
continuant_PhonemeFeatureText : str
voice_PhonemeFeatureText : str
atr_PhonemeFeatureText : str
nasal_PhonemeFeatureText : str
lateral_PhonemeFeatureText : str
delayedRelease_PhonemeFeatureText : str
spreadGlottis_PhonemeFeatureText : str
constrictedGlottis_PhonemeFeatureText : str
labial_PhonemeFeatureText : str
coronal_PhonemeFeatureText : str
dorsal_PhonemeFeatureText : str
pharyngeal_PhonemeFeatureText : str
laryngeal_PhonemeFeatureText : str
round_PhonemeFeatureText : str
anterior_PhonemeFeatureText : str
distributed_PhonemeFeatureText : str
strident_PhonemeFeatureText : str
high_PhonemeFeatureText : str
low_PhonemeFeatureText : str
back_PhonemeFeatureText : str




consonant_Text                = "consonant"
vowel_Text                    = "vowel"

front_BacknessText            = "front"  
central_BacknessText          = "central"
back_BacknessText             = "back"   


close_HeightText              = "close"     
nearClose_HeightText          = "near-close"
closeMid_HeightText           = "close-mid" 
mid_HeightText                = "mid"       
openMid_HeightText            = "open-mid"  
nearOpen_HeightText           = "near-open" 
open_HeightText               = "open"      



rounded_RoundingText          = "rounded"
unrounded_RoundingText        = "unrounded"


bilabial_PlaceText            = "bilabial"
labioDental_PlaceText         = "labio-dental"
dental_PlaceText              = "dental"
alveolar_PlaceText            = "alveolar"
postAlveolar_PlaceText        = "post-alveolar"
retroflex_PlaceText           = "retroflex"
palatal_PlaceText             = "palatal"
velar_PlaceText               = "velar"
uvular_PlaceText              = "uvular"
pharyngeal_PlaceText          = "pharyngeal"
glottal_PlaceText             = "glottal"
epiglottal_PlaceText          = "epiglottal"
labialVelar_PlaceText         = "labial-velar"
labialPalatal_PlaceText       = "labial-palatal"
alveoloPalatal_PlaceText      = "alveolo-palatal"
palatoAlveolar_PlaceText      = "palato-alveolar"


plosive_MannerText            = "plosive"
nasal_MannerText              = "nasal"
trill_MannerText              = "trill"
tapOrFlap_MannerText          = "tap or flap"
approximant_MannerText        = "approximant"
fricative_MannerText          = "fricative"
affricate_MannerText          = "affricate"
lateralFricative_MannerText   = "lateral fricative"
lateralApproximant_MannerText = "lateral approximant"
lateralFlap_MannerText        = "lateral flap"
lateral_MannerText            = "lateral"



pulmonicEgressive_AirstreamText       = "pulmonic egressive"
click_AirstreamText                   = "click"
implosive_AirstreamText               = "implosive"


voiced_VocalFoldsText                 = "voiced"
voiceless_VocalFoldsText              = "voiceless"
voicedAspirated_VocalFoldsText        = "voiced aspirated"
voicelessAspirated_VocalFoldsText     = "voiceless aspirated"
creakyVoiced_VocalFoldsText           = "creaky voiced"


syllabic_PhonemeFeatureText           = "syllabic"
consonantal_PhonemeFeatureText        = "consonantal"
sonorant_PhonemeFeatureText           = "sonorant"
continuant_PhonemeFeatureText         = "continuant"
voice_PhonemeFeatureText              = "voice"
atr_PhonemeFeatureText                = "ATR"
nasal_PhonemeFeatureText              = "nasal"
lateral_PhonemeFeatureText            = "lateral"
delayedRelease_PhonemeFeatureText     = "delayed release"
spreadGlottis_PhonemeFeatureText      = "spread glottis"
constrictedGlottis_PhonemeFeatureText = "constricted glottis"
labial_PhonemeFeatureText             = "labial"
coronal_PhonemeFeatureText            = "coronal"
dorsal_PhonemeFeatureText             = "dorsal"
pharyngeal_PhonemeFeatureText         = "pharyngeal"
laryngeal_PhonemeFeatureText          = "laryngeal"
round_PhonemeFeatureText              = "round"
anterior_PhonemeFeatureText           = "anterior"
distributed_PhonemeFeatureText        = "distributed"
strident_PhonemeFeatureText           = "strident"
high_PhonemeFeatureText               = "high"
low_PhonemeFeatureText                = "low"
back_PhonemeFeatureText               = "back"
