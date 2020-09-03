from functools import partial
from typing import Optional, List, Iterator, Callable, Tuple

from lib_type_helpers import is_consonant, is_vowel

from english_us_text import (
    SYLLABIC_PHONEME_FEATURE_TEXT,
    CONSONANTAL_PHONEME_FEATURE_TEXT,
    SONORANT_PHONEME_FEATURE_TEXT,
    CONTINUANT_PHONEME_FEATURE_TEXT,
    VOICE_PHONEME_FEATURE_TEXT,
    ATR_PHONEME_FEATURE_TEXT,
    NASAL_PHONEME_FEATURE_TEXT,
    LATERAL_PHONEME_FEATURE_TEXT,
    DELAYED_RELEASE_PHONEME_FEATURE_TEXT,
    SPREAD_GLOTTIS_PHONEME_FEATURE_TEXT,
    CONSTRICTED_GLOTTIS_PHONEME_FEATURE_TEXT,
    LABIAL_PHONEME_FEATURE_TEXT,
    CORONAL_PHONEME_FEATURE_TEXT,
    DORSAL_PHONEME_FEATURE_TEXT,
    PHARYNGEAL_PHONEME_FEATURE_TEXT,
    LARYNGEAL_PHONEME_FEATURE_TEXT,
    ROUND_PHONEME_FEATURE_TEXT,
    ANTERIOR_PHONEME_FEATURE_TEXT,
    DISTRIBUTED_PHONEME_FEATURE_TEXT,
    STRIDENT_PHONEME_FEATURE_TEXT,
    HIGH_PHONEME_FEATURE_TEXT,
    LOW_PHONEME_FEATURE_TEXT,
    BACK_PHONEME_FEATURE_TEXT,
)
from lib_functions import is_glide
from lib_types import (
    Phonet,
    Vowel,
    Consonant,
    Manner,
    Place,
    VocalFolds,
    Airstream,
    Height,
    Backness,
    Rounding,
)
from phonetic_features_types import (
    Polarity,
    PhonemeFeature,
    SyllabicFeature,
    ConsonantalFeature,
    SonorantFeature,
    ContinuantFeature,
    VoiceFeature,
    AdvancedTongueRootFeature,
    NasalFeature,
    LateralFeature,
    DelayedReleaseFeature,
    SpreadGlottisFeature,
    ConstrictedGlottisFeature,
    LabialFeature,
    CoronalFeature,
    DorsalFeature,
    PharyngealFeature,
    LaryngealFeature,
    RoundFeature,
    AnteriorFeature,
    DistributedFeature,
    StridentFeature,
    HighFeature,
    LowFeature,
    BackFeature,
)


def show_polarity(polarity: Polarity) -> str:
    """
    Text representation of the polarity of a sound
    patterns of English feature.
    e.g. +, or -
    """
    if polarity == Polarity.PLUS:
        return "+"
    if polarity == Polarity.MINUS:
        return "-"
    return "[Unrecognized polarity!]"


def show_phoneme_feature(feature: PhonemeFeature) -> str:
    """
    Provide a text representation of the Sound Patterns of English
    feature. For example: [+ voice]
    or [-voice]
    or [delayed release]
    """
    if isinstance(feature, SyllabicFeature):
        return show_polarity(feature.polarity) + SYLLABIC_PHONEME_FEATURE_TEXT
    if isinstance(feature, ConsonantalFeature):
        return show_polarity(feature.polarity) + CONSONANTAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, SonorantFeature):
        return show_polarity(feature.polarity) + SONORANT_PHONEME_FEATURE_TEXT
    if isinstance(feature, ContinuantFeature):
        return show_polarity(feature.polarity) + CONTINUANT_PHONEME_FEATURE_TEXT
    if isinstance(feature, VoiceFeature):
        return show_polarity(feature.polarity) + VOICE_PHONEME_FEATURE_TEXT
    if isinstance(feature, AdvancedTongueRootFeature):
        return show_polarity(feature.polarity) + ATR_PHONEME_FEATURE_TEXT
    if isinstance(feature, NasalFeature):
        return NASAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, LateralFeature):
        return LATERAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, DelayedReleaseFeature):
        return DELAYED_RELEASE_PHONEME_FEATURE_TEXT
    if isinstance(feature, SpreadGlottisFeature):
        return SPREAD_GLOTTIS_PHONEME_FEATURE_TEXT
    if isinstance(feature, ConstrictedGlottisFeature):
        return CONSTRICTED_GLOTTIS_PHONEME_FEATURE_TEXT
    if isinstance(feature, LabialFeature):
        return LABIAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, CoronalFeature):
        return CORONAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, DorsalFeature):
        return DORSAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, PharyngealFeature):
        return PHARYNGEAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, LaryngealFeature):
        return LARYNGEAL_PHONEME_FEATURE_TEXT
    if isinstance(feature, RoundFeature):
        return show_polarity(feature.polarity) + ROUND_PHONEME_FEATURE_TEXT
    if isinstance(feature, AnteriorFeature):
        return show_polarity(feature.polarity) + ANTERIOR_PHONEME_FEATURE_TEXT
    if isinstance(feature, DistributedFeature):
        return show_polarity(feature.polarity) + DISTRIBUTED_PHONEME_FEATURE_TEXT
    if isinstance(feature, StridentFeature):
        return show_polarity(feature.polarity) + STRIDENT_PHONEME_FEATURE_TEXT
    if isinstance(feature, HighFeature):
        return show_polarity(feature.polarity) + HIGH_PHONEME_FEATURE_TEXT
    if isinstance(feature, LowFeature):
        return show_polarity(feature.polarity) + LOW_PHONEME_FEATURE_TEXT
    if isinstance(feature, BackFeature):
        return show_polarity(feature.polarity) + BACK_PHONEME_FEATURE_TEXT
    return "[Unrecognized phoneme feature!]"


