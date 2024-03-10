from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.classes.Player import Player


class Bid:
    can_take_dog = True
    dog_score_to_taker = True
    multiplicator = None
    player: Player = None

    def __init__(self) -> None:
        pass

    def get_bid_from_str(self, bid):
        available_values = Bid.__subclasses__()
        filtered = [a for a in available_values if a.__name__ == bid]
        if len(filtered):
            return filtered[0]
        raise BaseException(f"Unknown type for str {bid}")


class Small(Bid):
    multiplicator = 1
    rank = 1


class Push(Bid):
    multiplicator = 1.5
    rank = 2


class Guard(Bid):
    multiplicator = 2
    rank = 3


class GardWithout(Bid):
    multiplicator = 4
    can_take_dog = False
    rank = 4


class GuardAgainst(Bid):
    multiplicator = 6
    can_take_dog = False
    dog_score_to_taker = False
    rank = 5
