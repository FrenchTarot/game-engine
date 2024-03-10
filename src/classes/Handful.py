from src.types.CardType import Trump
from src.types.CardValue import Fool


class Handful:
    bonus = 0
    shown_cards = []
    needed_cards = []

    def __init__(self, shown_cards) -> None:
        self.shown_cards = shown_cards

    def set_player(self, player):
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


class SingleHandful(Handful):
    bonus = 20
    needed_cards = 10


class DoubleHandful(Handful):
    bonus = 40
    needed_cards = 13


class TripleHandful(Handful):
    bonus = 60
    needed_cards = 15
