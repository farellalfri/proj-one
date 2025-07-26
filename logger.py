import time

class Logger:
  def __init__(self, time_delay=1.0):
    self.logs = []
    self.time_delay = time_delay

  def log(self, msg, delay):
    print(msg)
    self.logs.append(msg)
    if delay:
      time.sleep(self.time_delay)