def consonantal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Vowels are [-consonantal].
    Glides are [-consonantal].
    Consonants (that are not glides) are [+consonantal].

    (Source: page 258)
    """
    if is_vowel(phone):
        return ConsonantalFeature(Polarity.MINUS)
    if is_consonant(phone):
        if is_glide(phone):
            return ConsonantalFeature(Polarity.MINUS)
        return ConsonantalFeature(Polarity.PLUS)
    return None


def sonorant(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Oral stops are [-sonorant].
    Affricates are [-sonorant].
    Fricatives are [-sonorant].
    Nasals are [+sonorant].
    Approximants are [+sonorant].
    Laterals are [+sonorant].
    Vowels are [+sonorant].
    Glides are [+sonorant].

    (Source: page 258)
    """
    if is_consonant(phone):
        if phone.manner in [Manner.PLOSIVE, Manner.AFFRICATE, Manner.FRICATIVE]:
            return SonorantFeature(Polarity.MINUS)
        if phone.manner in [Manner.NASAL, Manner.APPROXIMANT, Manner.LATERAL]:
            return SonorantFeature(Polarity.PLUS)
        if is_glide(phone):
            return SonorantFeature(Polarity.PLUS)
        return SonorantFeature(Polarity.MINUS)
    if is_vowel(phone):
        return SonorantFeature(Polarity.PLUS)
    return None


def continuant(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Oral stops are [-continuant].
    Nasals stops are [-continuant].
    Affricates are [-continuant].
    Fricatives are [+continuant].
    Approximants are [+continuant].
    Vowels are [+continuant].
    Glides are [+continuant].

    (Source: page 258)

      Aside: we do not define lateral approximants for [+/-continuant] because the
      textbook puts it in parentheses. Usually this means, it depends on
      the language under study or
      it depends on the linguist.
      Lateral approximants may be considered [+continuant]. (arguable)
      (see chart on page 259))
    """
    if is_consonant(phone) and phone.manner in [
        Manner.PLOSIVE,
        Manner.NASAL,
        Manner.AFFRICATE,
    ]:
        return ContinuantFeature(Polarity.MINUS)
    if is_consonant(phone) and phone.manner == Manner.APPROXIMANT:
        return ContinuantFeature(Polarity.PLUS)
    if is_vowel(phone):
        return ContinuantFeature(Polarity.PLUS)
    if is_consonant(phone) and is_glide(phone):
        return ContinuantFeature(Polarity.PLUS)
    return None


def nasal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Nasal consonants are [nasal].
    # to do: add support for nasal vowels.
    All other segments are not defined for [nasal].
    """
    if is_consonant(phone) and phone.manner == Manner.NASAL:
        return NasalFeature()
    return None


