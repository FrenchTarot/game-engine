from src.classes.Card import CardFactory
from src.classes.CardType import *
from src.classes.CardValue import *


def create_deck(card_factory: CardFactory):
    cards = []
    for suit in [Diamond, Spade, Heart, Club]:
        for value in [
            Ace,
            Two,
            Three,
            Four,
            Five,
            Six,
            Seven,
            Eight,
            Nine,
            Ten,
            Jack,
            Knight,
            Queen,
            King,
        ]:
            cards.append(card_factory.from_json({"type": suit, "value": value}))

    for value in [
        One,
        Two,
        Three,
        Four,
        Five,
        Six,
        Seven,
        Eight,
        Nine,
        Ten,
        Eleven,
        Twelve,
        Thirteen,
        Fourteen,
        Fifteen,
        Sixteen,
        Seventeen,
        Eighteen,
        Nineteen,
        Twenty,
        TwentyOne,
        Fool,
    ]:
        cards.append(card_factory.from_json({"type": Trump, "value": value}))

    return cards
