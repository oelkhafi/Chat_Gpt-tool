import json

tmp_dict = {}
tmp_dict2 = {}

def rec_func(cl, check):
    if cl in tmp_dict[check]:
        return True
    elif tmp_dict[check] == []:
        return None
    for i in tmp_dict[check]:
        if rec_func(cl, i):
            return True


data = json.loads(input())
for cl in data:
    name, val = cl.values()
    tmp_dict[name] = val
for i in tmp_dict:
    cur_count = 1
    for check in tmp_dict:
        if i == check:
            continue
        else:
            if rec_func(i, check):
                cur_count += 1
    tmp_dict2[i] = cur_count
tmp_dict2 = sorted(tmp_dict2.items(), key = lambda x: x[0])
for name, count in tmp_dict2:
    print(f'{name} : {count}') 