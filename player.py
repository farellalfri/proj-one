import random

class Player:
  THREE_POINTS = 3
  TWO_POINTS = 2
  ZERO_POINTS = 0

  def __init__(self, name, position, two_pt_pct, three_pt_pct, weight=1.0):
    self.name = name
    self.position = position
    self.two_pt_pct = two_pt_pct
    self.three_pt_pct = three_pt_pct
    self.weight = weight

  def attempt_shot(self, is_three):
    if is_three and (random.random() < self.three_pt_pct):
      return self.THREE_POINTS
    elif not is_three and (random.random() < self.two_pt_pct):
      return self.TWO_POINTS
    else:
      return self.ZERO_POINTS
      


  