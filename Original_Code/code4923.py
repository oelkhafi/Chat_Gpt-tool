errors = {}

for i in range(int(input())):
    e = input().split(' : ')
    if len(e) == 1:
        e.append('')
    errors[e[0]] = e[1].split()
    for j in errors[e[0]]:
        if j not in errors:
            errors[j] = []

caught = []

def has_been_caught(e):
    return e in caught or any(map(lambda x: has_been_caught(x), errors[e]))

for i in range(int(input())):
    e = input()
    if has_been_caught(e):
        print(e)
    else:
        caught.append(e)
 