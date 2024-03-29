from typing import List
from src.classes.Bid import Bid
from src.classes.Card import Card, CardFactory
from src.classes.Handful import Handful
from src.classes.Player import Player
from src.classes.Result import Result
from src.classes.Turn import Turn
from src.classes.Viewer import Viewer
from src.consts.CONTRACT import CONTRACT
from src.classes.CardType import *
from src.classes.CardValue import *

import math
import random
from src.utils.create_deck import create_deck

from src.utils.default_distribute import default_distribute
from src.utils.get_playable_cards import get_playable_cards


class Game:
    name: None
    players: List[Player] = []
    viewers: List[Viewer] = []
    cards: List[Card] = []
    dog_cards: List[Card] = []
    set_history: List[Turn] = []
    game_history = []
    dealer: Player = None
    bid: Bid = None
    handful: Handful = None

    def __init__(self, name=None) -> None:
        self.shuffle_method = random.shuffle
        self.distribute_method = default_distribute
        self.init_deck()
        self.name = name

    def init_deck(self):
        self.cards = create_deck(CardFactory())
        self.shuffle_method(self.cards)

    def check_deck(self):
        if len(self.cards) != 78:
            raise BaseException(
                f"Incorrect number of cards {len(self.cards)} instead of 78"
            )

    def add_player(self, player: Player):
        self.players.append(player)

    def register_viewer(self, viewer: Viewer):
        self.viewers.append(viewer)

    def distribute_cards(self):
        self.dog_cards = []
        self.check_deck()
        for card, player in zip(
            self.cards,
            self.distribute_method(
                self.cards, self.players, self.dealer, 6, len(self.set_history)
            ),
        ):
            if player:
                player.add_card(card)
            else:
                card.set_owner(None)
                self.dog_cards.append(card)

    def start_game(self, dealer: Player = None):
        if dealer:
            if dealer not in self.players:
                raise BaseException("Selected dealer must be in players'list")
            self.dealer = dealer
        else:
            self.dealer = random.choice(self.players)
        self.game_history = []
        self.transmit_info("prepare_to_new_game", {"players": self.players})

    def play_set(self):
        if not self.dealer:
            raise BaseException(
                "No dealer selected, start a game to select the first dealer"
            )
        self.set_history = []
        self.handful = None
        self.transmit_info("prepare_to_new_set", {"dealer": self.dealer})
        self.distribute_cards()
        if not self.bidding():
            return Result(self.players)

        if self.bid.can_take_dog:
            self.transmit_info("view_dog", {"dog_cards": self.dog_cards})
            self.dog_cards = self.bid.player.make_dog(self.dog_cards)

        total_turn = int((78 - len(self.dog_cards)) / len(self.players))
        players_sequence = (
            self.players[self.players.index(self.dealer) + 1 :]
            + self.players[: self.players.index(self.dealer) + 1]
        )

        for turn_number in range(total_turn):
            print(turn_number + 1, "/", total_turn)
            turn = self.play_turn(players_sequence, turn_number)
            turn_winner = turn.get_turn_winner()
            players_sequence = (
                self.players[self.players.index(turn_winner) :]
                + self.players[: self.players.index(turn_winner)]
            )
            print(turn)

        unit_score = self.compute_set_score()
        return unit_score

    def compute_set_score(self):
        total_score = Result(self.players)
        for turn in self.set_history:
            score = turn.compute_score()
            total_score = total_score + score

        one_at_the_end = len([card for card in turn.played_cards if card.value == One])
        if one_at_the_end:
            bout_bonus = 10 if turn.get_turn_winner() == self.bid.player else 10
        else:
            bout_bonus = 0

        scores = total_score.get_scores()

        taker_score_dict = scores[self.bid.player].copy()
        if self.bid.dog_score_to_taker:
            taker_score_dict["score"] += sum(
                [card.get_score() for card in self.dog_cards]
            )
            taker_score_dict["oudlers"] += [
                card for card in self.dog_cards if card.value.is_oudler
            ]

        oudlers_count = len(taker_score_dict["oudlers"])

        print(self.bid.player.name)
        print(oudlers_count)
        print(CONTRACT[oudlers_count], taker_score_dict["score"])
        contract_made = taker_score_dict["score"] >= CONTRACT[oudlers_count]

        if contract_made:
            taker_score_dict["used_score"] = math.ceil(taker_score_dict["score"])
        else:
            taker_score_dict["used_score"] = math.floor(taker_score_dict["score"])

        difference = taker_score_dict["used_score"] - CONTRACT[oudlers_count]

        contract_score = 25 if contract_made else -25

        if self.handful:
            handful_bonus = self.handful.bonus if contract_made else -self.handful.bonus
        else:
            handful_bonus = 0
        slam_bonus = 0

        return (
            (difference + contract_score + bout_bonus) * self.bid.multiplicator
            + handful_bonus
            + slam_bonus
        )

    def bidding(self):
        self.bid = None
        players_sequence = (
            self.players[self.players.index(self.dealer) :]
            + self.players[: self.players.index(self.dealer)]
        )
        for player in players_sequence:
            player_bid = player.tell_bid(self.bid)
            if player_bid:
                if self.bid and player_bid.rank <= self.bid:
                    raise BaseException(
                        "Player's bid must be at least greater than the current bid"
                    )
                self.bid = player_bid
                self.bid.player = player

        self.transmit_info("view_bid", {"bid": self.bid})

        return self.bid

    def play_turn(self, players_sequence, turn_number):
        new_turn = Turn(players_sequence)
        for player in players_sequence:
            if turn_number == 0:
                player_handful = player.tell_handful()
                if player_handful:
                    self.handful = player_handful
                    self.handful.set_player(player)
                    player_handful.check_handful()
                    self._info("view_handful", {"handful": player_handful})
            played_card = player.tell_card_to_play(new_turn.played_cards)
            if played_card not in get_playable_cards(
                player.cards, new_turn.played_cards
            ):
                raise BaseException("Player cannot play this card")
            played_card.played = True
            new_turn.add_played_card(played_card)
            self.transmit_info("view_turn", {"turn": new_turn})

        self.set_history.append(new_turn)

        return new_turn

    def transmit_info(self, viewer_fn, fn_args, confidential=False):
        if not confidential:
            for player in self.players:
                player.__getattribute__(viewer_fn)(**fn_args)
        for viewer in self.viewers:
            viewer.__getattribute__(viewer_fn)(**fn_args)
