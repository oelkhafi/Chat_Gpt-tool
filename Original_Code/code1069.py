class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity:
            return True
        else:
            return False 

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v
#            print('В копилку еще можно положить -',  self.capacity)
#        else:
#            print('Больше не положить!Свободного места -', self.capacity)




 