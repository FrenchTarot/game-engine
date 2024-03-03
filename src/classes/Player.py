from typing import List
from src.classes.Bid import Bid, Small

from src.classes.Card import Card
import random

from src.utils.get_playable_cards import get_playable_cards


class Player:
    def __init__(self, name) -> None:
        self.cards: List[Card] = []
        self.name = name

    def prepare_to_new_game(self, players) -> None:
        pass

    def prepare_to_new_set(self, dealer) -> None:
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)
        card.set_owner(self)

    def view_dog(self, dog_cards):
        pass

    def view_turn(self, turn):
        pass

    def view_bid(self, bid: Bid):
        pass

    def make_dog(self, dog_cards):
        return dog_cards

    def tell_bid(self, current_bid) -> Bid:
        if not current_bid:
            return Small()
        return None

    def tell_card_to_play(self, current_turn_cards):
        playable_cards = get_playable_cards(self.cards, current_turn_cards)
        return random.choice(playable_cards)
