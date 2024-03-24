from typing import List
from src.classes.Card import Card
from src.classes.Player import Player
from src.consts.TERMINAL_GUI import TERMINAL_GUI
from src.classes.CardType import *
from src.utils.get_playable_cards import get_playable_cards


class UIPlayer(Player):
    def prepare_to_new_game(self, players: List[Player]) -> None:
        print(f"You are playing against {[player.name for player in players]}")

    def tell_card_to_play(self, current_turn_cards: List[Card]):
        print("Played cards :")
        self.sort_cards()
        [print(f"{c}") for i, c in enumerate(current_turn_cards)]
        playable_cards = get_playable_cards(self.cards, current_turn_cards)
        types = [Spade, Heart, Club, Diamond, Trump]
        cards_by_type = [[c for c in self.cards if c.type == t] for t in types]
        max_cards_in_color = max([len(cards) for cards in cards_by_type])
        [
            print(
                f"{TERMINAL_GUI.bg.red}{t.__name__: >16}{TERMINAL_GUI.style.reset}",
                end=" ",
            )
            for t in types
        ]
        print()
        for i in range(max_cards_in_color):
            for j, type in enumerate(types):
                card = cards_by_type[j][i] if len(cards_by_type[j]) > i else None
                is_card_playable = card in playable_cards
                play_index = (
                    f"#{playable_cards.index(card): >2} : " if is_card_playable else ""
                )
                str = f"{play_index}{card}" if card else ""
                style_card_played = (
                    TERMINAL_GUI.style.strikethrough if card and card.played else ""
                )
                style_card_can_be_played = (
                    TERMINAL_GUI.fg.green if is_card_playable else ""
                )
                print(
                    f"{style_card_can_be_played}{style_card_played}{str: >16}{TERMINAL_GUI.style.reset}",
                    end=" ",
                )
            print()

        card_index = -1
        while card_index not in range(len(playable_cards)):
            card_index = int(input("Select a card to play > "))
        return playable_cards[card_index]
