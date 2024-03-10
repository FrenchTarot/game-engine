from typing import List
from src.classes.Bid import Bid, Small

from src.classes.Card import Card
import random
from src.classes.Handful import Handful, SingleHandful
from src.classes.Viewer import Viewer

from src.utils.get_playable_cards import get_playable_cards


class UIPlayer(Viewer):
    def __init__(self, name) -> None:
        self.cards: List[Card] = []
        self.name = name
        self.set_dealer = None

    def add_card(self, card: Card):
        self.cards.append(card)
        card.set_owner(self)

    def prepare_to_new_set(self, dealer) -> None:
        self.cards = []

    def prepare_to_new_game(self, players) -> None:
        print(f"You are playing with {[player.name for player in players]}")

    def make_dog(self, dog_cards):
        return dog_cards

    def tell_bid(self, current_bid) -> Bid:
        if not current_bid:
            return Small()
        return None

    def tell_handful(self) -> Handful:
        return None

    def tell_card_to_play(self, current_turn_cards):
        print("Played cards :")
        [print(f"{c}") for i, c in enumerate(current_turn_cards)]
        playable_cards = get_playable_cards(self.cards, current_turn_cards)
        [print(f"#{i} : {c}") for i, c in enumerate(playable_cards)]

        card_index = -1
        while card_index not in range(len(playable_cards)):
            card_index = int(input("Select a card to play > "))
        return playable_cards[card_index]
