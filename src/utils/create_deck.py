from src.types.CardType import *
from src.types.CardValue import *


def create_deck(card_object):
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
            cards.append(card_object(suit, value))

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
        cards.append(card_object(Trump, value))

    return cards
