from typing import List
from src.classes.Bid import Bid
from src.classes.Card import Card
from src.classes.Player import Player
from src.classes.Score import Score
from src.classes.Turn import Turn
from src.types.CardType import *
from src.types.CardValue import *

import random
from src.utils.create_deck import create_deck

from src.utils.default_distribute import default_distribute


class Game:
    players: List[Player] = []
    cards: List[Card] = []
    dog_cards: List[Card] = []
    set_history: List[Turn] = []
    game_history = []
    dealer: Player = None
    bid: Bid = None

    def __init__(self) -> None:
        self.shuffle_method = random.shuffle
        self.distribute_method = default_distribute
        self.init_deck()

    def init_deck(self):
        self.cards = create_deck(Card)
        self.shuffle_method(self.cards)

    def check_deck(self):
        if len(self.cards) != 78:
            raise BaseException(
                f"Incorrect number of cards {len(self.cards)} instead of 78"
            )

    def add_player(self, player: Player):
        self.players.append(player)

    def reset_players(self):
        self.players = []

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

    def play_set(self):
        if not self.dealer:
            raise BaseException(
                "No dealer selected, start a game to select the first dealer"
            )
        self.set_history = []
        [player.prepare_to_new_set(self.dealer) for player in self.players]
        self.distribute_cards()
        if not self.bidding():
            return Score(self.players)

        if self.bid.can_take_dog:
            [player.view_dog(self.dog_cards) for player in self.players]
            self.dog_cards = self.bid.player.make_dog(self.dog_cards)

        total_turn = int((78 - len(self.dog_cards)) / len(self.players))
        for turn_number in range(total_turn):
            print(turn_number + 1, "/", total_turn)
            turn = self.play_turn()
            print(turn)

        print("Set ended")

    def bidding(self):
        self.bid = None
        for player in self.players:
            player_bid = player.tell_bid(self.bid)
            if player_bid:
                if self.bid and player_bid.rank <= self.bid:
                    raise BaseException(
                        "Player's bid must be at least greater than the current bid"
                    )
                self.bid = player_bid
                self.bid.player = player

        for player in self.players:
            player.view_bid(self.bid)

        return self.bid

    def play_turn(self):
        players_sequence = (
            self.players[self.players.index(self.dealer) + 1 :]
            + self.players[: self.players.index(self.dealer) + 1]
        )

        new_turn = Turn(players_sequence)
        for player in players_sequence:
            played_card = player.tell_card_to_play(new_turn.played_cards)
            played_card.played = True
            new_turn.add_played_card(played_card)
            for player in self.players:
                player.view_turn(new_turn)

        self.set_history.append(new_turn)

        return new_turn
