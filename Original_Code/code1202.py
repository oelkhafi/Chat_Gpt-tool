class Buffer:
    def __init__(self):
        self.mem = []

    def add(self, *args):
        a = len (self.mem)
        b = len (args)
        i = 0
        while a + b - i >= 5:
            if a > 0:
                r = sum (self.mem)
                j = 5 - a
                a = 0;
                self.mem = []
            else:
                r = 0
                j = 5
            r += sum (args [i : i + j])
            print (r)
            i += j
        self.mem += list (args [i:])
        
    def get_current_part(self):
        return self.mem
 