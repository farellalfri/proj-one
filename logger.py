class Logger:
  def __init__(self):
    self.logs = []

  def log(self, msg):
    print(msg)
    self.logs.append(msg)