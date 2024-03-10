from typing import List
from src.classes.Bid import Bid, Small

from src.classes.Card import Card
from src.classes.Handful import Handful
from src.classes.Player import Player

from src.utils.get_playable_cards import get_playable_cards


class UIPlayer(Player):
    def prepare_to_new_game(self, players: List[Player]) -> None:
        print(f"You are playing against {[player.name for player in players]}")

    def tell_card_to_play(self, current_turn_cards: List[Card]):
        print("Played cards :")
        [print(f"{c}") for i, c in enumerate(current_turn_cards)]
        playable_cards = get_playable_cards(self.cards, current_turn_cards)
        [print(f"#{i} : {c}") for i, c in enumerate(playable_cards)]

        card_index = -1
        while card_index not in range(len(playable_cards)):
            card_index = int(input("Select a card to play > "))
        return playable_cards[card_index]
