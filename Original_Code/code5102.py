from collections import deque

class Deque():
    def __init__(self):
        self.deque = deque()
        self.commands = {""1"":self.deque.appendleft,""2"":self.deque.popleft,
                        ""3"":self.deque.append,""4"":self.deque.pop}
    def __call__(self,_string):
        command, arg = _string.split()
        if command in (""1"",""3""):
            self.commands[command](arg)
            return True
        else:
            res = self.deque and self.commands[command]() or -1
            return int(res) == int(arg)
            
def main():
    data = Deque()
    result = ""YES""
    for i in range(int(input())):
        if not data(input()):
            result = ""NO""
            break
    print(result)        
                
main()

 