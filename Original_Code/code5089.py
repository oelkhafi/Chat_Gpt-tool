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
        

def get_command():
    for i in range(int(input())):
        yield input()

def command_handler(stack,_string):
    if _string.startswith(""pop""):
        stack.pop()
    elif _string.startswith(""max""):
        _max=stack.max()
        if _max!=None: 
            print(_max)
    else:
        stack.push(int(_string.split()[-1]))
        

def main():
    stack=Stack_with_max()
    for _string in get_command():
        command_handler(stack,_string)
        
main()
 
 
 
             