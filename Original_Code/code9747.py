class ExtendedStack(list):
    def sum(self):
        if len(self) >= 2:
            self.append(self.pop() + self.pop())
            return self

    def sub(self):
        if len(self) >= 2:
            self.append(self.pop() - self.pop())
            return self

    def mul(self):
        if len(self) >= 2:
            self.append(self.pop() * self.pop())
            return self

    def div(self):
        if len(self) >= 2:
            self.append(self.pop() // self.pop())
            return self
 