from player import Player
from team import Team
from game import Game

team1_players = [
  Player("Donovan Mitchell", "SG", 0.512, 0.368),
  Player("Darius Garland", "PG", 0.53, 0.401),
  Player("Evan Mobley", "PF", 0.621, 0.37)
]

team2_players = [
  Player("Shai Gilgeous-Alexander", "PG", 0.571, 0.375),
  Player("Jalen Williams", "SF", 0.533, 0.365),
  Player("Chet Holmgren", "PF", 0.547, 0.379)
]

cavs = Team("Cavaliers", team1_players)
thunder = Team("Thunder", team2_players)

game = Game(cavs, thunder)
game.simulate_game(possessions=20)