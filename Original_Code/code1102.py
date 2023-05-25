class Heap:
    
    def __init__(self):
        self.a = []
        

    def insert(self, value):
        self.a.append(value)
        i = len(self.a) - 1
        parent_i = self.parent(i)
        while i > 0 and self.a[i] > self.a[parent_i]:
            self.a[i], self.a[parent_i] = self.a[parent_i], self.a[i]
            i = parent_i
            parent_i = self.parent(i)
            
    def peek(self):
        if self.a:
            return self.a[0]
        return None

    def maxChild(self, i):
        left_i = self.left_child(i)
        right_i = self.right_child(i)
        if left_i == None:
            if right_i == None:
                return None
            elif self.a[i] < self.a[right_i]:
                return right_i
            else:
                return None
        elif right_i == None:
            if left_i == None:
                return None
            elif self.a[i] < self.a[left_i]:
                return left_i
            else:
                return None
        maxIdx = left_i
        if self.a[maxIdx] < self.a[right_i]:
            maxIdx = right_i
        if self.a[i] < self.a[maxIdx]:
            return maxIdx

        return None
            
        
    def pop(self):
        if self.a:
            value = self.a.pop()
            if self.a:
                self.a[0] = value
                i = 0
                while True:
                    max_i = self.maxChild(i)
                    if max_i != None:
                        self.a[i], self.a[max_i] = self.a[max_i], self.a[i]
                        i = max_i
                    else:
                        break
                                           

    def parent(self, i):
        if i == 0:
            return 0
        return (i - 1) // 2


    def left_child(self, i):
        left_idx = 2 * i + 1
        if len(self.a) > left_idx:
            return left_idx
        return None

    def right_child(self, i):
        right_idx = 2 * i + 2
        if len(self.a) > right_idx:
            return right_idx
        return None
   
            
def test(f):
    h = Heap()
    n = int(f.readline())
    res = []
    for _ in range(n):
        cmdlist = f.readline().split("" "")
        if len(cmdlist) == 1:
            num = h.peek()
            res.append(str(num))
            h.pop()
        else:
            x = int(cmdlist[1])
            h.insert(x)
    return res

            
if __name__ == ""__main__"":
    from sys import stdin
    res = test(stdin)
    print(""\n"".join(res)) 