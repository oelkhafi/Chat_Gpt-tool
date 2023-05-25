class MoneyBox:
    def __init__(self, capacity):
        self.capacity=capacity
        self.current=0
        self.adding=None
        self.v=0
    def can_add(self, v):
        self.v=v
        if self.current+self.v<=self.capacity:
            self.adding = True
            return True
        else:
            self.adding = False
            return False
    def add(self, v):
        self.v=v
        if self.can_add(self.v) is True:
            self.current+=self.v




 