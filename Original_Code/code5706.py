class ExtendedStack(list):
  def sum(self):
    if len(self) >= 2:
      self.append(self.pop() + self.pop())

  def sub(self):
    if len(self) >= 2:
      self.append(self.pop() - self.pop())
      
  def mul(self):
    if len(self) >= 2:
      self.append(self.pop() * self.pop())

  def div(self):
    if len(self) >= 2:
      self.append(self.pop() // self.pop())




 