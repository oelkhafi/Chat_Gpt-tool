from operator import add, sub, floordiv, mul

class ExtendedStack(list):
    def __op2__(self, f):
        a = self.pop()
        b = self.pop()
        self.append(f(a,b))
        
    def sum(self):
        self.__op2__(add)

    def sub(self):
        self.__op2__(sub)

    def mul(self):
        self.__op2__(mul)

    def div(self):
        self.__op2__(floordiv)

 