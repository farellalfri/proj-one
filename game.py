from logger import Logger
import random


class Game:
  def __init__(self, team1, team2):
    self.team1 = team1
    self.team2 = team2
    self.logger = Logger()

  def simulate_possession(self, offense):
    shooter = offense.choose_shooter()
    is_three = random.random() < 0.35
    points = shooter.attempt_shot(is_three)
    offense.score += points

    if is_three:
      self.logger.log(f"{shooter.name} attempts a 3PT")
    else:
      self.logger.log(f"{shooter.name} attempts a 2PT")

    if points > 0:
      self.logger.log('SCORED!')
    else:
      self.logger.log('Missed.')

  def simulate_game(self, possessions=20):
    for i in range(possessions):
      offense = self.team1 if i % 2 == 0 else self.team2
      self.simulate_possession(offense)

    self.logger.log(f"\nFinal Score: {self.team1.name} {self.team1.score} - {self.team2.name} {self.team2.score}")
    winner = self.team1.name if self.team1.score > self.team2.score else self.team2.name
    self.logger.log(f"Winner: {winner}")
