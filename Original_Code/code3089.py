import sys


def insert(h, point):
    h.append(point)
    i = len(h) - 1
    node = i // 2
    while h[node] < h[i]:
        h[node], h[i] = h[i], h[node]
        i = node
        node = i // 2
    else: 
        return h
    
def extractMax(h):
    i = 1
    while i * 2 + 1 < len(h):
        left = i * 2
        right = i * 2 + 1
        if h[right] >= h[left]:
            h[right], h[i] = h[i], h[right]
            i = right
        else:
            h[left], h[i] = h[i], h[left]
            i = left
    if h[i] != h[-1]:
        h[i], h[-1] = h[-1], h[i]
        node = i // 2
        while h[node] < h[i]:
            h[node], h[i] = h[i], h[node]
            i = node
            node = i // 2
    return h.pop(-1)
    
def main():
    h, num = [10**10], input()
    for action in sys.stdin.readlines():
        action = action.strip().split()
        if len(action) == 1:
            print(extractMax(h))
        else:
            insert(h, int(action[1]))
            
            
if __name__ == ""__main__"":
    main() 