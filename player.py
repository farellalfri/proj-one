import random

class Player:
  THREE_POINTS = 3
  TWO_POINTS = 2
  ZERO_POINTS = 0

  AVERAGE_POSITION_DRTG = {
        "PG": 115.7,
        "SG": 115.9,
        "SF": 115.7,
        "PF": 114.1,
        "C": 111.6
    }

  def __init__(self, name, position, two_pt_pct, three_pt_pct, height, drtg, dws, dbpm, weight=1.0):
    self.name = name
    self.position = position
    self.two_pt_pct = two_pt_pct
    self.three_pt_pct = three_pt_pct
    self.height = height
    self.drtg = drtg
    self.dws = dws
    self.dbpm = dbpm
    self.weight = weight


  def calculate_defensive_multiplier(self):
    """
    Returns a multiplier between ~0.85 to 1.05.
    Lower = better defender = shot success lowered.
    """
    # How much better than average is their DRtg for their position
    avg_drtg = self.AVERAGE_POSITION_DRTG.get(self.position, 115.7)
    drtg_component = max(0.85, min(1.15, avg_drtg / self.drtg))  # Lower DRtg -> higher penalty to shooter

    # DWS: average = 2.0
    dws_component = 1.0 - ((self.dws - 2.0) * 0.02)  # Higher DWS = better defense
    dws_component = max(0.95, min(1.05, dws_component))

    # DBPM: 0 is average
    dbpm_component = 1.0 - (self.dbpm * 0.015)
    dbpm_component = max(0.90, min(1.05, dbpm_component))

    # Final multiplier = product of effects
    return drtg_component * dws_component * dbpm_component
  

  def modify_shot_chance(self, base_pct, defender, team_modifier=0.0):
    """
    Applies defensive and team modifiers to base_pct.
    """
    defense_multiplier = defender.calculate_defensive_multiplier()
    effective_pct = (base_pct + team_modifier) * defense_multiplier
    return max(0.05, min(0.95, effective_pct))  # Clamp between 5% and 95%


  def attempt_shot(self, is_three, defender=None, team_modifier=0.0):
    base_pct = self.three_pt_pct if is_three else self.two_pt_pct
    if defender:
      shot_chance = self.modify_shot_chance(base_pct, defender, team_modifier)
    else:
      shot_chance = base_pct + team_modifier
    
    if random.random() < shot_chance:
      return self.THREE_POINTS if is_three else self.TWO_POINTS
    else:
      return self.ZERO_POINTS
    """
    if is_three and (random.random() < self.three_pt_pct):
      return self.THREE_POINTS
    elif not is_three and (random.random() < self.two_pt_pct):
      return self.TWO_POINTS
    else:
      return self.ZERO_POINTS
    """
      


  