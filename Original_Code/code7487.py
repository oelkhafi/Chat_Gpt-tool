a_dict = {'global': [None, set()]}
sample_input_lst = []

for i in range(int(input())):
    sample_input_lst.append(input().split())


def get(namespace, var):
    if a_dict.get(namespace) is None:
        print(None)
    else:
        if var in a_dict[namespace][1]:
            print(namespace)
        else:
            get(a_dict[namespace][0],var)


for i in sample_input_lst:
    if i[0] == 'create':
        a_dict[i[1]] = [i[2], set()]
    elif i[0] == 'add':
        a_dict[i[1]][1].add(i[2])
    elif i[0] == 'get':
        get(i[1], i[2]) 