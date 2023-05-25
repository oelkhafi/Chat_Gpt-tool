def collect_parents(exc, dict, parents = []):
    if dict[exc] != 'None':
        if dict[exc] not in parents:
            parents.extend(dict[exc])
            for parent in dict[exc]:
                exc = parent
                collect_parents(exc, dict, parents)
                return parents
    return parents
    
def check_order(exc, parents, exceptions):
    for parent in parents:
        if parent in exceptions:
            print(exc)
            parents[:] = []
            return
    parents[:] = []

def main():
    dict = {}

    for index in range(int(input())):
        parent = ""None""
        list = input().split()
        child, parent = list[0], list[2:]
        dict.update({child: parent})
        
    exceptions = []   
    
    for index in range(int(input())):
        exc = input()
        if exc in exceptions:
            print(exc)
            continue
        check_order(exc, collect_parents(exc, dict), exceptions)
        exceptions.append(exc)
        
main() 