from __future__ import annotations
from typing import TYPE_CHECKING, List

from src.classes.Card import Card

if TYPE_CHECKING:
    from src.classes import Player
    from src.classes.Bid import Bid
    from src.classes.Card import Card
    from src.classes.Handful import Handful
    from src.classes.Turn import Turn


class Viewer:
    def prepare_to_new_game(self, players: List[Card]) -> None:
        pass

    def prepare_to_new_set(self, dealer: Player) -> None:
        pass

    def view_dog(self, dog_cards: List[Card]):
        pass

    def view_turn(self, turn: Turn):
        pass

    def view_bid(self, bid: Bid):
        pass

    def view_handful(self, handful: Handful):
        pass

    def set_ended(self, set_score, global_score):
        pass

    def game_ended(self, global_score):
        pass
