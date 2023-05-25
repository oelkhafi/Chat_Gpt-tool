class ExtendedStack(list):
    def get(self):
        # читаем числа
        if len(self) > 1:
            self.top1 = self.pop()
            self.top2 = self.pop()
            return True
        else:   
            return False

    def sum(self):
        # операция сложения
        if self.get(): self.append(self.top1 + self.top2)

    def sub(self):
        # операция вычитания
        if self.get(): self.append(self.top1 - self.top2)

    def mul(self):
        # операция умножения
        if self.get(): self.append(self.top1 * self.top2)

    def div(self):
        # операция целочисленного деления
        if self.get() and self.top2!=0: self.append(self.top1 // self.top2) 