def lateral(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Lateral consonants are [lateral].
    Lateral approximant consonants are [lateral].
    Lateral fricative consonants are [lateral].
    Lateral flap consonants are [lateral].
    All other segments are not defined for [lateral].
    """
    if is_consonant(phone):
        if phone.manner in [
            Manner.LATERAL,
            Manner.LATERAL_APPROXIMANT,
            Manner.LATERAL_FRICATIVE,
            Manner.LATERAL_FLAP,
        ]:
            return LateralFeature()
    return None


def delayed_release(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Affricates are [+delayed release].
    All other segments are [-delayed release].

    (Source: page 260)
    """
    if is_consonant(phone) and phone.manner == Manner.AFFRICATE:
        return DelayedReleaseFeature()
    return None


def labial(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Bilabial consonants are [labial].
    Labio-dental consonants are [labial].
    All other segments are undefined for [labial].

    (Source: page 264)
    """
    if is_consonant(phone):
        if phone.place == Place.BILABIAL or phone.place == Place.LABIODENTAL:
            return LabialFeature()
    return None


def coronal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Dentals are [coronal].
    Alveolars are [coronal] also.
    Alveolopalatals are [coronal] also.
    Retroflexes are [coronal] also.
    Palatals are [coronal] also.

    Post-alveolars are [coronal] also.

    All other sounds are undefined for [coronal].

    (Source: page 264)
    (The fact that Post-alveolar consonants are coronal is indicated by
     Table 12. on page 265.)
    """
    if is_consonant(phone) and phone.place in [
        Place.DENTAL,
        Place.ALVEOLAR,
        Place.ALVEOLOPALATAL,
        Place.RETROFLEX,
        Place.PALATAL,
        Place.POSTALVEOLAR,
    ]:
        return CoronalFeature()
    return None


def dorsal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Palatals are [dorsal].

      Aside: alveolo-palatals do not seem to be dorsals,
      although the table 12.4 is confusing
      because it uses the IPA symbol for one.
      TODO: find more information on whether
      alveolo-palatals are [dorsal].

    Velars are [dorsal].
    Uvulars are [dorsal].
    All other segments are undefined for [dorsal].
    """
    if is_consonant(phone) and phone.place in [
        Place.PALATAL,
        Place.VELAR,
        Place.UVULAR,
    ]:
        return DorsalFeature()
    return None


def pharyngeal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Pharyngeal fricatives are [pharyngeal].
    All other segments are undefined for [pharyngeal].

    (Source: page 264)
    """
    if (
        is_consonant(phone)
        and phone.place == Place.PHARYNGEAL
        and phone.manner == Manner.FRICATIVE
    ):
        return PharyngealFeature()
    return None


def laryngeal(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Glottal consonants are [laryngeal].
    All other segments are undefined for [laryngeal].

    (Source: page 265)
    """
    if is_consonant(phone) and phone.place == Place.GLOTTAL:
        return LaryngealFeature()
    return None


def voice(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Voiced Aspirated consonants are [+voice].
    Voiced consonants are [+voice].
    Voiced vowels are [+voice].
    All other segments are [-voice].
    """
    if is_consonant(phone):
        if (
            phone.vocal_folds == VocalFolds.VOICELESS
            and phone.place == Place.GLOTTAL
            and phone.manner == Manner.PLOSIVE
            and phone.airstream == Airstream.PULMONIC_EGRESSIVE
        ):
            return VoiceFeature(
                Polarity.MINUS
            )  # The voiceless glottal plosive is [-voice]
        if phone.vocal_folds == VocalFolds.VOICED_ASPIRATED:
            return VoiceFeature(Polarity.PLUS)
        if phone.vocal_folds == VocalFolds.VOICED:
            return VoiceFeature(Polarity.PLUS)
        return VoiceFeature(Polarity.MINUS)
    if is_vowel(phone) and phone.vocal_folds == VocalFolds.VOICED:
        return VoiceFeature(Polarity.PLUS)
    return VoiceFeature(Polarity.MINUS)


def spread_glottis(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Voiceless aspirated plosives are [spread glottis].
    Voiced aspirated plosives are [spread glottis].
    All other segments are not defined for [spread glottis].
    (Source: page 262)
    """
    if (
        is_consonant(phone)
        and phone.vocal_folds
        in [VocalFolds.VOICELESS_ASPIRATED, VocalFolds.VOICED_ASPIRATED]
        and phone.manner == Manner.PLOSIVE
    ):
        return SpreadGlottisFeature()
    return None


def constricted_glottis(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Ejectives have the feature [constricted glottis].
    Glottal stop have the feature [constricted glottis].
    Creaky voiced sonorants have the feature [constricted glottis].

    (Source: page 262)
    """
    if (
        is_consonant(phone)
        and phone.place == Place.GLOTTAL
        and phone.manner == Manner.PLOSIVE
    ):
        return ConstrictedGlottisFeature()
    if is_consonant(phone) and phone.vocal_folds == VocalFolds.CREAKY_VOICED:
        if sonorant(phone) == SonorantFeature(Polarity.PLUS):
            return ConstrictedGlottisFeature()
        return None
    if is_vowel(phone) and phone.vocal_folds == VocalFolds.CREAKY_VOICED:
        if sonorant(phone) == SonorantFeature(Polarity.PLUS):
            return ConstrictedGlottisFeature()
        return None
    return None


def anterior(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Dentals are [+anterior].
    Alveolars are [+anterior].
    Post-alveolars are [-anterior].
    Retroflexes are [-anterior].
    Palatals are [-anterior].

    (Source: page 265)

    TODO: answer the question:
    Question: Are Alveolo-palatals [+anterior], or [-anterior]?
    Alveolo-palatals are [-anterior].
    (SOURCE: not found)
    """
    if is_consonant(phone) and phone.place in [Place.DENTAL, Place.ALVEOLAR]:
        return AnteriorFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place in [
        Place.POSTALVEOLAR,
        Place.RETROFLEX,
        Place.PALATAL,
        Place.ALVEOLOPALATAL,
    ]:
        return AnteriorFeature(Polarity.MINUS)
    return None


def distributed(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Given a phonete, returns the relevant distributed Sound Patterns of
    English Phoneme feature.

    Returns either [+ distributed], [- distributed] or nothing.
    """
    if is_consonant(phone) and phone.place == Place.DENTAL:
        return DistributedFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.ALVEOLAR:
        return DistributedFeature(Polarity.MINUS)
    if is_consonant(phone) and phone.place == Place.POSTALVEOLAR:
        return DistributedFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.RETROFLEX:
        return DistributedFeature(Polarity.MINUS)
    if is_consonant(phone) and phone.place == Place.PALATAL:
        return DistributedFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.ALVEOLOPALATAL:
        return DistributedFeature(Polarity.PLUS)
    return None


def strident(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Alveolar fricatives are [+strident].
    Alveolar affricates are [+strident], also.
    Post-alveolar fricatives are [+strident], also.
    Post-alveolar affricates are [+strident], also.
    Labio-dental fricatives are [+strident] , also.
    Labio-dental affricates are [+strident] , also.
    Uvular fricatives are [+strident], also.
    Uvular affricates are [+strident], also.

    All other fricatives are [-strident].
    All other affricates are [-strident], also.

    All other segments are undefined for [+/-strident].

    (Source: page 266, under [+/-strident] heading, under the subsection
    "Natural classes".)
    """
    if (
        is_consonant(phone)
        and phone.place == Place.ALVEOLAR
        and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]
    ):
        return StridentFeature(Polarity.PLUS)
    if (
        is_consonant(phone)
        and phone.place == Place.POSTALVEOLAR
        and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]
    ):
        return StridentFeature(Polarity.PLUS)
    if (
        is_consonant(phone)
        and phone.place == Place.LABIODENTAL
        and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]
    ):
        return StridentFeature(Polarity.PLUS)
    if (
        is_consonant(phone)
        and phone.place == Place.UVULAR
        and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]
    ):
        return StridentFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.manner in [Manner.FRICATIVE, Manner.AFFRICATE]:
        return StridentFeature(Polarity.MINUS)
    return None


def high(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Palatal consonants are [+high].
    Alveolo-palatal consonants are [+high].
    Velar consonants are [+high].

    Uvular consonants are [-high].
    All other consonants are undefined for [+/-high].
    Close vowels are [+high].
    Near-close vowels are [+high].
    All other vowels are [-high].
    """
    if is_consonant(phone) and phone.place == Place.PALATAL:
        return HighFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.ALVEOLOPALATAL:
        return HighFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.VELAR:
        return HighFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.UVULAR:
        return HighFeature(Polarity.MINUS)
    if is_consonant(phone):
        return None
    if is_vowel(phone) and phone.height == Height.CLOSE:
        return HighFeature(Polarity.PLUS)
    if is_vowel(phone) and phone.height == Height.NEAR_CLOSE:
        return HighFeature(Polarity.PLUS)
    if is_vowel(phone):
        return HighFeature(Polarity.MINUS)
    return None


def low(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Uvular consonants are [+low].
    Pharyngeal consonants are [+low].
    Glottal consonants are [+low].
    All other consonants are undefined for [+/-low].
    Open vowels are [+low].
    Near open vowels are [+low].
    All other vowels are [-low].
    """
    if is_consonant(phone) and phone.place == Place.UVULAR:
        return LowFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.PHARYNGEAL:
        return LowFeature(Polarity.PLUS)
    if is_consonant(phone) and phone.place == Place.GLOTTAL:
        return LowFeature(Polarity.PLUS)
    if is_consonant(phone):
        return None
    if is_vowel(phone) and phone.height == Height.OPEN:
        return LowFeature(Polarity.PLUS)
    if is_vowel(phone) and phone.height == Height.NEAR_OPEN:
        return LowFeature(Polarity.PLUS)
    if is_vowel(phone):
        return LowFeature(Polarity.MINUS)
    return None


def back(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Back vowels are [+back].
    Central vowels are [+back].
    Front vowels are [-back].
    All other segments are undefined for [+/-back].
    """
    if is_vowel(phone) and phone.backness == Backness.BACK:
        return BackFeature(Polarity.PLUS)
    if is_vowel(phone) and phone.backness == Backness.CENTRAL:
        return BackFeature(Polarity.PLUS)
    if is_vowel(phone) and phone.backness == Backness.FRONT:
        return BackFeature(Polarity.MINUS)
    return None


def lip_round(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Rounded vowels are [+round].
    All other vowels are [-round].
    All other segments are [-round].
    """
    if is_vowel(phone) and phone.rounding == Rounding.ROUNDED:
        return RoundFeature(Polarity.PLUS)
    if is_vowel(phone):
        return RoundFeature(Polarity.MINUS)
    return RoundFeature(Polarity.MINUS)


def atr(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Advanced tongue root
    """
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE_MID
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE
        and phone.backness == Backness.BACK
        and phone.rounding == Rounding.ROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE_MID
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.ROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE_MID
        and phone.backness == Backness.BACK
        and phone.rounding == Rounding.ROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.ROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.PLUS)
    if (
        is_vowel(phone)
        and phone.height == Height.NEAR_OPEN
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.OPEN
        and phone.backness == Backness.BACK
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.CLOSE
        and phone.backness == Backness.CENTRAL
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.OPEN_MID
        and phone.backness == Backness.BACK
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.NEAR_CLOSE
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.NEAR_CLOSE
        and phone.backness == Backness.BACK
        and phone.rounding == Rounding.ROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.OPEN_MID
        and phone.backness == Backness.FRONT
        and phone.rounding == Rounding.UNROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    if (
        is_vowel(phone)
        and phone.height == Height.OPEN_MID
        and phone.backness == Backness.BACK
        and phone.rounding == Rounding.ROUNDED
        and phone.vocal_folds == VocalFolds.VOICED
    ):
        return AdvancedTongueRootFeature(Polarity.MINUS)
    return None


def feature_matrix(phonete: Phonet) -> List[Optional[PhonemeFeature]]:
    """
    Given a phoneme (representation)
    Gives a feature matrix.

    Note: to non-linguists, feature matrices
    are 1-dimensional, always displayed
    as a single column.

    For example:
    /phone/
    """
    return [
        consonantal(phonete),
        syllabic(phonete),
        continuant(phonete),
        sonorant(phonete),
        delayed_release(phonete),
        anterior(phonete),
        distributed(phonete),
        strident(phonete),
        high(phonete),
        low(phonete),
        nasal(phonete),
        lateral(phonete),
        labial(phonete),
        coronal(phonete),
        dorsal(phonete),
        pharyngeal(phonete),
        laryngeal(phonete),
        back(phonete),
        lip_round(phonete),
        voice(phonete),
        atr(phonete),
        spread_glottis(phonete),
        constricted_glottis(phonete),
    ]


def analyze_features(phonete: Phonet) -> List[PhonemeFeature]:
    """
    A function that takes data representing
    how a phoneme is pronounced, and returns
    a list of phonemic features.
    """
    return list(filter(lambda x: x is not None, feature_matrix(phonete)))


def show_features(features: List[PhonemeFeature]) -> str:
    """
    Given a list of Sound Patterns of English phoneme features,
    print the phoneme features in their usual representation.
    e.g. [+ someFeature, - someOtherFeature, ...]
    """
    features_strings: Iterator[str] = map(show_phoneme_feature, features)
    return "[" + "; ".join(features_strings) + "]"


def relevant_binary(
    feature: Callable[[Polarity], PhonemeFeature], other_feature: PhonemeFeature
) -> bool:
    """
    Given a binary feature, and another feature.
    returns whether they are the same kind of feature.
    They don't have to be the same polarity.
    For example, [+voice] and [−voice] are mutually relevant features.
      As are [+sonorant] and [+sonorant].
      But [+sonorant] and [+voice] are not relevant because
    "voice" and "sonorant" are different.
    """
    return other_feature == feature(Polarity.PLUS) or other_feature == feature(
        Polarity.MINUS
    )


def binary_difference(
    feature: Callable[[Polarity], PhonemeFeature],
    list1: List[PhonemeFeature],
    list2: List[PhonemeFeature],
) -> Tuple[Optional[PhonemeFeature], Optional[PhonemeFeature]]:
    """
    Finds the difference between two lists of phoneme features with respect
    to a single Sound Patterns of English binary feature (e.g. +/-voice).
    """
    relevant_list_1 = list(filter(partial(relevant_binary, feature), list1))
    relevant_list_2 = list(filter(partial(relevant_binary, feature), list2))
    if relevant_list_1 == relevant_list_2:
        return None, None

    first_part = relevant_list_1[0] if len(relevant_list_1) > 0 else None
    second_part = relevant_list_2[0] if len(relevant_list_2) > 0 else None
    return first_part, second_part


def unary_difference(
    feature: PhonemeFeature, list1: List[PhonemeFeature], list2: List[PhonemeFeature]
) -> Tuple[Optional[PhonemeFeature], Optional[PhonemeFeature]]:
    """
    Finds the difference between two lists of phoneme features with respect
    to a single Sound Patterns of English unary feature (e.g. nasal).
    A unary feature is one that lacks polarity, that is it does not have +, or -.
    It is either present or is not present.
    """
    if (feature in list1) == (feature in list2):
        return None, None
    if feature in list1 and (feature not in list2):
        return feature, None
    return None, feature


def difference(
    list1: List[PhonemeFeature], list2: List[PhonemeFeature]
) -> List[Tuple[Optional[PhonemeFeature], Optional[PhonemeFeature]]]:
    """
    This function takes two lists of phoneme features
    and returns how they differ. Any phonemic
    feature present in one list, and absent in the other
    will be represented; and any phonemic
    feature that is positive in one list but absent
    in the other will be represented.
    """
    return [
        binary_difference(SyllabicFeature, list1, list2),
        binary_difference(ConsonantalFeature, list1, list2),
        binary_difference(SonorantFeature, list1, list2),
        binary_difference(ContinuantFeature, list1, list2),
        binary_difference(VoiceFeature, list1, list2),
        binary_difference(AdvancedTongueRootFeature, list1, list2),
        unary_difference(NasalFeature(), list1, list2),
        unary_difference(LateralFeature(), list1, list2),
        unary_difference(DelayedReleaseFeature(), list1, list2),
        unary_difference(SpreadGlottisFeature(), list1, list2),
        unary_difference(ConstrictedGlottisFeature(), list1, list2),
        unary_difference(LabialFeature(), list1, list2),
        unary_difference(CoronalFeature(), list1, list2),
        unary_difference(DorsalFeature(), list1, list2),
        unary_difference(PharyngealFeature(), list1, list2),
        unary_difference(LaryngealFeature(), list1, list2),
        binary_difference(RoundFeature, list1, list2),
        binary_difference(AnteriorFeature, list1, list2),
        binary_difference(DistributedFeature, list1, list2),
        binary_difference(StridentFeature, list1, list2),
        binary_difference(HighFeature, list1, list2),
        binary_difference(LowFeature, list1, list2),
        binary_difference(BackFeature, list1, list2),
    ]


def syllabic(phone: Phonet) -> Optional[PhonemeFeature]:
    """
    Vowels are [+syllabic]
    Consonants (glides included) are [-syllabic].

    (Source: page 258)
    """
    if is_vowel(phone):
        return SyllabicFeature(Polarity.PLUS)
    if is_consonant(phone):
        return SyllabicFeature(Polarity.MINUS)
    return None


def to_text_features(phonete: Phonet) -> str:
    """
    Given a phonete, gets all the Sound Patterns of English
    features for the phonete. Then it
    provides the user readable representation of the phoneme.

    For example when given the phonete represented by /b/,
    it will return something like [+ someFeature, - someOtherFeature, ...]
    """
    features = analyze_features(phonete)
    return show_features(features)
