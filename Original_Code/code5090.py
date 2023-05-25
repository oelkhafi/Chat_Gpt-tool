class Stack_with_max():
    def __init__(self):
        self._stack=[]
    def max(self):
        if self._stack:
            return self._stack[-1][-1]
        else:
            return None
    def pop(self):
        return self._stack.pop()[0]
    def push(self,num):
        if self.max()!=None:
            _max = max(self.max(),num)
        else: _max=num
        self._stack.append((num,_max))
    def empty(self):
        if self._stack:
            return False
        return True
        
class Deque_with_max():
    def __init__(self,max_size=float(""inf"")):
        self._stack_in=Stack_with_max()
        self._stack_out=Stack_with_max()
        self.max_size=max_size
        self.size=0
    def push(self,num):
        if self.size==self.max_size:
            self.pop()
        self._stack_in.push(num)
        self.size+=1
        
    def pop(self):
        if self._stack_out.empty():
            while not self._stack_in.empty():
                self._stack_out.push(self._stack_in.pop())
        if self.size!=0: 
            self.size-=1
        return self._stack_out.pop()
    def max(self):
        if self.size:
            if self._stack_out.empty() or self._stack_in.empty():
                return self._stack_in.empty() and self._stack_out.max() or self._stack_in.max()
            else :
                return max(self._stack_in.max(),self._stack_out.max())
        return None
        

def main():
    result=[]
    count=int(input())
    data=[int(i) for i in input().split()]
    size=int(input())
    deque=Deque_with_max(size)
    for i in range(size):
        deque.push(data.pop(0))
    while data:
        result.append(deque.max())
        deque.push(data.pop(0))
    result.append(deque.max())
    print(*result)
    
main()
 
 
 
             