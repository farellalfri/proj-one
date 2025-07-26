from player import Player
from team import Team
from game import Game

team1_players = [
  Player("Donovan Mitchell", "SG", 0.512, 0.368, height=190, drtg=113, dws=2.8, dbpm=-0.2),
  Player("Darius Garland", "PG", 0.53, 0.401, height=185, drtg=115, dws=2.3, dbpm=-0.8),
  Player("Evan Mobley", "PF", 0.621, 0.37, height=211, drtg=108, dws=3.8, dbpm=1.5)
]

team2_players = [
  Player("Shai Gilgeous-Alexander", "PG", 0.571, 0.375, height=197, drtg=107, dws=4.8, dbpm=2.6),
  Player("Jalen Williams", "SF", 0.533, 0.365, height=198, drtg=107, dws=4.1, dbpm=1.4),
  Player("Chet Holmgren", "PF", 0.547, 0.379, height=216, drtg=103, dws=2, dbpm=1.9)
]

cavs = Team("Cleveland Cavaliers", team1_players)
thunder = Team("OKC Thunder", team2_players)

game = Game(cavs, thunder)
game.simulate_game(possessions=20)