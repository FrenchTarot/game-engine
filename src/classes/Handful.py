from __future__ import annotations
from typing import TYPE_CHECKING, List
from src.classes.CardType import Trump
from src.classes.CardValue import Fool

if TYPE_CHECKING:
    from src.classes.Player import Player
    from src.classes.Card import Card


class Handful:
    name: str = None
    bonus: int = 0
    shown_cards: List[Card] = []
    needed_cards: int
    player: Player = None

    def __init__(self, shown_cards: List[Card]) -> None:
        self.shown_cards = shown_cards

        self.check_handful()

    def set_player(self, player: Player):
        self.player = player

    def check_handful(self):
        number_of_trumps = len(
            [card for card in self.shown_cards if card.type == Trump]
        )
        if number_of_trumps < self.needed_cards:
            raise BaseException(
                f"The player must show {self.needed_cards} trumps, not {number_of_trumps}"
            )

        player_trump_ranks = [
            card.value.rank
            for card in self.player.cards
            if card.type == Trump and card.value != Fool
        ]
        shown_cards_ranks = [
            card.value.rank
            for card in self.player.cards
            if card.type == Trump and card.value != Fool
        ]

        if max(player_trump_ranks) != max(shown_cards_ranks) or min(
            player_trump_ranks
        ) != min(shown_cards_ranks):
            raise BaseException(
                f"The player must show the minimum and maximum of his trumps"
            )

        for card in self.shown_cards:
            if card not in self.player.card:
                raise BaseException("The player must own the shown cards")

        fool_in_shown_cards = len(
            [card for card in self.shown_cards if card.value == Fool]
        )
        if fool_in_shown_cards and player_trump_ranks >= self.needed_cards:
            raise BaseException(
                "The player can't show the Fool if he has sufficient number of Trumps"
            )

        return True

    def to_json(self):
        return {
            "type": self.name,
            "player": self.player.to_json(),
            "shown_cards": [card.to_json() for card in self.shown_cards],
        }


class SingleHandful(Handful):
    name = "singlehandful"
    bonus = 20
    needed_cards = 10


class DoubleHandful(Handful):
    name = "doublehandful"
    bonus = 40
    needed_cards = 13


class TripleHandful(Handful):
    name = "triplehandful"
    bonus = 60
    needed_cards = 15
