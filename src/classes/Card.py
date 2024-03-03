from src.types.CardType import CardType, Trump
from src.types.CardValue import *


class Card:
    def __init__(self, type_: CardType, value_: CardValue, player=None) -> None:
        if type(type_) == str:
            type_ = self._get_type_from_str(type_)
        if type(value_) == str:
            value_ = self._get_value_from_str(value_)
        self.type: CardType = type_
        self.value: CardValue = value_
        self.played = False
        self.owner = player

        self._check_card_validity()

    def __str__(self) -> str:
        return f"{self.value.__name__} {self.type.__name__}"

    def set_owner(self, player):
        self.owner = player

    def get_score(self) -> float:
        if self.type == Trump:
            if self.value in [Ace, TwentyOne, Fool]:
                return 4.5
            return 0.5

        if self.value == Jack:
            return 1.5
        if self.value == Knight:
            return 2.5
        if self.value == Queen:
            return 3.5
        if self.value == King:
            return 4.5

        return 0.5

    def is_face(self) -> bool:
        if self.type != Trump:
            return False
        return self.value in [Jack, Knight, Queen, King]

    def is_oudler(self) -> bool:
        if self.type != Trump:
            return False
        return self.value in [Ace, TwentyOne, Fool]

    def _check_card_validity(self) -> None:
        if not self.type:
            raise BaseException("Missing card type")
        if not self.value:
            raise BaseException("Missing card value")
        if CardType not in list(self.type.__bases__):
            raise BaseException("Invalid card type")
        if CardValue not in list(self.value.__bases__):
            raise BaseException("Invalid card value")

        if self.type == Trump:
            if self.value in [Jack, Knight, Queen, King]:
                raise BaseException(f"Invalid card value {self.value} for a trump")
        else:
            if self.value.rank > 10 and self.value not in [Jack, Knight, Queen, King]:
                raise BaseException(f"Invalid card value {self.value} for a suite")
            if self.value == Fool:
                raise BaseException(f"Invalid card value {self.value} for a suite")

    def _get_value_from_str(self, str: str) -> CardValue:
        available_values = CardValue.__subclasses__()
        filtered = [a for a in available_values if a.__name__ == str]
        if len(filtered):
            return filtered[0]
        raise BaseException(f"Unknown value for str {str}")

    def _get_type_from_str(self, str: str) -> CardType:
        available_values = CardType.__subclasses__()
        filtered = [a for a in available_values if a.__name__ == str]
        if len(filtered):
            return filtered[0]
        raise BaseException(f"Unknown type for str {str}")