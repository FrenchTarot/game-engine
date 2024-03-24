from __future__ import annotations
from typing import TYPE_CHECKING, List

from src.classes.Card import Card

if TYPE_CHECKING:
    from src.classes.Player import Player
    from src.classes.Result import Result


class Result:
    def __init__(self, players: List[Player]) -> None:
        self.player_scores = {player: {"score": 0, "oudlers": []} for player in players}

    def add_score(self, player: Player, score: int):
        self.player_scores[player]["score"] += score

    def add_oudler(self, player: Player, oudler):
        self.player_scores[player]["oudlers"].append(oudler)

    def add_scores(self, scores):
        for player in scores:
            self.player_scores[player]["score"] += scores[player]

    def add_oudlers(self, oudlers: List[Card]):
        for player in oudlers:
            self.player_scores[player]["oudlers"].append(oudlers[player])

    def get_scores(self):
        return self.player_scores

    def __add__(self, score2: Result):
        if len(
            set(self.player_scores.keys()).difference(set(score2.player_scores.keys()))
        ):
            return BaseException("Result must have same players when adding them")

        result = Result(self.player_scores.keys())
        for player in self.player_scores:
            result.add_score(
                player,
                self.player_scores[player]["score"]
                + score2.player_scores[player]["score"],
            )
            for o in self.player_scores[player]["oudlers"]:
                result.add_oudler(player, o)
            for o in score2.player_scores[player]["oudlers"]:
                result.add_oudler(player, o)

        return result

    def to_json(self):
        return {
            player.name: self.player_scores[player]
            for player in self.player_scores.keys()
        }
