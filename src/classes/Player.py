from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.classes.Player import Player

from src.classes.Bid import Bid, Small

from src.classes.Card import Card
import random
from src.classes.Handful import Handful
from src.classes.Viewer import Viewer

from src.utils.get_playable_cards import get_playable_cards


class Player(Viewer):
    def __init__(self, name) -> None:
        self.cards: List[Card] = []
        self.name = name
        self.set_dealer = None

    def add_card(self, card: Card):
        self.cards.append(card)
        card.set_owner(self)

    def prepare_to_new_set(self, dealer: Player) -> None:
        self.cards = []

    def make_dog(self, dog_cards: List[Card]):
        return dog_cards

    def tell_bid(self, current_bid: Bid) -> Bid:
        if not current_bid:
            return Small()
        return None

    def tell_handful(self) -> Handful:
        return None

    def tell_card_to_play(self, current_turn_cards: List[Card]):
        playable_cards = get_playable_cards(self.cards, current_turn_cards)
        return random.choice(playable_cards)
