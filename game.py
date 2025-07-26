from logger import Logger
import random


class Game:
  def __init__(self, team1, team2):
    self.team1 = team1
    self.team2 = team2
    self.logger = Logger()


  def simulate_possession(self, offense):
    defense = self.team2 if offense == self.team1 else self.team1
    shooter = offense.choose_shooter()

    defender = min(defense.players, key=lambda d: abs(d.height - shooter.height))
    is_three = random.random() < 0.35
    points = shooter.attempt_shot(is_three)
    offense.score += points

    if is_three:
      self.logger.log(f"{shooter.name} attempts a 3PT... over {defender.name}", delay=True)
    else:
      self.logger.log(f"{shooter.name} attempts a 2PT... over {defender.name}", delay=True)

    if points > 0:
      self.logger.log('SCORED!', delay=False)
    else:
      self.logger.log('Missed.', delay=False)

    self.logger.log(f"{self.team1.name} {self.team1.score} - {self.team2.name} {self.team2.score}\n", delay=True)


  def simulate_game(self, possessions=20):
    self.logger.log(f"Starting game: {self.team1.name} vs {self.team2.name}\n", delay=False)

    for i in range(possessions):
      offense = self.team1 if i % 2 == 0 else self.team2
      self.simulate_possession(offense)

    self.logger.log(f"\nFinal Score: {self.team1.name} {self.team1.score} - {self.team2.name} {self.team2.score}", delay=False)
    if self.team1.score > self.team2.score:
      self.logger.log(f"Winner: {self.team1.name}", delay=False)
    elif self.team2.score > self.team1.score:
      self.logger.log(f"Winner: {self.team2.name}", delay=False)
    else:
      self.logger.log("It's a tie!", delay=False)
