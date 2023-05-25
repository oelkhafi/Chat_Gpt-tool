import heapq, math

class hpq:
    def __init__(self, lst, lift_cap):
        self.lst = [-i for i in lst]
        heapq.heapify(self.lst)
        self.lift_cap = lift_cap
    
    def attempt(self):
        lc = 0
        at = []
        while self.lst:
            p = -heapq.heappop(self.lst)
            lc += p
            if lc > self.lift_cap:
                heapq.heappush(self.lst, -p)
                break
            if p>1: at.append(int(p/2))
        for i in at:
            heapq.heappush(self.lst, -i)
        del at[:]
        return bool(self.lst) 
        

def main():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    k = int(input())
    #if n==10:
     #   raise Exception(k)
    fruits = hpq(lst, k)
    at_count = 1
    attempts = fruits.attempt()
    while attempts:
        at_count += 1
        attempts = fruits.attempt()
    print(at_count)

if __name__ == ""__main__"": main() 