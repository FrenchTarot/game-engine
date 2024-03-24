from __future__ import annotations
from typing import TYPE_CHECKING

from src.classes.Factory import Factory


if TYPE_CHECKING:
    from src.classes.Player import Player


class Bid:
    can_take_dog = True
    dog_score_to_taker = True
    multiplicator = None
    player: Player = None

    def to_json(self):
        return {"type": self.__class__.__name__}


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


class BidFactory(Factory):
    available_classes = [Small, Push, Guard, GardWithout, GuardAgainst]
