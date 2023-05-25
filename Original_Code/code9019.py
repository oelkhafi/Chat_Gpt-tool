class Buffer:
    def __init__(self):
        self.temp = []

    def add(self, *a):
        for item in a:
            self.temp.append(int(item))

        def remover(lst):
            if len(lst) >= 5:
                print(sum(lst[:5]))
                for i in range(4, -1, -1):
                    lst.pop(i)
                return remover(lst)
            return None

        if len(self.temp) >= 5:
            remover(self.temp)

    def get_current_part(self):
        return self.temp

 