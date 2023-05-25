import heapq
 
 
class heap_storage(list):
    def assign(self, array):
        super().extend(-v for v in array)
        heapq.heapify(self)
 
    def heappop(self):
        heapq.heappop(self)
 
    def heappush(self, v):
        heapq.heappush(self, -v)
 
    def get_max(self):
        return abs(self[0])
 
 
_ = input()
b = heap_storage()
b.assign(map(int, input().split()))
k = int(input())
 
z = 0
while b:
    r = 0
    a = []
    while b:
        v = b.get_max()
        r += v
        if r > k:
            break
        b.heappop()
        if v > 1:
            a.append(v >> 1)
    z += 1
    for v in a:
        b.heappush(v)
    
print(z) 