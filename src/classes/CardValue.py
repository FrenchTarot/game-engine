from src.classes.Factory import Factory


class CardValue:
    rank = None
    is_oudler = False


class Jack(CardValue):
    rank = 11
    str = 11


class Knight(CardValue):
    rank = 12
    str = "C"


class Queen(CardValue):
    rank = 13
    str = "Q"


class King(CardValue):
    rank = 14
    str = "K"


class Fool(CardValue):
    rank = 0
    is_oudler = True
    str = "Fool"


class Ace(CardValue):
    rank = 1
    str = "1"


class One(CardValue):
    rank = 1
    is_oudler = True
    str = "1"


class Two(CardValue):
    rank = 2
    str = "2"


class Three(CardValue):
    rank = 3
    str = "3"


class Four(CardValue):
    rank = 4
    str = "4"


class Five(CardValue):
    rank = 5
    str = "5"


class Six(CardValue):
    rank = 6
    str = "6"


class Seven(CardValue):
    rank = 7
    str = "7"


class Eight(CardValue):
    rank = 8
    str = "8"


class Nine(CardValue):
    rank = 9
    str = "9"


class Ten(CardValue):
    rank = 10
    str = "10"


class Eleven(CardValue):
    rank = 11
    str = "11"


class Twelve(CardValue):
    rank = 12
    str = "12"


class Thirteen(CardValue):
    rank = 13
    str = "13"


class Fourteen(CardValue):
    rank = 14
    str = "14"


class Fifteen(CardValue):
    rank = 15
    str = "15"


class Sixteen(CardValue):
    rank = 16
    str = "16"


class Seventeen(CardValue):
    rank = 17
    str = "17"


class Eighteen(CardValue):
    rank = 18
    str = "18"


class Nineteen(CardValue):
    rank = 19
    str = "19"


class Twenty(CardValue):
    rank = 20
    str = "20"


class TwentyOne(CardValue):
    rank = 21
    is_oudler = True
    str = "21"


class CardValueFactory(Factory):
    available_classes = CardValue.__subclasses__()
