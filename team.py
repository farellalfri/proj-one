import random

class Team:
  def __init__(self, name, players):
    self.name = name
    self.players = players
    self.score = 0

  def choose_shooter(self):
    weights = []
    for player in self.players:
      weights.append(player.weight)
    return random.choices(self.players, weights=weights)[0]