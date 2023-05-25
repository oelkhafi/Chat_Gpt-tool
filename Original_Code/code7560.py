import json

js = json.loads(input())


def search_chl(chl, w, path=1):

    for dict_js in js:

        if (chl in dict_js['parents']) and (dict_js['name'] not in w):
            path += 1
            w.append(dict_js['name'])
            path, w = search_chl(dict_js['name'], w, path)

    return path, w


par = dict()

for d in js:
    w = []
    par[d['name']], w = search_chl(d['name'], w)

for i in sorted(par):
    print(i, ':', par[i])
 