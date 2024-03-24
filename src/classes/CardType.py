from src.classes.Factory import Factory


class CardType:
    pass


class Trump(CardType):
    str = "Trump"


class Heart(CardType):
    str = "♥"


class Club(CardType):
    str = "♣"


class Diamond(CardType):
    str = "♦"


class Spade(CardType):
    str = "♠"


class CardTypeFactory(Factory):
    available_classes = CardType.__subclasses__()
