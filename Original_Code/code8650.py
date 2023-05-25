class queue_with_prior:
    def __init__(self, queue=[]):
        self.queue = queue

    def shift_up(self, i):
        while (i > 0) and (self.queue[i // 2] < self.queue[i]):
            self.queue[i // 2], self.queue[i] = self.queue[i], self.queue[i // 2]
            i //= 2

    def shift_down(self, i):
        while (2 * i < len(self.queue)):
            j = i
            if self.queue[2 * i] > self.queue[i]:
                j = 2 * i
            if (2 * i + 1 < len(self.queue)) and (self.queue[2 * i + 1] > self.queue[j]):
                j = 2 * i + 1
            if j == i:
                break
            self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
            i = j

    def insert(self, n):
        self.queue.append(n)
        self.shift_up(len(self.queue) - 1)

    def get_max(self):
        return self.queue[0]

    def extract_max(self):
        res = self.get_max()
        self.queue[0] = self.queue[-1]
        self.shift_down(0)
        del self.queue[-1]
        return res

    def change_priority(self, i, p):
        self.queue[i] = p
        self.shift_up(i)
        self.shift_down(i)

a = queue_with_prior()
for i in range(int(input())):
    cmnd, *val = input().split()
    if cmnd == 'Insert':
        a.insert(int(val[0]))
    elif cmnd == 'ExtractMax':
        print(a.extract_max())
         