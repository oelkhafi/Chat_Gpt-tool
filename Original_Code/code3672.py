import sys
m = int(sys.stdin.readline())
hash_table = [[] for i in range(m)]

def H(s):
    a = ord(s[0]) % 1000000007
    x = 1
    for i in range(1, len(s)):
        x = x * 263 % 1000000007
        a += ord(s[i]) * x % 1000000007
    return a % 1000000007 % m

for i in range(int(sys.stdin.readline())):
    command = list(map(str, sys.stdin.readline().split()))
    h = H(command[1])

    if command[0] == 'add':
        if command[1] not in hash_table[h]:
            hash_table[h].insert(0,command[1])
    elif command[0] == 'find':
        if command[1] in hash_table[h]:
            print('yes')
        else:
            print('no')
    elif command[0] == 'del':
        if command[1] in hash_table[h]:
            hash_table[h].remove(command[1])
    elif command[0] == 'check':
        print(*hash_table[int(command[1])]) 