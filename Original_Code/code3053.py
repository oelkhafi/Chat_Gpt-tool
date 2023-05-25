dict = {}

for i in range(int(input())):  
    tmp = [i for i in input().split() if i.isalpha()]
    child, parent = tmp[0], tmp[1:1000]
    if parent == []:
        parent = child
    dict.update({child:(parent)})
    
def get_parent(parent, child, visited = []):
        visited += [child]
        if child == parent:
            return ""Yes""
        elif parent in dict[child]:
            return ""Yes""
        for every in dict[child]:
            if every not in visited:
                if every in dict:
                    child = every
                    newpath = get_parent(parent, child, visited)
                    if newpath==""Yes"":
                        return ""Yes""
                else: continue
        return ""No""

for i in range(int(input())):
    parent, child = input().split()
    print(get_parent(parent, child, visited = [])) 