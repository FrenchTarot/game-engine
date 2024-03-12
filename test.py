from Game import Game
from src.classes.Card import Card
from src.classes.Player import Player
from src.classes.Result import Result
from src.classes.Turn import Turn
from src.classes.UIPlayer import UIPlayer
from src.types.CardType import *
from src.types.CardValue import *

game = Game()

players = [Player(name) for name in ["Gui", "Seb", "Cricar"]]
players += [UIPlayer("Stéphane")]
[game.add_player(player) for player in players]
game.start_game(players[-2])
game.play_set()
