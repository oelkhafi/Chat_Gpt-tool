# put your python code here
class NameSpace:
    def __init__(self):
        self.g = {'global': set()}  # graph_name_space

    def create(self, namespace, parent):
        self.g[parent].add(namespace)
        self.g[namespace] = set()
        pass

    def add(self, namespace, var):
        namespace = namespace
        var = var
        if namespace in self.g:
            self.g[namespace].add(var)

    def get(self, namespace, var):
        namespace = namespace
        var = var
        ans = None
        if var in self.g[namespace]:
            return namespace
        else:
            for n in self.g:
                if namespace in self.g[n]:
                    ans = self.get(n, var)
        return ans

    def read_data(self, data):
        o, n, t = [d.strip() for d in data.split()]
        if o == 'add':
            self.add(n, t)
        elif o == 'create':
            self.create(n, t, )
        elif o == 'get':
            print(self.get(n, t))
        else:
            print('Error!')


n = NameSpace()
for i in range(int(input())):
    n.read_data(input()) 