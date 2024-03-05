from typing import Dict, List
from src.classes.Card import Card
from src.classes.Player import Player
from src.classes.Score import Score
from src.types.CardType import Trump
from src.types.CardValue import Fool


class Turn:
    def __init__(self, players) -> None:
        self.played_cards: List[Card] = []
        self.players: List[Player] = players

    def add_played_card(self, card: Card):
        if self.is_turn_finished():
            raise BaseException("All players have already played")
        self.played_cards.append(card)

    def is_turn_finished(self):
        return len(self.played_cards) >= len(self.players)

    def get_turn_winner(self):
        potential_winners = list(
            filter(lambda card: card.value != Fool, self.played_cards)
        )
        if not len(potential_winners):
            return None

        asked_card = potential_winners[0]

        potential_winners = list(
            filter(
                lambda card: card.type == asked_card.type or card.type == Trump,
                potential_winners,
            )
        )

        if Trump in [card.type for card in potential_winners]:
            potential_winners = list(
                filter(lambda card: card.type == Trump, potential_winners)
            )
        potential_winners.sort(key=lambda card: card.value.rank, reverse=True)

        winner_index = self.played_cards.index(potential_winners[0])
        return self.players[winner_index]

    def compute_score(self, last_turn=False):
        score = Score(self.players)

        turn_winner_player = self.get_turn_winner()
        for card_index, card in enumerate(self.played_cards):
            if card.value == Fool and not last_turn:
                score.add_score(self.players[card_index], card.get_score())
                score.add_oudler(self.players[card_index], card)
            else:
                score.add_score(turn_winner_player, card.get_score())
                if card.value.is_oudler:
                    score.add_oudler(turn_winner_player, card)

        return score

    def __str__(self) -> str:
        score = self.compute_score().get_scores()
        str = ""
        for player_index, player in enumerate(self.players):
            str += f"{player.name} ({score[player]}) : {self.played_cards[player_index] if len(self.played_cards) > player_index else 'not played yet'}\n"

        return str
