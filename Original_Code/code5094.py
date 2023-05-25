def main():
    lenght,lst = int(input()),[int(i) for i in input().split()]
    build_heap(lenght,lst)
    print(len(LOG),*(""{} {}"".format(*i) for i in LOG),sep = ""\n"")
    
def build_heap(lenght,lst):
    global LOG
    def siftdown(heap,pos):
        child_l, child_r, idx = pos*2+1, pos*2+2, pos
        for child in child_l, child_r:
            if child < len(heap) and heap[child] < heap[idx]:
                idx = child
        if idx != pos:
            heap[pos], heap[idx] = heap[idx], heap[pos]
            LOG.append((pos,idx))
            siftdown(heap,idx)
    for pos in range(lenght//2,-1,-1):
        siftdown(lst,pos)
        
LOG=[]        
main() 