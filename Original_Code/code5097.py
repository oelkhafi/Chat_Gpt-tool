from array import array

def find(tables, indexies, pos):
    steps=[]
    while pos!=indexies[pos]:
        steps.append(pos)
        pos=indexies[pos]
    for i in steps:
        indexies[i]=pos
    return pos

def union(tables, indexies, destination, source):
    id_destination = find(tables, indexies, destination)
    id_source = find(tables, indexies, source)
    if id_destination != id_source:
        tables[id_destination] += tables[id_source]
        indexies[id_source] = id_destination
        if tables[0] < tables[id_destination]:
            tables[0] = tables[id_destination]
    print(tables[0])

def main():
    n_tables, n_requests = [int(i) for i in input().split()]
    tables = array(""I"",[0,]+[int(i) for i in input().split()])
    indexies = array(""I"",[i for i in range(n_tables + 1)])
    tables[0] = max(tables)
    for i in range(n_requests):
        destination, source = [int(i) for i in input().split()]
        union(tables, indexies, destination, source)

if __name__ == ""__main__"":
    main()





 