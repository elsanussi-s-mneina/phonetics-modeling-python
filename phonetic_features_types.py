from enum import unique, Enum, auto


@unique
class Polarity(Enum):
    """
     Represents the '+' (plus) or '-' (minus)
     of a binary feature. e.g. [+sonorant],
     [-sonorant]
    """
    PLUS = auto()
    MINUS = auto()


class PhonemeFeature:
    """
     According to Linguistics, phonemes can be
     analyzed as a set of features. One phoneme
     will have one set of features, and a different
     phoneme will have a different set of features.

     These features are well known in phonology, and
     are limited in number. There are two kinds of
     features, unary features, and binary features. The
     difference is obvious in how they are represented in
     the notation that linguists use. Unary features,
     are either present or absent. Binary features
     can be positive or negative. For example, Nasal
     is a unary feature. A phoneme is either nasal,
     or it isn't. i.e. [nasal] or not. For example,
     Voice is a binary feature, a phoneme can be
     [+voice] (can be pronounced: "plus voice")
     or [-voice] (can be pronounced: "minus voice").

     Because linguists represent phonemic features in these
     two different ways. We represent these as two
     different kinds of types.

     So [nasal] which is a unary feature would be
     represented by a value `NasalFeature` of type `PhonemeFeature`.
     And [+voice] which is a binary feature would
     be represented by a value `VoiceFeature Plus` of type
     `PhonemeFeature`.

     We represent the plus or minus symbol by
     the type Polarity.

     Notice that: Linguists write a set of features
     as a 2D matrix with one column, roughly like this:
     ⎡ +voice    ⎤
     ⎢ +sonorant ⎥
     ⎣  nasal    ⎦

    Note that certain sets of features cannot coexist,
    syntactically. For example a phoneme cannot be
    [+voice] and [-voice].

     Note that some analyses
    are language specific, so for some phonemes (not
    the usual case) whether it has feature X (say 'coronal')
    depends on the language (theoretical example: e.g. Swahili,
    vs French). This is not implemented here.
    """

    def __init__(self):
        pass


class SyllabicFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class ConsonantalFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class SonorantFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class ContinuantFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class VoiceFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class AdvancedTongueRootFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity


class NasalFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class LateralFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class DelayedReleaseFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class SpreadGlottisFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class ConstrictedGlottisFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class LabialFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class CoronalFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class DorsalFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class PharyngealFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class LaryngealFeature(PhonemeFeature):
    def __init__(self):
        super().__init__()


class RoundFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class AnteriorFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class DistributedFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class StridentFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class HighFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class LowFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)


class BackFeature(PhonemeFeature):
    def __init__(self, polarity: Polarity):
        super().__init__()
        self.polarity = polarity

    def __eq__(self, other):
        return self.polarity == other.polarity

    def __ne__(self, other):
        return not self.__eq__(other)