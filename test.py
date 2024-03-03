from Game import Game
from src.classes.Card import Card
from src.classes.Player import Player
from src.classes.Turn import Turn
from src.types.CardType import *
from src.types.CardValue import *

game = Game()

players = [Player(name) for name in ["Ste", "Gui", "Seb", "Cricar"]]
[game.add_player(player) for player in players]
game.start_game(players[0])
game.play_set()
