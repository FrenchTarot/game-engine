from Game import Game
from src.classes.Bid import *
from src.classes.Card import Card, CardFactory
from src.classes.Player import Player
from src.classes.Result import Result
from src.classes.Turn import Turn
from src.classes.UIPlayer import UIPlayer
from src.classes.CardType import *
from src.classes.CardValue import *


game = Game()

players = [Player(name) for name in ["Gui", "Seb", "Cricar"]]
players += [Player("Stéphane")]
[game.add_player(player) for player in players]
game.start_game(players[-2])
final_unit_score = game.play_set()
print(final_unit_score)

# bid_factory = BidFactory()
# print(bid_factory.from_json({"type": "small"}))
